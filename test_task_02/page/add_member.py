# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   add_member.py    
@Author :   maodou
@Date   : 2021/4/19 15:11
'''
from selenium.webdriver.common.by import By

from test_task_02.page.base_page import BasePage
from test_task_02.page.contact import ContactPage


class AddMemberPage(BasePage):

    def add_member(self, username, accid, phone):

        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("memberAdd_acctid").send_keys(accid)
        self.driver.find_element_by_id("memberAdd_phone").send_keys(phone)
        self.driver.find_element(by=By.CSS_SELECTOR,value='.js_btn_save').click()
        return ContactPage(self.driver)