# TongWnB

一个用于AI训练过程跟踪和管理的Python库，支持实验指标记录、分组管理和可视化。

## 安装

### 从PyPI安装（推荐）

```shell
pip install tongwnb
```

### 从源码安装

```shell
# 进入目录后:
pip install -U .
```

## 使用说明

### 1. 初始化

```python
import tongWnB

tongWnB.init(
    labHost="http://127.0.0.1:8081",  # WnBlab 平台地址
    nodeIP="10.10.10.10",  # 当前节点ip地址，选填。如果不传，工具会自动获取当前节点ip
    gpus=[0],  # 训练用到的 gpu 编号
    company="公司名",  # WnBlab 平台中公司的名字
    projectName="pythonTest",  # 项目名字
    experimentName="python_package_thirdpart",  # 实验名。如果实验不存在会自动创建该名字
    apiKey="xxx",  # 用户用到的WnBkey。请到 WnBlab 平台个人信息处查看 WnBkey
    experimentConfig={"day": "0829", "climate": "rainning"}  # 自定义的配置信息
)
```

### 2. 记录训练指标

#### 简单方式 - 直接记录指标

```python
tongWnB.log({"loss": 0.1, "acc": 0.9})
tongWnB.log({"loss": 0.2, "acc": 0.8})
```

#### 分组方式 - 按类别组织指标（推荐）

```python
tongWnB.log({
    # 训练指标组 - 核心训练指标
    "training_metrics": {
        "loss": 0.1,
        "acc": 0.9,
        "learning_rate": 0.001
    },
    # 性能指标组 - 模型性能相关指标
    "performance_metrics": {
        "precision": 0.85,
        "recall": 0.88,
        "f1_score": 0.86
    },
    # 系统指标组 - 系统资源监控指标
    "system_metrics": {
        "gpu_usage": 75.2,
        "memory_usage": 68.5,
        "cpu_usage": 45.0
    },
    # 自定义指标组 - 用户自定义指标
    "custom_metrics": {
        "custom_metric_1": 42.0,
        "custom_metric_2": 37.8
    }
})
```

### 3. 完整示例

#### 基础用例

```python
import tongWnB

tongWnB.init(
    labHost="http://127.0.0.1:8081",
    nodeIP="YOUR_NODE_IP",
    gpus=[0],
    company="YOUR_COMPANY",
    projectName="YOUR_PROJECT",
    experimentName="YOUR_EXPERIMENT",
    apiKey="YOUR_API_KEY",
    experimentConfig={"day": "0829", "climate": "rainning"}
)

for i in range(10):
    tongWnB.log({"loss": 1.0 - i*0.1, "acc": i*0.1})
```

#### 分组指标完整示例

```python
import tongWnB
import time
import random

tongWnB.init(
    labHost="http://127.0.0.1:8081",
    nodeIP="YOUR_NODE_IP",
    gpus=[0],
    company="YOUR_COMPANY",
    projectName="YOUR_PROJECT",
    experimentName="grouped_metrics_experiment",
    apiKey="YOUR_API_KEY",
    experimentConfig={"version": "1.0", "model": "ResNet50"}
)

for epoch in range(20):
    tongWnB.log({
        "training_metrics": {
            "loss": random.uniform(0.1, 2.0),
            "acc": random.uniform(70, 95),
            "learning_rate": 0.001 * (0.9 ** epoch)
        },
        "validation_metrics": {
            "val_loss": random.uniform(0.2, 2.5),
            "val_acc": random.uniform(65, 90)
        },
        "system_metrics": {
            "gpu_memory": random.uniform(50, 90),
            "cpu_usage": random.uniform(20, 80)
        }
    })
    time.sleep(1)  # 模拟训练间隔

print("训练完成!")
```

## 功能特性

- ✅ **简单易用**: 几行代码即可集成训练指标记录
- ✅ **分组管理**: 支持按类别组织指标，便于管理和可视化  
- ✅ **自动重试**: 网络异常时自动重试上传
- ✅ **实时同步**: 实时将指标同步到WnBlab平台
- ✅ **灵活配置**: 支持自定义实验配置和元数据

## 版本信息

- 当前版本: 1.0.0
- Python版本要求: >=3.10
- 依赖: requests>=2.25.0
