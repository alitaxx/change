''''''
import os
import unittest

import requests
from libs.hash_a import hash_pwd

import ddt

from setting import DATA_PATH

@ddt.ddt
class LoginTestCase(unittest.TestCase):

    @ddt.file_data(os.path.join(DATA_PATH,'login.yaml'))
    def test_login_a(self,**user_data):
        '''登录'''
        #接收yaml数据
        url = user_data.get('url')
        assert_result = user_data.get('assert_result')
        data = user_data.get('case_data')
        data['password']=str(data['password'])
        # 打印数据类型
        print(type(data['password']))
        #处理请求
        data['password'] = hash_pwd(data['password'])

        result = requests.post(url=url, data=data)
        print(result)
        #结果处理
        result = result.text.replace('":"','=').replace('":','=')
        print(result)
        for res in assert_result:
            self.assertIn(res,result)

if __name__ == '__main__':
    unittest.main()
