# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   main_page.py    
@Author :   maodou
@Date   : 2021/4/19 15:10
'''
from selenium.webdriver.common.by import By

from test_task_02.page.add_member import AddMemberPage
from test_task_02.page.base_page import BasePage

import selenium

from test_task_02.page.contact import ContactPage


class MainPage(BasePage):

    def goto_contact(self):
        '''

        :return:
        '''
        #self.driver.find_element_by_css_selector('$(".frame_nav_item_title:nth(1)")').click()
        self.driver.find_element(By.ID,'menu_contacts').click()
        return ContactPage(self.driver)


    def goto_add_member(self):

        self.driver.find_element(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()

        return AddMemberPage(self.driver)

