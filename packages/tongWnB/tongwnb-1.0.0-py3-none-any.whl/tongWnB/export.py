from .swan import SwanRun
import threading
import time
import socket

run: SwanRun | None = None


def should_call_after_init(text):
    """
    装饰器，限制必须在实验初始化后调用
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            global run
            if run is None:
                raise RuntimeError("run is not initialized")
            return func(*args, **kwargs)

        return wrapper

    return decorator


def init(
    labHost: str = "",
    nodeIP: str | None = None,
    gpus: list[int] | None = None,
    company: str = "",
    projectName: str = "",
    experimentName: str = "",
    apiKey: str = "",
    experimentConfig: dict | None = None):
    """
    Initialize the run object. If the run object already exists, return it.
 
    初始化 run 对象。如果 run 对象已存在，则返回它。

    Args:
        labHost (str): 实验平台 host。
        nodeIP (str, optional): 训练节点 IP。
        gpus (list[int]): 使用的 GPU 列表。
        company (str): 公司名称。
        projectName (str): 项目名称。
        experimentName (str): 实验名称。
        apiKey (str): 训练使用的 API key。
        experimentConfig (list[dict]): 实验配置。

    Returns:
        None
    """
    if not nodeIP:
        nodeIP = get_node_ip()
        

    global run
    run = SwanRun(labHost, nodeIP, gpus, company, projectName, experimentName, apiKey, "", experimentConfig)
    run.create_experiment()

    # 创建一个后台线程，每 5 秒创建一个系统图表
    def create_system_chart() -> None:
        """
        后台线程任务，持续运行。
        """
        # print("tongWnB开始上传系统数据...")
        while True:
            try:
                if run is not None:
                    run.create_system_chart()
            except Exception as e:
                print(f"tongWnB系统监控数据上传失败: {e}")
                # 如果系统数据上传失败，等待更长时间再重试
                time.sleep(10)
                continue
            time.sleep(5)

    thread = threading.Thread(target=create_system_chart, daemon=True)
    thread.start()

    return


@should_call_after_init("You must call tongWnB.init() before using log()")
def log(data: dict[str, float | dict]):
    """
    记录指标数据到实验日志中。

    Args:
        data: 指标数据字典，支持两种格式：
            1. float: 指标值（保持向后兼容）
            2. dict: 一个groupName对应多个指标的字典（推荐用法）
               例如: {"training_metrics": {"loss": 0.5, "accuracy": 0.95}}
              
    示例:
        # 原有用法（向后兼容）
        tongWnB.log({"loss": 0.5, "accuracy": 0.95})
        
        # 推荐用法：一个groupName对应多个指标
        tongWnB.log({
            "training_metrics": {
                "loss": 0.5,
                "accuracy": 0.95,
                "learning_rate": 0.001
            },
            "validation_metrics": {
                "val_loss": 0.3,
                "val_accuracy": 0.97
            }
        })
        
        # 混合用法
        tongWnB.log({
            "loss": 0.5,  # 不指定分组
            "training_metrics": {  # 组合指定分组
                "epoch_loss": 0.4,
                "epoch_acc": 0.96
            }
        })
    """
    r = get_run()
    r.create_chart(data)


def get_run() -> SwanRun:
    """
    Get the current run object. If the experiment has not been initialized, raise an error.
    """
    global run
    if run is None:
        raise RuntimeError("run is not initialized")

    return run


def get_node_ip() -> str:
    """
    获取当前节点的主机 IP 地址。

    Returns:
        str: 当前主机的 IP 地址。

    Raises:
        RuntimeError: 无法获取本机 IP 地址时抛出异常。
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
