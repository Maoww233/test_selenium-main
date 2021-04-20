# -*- encoding: utf-8 -*-
'''
@Project : Test_selenium_studey_1
@File    :   test_add_menber.py    
@Author :   maodou
@Date   : 2021/4/19 17:14
'''
from test_task_02.page.main_page import MainPage
import pytest
import yaml

class TestAddMember:


    def setup_class(self):

        self.main_page = MainPage()

    yaml_result = yaml.load(open("testcase.yaml", encoding="utf-8"), Loader=yaml.FullLoader)
    @pytest.mark.parametrize("username,accid,phone",yaml_result["add_menber"])
    def test_add_member(self,username,accid,phone):
        """
        :param username: 成员姓名
        :param accid: 成员账号
        :param phone:成员手机号[断言手机号]
        :return:
        """
        phone_list = self.main_page.goto_add_member().add_member(username,accid,phone).get_contact_list()

        assert str(phone) in phone_list

