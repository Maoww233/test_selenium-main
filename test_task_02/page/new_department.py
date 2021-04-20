# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   new_department.py    
@Author :   maodou
@Date   : 2021/4/19 15:11
'''
from selenium.webdriver.common.by import By

from test_task_02.page.base_page import BasePage
#from test_task_02.page.contact import ContactPage
#from test_task_02.page.contact import ContactPage


class NewDepartment(BasePage):

    def add_department(self):

        self.driver.switch_to.default_content()
        self.driver.find_element(By.CSS_SELECTOR, '..inputDlg_item:nth(0)>input').send_keys("学习2")

        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        self.driver.find_element(By.ID, '1688852014214296_anchor').click()
        self.driver.find_element(By.CSS_SELECTOR, ".qui_btn.ww_btn.ww_btn_Blue:nth(1)").click()
        #return ContactPage(self.driver)
