from get_weather import get_resp
 
import unittest
from unittest import mock
 
# requests lib の mock
def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code
 
        def json(self):
            return self.json_data
 
    if args[0] == 'url_valid':
        return MockResponse({"key1": "value1"}, 200)
 
    return MockResponse({}, 404)
 
# テスト用クラス
class TestGetResp(unittest.TestCase):
 
    # 正常系確認テストケース
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_resp_ok(self, mock_get):
        json_data = get_resp('url_valid')
        self.assertEqual(json_data, {"key1": "value1"})
 
    # 異常系確認テストケース
    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_resp_ng(self, mock_get):
        with self.assertRaises(RuntimeError):
            json_data = get_resp('url_invalid')
 
if __name__ == '__main__':
    unittest.main()
    
