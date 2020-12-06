import os
import unittest

import ddt
import requests

from libs.hash_a import hash_pwd
from setting import DATA_PATH


@ddt.ddt
class SignTestCase(unittest.TestCase):
    @ddt.file_data(os.path.join(DATA_PATH,'sign.yaml'))
    def test_sign(self,**sign_data):
        #注册
        #接收数据
        url = sign_data.get('url')
        err_code = sign_data.get('err_code')
        data = sign_data.get('sign_data')
        # data['password']=str(data['password'])
        print(type(data['password'])) #打印数据类型
        #处理请求
        data['password'] = hash_pwd(data['password'])
        result = requests.post(url=url, data=data)
        print(result.json())
        self.assertEqual(err_code, result.json()['data']['err_code'])

if __name__ == '__main__':
    unittest.main()
