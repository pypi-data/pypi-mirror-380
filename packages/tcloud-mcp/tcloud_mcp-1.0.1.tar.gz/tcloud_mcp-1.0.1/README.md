# 腾讯云MCP服务器

通过自然语言与腾讯云服务交互的模型上下文协议(MCP)服务器。

## ✨ 特性

- **开箱即用**: 无需安装TCCLI，只需要腾讯云SDK
- **轻量级**: 直接调用SDK，性能优异
- **易部署**: 分发友好，部署简单
- **安全**: 支持环境变量配置密钥

## 🚀 快速开始

1. **安装依赖**:
   ```bash
   pip install -r requirements.txt
   ```

2. **配置Claude Desktop**:
   ```json
   {
     "mcpServers": {
       "tencent-cloud": {
         "command": "python",
         "args": ["/path/to/main.py"],
         "env": {
           "TENCENTCLOUD_SECRET_ID": "your-secret-id",
           "TENCENTCLOUD_SECRET_KEY": "your-secret-key",
           "TENCENTCLOUD_REGION": "ap-guangzhou"
         }
       }
     }
   }
   ```

3. **开始使用**:
   ```
   你: 腾讯云有哪些可用地域？
   你: 帮我查看广州地区的云服务器
   你: 创建一个新的VPC网络
   ```

## 📁 项目结构

```
tccli-mcp/
├── main.py                      # 主入口文件
├── requirements.txt             # 依赖文件
├── src/                         # 源代码
│   ├── sdk_server.py           # MCP服务器实现
│   └── tencent_sdk_wrapper.py  # SDK包装器
├── config/                      # 配置文件
├── docs/                        # 文档
├── examples/                    # 使用示例
└── tests/                       # 测试文件
```

## 🎯 支持的服务

- **CVM**: 云服务器管理
- **VPC**: 私有网络管理
- **CBS**: 云硬盘管理
- **CLS**: 日志服务管理
- **CLB**: 负载均衡管理
- **Monitor**: 监控数据获取

## 🛠️ 可用工具

1. **tencent_call_api** - 调用腾讯云API
2. **tencent_get_regions** - 获取可用地域列表
3. **tencent_get_services** - 获取支持的服务列表
4. **tencent_get_service_info** - 获取服务详细信息
5. **tencent_get_action_info** - 获取API操作详细信息

## 🌍 常用地域

- `ap-guangzhou`: 华南地区(广州)
- `ap-shanghai`: 华东地区(上海)
- `ap-beijing`: 华北地区(北京)
- `ap-chengdu`: 西南地区(成都)
- `ap-hongkong`: 港澳台地区(香港)

## 📖 详细文档

- [配置示例](config/) - Claude Desktop配置模板
- [使用示例](examples/) - 各种使用场景示例

## 🔒 安全建议

1. 使用子用户密钥，避免使用主账户密钥
2. 只授予必要的权限
3. 定期轮换密钥
4. 不要将密钥提交到版本控制系统

## 📝 许可证

MIT License

---

开始使用腾讯云MCP服务器，体验AI与云服务的无缝交互！🎉