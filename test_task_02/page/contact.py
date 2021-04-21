# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   contact.py    
@Author :   maodou
@Date   : 2021/4/19 15:11
'''
from selenium.webdriver.common.by import By
from selenium import webdriver
from test_task_02.page.base_page import BasePage
from test_task_02.page.new_department import NewDepartment


class ContactPage(BasePage):

    __contact_list = ".member_colRight_memberTable_td:nth-child(5)"
    __add_darpatment = ".member_colLeft_top_addBtn"
    __add_darpat =".js_create_party"

    def get_contact_list(self):

        #获取通讯录元素列表
        ele_list = self.driver.find_elements(By.CSS_SELECTOR,self.__contact_list)
        print(type(ele_list))
        phone_list = []
        for ele in list(ele_list):
            phone_list.append(ele.text)
        print(phone_list)
        return phone_list

    def goto_add_department(self):
        '''
        点击+号进入添加成员页面
        :return:
        '''

        self.driver.find_element(By.CSS_SELECTOR,self.__add_darpatment).click()
        self.driver.find_element(By.CSS_SELECTOR,self.__add_darpat).click()

        return NewDepartment(self.driver)

    def get_contact_departmentlist(self,department):

        departmentlist = self.driver.find_elements(By.LINK_TEXT,department)
        department_list = []

        for dle in list(departmentlist):
            department_list.append(dle.text)
        return department_list



