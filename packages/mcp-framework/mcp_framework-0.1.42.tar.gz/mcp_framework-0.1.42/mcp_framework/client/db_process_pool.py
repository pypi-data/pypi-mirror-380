"""
基于数据库的MCP进程池
使用SQLite数据库来管理进程状态，避免内存状态不一致问题
"""

import asyncio
import time
from typing import Dict, Optional, Tuple, Any
import logging
from .base import MCPStdioClient
from .db_client_manager import DBClientManager, get_client_manager
from .tools import ToolsClient

logger = logging.getLogger(__name__)


class DBProcessPool:
    """基于数据库的MCP进程池"""
    
    _instance = None
    _lock = asyncio.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, '_initialized'):
            self._client_manager: Optional[DBClientManager] = None
            self._cleanup_task = None
            self._initialized = True
            self._start_cleanup_task()
    
    async def _get_client_manager(self) -> DBClientManager:
        """获取客户端管理器"""
        if self._client_manager is None:
            self._client_manager = await get_client_manager()
        return self._client_manager
    
    def _start_cleanup_task(self):
        """启动清理任务"""
        if self._cleanup_task is None or self._cleanup_task.done():
            self._cleanup_task = asyncio.create_task(self._cleanup_loop())
    
    async def _cleanup_loop(self):
        """清理循环"""
        while True:
            try:
                await asyncio.sleep(300)  # 每5分钟清理一次
                await self._cleanup_idle_processes()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"清理任务出错: {e}")
    
    async def _cleanup_idle_processes(self):
        """清理空闲进程"""
        try:
            client_manager = await self._get_client_manager()
            await client_manager.cleanup_idle_clients(idle_timeout=1800)  # 30分钟超时
        except Exception as e:
            logger.error(f"清理空闲进程失败: {e}")
    
    async def get_client(self, server_script: str, alias: Optional[str] = None,
                        config_dir: Optional[str] = None, **kwargs) -> Tuple[ToolsClient, str]:
        """
        获取客户端实例
        
        Args:
            server_script: 服务器脚本路径
            alias: 服务器别名
            config_dir: 配置目录
            **kwargs: 其他参数
            
        Returns:
            Tuple[ToolsClient, str]: 包装后的工具客户端实例和池键
        """
        try:
            client_manager = await self._get_client_manager()
            raw_client, pool_key = await client_manager.get_or_create_client(
                server_script=server_script,
                alias=alias,
                config_dir=config_dir,
                **kwargs
            )
            
            # 包装为ToolsClient
            tools_client = ToolsClient._wrap_existing_client(raw_client)
            return tools_client, pool_key
            
        except Exception as e:
            logger.error(f"获取客户端失败: {e}")
            raise
    
    async def release_client(self, pool_key: str, alias: Optional[str] = None):
        """
        释放客户端
        
        Args:
            pool_key: 池键（暂时保留兼容性）
            alias: 别名
        """
        try:
            client_manager = await self._get_client_manager()
            
            # 如果没有提供alias，尝试从pool_key推断
            if alias is None:
                alias = pool_key
            
            await client_manager.release_client(alias)
        except Exception as e:
            logger.error(f"释放客户端失败: {e}")
    
    async def force_cleanup(self, alias: Optional[str] = None):
        """
        强制清理指定别名的进程，如果alias为None则清理所有
        
        Args:
            alias: 要清理的别名，None表示清理所有
        """
        try:
            client_manager = await self._get_client_manager()
            
            if alias is None:
                # 清理所有
                await client_manager.cleanup_all()
            else:
                # 清理指定别名（这里需要扩展DBClientManager来支持单个别名清理）
                # 暂时使用cleanup_idle_clients with 0 timeout来强制清理
                await client_manager.cleanup_idle_clients(idle_timeout=0)
        except Exception as e:
            logger.error(f"强制清理失败: {e}")
    
    async def get_status(self) -> Dict[str, Any]:
        """
        获取进程池状态
        
        Returns:
            Dict[str, Any]: 状态信息
        """
        try:
            client_manager = await self._get_client_manager()
            status = await client_manager.get_status()
            
            return {
                'pool_type': 'database_based',
                'total_processes': status['total_processes'],
                'active_clients': status['active_clients'],
                'processes': status['processes'],
                'cleanup_task_running': self._cleanup_task and not self._cleanup_task.done()
            }
        except Exception as e:
            logger.error(f"获取状态失败: {e}")
            return {
                'pool_type': 'database_based',
                'error': str(e),
                'total_processes': 0,
                'active_clients': 0,
                'processes': [],
                'cleanup_task_running': False
            }
    
    async def cleanup_all(self):
        """清理所有进程和资源"""
        try:
            # 停止清理任务
            if self._cleanup_task and not self._cleanup_task.done():
                self._cleanup_task.cancel()
                try:
                    await self._cleanup_task
                except asyncio.CancelledError:
                    pass
            
            # 清理所有客户端和进程
            if self._client_manager:
                await self._client_manager.cleanup_all()
            
            logger.info("进程池清理完成")
        except Exception as e:
            logger.error(f"清理进程池失败: {e}")
    
    async def shutdown(self):
        """关闭进程池"""
        await self.cleanup_all()
        
        # 重置实例
        DBProcessPool._instance = None


# 全局进程池实例
_db_process_pool = None


def get_db_process_pool() -> DBProcessPool:
    """获取基于数据库的进程池实例"""
    global _db_process_pool
    if _db_process_pool is None:
        _db_process_pool = DBProcessPool()
    return _db_process_pool


class DBPooledClient:
    """基于数据库的池化客户端上下文管理器"""
    
    def __init__(self, server_script: str, alias: Optional[str] = None,
                 config_dir: Optional[str] = None, **kwargs):
        self.server_script = server_script
        self.alias = alias
        self.config_dir = config_dir
        self.kwargs = kwargs
        self.client = None
        self.pool_key = None
    
    async def __aenter__(self):
        pool = get_db_process_pool()
        self.client, self.pool_key = await pool.get_client(
            self.server_script, self.alias, self.config_dir, **self.kwargs
        )
        return self.client
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.client and self.pool_key:
            pool = get_db_process_pool()
            await pool.release_client(self.pool_key, self.alias)


# 便利函数
async def get_db_pooled_client(server_script: str, alias: Optional[str] = None,
                               config_dir: Optional[str] = None, **kwargs) -> Tuple[ToolsClient, str]:
    """获取数据库池化客户端"""
    pool = get_db_process_pool()
    return await pool.get_client(server_script, alias, config_dir, **kwargs)


async def release_db_pooled_client(pool_key: str, alias: Optional[str] = None):
    """释放池化客户端"""
    pool = get_db_process_pool()
    await pool.release_client(pool_key, alias)


async def cleanup_db_process(alias: Optional[str] = None):
    """清理进程"""
    pool = get_db_process_pool()
    await pool.force_cleanup(alias)


async def get_db_pool_status() -> Dict[str, Any]:
    """获取池状态"""
    pool = get_db_process_pool()
    return await pool.get_status()