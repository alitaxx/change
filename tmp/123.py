'''
2-22 crm
'''
import time
from selenium import webdriver

# 首页
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
url = "http://192.168.146.128/crm/index.php?m=user&a=login"
driver.get(url=url)
# 登录
driver.find_element(By.NAME,"name").send_keys("admin")
driver.find_element(By.NAME,"password").send_keys("dami131441")
driver.find_element(By.NAME,"submit").click()

#新建客户
driver.find_element(By.LINK_TEXT,"客户").click()
driver.find_element(By.CLASS_NAME,"btn-primary").click()
driver.find_element(By.ID,"name").send_keys("小荷才露尖尖")


time.sleep(3)
driver.quit()