# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   test_two.py    
@Author :   maodou
@Date   : 2021/4/16 16:03
'''

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
import time
def test_debugchrome():
    # 开启debug浏览器
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.implicitly_wait(5)  # 隐式等待
    # 获取cookie信息
    driver.find_element_by_link_text("添加成员").click()
    time.sleep(2)
    driver.find_element_by_id("username").send_keys("jeck")
    driver.find_element_by_id("memberAdd_english_name").send_keys("jeck")
    driver.find_element_by_name("acctid").send_keys("jeck@qq.com")
    driver.find_element_by_link_text("女").click()