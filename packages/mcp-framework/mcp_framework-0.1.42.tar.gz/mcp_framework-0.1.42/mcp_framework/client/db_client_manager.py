"""
基于数据库的客户端管理器
通过进程ID来管理和获取MCP客户端实例
"""

import asyncio
import psutil
import weakref
from typing import Dict, Optional, Tuple, Any
import logging
from .base import MCPStdioClient
from .db_process_manager import ProcessStateDB

logger = logging.getLogger(__name__)


class DBClientManager:
    """基于数据库的客户端管理器"""
    
    def __init__(self, db_path: Optional[str] = None):
        self.db = ProcessStateDB(db_path)
        # 使用弱引用来存储活跃的客户端，避免内存泄漏
        self._active_clients: Dict[int, weakref.ref] = {}
        self._lock = asyncio.Lock()
    
    async def get_or_create_client(self, server_script: str, alias: Optional[str] = None,
                                 config_dir: Optional[str] = None, 
                                 server_args: Optional[list] = None,
                                 **kwargs) -> Tuple[MCPStdioClient, str]:
        """获取或创建客户端"""
        async with self._lock:
            # 生成唯一的pool_key
            pool_key = self._generate_pool_key(server_script, alias, config_dir, **kwargs)
            
            # 如果没有指定别名，使用pool_key作为别名
            if alias is None:
                alias = pool_key
            
            # 尝试从数据库获取现有进程
            process_info = await self.db.acquire_process(alias)
            
            if process_info:
                # 找到现有进程，尝试获取客户端
                process_id = process_info['process_id']
                client = await self._get_client_by_process_id(process_id)
                
                if client:
                    logger.info(f"复用现有客户端: alias={alias}, pid={process_id}")
                    return client, pool_key
                else:
                    # 客户端不存在，可能进程已死，清理数据库记录
                    logger.warning(f"进程存在但客户端不可用: alias={alias}, pid={process_id}")
                    await self.db._cleanup_dead_process(alias)
            
            # 创建新的客户端和进程
            client = await self._create_new_client(server_script, alias, config_dir, 
                                                 server_args, pool_key, **kwargs)
            return client, pool_key
    
    async def _get_client_by_process_id(self, process_id: int) -> Optional[MCPStdioClient]:
        """通过进程ID获取客户端"""
        # 首先检查内存中的弱引用
        if process_id in self._active_clients:
            client_ref = self._active_clients[process_id]
            client = client_ref()
            if client is not None:
                # 检查客户端是否还健康
                if await self._is_client_healthy(client):
                    return client
                else:
                    # 客户端不健康，清理引用
                    del self._active_clients[process_id]
        
        # 尝试通过进程ID重新连接到现有进程
        try:
            process = psutil.Process(process_id)
            if not process.is_running():
                return None
            
            # 这里需要重新连接到现有的stdio进程
            # 由于MCP使用stdio通信，我们需要重新创建客户端连接
            # 但这在实际中很困难，因为stdio管道是一次性的
            logger.warning(f"无法重新连接到现有进程 {process_id}，需要重新创建")
            return None
            
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return None
    
    async def _create_new_client(self, server_script: str, alias: str, 
                               config_dir: Optional[str], server_args: Optional[list],
                               pool_key: str, **kwargs) -> MCPStdioClient:
        """创建新的客户端"""
        try:
            # 创建新的MCP客户端
            client = MCPStdioClient(
                server_script=server_script,
                alias=alias,
                config_dir=config_dir,
                server_args=server_args,
                **kwargs
            )
            
            # 连接并初始化客户端
            await client.connect()
            await client.initialize()
            
            # 获取进程ID
            process_id = client.process.pid
            
            # 注册到数据库
            await self.db.register_process(
                alias=alias,
                process_id=process_id,
                server_script=server_script,
                pool_key=pool_key,
                config_dir=config_dir,
                server_args=server_args
            )
            
            # 添加到活跃客户端列表（使用弱引用）
            self._active_clients[process_id] = weakref.ref(client, 
                lambda ref: self._cleanup_client_ref(process_id))
            
            logger.info(f"创建新客户端: alias={alias}, pid={process_id}")
            return client
            
        except Exception as e:
            logger.error(f"创建客户端失败: {e}")
            raise
    
    def _cleanup_client_ref(self, process_id: int):
        """清理客户端弱引用"""
        if process_id in self._active_clients:
            del self._active_clients[process_id]
    
    async def _is_client_healthy(self, client: MCPStdioClient) -> bool:
        """检查客户端是否健康"""
        try:
            # 检查进程是否还在运行
            if not client.process:
                return False
            
            # 检查进程状态 - 兼容不同类型的process对象
            try:
                if hasattr(client.process, 'poll'):
                    # asyncio.subprocess.Process
                    if client.process.poll() is not None:
                        return False
                elif hasattr(client.process, 'returncode'):
                    # 检查returncode
                    if client.process.returncode is not None:
                        return False
                else:
                    # 其他类型的process对象，假设健康
                    pass
            except Exception as e:
                logger.warning(f"进程状态检查失败: {e}")
                return False
            
            # 检查连接状态
            if not hasattr(client, '_is_connected') or not client._is_connected:
                return False
            
            # 检查读写器状态
            if not hasattr(client, 'reader') or not hasattr(client, 'writer'):
                return False
                
            if not client.reader or not client.writer:
                return False
            
            if client.writer.is_closing():
                return False
            
            return True
        except Exception as e:
            logger.warning(f"客户端健康检查失败: {e}")
            return False
    
    def _generate_pool_key(self, server_script: str, alias: Optional[str] = None,
                          config_dir: Optional[str] = None, **kwargs) -> str:
        """生成池键"""
        import hashlib
        
        # 构建键的组件
        components = [server_script]
        
        if alias:
            components.append(f"alias:{alias}")
        
        if config_dir:
            components.append(f"config:{config_dir}")
        
        # 添加其他参数
        for key, value in sorted(kwargs.items()):
            if key not in ['client_name', 'client_version', 'startup_timeout', 'response_timeout']:
                components.append(f"{key}:{value}")
        
        # 生成哈希
        key_string = "|".join(components)
        return hashlib.md5(key_string.encode()).hexdigest()[:16]
    
    async def release_client(self, alias: str):
        """释放客户端"""
        await self.db.release_process(alias)
    
    async def cleanup_idle_clients(self, idle_timeout: int = 1800):
        """清理空闲客户端"""
        cleaned_aliases = await self.db.cleanup_idle_processes(idle_timeout)
        
        # 清理对应的客户端引用
        for alias in cleaned_aliases:
            # 从活跃客户端中移除（通过进程ID）
            process_info = await self.db.get_process_info(alias)
            if process_info:
                process_id = process_info['process_id']
                if process_id in self._active_clients:
                    del self._active_clients[process_id]
    
    async def get_status(self) -> Dict[str, Any]:
        """获取管理器状态"""
        all_processes = await self.db.get_all_processes()
        active_clients_count = len([ref for ref in self._active_clients.values() if ref() is not None])
        
        return {
            'total_processes': len(all_processes),
            'active_clients': active_clients_count,
            'processes': all_processes
        }
    
    async def cleanup_all(self):
        """清理所有客户端和进程"""
        # 清理数据库中的所有进程
        await self.db.cleanup_all()
        
        # 清理内存中的客户端引用
        self._active_clients.clear()


# 全局客户端管理器实例
_client_manager = None
_manager_lock = asyncio.Lock()


async def get_client_manager() -> DBClientManager:
    """获取全局客户端管理器实例"""
    global _client_manager
    
    if _client_manager is None:
        async with _manager_lock:
            if _client_manager is None:
                _client_manager = DBClientManager()
    
    return _client_manager