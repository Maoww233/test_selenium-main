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


    __department_name = '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input'
    __affiliation_department ='.js_parent_party_name'
    __affiliation_department_two = '.ww_dialog_body [id="1688852014214296_anchor"]'
    __buthon_text = '确定'

    def add_department(self,department):


        self.driver.find_element(By.XPATH,self.__department_name).send_keys(department)
        self.driver.find_element(By.CSS_SELECTOR,self.__affiliation_department).click()
        self.driver.find_element(By.CSS_SELECTOR,self.__affiliation_department_two).click()
        self.driver.find_element(By.LINK_TEXT,self.__buthon_text).click()

        from test_task_02.page.contact import ContactPage
        return ContactPage(self.driver)
