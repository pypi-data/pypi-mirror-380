import requests
from urllib.parse import urlparse
import logging
import json
import time


class ChartValue:
    """
    表示图表中的一个数据点。

    Attributes:
        name (str): 数据点名称。
        value (float): 数据点的数值。
        groupName (str): 数据点分组名称。
    """

    def __init__(self, name: str, value: float, step: int, epoch: int, groupName: str | None = None) -> None:
        """
        初始化 ChartValue 实例。

        Args:
            name (str): 数据点名称。
            value (float): 数据点的数值。
            step (int): 步数。
            epoch (int): 轮数。
            groupName (str, optional): 数据点分组名称。
        """
        self.name: str = name
        self.value: float = value
        self.epoch: int = epoch
        self.step: int = step
        self.groupName: str | None = groupName

    def to_json(self) -> dict[str, float | str | int]:
        """
        将 ChartValue 实例转换为 JSON 格式的字典。

        Returns:
            dict[str, float | str | int]
        """
        json_data = {"name": self.name, "value": self.value, "epoch": self.epoch, "step": self.step}
        if self.groupName is not None:
            json_data["groupName"] = self.groupName
        return json_data


class SwanRun:
    """
    创建项目、实验。并上传自定义的用户数据
    """

    def __init__(self,
                 labHost: str | None = None,
                 nodeIP: str | None = None,
                 gpus: list[int] | None = None,
                 company: str | None = None,
                 projectName: str | None = None,
                 experimentName: str | None = None,
                 apiKey: str | None = None,
                 desc: str | None = None,
                 experimentConfig: dict | None = None,
                 ):
        """
        实验初始化

        Parameters
        ----------
        labHost (str, optional):  
            实验平台 host.
        nodeIP (str, optional):  
            训练节点ip.
        gpuNumber (list[int], optional): 
            使用的gpu列表.
        company (str, optional): 
            公司名称.
        projectName (str, optional): 
            项目名称.
        experimentName (str, optional): 
            实验名称. 
        apiKey (str, optional): 
            训练使用的 api key. 
        desc (str, optional): 
            实验描述. 
        experimentConfig (dict, optional): 
            实验配置.
        """
        self.labHost = labHost
        self.nodeIP = nodeIP
        self.gpus = gpus
        self.company = company
        self.projectName = projectName
        self.experimentName = experimentName
        self.apiKey = apiKey
        self.desc = desc
        self.experimentConfig = experimentConfig

        # 内部方法使用的成员变量
        self.__step = 0  # user step
        self.__system_step = 0  # system step
        self._check_errors: list[str] = []
        self.__projectID: str = ""
        self.__experimentID: str = ""
        self.__taskID: str = ""

        if not self.__check():
            raise ValueError(self.__get_check_errors())

    def create_experiment(self):
        """
        创建实验，将实例属性作为 POST 请求的 body 参数发送到实验平台。

        Returns:
            dict: 响应的 JSON 数据

        Raises:
            ValueError: labHost 未设置时抛出异常
            requests.RequestException: 请求失败时抛出异常
        """

        url = f"{self.labHost}/tong-swan/api/v1/experiment"
        self.__check_url(url)

        # 将 self.experimentConfig 转换成 list[dict]，每个 dict 形如 {"name": k, "value": v}，不覆盖原变量
        experiment_config_list: list[dict] = []
        if self.experimentConfig is not None:
            experiment_config_list = [
                {"name": k, "value": v} for k, v in self.experimentConfig.items()
            ]

        body = {
            "company": self.company,
            "projectName": self.projectName,
            "experimentName": self.experimentName,
            "experimentConfig": experiment_config_list,
            "apiKey": self.apiKey,
            "desc": self.desc,
            "gpus": self.gpus,
        }

        response_json = self.__post(url, body)

        if "projectID" not in response_json or "experimentID" not in response_json:
            raise ValueError(
                f"响应缺少 projectID 或 experimentID 字段: {response_json}"
            )

        if response_json["projectID"] == "":
            raise ValueError(f"响应缺少 projectID 值为空")

        if response_json["experimentID"] == "":
            raise ValueError(f"响应缺少 experimentID 值为空")

        self.__projectID = response_json["projectID"]
        self.__experimentID = response_json["experimentID"]

        # 只在第一次创建实验时生成 taskID，保证任务中 ID 唯一
        if not self.__taskID:
            self.__taskID = str(int(time.time() * 1000))  # 生成毫秒级时间戳作为taskId

    def create_chart(self, val: dict[str, float | dict]):
        """
        创建用户图表
        
        Args:
            val: 指标数据字典，支持两种格式：
                1. float: 指标值（保持向后兼容）
                   例如: {"loss": 0.5, "accuracy": 0.95}
                2. dict: 一个groupName对应多个指标的字典
                   例如: {"accuracy": {"loss": 0.5, "acc": 0.95}}
        """
        if not self.__projectID:
            raise ValueError("__projectID is required.")
        if not self.__experimentID:
            raise ValueError("__experimentID is required.")
        if not self.nodeIP:
            raise ValueError("nodeIP is required.")

        charts: list[dict] = []
        for name, data in val.items():
            if isinstance(data, dict):
                # 格式2: {"groupName": {"指标1": 值1, "指标2": 值2}}
                group_name = name  # 外层的key就是groupName
                for metric_name, metric_value in data.items():
                    if not isinstance(metric_value, (int, float)):
                        raise ValueError(f"指标组 '{group_name}' 中的指标 '{metric_name}' 的值必须是数字")
                    
                    chart_value = ChartValue(
                        name=metric_name,
                        value=float(metric_value),
                        step=self.__step,
                        epoch=self.__step + 1,
                        groupName=group_name
                    )
                    charts.append(chart_value.to_json())
            else:
                # 格式1: 向后兼容，直接传数值的情况
                value = data
                group_name = None
                
                chart_value = ChartValue(
                    name=name,
                    value=value,
                    step=self.__step,
                    epoch=self.__step + 1,
                    groupName=group_name
                )
                charts.append(chart_value.to_json())

        body: dict = {
            "apiKey": self.apiKey,
            "projectID": self.__projectID,
            "experimentID": self.__experimentID,
            "nodeIP": self.nodeIP,
            "chartValues": charts,
            "taskID": self.__taskID
        }

        url = f"{self.labHost}/tong-swan/api/v1/chart"
        self.__check_url(url)
        self.__post(url, body)

        self.__step += 1

    def create_system_chart(self):
        """
        创建系统图表
        """
        if not self.__projectID:
            raise ValueError("__projectID is required.")
        if not self.__experimentID:
            raise ValueError("__experimentID is required.")
        if not self.nodeIP:
            raise ValueError("nodeIP is required.")

        body: dict = {
            "apiKey": self.apiKey,
            "projectID": self.__projectID,
            "experimentID": self.__experimentID,
            "step": self.__system_step,
            "epoch": self.__system_step + 1,
            "nodeIP": self.nodeIP,
            "taskID": self.__taskID
        }

        url = f"{self.labHost}/tong-swan/api/v1/system-chart"
        self.__check_url(url)
        self.__post(url, body)

        self.__system_step += 1

    def __check(self) -> bool:
        """
        校验实验配置。

        Returns:
            bool: 所有校验通过返回 True，否则返回 False。
        """
        # 校验 labHost
        if not self.labHost:
            self._check_errors.append("labHost 未设置。")
        else:
            self.__check_url(self.labHost)

        # 检查 nodeIP
        if not self.nodeIP:
            self._check_errors.append("nodeIP 未设置。")
        # 检查 gpus
        if not self.gpus:
            self._check_errors.append("gpus 未设置。")
        # 检查 company
        if not self.company:
            self._check_errors.append("company 未设置。")
        # 检查 projectName
        if not self.projectName:
            self._check_errors.append("projectName 未设置。")
        # 检查 experimentName
        if not self.experimentName:
            self._check_errors.append("experimentName 未设置。")
        # 检查 apiKey
        if not self.apiKey:
            self._check_errors.append("apiKey 未设置。")
        # 检查 experimentConfig
        if not self.experimentConfig:
            self._check_errors.append("experimentConfig 未设置。")

        if not isinstance(self.experimentConfig, dict):
            self._check_errors.append("experimentConfig 类型必须是 dict")

        return len(self._check_errors) == 0

    def __get_check_errors(self) -> list[str]:
        """
        获取最近一次 check() 校验失败的错误信息列表。

        Returns:
            list[str]: 错误信息列表。如果校验通过则为空列表。
        """
        return getattr(self, "_check_errors", [])

    def __check_url(self, url: str):
        parsed_url = urlparse(url)
        if not (parsed_url.scheme in ("http", "https") and parsed_url.netloc):
            raise ValueError(f"无效 URL: {url}")

    def __post(self, url: str, body: dict) -> dict:
        import time
        max_retries = 3
        retry_delay = 1  # 秒

        for attempt in range(max_retries):
            try:
                response = requests.post(url, json=body, timeout=60)
                response_json = response.json()

                if response.status_code >= 400:
                    error_message = (
                        f"http code: {response.status_code}, "
                        f"http response: {response_json}"
                    )
                    raise requests.HTTPError(error_message, response=response)

                return response_json
            except (requests.ConnectionError, requests.Timeout) as e:
                if attempt < max_retries - 1:
                    print(f"请求失败{url}，{retry_delay}秒后重试 (第{attempt + 1}次重试): {e}")
                    time.sleep(retry_delay)
                    retry_delay *= 2  # 指数退避
                    continue
                else:
                    raise requests.RequestException(f"请求失败{url}，已重试{max_retries}次: {e}") from e
            except requests.RequestException as e:
                raise requests.RequestException(f"创建仪表请求失败: {e}") from e

        # 这行代码理论上永远不会执行，因为上面的逻辑要么返回值要么抛出异常
        # 但添加它可以消除linter警告
        raise RuntimeError("Unexpected code path")
