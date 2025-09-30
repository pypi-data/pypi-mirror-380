#!/usr/bin/env python3
"""
Tencent Cloud SDK MCP Server

A Model Context Protocol server using Tencent Cloud SDK directly.
No TCCLI installation required - only needs tencentcloud-sdk-python.
"""

import asyncio
import json
import sys
import logging
from typing import Dict, Any
from .tencent_sdk_wrapper import TencentSDKWrapper

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class TencentSDKMCPServer:
    """MCP Server using Tencent Cloud SDK directly."""

    def __init__(self):
        self.name = "tencent-cloud-mcp"
        self.version = "1.0.0"
        self.sdk_wrapper = None

    def _ensure_sdk_wrapper(self):
        """Lazy initialization of SDK wrapper."""
        if self.sdk_wrapper is None:
            try:
                self.sdk_wrapper = TencentSDKWrapper()
            except ValueError as e:
                logger.error(f"Failed to initialize SDK: {e}")
                raise

    async def handle_initialize(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Handle MCP initialize request."""
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {}
            },
            "serverInfo": {
                "name": self.name,
                "version": self.version
            }
        }

    async def handle_tools_list(self) -> Dict[str, Any]:
        """Return list of available tools."""
        return {
            "tools": [
                {
                    "name": "tencent_call_api",
                    "description": """调用腾讯云API执行操作。

⚠️ 重要提醒：
- 需要设置环境变量 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY
- 大多数API需要指定region参数，建议明确指定避免误操作
- 支持的服务：cvm(云服务器)、vpc(私有网络)、cbs(云硬盘)、cls(日志服务)、clb(负载均衡)、monitor(监控)

常用地域：
- ap-guangzhou: 华南地区(广州)
- ap-shanghai: 华东地区(上海)
- ap-beijing: 华北地区(北京)
- ap-chengdu: 西南地区(成都)
- ap-hongkong: 港澳台地区(香港)

常用操作：
- Describe*: 查询资源
- Create*: 创建资源
- Delete*/Terminate*: 删除资源
- Modify*: 修改资源配置""",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "service": {
                                "type": "string",
                                "description": "腾讯云服务名称：cvm, vpc, cbs, cls, clb, monitor"
                            },
                            "action": {
                                "type": "string",
                                "description": "API操作名称，如DescribeInstances、RunInstances等"
                            },
                            "parameters": {
                                "type": "object",
                                "description": "API参数，JSON对象格式"
                            },
                            "region": {
                                "type": "string",
                                "description": "地域代码，强烈建议明确指定。常用：ap-guangzhou(广州)、ap-shanghai(上海)、ap-beijing(北京)"
                            }
                        },
                        "required": ["service", "action"]
                    }
                },
                {
                    "name": "tencent_get_regions",
                    "description": """获取所有可用的腾讯云地域列表。

返回腾讯云支持的所有地域信息，包括地域代码、中文名称和可用状态。
在调用需要指定地域的API前，建议先了解可用地域。""",
                    "inputSchema": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "tencent_get_services",
                    "description": """获取当前支持的腾讯云服务列表。

返回MCP服务器支持的腾讯云服务列表。目前支持：
- cvm: 云服务器
- vpc: 私有网络
- cbs: 云硬盘
- cls: 日志服务
- clb: 负载均衡
- monitor: 监控""",
                    "inputSchema": {
                        "type": "object",
                        "properties": {}
                    }
                },
                {
                    "name": "tencent_get_service_info",
                    "description": """获取特定服务的详细信息。

返回指定服务支持的所有API操作列表，帮助了解可以调用哪些功能。""",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "service": {
                                "type": "string",
                                "description": "腾讯云服务名称，如cvm、vpc等"
                            }
                        },
                        "required": ["service"]
                    }
                },
                {
                    "name": "tencent_get_action_info",
                    "description": """获取特定API操作的详细信息。

返回指定API的参数结构和示例，帮助理解如何调用该API。""",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "service": {
                                "type": "string",
                                "description": "腾讯云服务名称"
                            },
                            "action": {
                                "type": "string",
                                "description": "API操作名称"
                            }
                        },
                        "required": ["service", "action"]
                    }
                }
            ]
        }

    async def handle_tools_call(self, name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """Handle tool calls."""
        try:
            self._ensure_sdk_wrapper()

            if name == "tencent_call_api":
                result = await self.sdk_wrapper.call_api(
                    service=arguments["service"],
                    action=arguments["action"],
                    parameters=arguments.get("parameters"),
                    region=arguments.get("region")
                )

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": json.dumps(result, ensure_ascii=False, indent=2)
                        }
                    ]
                }

            elif name == "tencent_get_regions":
                regions = await self.sdk_wrapper.get_regions()

                # Format regions nicely
                if regions:
                    formatted_text = "=== 腾讯云可用地域列表 ===\n\n"
                    formatted_text += f"总计: {len(regions)} 个地域\n\n"

                    for region in regions:
                        region_code = region.get("Region", "")
                        region_name = region.get("RegionName", "")
                        region_state = region.get("RegionState", "")

                        status_icon = "✅" if region_state == "AVAILABLE" else "❌"
                        formatted_text += f"{status_icon} {region_code} - {region_name}\n"
                else:
                    formatted_text = "❌ 无法获取地域列表"

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": formatted_text
                        }
                    ]
                }

            elif name == "tencent_get_services":
                services = await self.sdk_wrapper.get_available_services()

                formatted_text = "=== 支持的腾讯云服务 ===\n\n"
                service_descriptions = {
                    "cvm": "云服务器 - 管理虚拟机实例",
                    "vpc": "私有网络 - 管理网络和子网",
                    "cbs": "云硬盘 - 管理存储设备",
                    "cls": "日志服务 - 管理日志收集和分析",
                    "clb": "负载均衡 - 管理流量分发",
                    "monitor": "监控 - 获取监控数据和告警"
                }

                for service in services:
                    description = service_descriptions.get(service, "腾讯云服务")
                    formatted_text += f"✅ {service} - {description}\n"

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": formatted_text
                        }
                    ]
                }

            elif name == "tencent_get_service_info":
                service = arguments["service"]
                info = self.sdk_wrapper.get_service_info(service)

                if "error" in info:
                    formatted_text = f"❌ {info['error']}"
                else:
                    formatted_text = f"=== {service.upper()} 服务信息 ===\n\n"
                    formatted_text += f"服务: {info['service']}\n"
                    formatted_text += f"接入点: {info['endpoint']}\n"
                    formatted_text += f"可用API数量: {info['total_actions']}\n\n"
                    formatted_text += "可用API操作:\n"

                    for action in info['available_actions'][:20]:  # Show first 20
                        formatted_text += f"  - {action}\n"

                    if info['total_actions'] > 20:
                        formatted_text += f"  ... 还有 {info['total_actions'] - 20} 个API\n"

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": formatted_text
                        }
                    ]
                }

            elif name == "tencent_get_action_info":
                service = arguments["service"]
                action = arguments["action"]
                info = self.sdk_wrapper.get_action_info(service, action)

                if "error" in info:
                    formatted_text = f"❌ {info['error']}"
                else:
                    formatted_text = f"=== {service.upper()}.{action} API信息 ===\n\n"
                    formatted_text += f"服务: {info['service']}\n"
                    formatted_text += f"操作: {info['action']}\n"
                    formatted_text += f"请求类: {info['request_class']}\n"
                    formatted_text += f"响应类: {info['response_class']}\n\n"

                    if info.get('request_available'):
                        formatted_text += "参数结构示例:\n"
                        formatted_text += info.get('sample_request', '{}')
                    else:
                        formatted_text += "❌ 该API不可用"

                return {
                    "content": [
                        {
                            "type": "text",
                            "text": formatted_text
                        }
                    ]
                }

            else:
                return {
                    "content": [
                        {
                            "type": "text",
                            "text": f"Unknown tool: {name}"
                        }
                    ],
                    "isError": True
                }

        except Exception as e:
            logger.error(f"Tool call error: {e}")
            return {
                "content": [
                    {
                        "type": "text",
                        "text": f"Error: {str(e)}"
                    }
                ],
                "isError": True
            }

    async def handle_request(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming MCP request."""
        method = request.get("method")
        params = request.get("params", {})
        request_id = request.get("id")

        try:
            if method == "initialize":
                result = await self.handle_initialize(params)
            elif method == "tools/list":
                result = await self.handle_tools_list()
            elif method == "tools/call":
                result = await self.handle_tools_call(
                    params["name"],
                    params["arguments"]
                )
            else:
                raise Exception(f"Unknown method: {method}")

            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "result": result
            }

        except Exception as e:
            logger.error(f"Request handling error: {e}")
            return {
                "jsonrpc": "2.0",
                "id": request_id,
                "error": {
                    "code": -1,
                    "message": str(e)
                }
            }

    async def run(self):
        """Run the MCP server using stdio."""
        logger.info("Starting Tencent Cloud SDK MCP Server")

        try:
            while True:
                # Read request from stdin
                line = await asyncio.get_event_loop().run_in_executor(
                    None, sys.stdin.readline
                )

                if not line:
                    break

                line = line.strip()
                if not line:
                    continue

                try:
                    request = json.loads(line)
                    response = await self.handle_request(request)

                    # Write response to stdout
                    print(json.dumps(response, ensure_ascii=False), flush=True)

                except json.JSONDecodeError as e:
                    logger.error(f"Invalid JSON request: {e}")
                    error_response = {
                        "jsonrpc": "2.0",
                        "id": None,
                        "error": {
                            "code": -32700,
                            "message": "Parse error"
                        }
                    }
                    print(json.dumps(error_response), flush=True)

        except KeyboardInterrupt:
            logger.info("Server stopped by user")
        except Exception as e:
            logger.error(f"Server error: {e}")
            raise


async def main():
    """Main entry point."""
    server = TencentSDKMCPServer()
    await server.run()


if __name__ == "__main__":
    asyncio.run(main())