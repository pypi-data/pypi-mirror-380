# 腾讯云MCP基本使用示例

本文档展示了如何在Claude中使用腾讯云MCP服务器进行各种腾讯云操作。

## 1. 查看服务列表

**用户输入**：
```
我想了解腾讯云都有哪些服务
```

**Claude会执行**：
```json
{
  "name": "tencent_get_services",
  "arguments": {}
}
```

**期望结果**：返回支持的腾讯云服务列表，包括CVM、VPC、CBS等。

## 2. 了解特定服务的API

**用户输入**：
```
CVM服务都有哪些API可以调用？
```

**Claude会执行**：
```json
{
  "name": "tencent_get_service_info",
  "arguments": {
    "service": "cvm"
  }
}
```

**期望结果**：返回CVM服务的所有API列表和简要说明。

## 3. 获取API详细信息

**用户输入**：
```
我想了解DescribeInstances这个API怎么使用
```

**Claude会执行**：
```json
{
  "name": "tencent_get_action_info",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances"
  }
}
```

**期望结果**：返回DescribeInstances API的详细参数说明、使用方法和示例。

## 4. 查看可用地域

**用户输入**：
```
腾讯云有哪些可用地域？
```

**Claude会执行**：
```json
{
  "name": "tencent_get_regions",
  "arguments": {}
}
```

**期望结果**：返回所有可用地域列表，包括地域代码和中文名称。

## 5. 查询云服务器实例

**用户输入**：
```
帮我查看广州地区的所有云服务器实例
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "region": "ap-guangzhou",
    "parameters": {
      "Limit": 20
    }
  }
}
```

**期望结果**：返回广州地区的云服务器实例列表。

## 6. 查询特定实例

**用户输入**：
```
查看实例ID为ins-12345678的详细信息
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "parameters": {
      "InstanceIds": ["ins-12345678"]
    }
  }
}
```

## 7. 查询可用区

**用户输入**：
```
广州地区有哪些可用区？
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeZones",
    "region": "ap-guangzhou"
  }
}
```

## 8. 查询VPC列表

**用户输入**：
```
查看我的VPC网络列表
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "DescribeVpcs",
    "parameters": {
      "Limit": 20
    }
  }
}
```

## 9. 查询云硬盘

**用户输入**：
```
查看我的云硬盘使用情况
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "DescribeDisks",
    "parameters": {
      "Limit": 50
    }
  }
}
```

## 复合查询示例

### 查看资源概览

**用户输入**：
```
帮我查看腾讯云资源的整体情况，包括云服务器、VPC和云硬盘
```

Claude会依次执行多个查询：

1. 查询云服务器：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "parameters": {"Limit": 100}
  }
}
```

2. 查询VPC：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "DescribeVpcs",
    "parameters": {"Limit": 20}
  }
}
```

3. 查询云硬盘：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "DescribeDisks",
    "parameters": {"Limit": 100}
  }
}
```

然后Claude会汇总和分析这些结果，为用户提供清晰的资源概览。

## 监控数据查询

**用户输入**：
```
查看过去24小时内实例ins-12345678的CPU使用率
```

**Claude会执行**：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "monitor",
    "action": "GetMonitorData",
    "parameters": {
      "Namespace": "QCE/CVM",
      "MetricName": "CPUUsage",
      "Period": 300,
      "StartTime": "2024-11-28T00:00:00Z",
      "EndTime": "2024-11-29T00:00:00Z",
      "Instances": [
        {
          "Dimensions": [
            {
              "Name": "InstanceId",
              "Value": "ins-12345678"
            }
          ]
        }
      ]
    }
  }
}
```

## 错误处理示例

如果API调用失败，Claude会收到错误信息并帮助用户解决：

**用户输入**：
```
查看一个不存在的实例ins-notexist
```

**可能的错误响应**：
```
Error: Tencent Cloud API error: InvalidInstanceId.NotFound
```

Claude会解释错误含义并建议解决方案。

## 使用技巧

1. **先了解API**：在调用API前，先使用`tencent_get_action_info`了解参数要求
2. **指定地域**：根据需要指定region参数
3. **批量操作**：利用Limit参数控制返回数量
4. **自然语言**：可以用自然语言描述需求，Claude会选择合适的API调用