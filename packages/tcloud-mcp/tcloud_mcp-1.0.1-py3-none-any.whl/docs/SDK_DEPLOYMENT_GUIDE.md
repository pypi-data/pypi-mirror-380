# 腾讯云MCP服务器部署指南

## 🎯 无需安装TCCLI的解决方案

这个版本直接使用腾讯云Python SDK，**无需安装TCCLI**，大大简化了部署过程。

## 📦 安装依赖

### 方法1：使用requirements文件
```bash
pip install -r requirements.txt
```

### 方法2：手动安装
```bash
pip install tencentcloud-sdk-python>=3.0.1399 jmespath==0.10.0 six==1.16.0
```

## ⚙️ Claude Desktop配置

### 配置文件位置
- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%/Claude/claude_desktop_config.json`
- **Linux**: `~/.config/claude/claude_desktop_config.json`

### 配置内容
```json
{
  "mcpServers": {
    "tencent-cloud": {
      "command": "python",
      "args": ["/path/to/tccli-mcp/main.py"],
      "env": {
        "TENCENTCLOUD_SECRET_ID": "your-secret-id-here",
        "TENCENTCLOUD_SECRET_KEY": "your-secret-key-here",
        "TENCENTCLOUD_REGION": "ap-guangzhou"
      }
    }
  }
}
```

### 配置步骤
1. **获取腾讯云密钥**：
   - 登录[腾讯云控制台](https://console.cloud.tencent.com/)
   - 进入"访问管理" → "API密钥管理"
   - 创建或查看现有密钥

2. **修改配置**：
   - 将 `/path/to/tccli-mcp/main.py` 替换为实际路径
   - 将 `your-secret-id-here` 替换为真实SecretId
   - 将 `your-secret-key-here` 替换为真实SecretKey

3. **重启Claude Desktop**

## 🚀 功能特性

### 支持的服务
- **cvm**: 云服务器管理
- **vpc**: 私有网络管理
- **cbs**: 云硬盘管理
- **cls**: 日志服务管理
- **clb**: 负载均衡管理
- **monitor**: 监控数据获取

### 可用工具

#### 1. `tencent_call_api` - 调用API
```
用法示例：
- "帮我查看广州地区的云服务器"
- "创建一台2核4G的云服务器"
- "查看我的VPC网络列表"
```

#### 2. `tencent_get_regions` - 获取地域列表
```
用法示例：
- "腾讯云有哪些可用地域？"
```

#### 3. `tencent_get_services` - 获取支持的服务
```
用法示例：
- "这个MCP支持哪些腾讯云服务？"
```

#### 4. `tencent_get_service_info` - 获取服务信息
```
用法示例：
- "CVM服务有哪些API可以调用？"
```

#### 5. `tencent_get_action_info` - 获取API详情
```
用法示例：
- "DescribeInstances这个API怎么使用？"
```

## 💡 优势特点

### 相比TCCLI版本的优势

| 特性 | SDK版本 | TCCLI版本 |
|------|---------|-----------|
| **部署难度** | ✅ 简单 | ❌ 复杂 |
| **依赖要求** | ✅ 只需SDK | ❌ 需要安装TCCLI |
| **性能** | ✅ 直接调用 | ⚠️ 命令行开销 |
| **功能覆盖** | ⚠️ 6个核心服务 | ✅ 所有服务 |
| **文档丰富度** | ⚠️ 基础文档 | ✅ 完整help系统 |
| **维护成本** | ✅ 低 | ⚠️ 中等 |

### 推荐使用场景

**SDK版本适合**：
- ✅ 新用户快速上手
- ✅ 主要使用核心服务（CVM、VPC、CBS等）
- ✅ 追求简单部署
- ✅ 分发给团队成员

## 🔧 测试验证

### 手动测试
```bash
cd /path/to/tccli-mcp
python main.py
```

发送测试请求：
```json
{"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
```

### Claude Desktop测试
```
你: 腾讯云有哪些可用地域？
你: 帮我查看广州地区的云服务器
你: CVM服务有哪些API可以调用？
```

## 📁 项目结构

```
tccli-mcp/
├── main.py                      # 主入口文件
├── src/
│   ├── tencent_sdk_wrapper.py   # SDK包装器
│   └── sdk_server.py            # MCP服务器
├── requirements.txt             # 依赖文件
└── config/claude_desktop_config.json # 配置模板
```

## 🛡️ 安全建议

1. **使用子用户密钥**：
   - 不要使用主账户密钥
   - 为MCP创建专门的子用户
   - 只授予必要的权限

2. **保护配置文件**：
   ```bash
   chmod 600 ~/.config/claude/claude_desktop_config.json
   ```

3. **定期轮换密钥**：
   - 定期更新SecretId和SecretKey
   - 删除不再使用的密钥

## 🎉 部署完成

选择SDK版本可以：
- 🚀 3分钟完成部署
- 💻 无需额外安装工具
- 🔧 支持核心云服务管理
- 📱 易于分享和部署

立即开始通过自然语言管理腾讯云资源！