"""
基于数据库的进程池管理器
使用SQLite数据库来持久化进程状态，避免内存状态不一致问题
"""

import sqlite3
import asyncio
import time
import os
import psutil
import json
from typing import Dict, Optional, Any, List
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class ProcessStateDB:
    """进程状态数据库管理器"""
    
    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            # 默认在用户目录下创建数据库
            home_dir = Path.home()
            db_dir = home_dir / ".mcp_framework"
            db_dir.mkdir(exist_ok=True)
            db_path = str(db_dir / "process_pool.db")
        
        self.db_path = db_path
        self._lock = asyncio.Lock()
        self._init_db()
    
    def _init_db(self):
        """初始化数据库表"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS process_pool (
                    alias TEXT PRIMARY KEY,
                    process_id INTEGER NOT NULL,
                    server_script TEXT NOT NULL,
                    config_dir TEXT,
                    server_args TEXT,
                    created_at REAL NOT NULL,
                    last_used REAL NOT NULL,
                    ref_count INTEGER DEFAULT 0,
                    is_healthy INTEGER DEFAULT 1,
                    pool_key TEXT NOT NULL
                )
            """)
            conn.commit()
        finally:
            conn.close()
    
    async def register_process(self, alias: str, process_id: int, server_script: str, 
                             pool_key: str, config_dir: Optional[str] = None, 
                             server_args: Optional[List[str]] = None) -> bool:
        """注册一个新进程"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                now = time.time()
                server_args_json = json.dumps(server_args) if server_args else None
                
                conn.execute("""
                    INSERT OR REPLACE INTO process_pool 
                    (alias, process_id, server_script, config_dir, server_args, 
                     created_at, last_used, ref_count, is_healthy, pool_key)
                    VALUES (?, ?, ?, ?, ?, ?, ?, 0, 1, ?)
                """, (alias, process_id, server_script, config_dir, server_args_json, 
                      now, now, pool_key))
                
                conn.commit()
                logger.info(f"注册进程: alias={alias}, pid={process_id}")
                return True
            except Exception as e:
                logger.error(f"注册进程失败: {e}")
                return False
            finally:
                conn.close()
    
    async def get_process_info(self, alias: str) -> Optional[Dict[str, Any]]:
        """根据别名获取进程信息"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                cursor = conn.execute("""
                    SELECT process_id, server_script, config_dir, server_args, 
                           created_at, last_used, ref_count, is_healthy, pool_key
                    FROM process_pool WHERE alias = ?
                """, (alias,))
                
                row = cursor.fetchone()
                if row:
                    server_args = json.loads(row[3]) if row[3] else None
                    return {
                        'process_id': row[0],
                        'server_script': row[1],
                        'config_dir': row[2],
                        'server_args': server_args,
                        'created_at': row[4],
                        'last_used': row[5],
                        'ref_count': row[6],
                        'is_healthy': bool(row[7]),
                        'pool_key': row[8]
                    }
                return None
            finally:
                conn.close()
    
    async def is_process_alive(self, process_id: int) -> bool:
        """检查进程是否还活着"""
        try:
            process = psutil.Process(process_id)
            return process.is_running()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            return False
    
    async def acquire_process(self, alias: str) -> Optional[Dict[str, Any]]:
        """获取进程（增加引用计数）"""
        async with self._lock:
            # 直接在锁内获取进程信息，避免重复获取锁
            conn = sqlite3.connect(self.db_path)
            try:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT process_id, server_script, config_dir, server_args,
                           created_at, last_used, ref_count, is_healthy, pool_key
                    FROM process_pool WHERE alias = ?
                """, (alias,))
                
                row = cursor.fetchone()
                if not row:
                    return None
                
                process_id = row[0]
                
                # 检查进程是否还活着
                if not await self.is_process_alive(process_id):
                    # 进程已死，清理记录
                    conn.execute("DELETE FROM process_pool WHERE alias = ?", (alias,))
                    conn.commit()
                    return None
                
                # 增加引用计数并更新最后使用时间
                conn.execute("""
                    UPDATE process_pool 
                    SET ref_count = ref_count + 1, last_used = ?
                    WHERE alias = ?
                """, (time.time(), alias))
                conn.commit()
                
                # 重新获取更新后的信息
                cursor.execute("""
                    SELECT process_id, server_script, config_dir, server_args,
                           created_at, last_used, ref_count, is_healthy, pool_key
                    FROM process_pool WHERE alias = ?
                """, (alias,))
                
                row = cursor.fetchone()
                if row:
                    server_args = json.loads(row[3]) if row[3] else None
                    return {
                        'process_id': row[0],
                        'server_script': row[1],
                        'config_dir': row[2],
                        'server_args': server_args,
                        'created_at': row[4],
                        'last_used': row[5],
                        'ref_count': row[6],
                        'is_healthy': bool(row[7]),
                        'pool_key': row[8]
                    }
                return None
            finally:
                conn.close()
    
    async def release_process(self, alias: str) -> bool:
        """释放进程（减少引用计数）"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                conn.execute("""
                    UPDATE process_pool 
                    SET ref_count = MAX(0, ref_count - 1), last_used = ?
                    WHERE alias = ?
                """, (time.time(), alias))
                conn.commit()
                return True
            except Exception as e:
                logger.error(f"释放进程失败: {e}")
                return False
            finally:
                conn.close()
    
    async def _cleanup_dead_process(self, alias: str):
        """清理死进程记录"""
        conn = sqlite3.connect(self.db_path)
        try:
            conn.execute("DELETE FROM process_pool WHERE alias = ?", (alias,))
            conn.commit()
            logger.info(f"清理死进程记录: alias={alias}")
        finally:
            conn.close()
    
    async def cleanup_idle_processes(self, idle_timeout: int = 1800) -> List[str]:
        """清理空闲进程（返回被清理的别名列表）"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                cutoff_time = time.time() - idle_timeout
                
                # 查找空闲进程
                cursor = conn.execute("""
                    SELECT alias, process_id FROM process_pool 
                    WHERE ref_count = 0 AND last_used < ?
                """, (cutoff_time,))
                
                idle_processes = cursor.fetchall()
                cleaned_aliases = []
                
                for alias, process_id in idle_processes:
                    try:
                        # 尝试终止进程
                        process = psutil.Process(process_id)
                        process.terminate()
                        process.wait(timeout=5)
                    except (psutil.NoSuchProcess, psutil.TimeoutExpired, psutil.AccessDenied):
                        pass
                    
                    # 删除数据库记录
                    conn.execute("DELETE FROM process_pool WHERE alias = ?", (alias,))
                    cleaned_aliases.append(alias)
                    logger.info(f"清理空闲进程: alias={alias}, pid={process_id}")
                
                conn.commit()
                return cleaned_aliases
            finally:
                conn.close()
    
    async def get_all_processes(self) -> List[Dict[str, Any]]:
        """获取所有进程信息"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                cursor = conn.execute("""
                    SELECT alias, process_id, server_script, config_dir, server_args,
                           created_at, last_used, ref_count, is_healthy, pool_key
                    FROM process_pool
                """)
                
                processes = []
                for row in cursor.fetchall():
                    server_args = json.loads(row[4]) if row[4] else None
                    processes.append({
                        'alias': row[0],
                        'process_id': row[1],
                        'server_script': row[2],
                        'config_dir': row[3],
                        'server_args': server_args,
                        'created_at': row[5],
                        'last_used': row[6],
                        'ref_count': row[7],
                        'is_healthy': bool(row[8]),
                        'pool_key': row[9]
                    })
                return processes
            finally:
                conn.close()
    
    async def cleanup_all(self):
        """清理所有进程"""
        async with self._lock:
            conn = sqlite3.connect(self.db_path)
            try:
                # 获取所有进程
                cursor = conn.execute("SELECT alias, process_id FROM process_pool")
                all_processes = cursor.fetchall()
                
                # 终止所有进程
                for alias, process_id in all_processes:
                    try:
                        process = psutil.Process(process_id)
                        process.terminate()
                        process.wait(timeout=5)
                    except (psutil.NoSuchProcess, psutil.TimeoutExpired, psutil.AccessDenied):
                        pass
                    logger.info(f"终止进程: alias={alias}, pid={process_id}")
                
                # 清空数据库
                conn.execute("DELETE FROM process_pool")
                conn.commit()
                logger.info("清理所有进程完成")
            finally:
                conn.close()