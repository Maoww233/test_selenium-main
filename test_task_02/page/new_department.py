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

    def add_department(self,department):

        #self.driver.switch_to.frame("__dialog__MNDialog__")
        #self.driver.find_element(By.CSS_SELECTOR, '..inputDlg_item:nth(0)>input').send_keys("学习2")
        self.driver.find_element(By.XPATH,'//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(department)
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        #self.driver.find_element(By.ID, '1688852014214296_anchor').click()
        #self.driver.find_element(By.XPATH,'//*[@id="1688852014214296_anchor"]').click()
        self.driver.find_element(By.CSS_SELECTOR,'.ww_dialog_body [id="1688852014214296_anchor"]').click()
        self.driver.find_element(By.LINK_TEXT,'确定').click()
        from test_task_02.page.contact import ContactPage
        return ContactPage(self.driver)
