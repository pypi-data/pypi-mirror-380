import unittest
from tongWnB.export import init,log,get_run,get_node_ip
from tongWnB.swan import SwanRun
import time



class TestExportInit(unittest.TestCase):
    """测试 export 模块中的 init 函数"""
    
    def test_init(self):
        """测试 init 函数初始化 run 对象"""
        # 调用 init 函数
        init()
        
        # 验证可以通过 get_run 获取 SwanRun 实例
        result = get_run()
        self.assertIsInstance(result, SwanRun)

    def test_get_run(self):
        # rr = get_run()
        init(
            labHost="http://127.0.0.1:8081",
            nodeIP="10.10.1.85",  # 记得等会改成10.10.1.85
            gpus=[0],
            company="公司hhh",
            projectName="pythonTest",
            experimentName="python_package_test2",
            apiKey="TSPQyMn14VKBI3M",
            experimentConfig={
                "time": int(time.time()),
                "day": "0829",
                "climate": "rainning",
                }
        )

        log({"loss": 0.3, "acc": 1})
        log({"loss": 0.19, "acc": 2})
        log({"loss": 0.34, "acc": 3})

        count: float=0
        while True:
            time.sleep(5)
            log({"loss": count, "acc": count})
            count+=1.2
            if count >= 10:
                break

        # self.assertIsInstance(rr, SwanRun)

    def test_get_node_ip(self):
        ip = get_node_ip()
        print(ip)

if __name__ == '__main__':
    unittest.main() 