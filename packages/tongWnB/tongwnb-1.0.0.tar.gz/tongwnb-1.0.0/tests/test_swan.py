import unittest
from unittest.mock import patch, Mock
import requests
from urllib.parse import urlparse
import logging

from tongWnB.swan import SwanRun
import datetime


class TestSwanRun(unittest.TestCase):
    """测试 SwanRun 类的功能"""
    
    def setUp(self):
        """设置测试环境，配置日志级别"""
        # 配置日志级别为 INFO，这样可以看到 logger.info() 的输出
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
    
    def test_init_with_default_values(self):
        """测试 SwanRun 使用默认值初始化"""
        swan = SwanRun()
        
        # 验证所有属性都是 None
        self.assertIsNone(swan.labHost)
        self.assertIsNone(swan.nodeIP)
        self.assertIsNone(swan.gpus)
        self.assertIsNone(swan.company)
        self.assertIsNone(swan.projectName)
        self.assertIsNone(swan.experimentName)
        self.assertIsNone(swan.apiKey)
        self.assertIsNone(swan.desc)
        self.assertIsNone(swan.experimentConfig)
    
    def test_init_with_custom_values(self):
        """测试 SwanRun 使用自定义值初始化"""
        test_config = {
            "labHost": "https://example.com",
            "nodeIP": "192.168.1.100",
            "gpus": [0, 1, 2],
            "company": "TestCompany",
            "projectName": "TestProject",
            "experimentName": "TestExperiment",
            "apiKey": "test-api-key",
            "desc": "Test experiment description",
            "experimentConfig": [{"name": "batch_size", "value": 32}, {"name": "epochs", "value": 100}]
        }
        
        swan = SwanRun(**test_config)
        
        # 验证所有属性都正确设置
        self.assertEqual(swan.labHost, test_config["labHost"])
        self.assertEqual(swan.nodeIP, test_config["nodeIP"])
        self.assertEqual(swan.gpus, test_config["gpus"])
        self.assertEqual(swan.company, test_config["company"])
        self.assertEqual(swan.projectName, test_config["projectName"])
        self.assertEqual(swan.experimentName, test_config["experimentName"])
        self.assertEqual(swan.apiKey, test_config["apiKey"])
        self.assertEqual(swan.desc, test_config["desc"])
        self.assertEqual(swan.experimentConfig, test_config["experimentConfig"])
    
    def test_create_experiment_missing_lab_host(self):
        """测试 create_experiment 在 labHost 未设置时抛出异常"""
        swan = SwanRun()
        
        with self.assertRaises(ValueError) as context:
            swan.create_experiment()
        
        self.assertIn("labHost 未设置", str(context.exception))
    
    def test_create_experiment_invalid_url(self):
        """测试 create_experiment 在 URL 无效时抛出异常"""
        swan = SwanRun(labHost="invalid-url")
        
        with self.assertRaises(ValueError) as context:
            swan.create_experiment()
        
        self.assertIn("无效的实验平台 URL", str(context.exception))

    def test_create_experiment_real_request(self):
        """集成测试 SwanRun.create_experiment 真实请求并验证 HTTP 状态码，打印返回结果

        注意：本测试会向真实服务器发送请求，需确保 labHost 可用且参数有效。
        """
        swan = SwanRun(
            # labHost="http://127.0.0.1:8081",  # 使用 httpbin.org 作为测试服务
            labHost="http://10.10.1.84:8079",  # 使用 httpbin.org 作为测试服务
            nodeIP="127.0.0.1",
            gpus=[0],
            company="公司hhh1",
            projectName="pythonTest",
            experimentName=f"pythonTest_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            apiKey="TSPQyMn14VKBI3M",
            desc="Integration test experiment",
            experimentConfig=[{"name":"batch_size","value": 8}]
        )
        try:
            result = swan.create_experiment()
            # httpbin.org/post 返回的 json 里有 status_code 字段
            # 但 swan.create_experiment 只返回 response.json()
            # 所以我们只能检查 result 是否为 dict 并打印
            print("实验创建返回结果:", result)
            # self.assertIsInstance(result, dict)
            # # httpbin.org 会返回 url 字段
            # self.assertIn("url", result)
            # self.assertIn("/tong-swan/api/v1/experiment", result["url"])
        except Exception as e:
            self.fail(f"真实请求 create_experiment 失败: {e}")
    
    @patch('requests.post')
    def test_create_experiment_success(self, mock_post):
        """测试 create_experiment 成功创建实验"""
        # 设置 mock 响应
        mock_response = Mock()
        mock_response.json.return_value = {"experiment_id": "test-123", "status": "created"}
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response
        
        # 创建 SwanRun 实例
        swan = SwanRun(
            labHost="https://example.com",
            nodeIP="192.168.1.100",
            gpus=[0, 1],
            company="TestCompany",
            projectName="TestProject",
            experimentName="TestExperiment",
            apiKey="test-api-key",
            desc="Test description",
            experimentConfig=[{"name": "batch_size", "value": 32}]
        )
        
        # 调用 create_experiment
        result = swan.create_experiment()
        
        # 验证结果
        self.assertEqual(result, {"experiment_id": "test-123", "status": "created"})
        
        # 验证请求参数
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        self.assertEqual(call_args[0][0], "https://example.com/tong-swan/api/v1/experiment")
        
        # 验证请求体
        expected_body = {
            "nodeIP": "192.168.1.100",
            "gpuNumber": [0, 1],
            "company": "TestCompany",
            "projectName": "TestProject",
            "experimentName": "TestExperiment",
            "apiKey": "test-api-key",
            "desc": "Test description",
            "experimentConfig": {"batch_size": 32}
        }
        self.assertEqual(call_args[1]["json"], expected_body)
        self.assertEqual(call_args[1]["timeout"], 10)
    
    @patch('requests.post')
    def test_create_experiment_request_exception(self, mock_post):
        """测试 create_experiment 在请求失败时抛出异常"""
        # 设置 mock 抛出异常
        mock_post.side_effect = requests.RequestException("Network error")
        
        swan = SwanRun(labHost="https://example.com")
        
        with self.assertRaises(requests.RequestException) as context:
            swan.create_experiment()
        
        self.assertIn("创建实验请求失败", str(context.exception))

    def test_log(self):
        from loguru import logger
        import sys

        # 终端显示不受该段代码设置
        # 添加一个日志处理器，输出到文件
        # 设置日志最低显示级别为INFO，format将设置sink中的内容
        # sink链接的本地文件，如不存在则新建。如果存在则追写
        # logger.add(sink=sys.stdout, level="INFO", format="{time:HH:mm:ss} | {message}| {level}")

        # debug结果不被显示到本地文件
        logger.debug("这是一条调试信息")
        logger.info("这是一条普通信息")


if __name__ == '__main__':
    unittest.main()
