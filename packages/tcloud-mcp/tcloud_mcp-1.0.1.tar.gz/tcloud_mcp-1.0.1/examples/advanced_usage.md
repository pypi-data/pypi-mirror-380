# 腾讯云MCP高级使用示例

本文档展示了腾讯云MCP的高级使用场景和复杂操作示例。

## 1. 创建云服务器实例

### 场景：创建一台用于开发的云服务器

**用户输入**：
```
我需要在广州创建一台2核4G的云服务器，用于开发测试，要求：
- 使用CentOS 7.9镜像
- 系统盘50GB
- 要有公网IP
- 设置自定义密码
```

**Claude的操作流程**：

1. 首先获取RunInstances API信息：
```json
{
  "name": "tencent_get_action_info",
  "arguments": {
    "service": "cvm",
    "action": "RunInstances"
  }
}
```

2. 查询可用的镜像ID：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeImages",
    "region": "ap-guangzhou",
    "parameters": {
      "Filters": [
        {
          "Name": "image-name",
          "Values": ["CentOS 7.9*"]
        }
      ],
      "Limit": 10
    }
  }
}
```

3. 执行创建操作：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "RunInstances",
    "region": "ap-guangzhou",
    "parameters": {
      "InstanceType": "S5.MEDIUM2",
      "ImageId": "img-l8og963d",
      "Placement": {
        "Zone": "ap-guangzhou-3"
      },
      "SystemDisk": {
        "DiskType": "CLOUD_PREMIUM",
        "DiskSize": 50
      },
      "InternetAccessible": {
        "InternetChargeType": "TRAFFIC_POSTPAID_BY_HOUR",
        "InternetMaxBandwidthOut": 10,
        "PublicIpAssigned": true
      },
      "InstanceCount": 1,
      "InstanceName": "dev-server-001",
      "LoginSettings": {
        "Password": "DevServer@123"
      },
      "InstanceChargeType": "POSTPAID_BY_HOUR"
    }
  }
}
```

## 2. 网络配置管理

### 场景：创建完整的网络环境

**用户输入**：
```
帮我在北京创建一个完整的网络环境：
- VPC网络段：10.0.0.0/16
- 两个子网：web子网(10.0.1.0/24)和db子网(10.0.2.0/24)
- 配置安全组规则
```

**Claude的操作流程**：

1. 创建VPC：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "CreateVpc",
    "region": "ap-beijing",
    "parameters": {
      "VpcName": "production-vpc",
      "CidrBlock": "10.0.0.0/16"
    }
  }
}
```

2. 创建Web子网：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "CreateSubnet",
    "region": "ap-beijing",
    "parameters": {
      "VpcId": "vpc-xxxxxxxx",
      "SubnetName": "web-subnet",
      "CidrBlock": "10.0.1.0/24",
      "Zone": "ap-beijing-1"
    }
  }
}
```

3. 创建DB子网：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "CreateSubnet",
    "region": "ap-beijing",
    "parameters": {
      "VpcId": "vpc-xxxxxxxx",
      "SubnetName": "db-subnet",
      "CidrBlock": "10.0.2.0/24",
      "Zone": "ap-beijing-1"
    }
  }
}
```

4. 创建安全组：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "vpc",
    "action": "CreateSecurityGroup",
    "region": "ap-beijing",
    "parameters": {
      "GroupName": "web-security-group",
      "GroupDescription": "Web服务器安全组"
    }
  }
}
```

## 3. 批量资源管理

### 场景：批量管理云服务器

**用户输入**：
```
查看所有地区的云服务器资源使用情况，并统计各地区的实例数量和规格分布
```

**Claude的操作流程**：

1. 获取所有可用地区：
```json
{
  "name": "tencent_get_regions",
  "arguments": {}
}
```

2. 逐个查询每个地区的实例（示例中仅显示几个主要地区）：

广州地区：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "region": "ap-guangzhou",
    "parameters": {
      "Limit": 100
    }
  }
}
```

上海地区：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "region": "ap-shanghai",
    "parameters": {
      "Limit": 100
    }
  }
}
```

北京地区：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "region": "ap-beijing",
    "parameters": {
      "Limit": 100
    }
  }
}
```

Claude会汇总所有结果，生成类似以下的统计报告：
```
腾讯云服务器资源统计报告
========================

总览：
- 总实例数：45台
- 运行中：38台
- 已停止：7台

按地区分布：
- 广州地区：20台 (运行中18台)
- 上海地区：15台 (运行中12台)
- 北京地区：10台 (运行中8台)

按规格分布：
- 2核4G：25台
- 4核8G：15台
- 8核16G：5台
```

## 4. 存储资源管理

### 场景：云硬盘扩容和快照管理

**用户输入**：
```
我需要为disk-12345678这块云硬盘扩容到200GB，并创建一个快照备份
```

**Claude的操作流程**：

1. 查询当前云硬盘信息：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "DescribeDisks",
    "parameters": {
      "DiskIds": ["disk-12345678"]
    }
  }
}
```

2. 创建快照：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "CreateSnapshot",
    "parameters": {
      "DiskId": "disk-12345678",
      "SnapshotName": "backup-before-resize-20241129"
    }
  }
}
```

3. 扩容云硬盘：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "ResizeDisk",
    "parameters": {
      "DiskId": "disk-12345678",
      "DiskSize": 200
    }
  }
}
```

## 5. 负载均衡配置

### 场景：创建负载均衡并配置后端服务器

**用户输入**：
```
创建一个应用型负载均衡，配置HTTP监听器，后端绑定两台云服务器
```

**Claude的操作流程**：

1. 创建负载均衡：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "clb",
    "action": "CreateLoadBalancer",
    "parameters": {
      "LoadBalancerType": "APPLICATION",
      "LoadBalancerName": "web-app-lb"
    }
  }
}
```

2. 创建监听器：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "clb",
    "action": "CreateListener",
    "parameters": {
      "LoadBalancerId": "lb-xxxxxxxx",
      "Ports": [80],
      "Protocol": "HTTP",
      "ListenerNames": ["web-http-listener"]
    }
  }
}
```

3. 绑定后端服务器：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "clb",
    "action": "RegisterTargets",
    "parameters": {
      "LoadBalancerId": "lb-xxxxxxxx",
      "ListenerId": "lbl-xxxxxxxx",
      "Targets": [
        {
          "InstanceId": "ins-11111111",
          "Port": 80,
          "Weight": 10
        },
        {
          "InstanceId": "ins-22222222",
          "Port": 80,
          "Weight": 10
        }
      ]
    }
  }
}
```

## 6. 监控和告警

### 场景：查看资源监控数据

**用户输入**：
```
查看过去24小时内实例ins-12345678的CPU使用率和内存使用情况
```

**Claude的操作流程**：

1. 获取CPU使用率数据：
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

2. 获取内存使用率数据：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "monitor",
    "action": "GetMonitorData",
    "parameters": {
      "Namespace": "QCE/CVM",
      "MetricName": "MemUsage",
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

## 7. 日志服务管理

### 场景：创建日志主题和配置收集

**用户输入**：
```
帮我创建一个日志主题用于收集Web服务器的访问日志
```

**Claude的操作流程**：

1. 创建日志集：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cls",
    "action": "CreateLogset",
    "parameters": {
      "LogsetName": "web-access-logs",
      "Period": 30
    }
  }
}
```

2. 创建日志主题：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cls",
    "action": "CreateTopic",
    "parameters": {
      "LogsetId": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "TopicName": "nginx-access-log",
      "StorageType": "hot"
    }
  }
}
```

## 8. 成本分析

### 场景：查看各服务的成本分布

**用户输入**：
```
帮我分析一下各个地区和服务的资源使用情况，我想了解成本分布
```

**Claude的操作流程**：

1. 查询各地区CVM实例：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cvm",
    "action": "DescribeInstances",
    "region": "ap-guangzhou"
  }
}
```

2. 查询云硬盘使用：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "cbs",
    "action": "DescribeDisks",
    "region": "ap-guangzhou"
  }
}
```

3. 查询负载均衡：
```json
{
  "name": "tencent_call_api",
  "arguments": {
    "service": "clb",
    "action": "DescribeLoadBalancers",
    "region": "ap-guangzhou"
  }
}
```

Claude会分析这些数据，生成成本分布报告，包括：
- 各地区资源分布
- 各服务类型的实例数量
- 规格配置统计
- 优化建议

## 使用技巧

1. **分步执行**：复杂操作先查询当前状态，再执行变更
2. **备份优先**：重要变更前先创建快照或备份
3. **验证结果**：执行操作后查询结果确认成功
4. **错误处理**：遇到错误时查看详细错误信息并提供解决方案
5. **资源优化**：定期检查资源使用情况，优化成本
6. **自然语言**：善用自然语言描述复杂需求，Claude会自动分解为多个API调用