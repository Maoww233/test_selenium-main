# -*- coding: utf-8 -*- 
# @Time : 2021/4/20 10:32 下午 
# @Author : maodou 
# @File : test_add_department.py


from test_task_02.page.main_page import MainPage
import pytest
import yaml


class TestAddDepartment:

    def setup_class(self):

        self.main_page = MainPage()

    def test_add_department(self):

        self.main_page.goto_contact().goto_add_department().add_department().goto_add_department()