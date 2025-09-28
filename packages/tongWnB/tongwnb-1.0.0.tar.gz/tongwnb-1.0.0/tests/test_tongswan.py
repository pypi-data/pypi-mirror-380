import tongWnB
import time


def generate_random_float(min_value: float = 0.0, max_value: float = 1.0) -> float:
    """生成指定范围内的随机浮点数

    Args:
        min_value (float): 最小值，包含。默认为 0.0。
        max_value (float): 最大值，包含。默认为 1.0。

    Returns:
        float: 随机浮点数
    """
    import random
    return random.uniform(min_value, max_value)


def generate_random_string(length: int = 8) -> str:
    """生成指定长度的随机字符串

    Args:
        length (int): 字符串长度，默认为 8。

    Returns:
        str: 随机字符串
    """
    import random
    import string

    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


# tongWnB.init(
#     # labHost="http://127.0.0.1:8081",
#     labHost="http://10.10.1.100:30800",
#     nodeIP="10.10.1.84",
#     gpus=[0],
#     company="yc_test",
#     projectName="yc001",
#     experimentName="python_package_random_data06",
#     apiKey="RmQADZEXt6GjPil",
#     experimentConfig={"time": int(time.time()), "day": "0923", "climate": "rainning"}
# )
tongWnB.init(
    labHost="http://10.10.1.100:30800",
    nodeIP="10.10.1.84",
    gpus=[0],
    company="公司hhh",
    projectName="pythonTest",
    experimentName="configpprof02",
    apiKey="TSPQyMn14VKBI3M",
    experimentConfig={"time": int(time.time()), "day": "0923", "climate": "rainning"}
)

random_strs = [
    "a1B", "x9z", "Qw2", "LmN", "8pQ", "rT3", "b7K", "Zx1", "cD4",
    "eF5", "gH6", "jK7", "mN8", "pQ9", "sT0", "uV1", "wX2", "yZ3"
]

for i in range(20):
    try:
        # 使用新的groupName对应多个指标的传入方式
        tongWnB.log({
            # 训练指标组 - 核心训练指标
            "training_metrics": {
                "loss": generate_random_float(0, 100),
                "acc": generate_random_float(0, 100),
            },
            # 性能指标组 - 模型性能相关指标
            "performance_metrics": {
                random_strs[0]: generate_random_float(0, 100),
                random_strs[1]: generate_random_float(0, 100),
                random_strs[2]: generate_random_float(0, 100),
                random_strs[3]: generate_random_float(0, 100),
                random_strs[4]: generate_random_float(0, 100),
                random_strs[5]: generate_random_float(0, 100)
            },
            # 系统指标组 - 系统资源监控指标
            "system_metrics": {
                random_strs[6]: generate_random_float(0, 100),
                random_strs[7]: generate_random_float(0, 100),
                random_strs[8]: generate_random_float(0, 100),
                random_strs[9]: generate_random_float(0, 100),
                random_strs[10]: generate_random_float(0, 100),
                random_strs[11]: generate_random_float(0, 100)
            },
            # 自定义指标组 - 用户自定义指标
            "custom_metrics": {
                random_strs[12]: generate_random_float(0, 100),
                random_strs[13]: generate_random_float(0, 100),
                random_strs[14]: generate_random_float(0, 100),
                random_strs[15]: generate_random_float(0, 100),
                random_strs[16]: generate_random_float(0, 100),
                random_strs[17]: generate_random_float(0, 100)
            }
        })
        print(f"第 {i + 1} 次数据上传成功")
        # 添加请求间隔，避免并发请求过多
        time.sleep(0.5)
    except Exception as e:
        print(f"第 {i + 1} 次数据上传失败: {e}")
        # 如果失败，等待更长时间再继续
        time.sleep(2)

print("done...")
