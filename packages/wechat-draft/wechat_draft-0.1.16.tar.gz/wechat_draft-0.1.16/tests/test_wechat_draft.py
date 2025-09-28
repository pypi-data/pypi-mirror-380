import os
import unittest
from unittest.mock import patch, MagicMock
from wechat_draft.wechat_draft import WechatDraft
from wechat_draft.utils.logger import log
import requests  # 导入 requests
import time  # 导入 time 模块用于模拟重试延迟


class TestWechatDraft(unittest.TestCase):
    def setUp(self):
        self.app_id = "your_app_id"
        self.app_secret = "your_app_secret"
        self.access_token_file = "test_access_token.json"
        if os.path.exists(self.access_token_file):
            os.remove(self.access_token_file)

        self.wechat_draft = WechatDraft(
            app_id=self.app_id,
            app_secret=self.app_secret,
            access_token_file=self.access_token_file,
            get_token_from_server_url="https://fastapi.xiaoqiangclub.qzz.io/wechat/access_token",
            server_token="czq087405"
        )

    def tearDown(self):
        if os.path.exists(self.access_token_file):
            os.remove(self.access_token_file)

    @patch('requests.post')
    def test_get_access_token_from_server(self, mock_post):
        log.info("ℹ️ 测试从自定义服务器获取 access_token")
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "access_token": "server_test_token",
            "expires_in": 7200
        }
        mock_post.return_value = mock_response

        token = self.wechat_draft.get_access_token(use_server_token=True)
        self.assertEqual(token, "server_test_token")
        mock_post.assert_called_once_with(
            self.wechat_draft.get_token_from_server_url,
            headers={'Content-Type': 'application/json'},
            json={"token": self.wechat_draft.server_token},
            timeout=10
        )
        self.assertTrue(os.path.exists(self.access_token_file))

    @patch('wechat_draft.wechat_draft.WechatDraft.get_access_token_from_wechat_api')
    def test_get_access_token_from_wechat_api(self, mock_get_wechat_api):
        log.info("ℹ️ 测试从微信官方API获取 access_token")
        mock_get_wechat_api.return_value = {
            "access_token": "wechat_test_token",
            "expires_in": 7200,
            "errcode": 0
        }

        token = self.wechat_draft.get_access_token(use_server_token=False)
        self.assertEqual(token, "wechat_test_token")
        mock_get_wechat_api.assert_called_once()
        self.assertTrue(os.path.exists(self.access_token_file))

    @patch('requests.post')
    # Mock time.sleep to avoid actual delays
    @patch('time.sleep', return_value=None)
    def test_get_access_token_from_server_retries(self, mock_sleep, mock_post):
        log.info("ℹ️ 测试从自定义服务器获取 access_token 的重试机制")
        # Configure mock to fail twice, then succeed
        mock_post.side_effect = [
            requests.exceptions.RequestException("Connection error"),
            requests.exceptions.RequestException("Another connection error"),
            MagicMock(status_code=200, json=lambda: {
                      "access_token": "server_retry_token", "expires_in": 7200})
        ]

        # Ensure the mock_post.json() is callable and returns the expected value for the successful call
        mock_post.side_effect[2].json.return_value = {
            "access_token": "server_retry_token", "expires_in": 7200}

        token = self.wechat_draft.get_access_token(use_server_token=True)
        self.assertEqual(token, "server_retry_token")
        # Should be called 3 times (initial + 2 retries)
        self.assertEqual(mock_post.call_count, 3)
        self.assertEqual(mock_sleep.call_count, 2)  # Should sleep twice
        self.assertTrue(os.path.exists(self.access_token_file))


if __name__ == '__main__':
    unittest.main()
