# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   test_First.py
@Author :   maodou
@Date   : 2021/4/15 14:31
'''
import yaml

'''
mac 版本启动debug模式
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
Windows版本启动debug模式
Chrome --remote-debugging-port=9222

1.打开浏览器
2.搜索内容
3.直接等待time.sleep(1),每个操作都必须等待，造成浪费时间
4.隐式等待implicitly_wait(5)默认0.5S轮询查找，如果没找到元素着抛出异常，全局设置
5.显式等待，在代码中自定义等待条件，当条件发生时才继续执行代码，会反复查找，知道等待时间结束
'''

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import yaml

class TestHogwarts:

    def setup(self):

        #开启debug浏览器
        opt = webdriver.ChromeOptions()
        opt.debugger_address="127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(5)#隐式等待
        #获取cookie信息
        print(self.driver.get_cookies())
        cookie = self.driver.get_cookies()
        with open("data.yaml","w",encoding="utf-8") as f:
            yaml.dump(cookie,f)


    def teardown(self):
        #self.dirvers.quit()
        pass
    # def test_baidu(self):
    #
    #     self.driver.find_element(By.ID,"menu_contacts").click()
    #     #回去cookies
    #     print(self.driver.get_cookies())

    def test_cookies(self):

        self.dirvers = webdriver.Chrome()
        self.dirvers.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")

        with open("data.yaml",encoding="utf-8") as f:
             yaml_data = yaml.safe_load(f)
             for cookie in yaml_data:
                 self.dirvers.add_cookie(cookie)

        self.dirvers.get("https://work.weixin.qq.com/wework_admin/frame")
        #self.dirvers.find_element(By.ID, "menu_contacts").click()

        self.dirvers.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div').click()

