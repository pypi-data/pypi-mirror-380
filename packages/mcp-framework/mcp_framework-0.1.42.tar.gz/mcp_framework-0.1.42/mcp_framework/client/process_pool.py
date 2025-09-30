"""
MCP 进程池管理器
基于别名管理MCP服务器进程，支持进程复用和自动超时关闭
"""

import asyncio
import time
import weakref
from typing import Dict, Optional, Tuple, Any
from pathlib import Path
import logging
from .base import MCPStdioClient

logger = logging.getLogger(__name__)


class SharedClientWrapper:
    """共享客户端包装器，允许多个实例安全地共享同一个底层客户端"""
    
    def __init__(self, underlying_client: MCPStdioClient, pool_entry: 'ProcessPoolEntry', pool_key: str):
        self._underlying_client = underlying_client
        self._pool_entry = pool_entry
        self._pool_key = pool_key
        self._is_released = False
        
        # 直接复制底层客户端的所有属性，而不是使用代理
        for attr_name in dir(underlying_client):
            if not attr_name.startswith('_') and not callable(getattr(underlying_client, attr_name)):
                try:
                    setattr(self, attr_name, getattr(underlying_client, attr_name))
                except (AttributeError, TypeError):
                    pass
        
        # 复制重要的私有属性
        for attr_name in ['_request_id', '_is_connected', '_is_initialized', 
                         'process', 'reader', 'writer', 'server_script', 'alias']:
            if hasattr(underlying_client, attr_name):
                try:
                    setattr(self, attr_name, getattr(underlying_client, attr_name))
                except (AttributeError, TypeError):
                    pass
        
        # 复制底层客户端的类型信息，以便isinstance检查正常工作
        self.__class__ = type(
            f"Wrapped{underlying_client.__class__.__name__}",
            (self.__class__, underlying_client.__class__),
            {}
        )
    
    def __getattr__(self, name):
        """代理方法调用到底层客户端"""
        if self._is_released:
            raise RuntimeError("客户端已释放，无法使用")
        
        attr = getattr(self._underlying_client, name)
        if callable(attr):
            # 对于方法调用，直接返回底层客户端的方法
            return attr
        else:
            # 对于属性访问，返回当前值
            return attr
    
    async def disconnect(self):
        """重写disconnect方法，不实际断开连接，而是释放引用"""
        if not self._is_released:
            await self._pool_entry.release()
            self._is_released = True
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.disconnect()


class ProcessPoolEntry:
    """进程池条目"""
    
    def __init__(self, client: MCPStdioClient, alias: str):
        self.client = client
        self.alias = alias
        self.last_used = time.time()
        self.ref_count = 0
        self.is_healthy = True
        self._lock = asyncio.Lock()
    
    async def acquire(self, pool_key: str) -> SharedClientWrapper:
        """获取客户端引用"""
        async with self._lock:
            self.ref_count += 1
            self.last_used = time.time()
            return SharedClientWrapper(self.client, self, pool_key)
    
    async def release(self):
        """释放客户端引用"""
        async with self._lock:
            self.ref_count = max(0, self.ref_count - 1)
            self.last_used = time.time()
    
    def is_idle(self, timeout_seconds: int = 1800) -> bool:
        """检查是否空闲（默认30分钟超时）"""
        return (self.ref_count == 0 and 
                time.time() - self.last_used > timeout_seconds)
    
    async def health_check(self) -> bool:
        """检查进程健康状态"""
        try:
            if not self.client or not hasattr(self.client, '_process') or not self.client._process:
                self.is_healthy = False
                return False
            
            # 检查进程是否还在运行
            if self.client._process.poll() is not None:
                # 进程已经结束
                self.is_healthy = False
                return False
            
            # 检查是否有读写器
            if not hasattr(self.client, '_reader') or not hasattr(self.client, '_writer'):
                self.is_healthy = False
                return False
            
            if not self.client._reader or not self.client._writer:
                self.is_healthy = False
                return False
            
            # 检查写器是否关闭
            if self.client._writer.is_closing():
                self.is_healthy = False
                return False
            
            self.is_healthy = True
            return True
        except Exception as e:
            logger.warning(f"进程 {self.alias} 健康检查失败: {e}")
            self.is_healthy = False
            return False
    
    async def cleanup(self):
        """清理资源"""
        try:
            if self.client:
                await self.client.disconnect()
        except Exception as e:
            logger.warning(f"清理进程 {self.alias} 时出错: {e}")


class MCPProcessPool:
    """MCP进程池管理器"""
    
    _instance = None
    _lock = asyncio.Lock()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if hasattr(self, '_initialized'):
            return
        
        self._processes: Dict[str, ProcessPoolEntry] = {}
        self._cleanup_task: Optional[asyncio.Task] = None
        self._cleanup_interval = 300  # 5分钟检查一次
        self._timeout_seconds = 1800  # 30分钟超时
        self._initialized = True
        
        # 启动清理任务
        self._start_cleanup_task()
    
    def _start_cleanup_task(self):
        """启动清理任务"""
        if self._cleanup_task is None or self._cleanup_task.done():
            self._cleanup_task = asyncio.create_task(self._cleanup_loop())
    
    async def _cleanup_loop(self):
        """清理循环"""
        while True:
            try:
                await asyncio.sleep(self._cleanup_interval)
                await self._cleanup_idle_processes()
            except asyncio.CancelledError:
                break
            except Exception as e:
                logger.error(f"清理任务出错: {e}")
    
    async def _cleanup_idle_processes(self):
        """清理空闲进程"""
        async with self._lock:
            to_remove = []
            
            for alias, entry in self._processes.items():
                if entry.is_idle(self._timeout_seconds):
                    logger.info(f"清理空闲进程: {alias}")
                    await entry.cleanup()
                    to_remove.append(alias)
                elif not entry.is_healthy:
                    # 健康检查失败的进程也要清理
                    if not await entry.health_check():
                        logger.info(f"清理不健康进程: {alias}")
                        await entry.cleanup()
                        to_remove.append(alias)
            
            for alias in to_remove:
                del self._processes[alias]
    
    def _generate_key(self, server_script: str, alias: Optional[str] = None, 
                     config_dir: Optional[str] = None, **kwargs) -> str:
        """生成进程池键"""
        # 使用绝对路径确保一致性
        script_path = str(Path(server_script).resolve())
        
        # 构建键值
        key_parts = [script_path]
        
        if alias:
            key_parts.append(f"alias:{alias}")
        
        if config_dir:
            key_parts.append(f"config:{str(Path(config_dir).resolve())}")
        
        # 添加其他重要参数
        for k, v in sorted(kwargs.items()):
            if k not in ['timeout']:  # 排除不影响进程身份的参数
                key_parts.append(f"{k}:{v}")
        
        return "|".join(key_parts)
    
    async def get_client(self, server_script: str, alias: Optional[str] = None,
                        config_dir: Optional[str] = None, **kwargs) -> Tuple[MCPStdioClient, str]:
        """
        获取或创建客户端 - 相同配置的客户端复用同一个进程
        
        Returns:
            Tuple[MCPStdioClient, str]: (客户端实例, 进程池键)
        """
        pool_key = self._generate_key(server_script, alias, config_dir, **kwargs)
        
        async with self._lock:
            # 检查是否已存在相同配置的进程
            if pool_key in self._processes:
                entry = self._processes[pool_key]
                
                # 健康检查
                if await entry.health_check():
                    client = await entry.acquire(pool_key)
                    logger.debug(f"复用进程: {alias or 'default'}")
                    return client, pool_key
                else:
                    # 不健康的进程，清理并重新创建
                    logger.info(f"清理不健康进程并重新创建: {alias or 'default'}")
                    await entry.cleanup()
                    del self._processes[pool_key]
            
            # 创建新进程
            logger.info(f"创建新进程: {alias or 'default'}")
            client = MCPStdioClient(
                server_script=server_script,
                alias=alias,
                config_dir=config_dir,
                **kwargs
            )
            
            # 连接并初始化
            await client.connect()
            await client.initialize()
            
            # 添加到进程池
            entry = ProcessPoolEntry(client, alias or 'default')
            self._processes[pool_key] = entry
            
            client_ref = await entry.acquire(pool_key)
            return client_ref, pool_key
    
    async def release_client(self, pool_key: str):
        """释放客户端"""
        async with self._lock:
            if pool_key in self._processes:
                await self._processes[pool_key].release()
    
    async def force_cleanup(self, alias: Optional[str] = None):
        """强制清理指定别名的进程"""
        async with self._lock:
            to_remove = []
            
            for key, entry in self._processes.items():
                if alias is None or entry.alias == alias:
                    logger.info(f"强制清理进程: {entry.alias}")
                    await entry.cleanup()
                    to_remove.append(key)
            
            for key in to_remove:
                del self._processes[key]
    
    async def get_status(self) -> Dict[str, Any]:
        """获取进程池状态"""
        async with self._lock:
            active_count = sum(1 for entry in self._processes.values() if entry.ref_count > 0)
            
            status = {
                'total_processes': len(self._processes),
                'active_processes': active_count,
                'processes': {}
            }
            
            for key, entry in self._processes.items():
                status['processes'][entry.alias] = {
                    'ref_count': entry.ref_count,
                    'last_used': time.time() - entry.last_used,
                    'is_healthy': entry.is_healthy,
                    'is_idle': entry.is_idle(self._timeout_seconds)
                }
            
            return status
    
    async def cleanup_all(self):
        """清理所有进程"""
        async with self._lock:
            for entry in list(self._processes.values()):
                await entry.cleanup()
            self._processes.clear()
            logger.info("已清理所有进程")
    
    async def shutdown(self):
        """关闭进程池"""
        # 停止清理任务
        if self._cleanup_task and not self._cleanup_task.done():
            self._cleanup_task.cancel()
            try:
                await self._cleanup_task
            except asyncio.CancelledError:
                pass
        
        # 清理所有进程
        await self.cleanup_all()


# 全局进程池实例
_process_pool = None


def get_process_pool() -> MCPProcessPool:
    """获取全局进程池实例"""
    global _process_pool
    if _process_pool is None:
        _process_pool = MCPProcessPool()
    return _process_pool


class PooledClient:
    """使用进程池的客户端包装器"""
    
    def __init__(self, server_script: str, alias: Optional[str] = None,
                 config_dir: Optional[str] = None, **kwargs):
        self.server_script = server_script
        self.alias = alias
        self.config_dir = config_dir
        self.kwargs = kwargs
        self._client = None
        self._pool_key = None
        self._pool = get_process_pool()
    
    async def __aenter__(self):
        """异步上下文管理器入口"""
        self._client, self._pool_key = await self._pool.get_client(
            self.server_script, self.alias, self.config_dir, **self.kwargs
        )
        return self._client
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """异步上下文管理器出口"""
        if self._pool_key:
            await self._pool.release_client(self._pool_key)
            self._client = None
            self._pool_key = None


# 便捷函数
async def get_pooled_client(server_script: str, alias: Optional[str] = None,
                           config_dir: Optional[str] = None, **kwargs) -> Tuple[MCPStdioClient, str]:
    """获取池化的客户端"""
    pool = get_process_pool()
    return await pool.get_client(server_script, alias, config_dir, **kwargs)


async def release_pooled_client(pool_key: str):
    """释放池化的客户端"""
    pool = get_process_pool()
    await pool.release_client(pool_key)


async def cleanup_process(alias: Optional[str] = None):
    """清理指定别名的进程"""
    pool = get_process_pool()
    await pool.force_cleanup(alias)


async def get_pool_status() -> Dict[str, Any]:
    """获取进程池状态"""
    pool = get_process_pool()
    return await pool.get_status()