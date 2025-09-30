"""
MCP 工具调用客户端
提供便捷的工具列表获取和工具调用功能
"""

import json
import asyncio
from typing import Dict, Any, List, Optional, AsyncGenerator
from .enhanced import EnhancedMCPStdioClient


class Tool:
    """工具信息类"""
    
    def __init__(self, name: str, description: str = "", input_schema: Optional[Dict[str, Any]] = None):
        self.name = name
        self.description = description
        self.input_schema = input_schema or {}
    
    def __repr__(self):
        return f"Tool(name='{self.name}', description='{self.description}')"


class ToolsClient(EnhancedMCPStdioClient):
    """MCP 工具调用客户端"""
    
    @classmethod
    def _wrap_existing_client(cls, existing_client):
        """
        包装现有的MCPStdioClient实例为ToolsClient
        用于进程池管理中复用已连接的客户端
        
        Args:
            existing_client: 已连接的MCPStdioClient实例或SharedClientWrapper
            
        Returns:
            ToolsClient: 包装后的工具客户端
        """
        # 创建一个新的ToolsClient实例，但不调用父类初始化
        instance = cls.__new__(cls)
        
        # 检查是否是SharedClientWrapper
        if hasattr(existing_client, '_underlying_client'):
            # 这是一个SharedClientWrapper，我们需要从底层客户端复制属性
            underlying_client = existing_client._underlying_client
            instance.__dict__.update(underlying_client.__dict__)
            
            # 同时保留包装器的特殊属性
            instance._underlying_client = existing_client._underlying_client
            instance._pool_entry = existing_client._pool_entry
            instance._pool_key = existing_client._pool_key
            instance._is_released = existing_client._is_released
            
            # 重要：重写关键方法以使用底层客户端
            def get_next_id_wrapper():
                return underlying_client.get_next_id()
            instance.get_next_id = get_next_id_wrapper
            
            # 代理send_request方法到底层客户端
            async def send_request_wrapper(method, params=None, timeout=None):
                return await underlying_client.send_request(method, params, timeout)
            instance.send_request = send_request_wrapper
            
            # 代理_read_response方法到底层客户端
            async def read_response_wrapper():
                return await underlying_client._read_response()
            instance._read_response = read_response_wrapper
            
            # 直接设置process属性指向底层客户端的process
            instance.process = underlying_client.process
            
            # 确保连接和初始化状态正确传递
            instance.is_connected = underlying_client.is_connected
            instance.is_initialized = underlying_client.is_initialized
        else:
            # 这是一个普通的MCPStdioClient，需要正确代理所有方法
            underlying_client = existing_client
            
            # 复制基本属性
            for attr in ['server_script', 'alias', 'server_args', 'client_name', 
                        'client_version', 'startup_timeout', 'response_timeout', 
                        'config_dir', '_request_id', 'process']:
                if hasattr(existing_client, attr):
                    setattr(instance, attr, getattr(existing_client, attr))
            
            # 代理关键方法
            def get_next_id_wrapper():
                return underlying_client.get_next_id()
            instance.get_next_id = get_next_id_wrapper
            
            # 代理send_request方法到底层客户端
            async def send_request_wrapper(method, params=None, timeout=None):
                return await underlying_client.send_request(method, params, timeout)
            instance.send_request = send_request_wrapper
            
            # 代理_read_response方法到底层客户端
            async def read_response_wrapper():
                return await underlying_client._read_response()
            instance._read_response = read_response_wrapper
            
            # 代理connect方法
            async def connect_wrapper():
                return await underlying_client.connect()
            instance.connect = connect_wrapper
            
            # 代理initialize方法
            async def initialize_wrapper(protocol_version="2024-11-05", capabilities=None):
                return await underlying_client.initialize(protocol_version, capabilities)
            instance.initialize = initialize_wrapper
            
            # 代理disconnect方法
            async def disconnect_wrapper():
                return await underlying_client.disconnect()
            instance.disconnect = disconnect_wrapper
            
            # 确保连接和初始化状态正确传递
            instance.is_connected = existing_client.is_connected
            instance.is_initialized = existing_client.is_initialized
        
        # 设置ToolsClient特有的属性
        instance._tools_cache = None
        instance._tools_cache_time = 0
        instance._cache_ttl = 60  # 缓存60秒
        
        # 确保EnhancedMCPStdioClient的属性存在
        if not hasattr(instance, 'debug_mode'):
            instance.debug_mode = False
        
        return instance
    
    def __init__(self, 
                 server_script: str,
                 alias: Optional[str] = None,
                 config_dir: Optional[str] = None,
                 server_args: Optional[List[str]] = None,
                 client_name: str = "mcp-framework-client",
                 client_version: str = "1.0.0",
                 startup_timeout: float = 5.0,
                 response_timeout: float = 30.0):
        """
        初始化 MCP 工具调用客户端
        
        Args:
            server_script: 服务器脚本路径
            alias: 服务器别名（重要参数，用于多实例管理）
            config_dir: 自定义配置目录路径（可选）
            server_args: 额外的服务器参数
            client_name: 客户端名称
            client_version: 客户端版本
            startup_timeout: 启动超时时间（秒）
            response_timeout: 响应超时时间（秒）
        """
        super().__init__(
            server_script=server_script,
            alias=alias,
            config_dir=config_dir,
            server_args=server_args,
            client_name=client_name,
            client_version=client_version,
            startup_timeout=startup_timeout,
            response_timeout=response_timeout
        )
        self._tools_cache = None
    
    async def _ensure_connected(self):
        """确保客户端已连接和初始化"""
        # 如果这是一个包装的客户端（来自进程池），不要重新连接
        if hasattr(self, '_underlying_client') and hasattr(self, '_pool_entry'):
            # 这是一个SharedClientWrapper，检查底层客户端状态
            if not self._underlying_client.is_connected:
                raise RuntimeError("进程池中的客户端连接已断开")
            if not self._underlying_client.is_initialized:
                raise RuntimeError("进程池中的客户端未初始化")
            return
        
        # 普通客户端的连接逻辑
        if not self.is_connected:
            await self.connect()
        if not self.is_initialized:
            await self.initialize()
    
    async def list_tools(self, force_refresh: bool = False) -> List[Tool]:
        """
        获取可用工具列表
        
        Args:
            force_refresh: 是否强制刷新缓存
            
        Returns:
            List[Tool]: 工具列表
            
        Raises:
            Exception: 获取工具列表失败
        """
        await self._ensure_connected()
        
        # 使用缓存（除非强制刷新）
        if self._tools_cache is not None and not force_refresh:
            return self._tools_cache
        
        response = await self.send_request("tools/list")
        
        if "error" in response:
            raise Exception(f"获取工具列表失败: {response['error']}")
        
        result = response.get("result", {})
        tools_data = result.get("tools", [])
        
        # 转换为 Tool 对象
        tools = []
        for tool_data in tools_data:
            tool = Tool(
                name=tool_data.get("name", ""),
                description=tool_data.get("description", ""),
                input_schema=tool_data.get("inputSchema", {})
            )
            tools.append(tool)
        
        # 缓存结果
        self._tools_cache = tools
        return tools
    
    async def get_tool(self, tool_name: str) -> Optional[Tool]:
        """
        获取特定工具的信息
        
        Args:
            tool_name: 工具名称
            
        Returns:
            Optional[Tool]: 工具对象，如果不存在则返回 None
        """
        tools = await self.list_tools()
        
        for tool in tools:
            if tool.name == tool_name:
                return tool
        
        return None
    
    async def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        调用指定工具
        
        Args:
            tool_name: 工具名称
            arguments: 工具参数
            
        Returns:
            Dict[str, Any]: 工具执行结果
            
        Raises:
            Exception: 工具调用失败
        """
        await self._ensure_connected()
        
        params = {
            "name": tool_name,
            "arguments": arguments
        }
        
        response = await self.send_request("tools/call", params)
        
        if "error" in response:
            raise Exception(f"工具调用失败: {response['error']}")
        
        return response.get("result", {})
    
    async def tool_exists(self, tool_name: str) -> bool:
        """
        检查工具是否存在
        
        Args:
            tool_name: 工具名称
            
        Returns:
            bool: 工具是否存在
        """
        tool = await self.get_tool(tool_name)
        return tool is not None
    
    async def get_tool_names(self) -> List[str]:
        """
        获取所有工具名称列表
        
        Returns:
            List[str]: 工具名称列表
        """
        tools = await self.list_tools()
        return [tool.name for tool in tools]
    
    async def call_tool_stream(self, tool_name: str, arguments: Dict[str, Any]) -> AsyncGenerator[str, None]:
        """
        流式调用指定工具
        
        Args:
            tool_name: 工具名称
            arguments: 工具参数
            
        Yields:
            str: 流式输出的内容块
            
        Raises:
            Exception: 工具调用失败
        """
        await self._ensure_connected()
        
        params = {
            "name": tool_name,
            "arguments": arguments,
            "stream": True  # 标记为流式请求
        }
        
        # 发送流式请求
        request = {
            "jsonrpc": "2.0",
            "method": "tools/call",
            "id": self.get_next_id(),
            "params": params
        }
        
        request_json = json.dumps(request) + "\n"
        
        try:
            # 检查进程状态
            if self.process.returncode is not None:
                raise Exception(f"服务器进程已退出，返回码: {self.process.returncode}")
            
            # 发送请求
            self.process.stdin.write(request_json.encode())
            await self.process.stdin.drain()
            
            # 读取流式响应
            async for chunk in self._read_stream_response():
                yield chunk
                
        except Exception as e:
            raise Exception(f"流式工具调用失败: {e}")
    
    async def _read_stream_response(self) -> AsyncGenerator[str, None]:
        """
        读取流式响应
        
        Yields:
            str: 流式内容块
        """
        while True:
            try:
                # 读取一行响应
                response_line = await asyncio.wait_for(
                    self.process.stdout.readline(),
                    timeout=30.0
                )
                
                if not response_line:
                    break
                
                line_text = response_line.decode().strip()
                
                if not line_text:
                    continue
                
                # 跳过非JSON行（如日志输出）
                if (line_text.startswith('✅') or 
                    line_text.startswith('📂') or 
                    line_text.startswith('🔍') or 
                    line_text.startswith('❌') or 
                    line_text.startswith('🔧') or 
                    line_text.startswith('🚀') or 
                    line_text.startswith('🎯') or 
                    line_text.startswith('🛠️') or 
                    line_text.startswith('📁') or 
                    line_text.startswith('📡') or 
                    line_text.startswith('👋') or
                    not line_text.startswith('{')):
                    continue
                
                try:
                    response = json.loads(line_text)
                    
                    # 检查是否是有效的JSON-RPC响应
                    if not isinstance(response, dict) or 'jsonrpc' not in response:
                        continue
                    
                    # 检查是否有错误
                    if "error" in response:
                        raise Exception(f"流式调用错误: {response['error']}")
                    
                    # 处理不同类型的流式响应
                    method = response.get("method", "")
                    
                    # 处理流式数据块
                    if method == "stream/chunk":
                        params = response.get("params", {})
                        chunk = params.get("chunk", {})
                        content = chunk.get("content", "")
                        if content:
                            yield content
                    
                    # 处理流结束标记
                    elif method == "stream/end":
                        break
                    
                    # 处理流错误
                    elif method == "stream/error":
                        params = response.get("params", {})
                        error_msg = params.get("error", "未知流式错误")
                        raise Exception(f"流式调用错误: {error_msg}")
                    
                    # 兼容标准JSON-RPC响应格式
                    elif "result" in response:
                        result = response.get("result", {})
                        
                        # 检查是否是流结束标记
                        if result.get("type") == "stream_end":
                            break
                        
                        # 提取内容
                        if result.get("type") == "tool_result_chunk":
                            content = result.get("content", "")
                            if content:
                                yield content
                        elif "content" in result:
                            # 兼容其他格式
                            yield str(result["content"])
                        
                except json.JSONDecodeError:
                    continue
                    
            except asyncio.TimeoutError:
                break
            except Exception as e:
                raise Exception(f"读取流式响应失败: {e}")

    async def validate_tool_arguments(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        验证工具参数（基于工具的输入模式）
        
        Args:
            tool_name: 工具名称
            arguments: 要验证的参数
            
        Returns:
            Dict[str, Any]: 验证结果，包含 valid 字段和可能的错误信息
        """
        tool = await self.get_tool(tool_name)
        
        if not tool:
            return {
                "valid": False,
                "errors": [f"工具 '{tool_name}' 不存在"]
            }
        
        # 简单的参数验证（基于 JSON Schema）
        input_schema = tool.input_schema
        errors = []
        
        # 检查必需参数
        required_props = input_schema.get("required", [])
        for prop in required_props:
            if prop not in arguments:
                errors.append(f"缺少必需参数: {prop}")
        
        # 检查参数类型（简化版本）
        properties = input_schema.get("properties", {})
        for arg_name, arg_value in arguments.items():
            if arg_name in properties:
                prop_schema = properties[arg_name]
                expected_type = prop_schema.get("type")
                
                if expected_type == "string" and not isinstance(arg_value, str):
                    errors.append(f"参数 '{arg_name}' 应为字符串类型")
                elif expected_type == "integer" and not isinstance(arg_value, int):
                    errors.append(f"参数 '{arg_name}' 应为整数类型")
                elif expected_type == "boolean" and not isinstance(arg_value, bool):
                    errors.append(f"参数 '{arg_name}' 应为布尔类型")
                elif expected_type == "object" and not isinstance(arg_value, dict):
                    errors.append(f"参数 '{arg_name}' 应为对象类型")
                elif expected_type == "array" and not isinstance(arg_value, list):
                    errors.append(f"参数 '{arg_name}' 应为数组类型")
        
        return {
            "valid": len(errors) == 0,
            "errors": errors
        }


# 便捷函数
async def list_server_tools(server_script: str, 
                           alias: Optional[str] = None,
                           **kwargs) -> List[Tool]:
    """
    便捷函数：获取服务器工具列表
    
    Args:
        server_script: 服务器脚本路径
        alias: 服务器别名
        **kwargs: 其他客户端参数
        
    Returns:
        List[Tool]: 工具列表
    """
    async with ToolsClient(server_script, alias, **kwargs) as client:
        return await client.list_tools()


async def call_server_tool(server_script: str,
                          tool_name: str,
                          arguments: Dict[str, Any],
                          alias: Optional[str] = None,
                          **kwargs) -> Dict[str, Any]:
    """
    便捷函数：调用服务器工具
    
    Args:
        server_script: 服务器脚本路径
        tool_name: 工具名称
        arguments: 工具参数
        alias: 服务器别名
        **kwargs: 其他客户端参数
        
    Returns:
        Dict[str, Any]: 工具执行结果
    """
    async with ToolsClient(server_script, alias, **kwargs) as client:
        return await client.call_tool(tool_name, arguments)