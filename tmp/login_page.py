

# 登录MD5加密过后的密码
import requests
from libs.hash_a import hash_pwd

url = 'http://hn216.api.yesapi.cn/?s=App.User.Login'
data = {'app_key':'29E362F90C9CAB765A7F56A52B0F2262','username':'alita2','password':'dami131441'}
data['password'] = hash_pwd(data['password'])
result = requests.post(url=url,data=data)
print(result.json())


#注册使用加密过后的密码
url = 'http://hn216.api.yesapi.cn/?s=App.User.Register'
data = {'app_key':'29E362F90C9CAB765A7F56A52B0F2262','username':'alita2','password':'dami131441'}
data['password'] = hash_pwd(data['password'])
result = requests.post(url=url,data=data)
print(result.json())