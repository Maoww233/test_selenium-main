# -*- coding: utf-8 -*- 
# @Time : 2021/4/20 10:32 下午 
# @Author : maodou 
# @File : test_add_department.py


from test_task_02.page.main_page import MainPage
import pytest
import yaml


class TestAddDepartment:


    yaml_result = yaml.load(open("testcase.yaml", encoding="utf-8"), Loader=yaml.FullLoader)
    def setup_class(self):

        self.main_page = MainPage()

    @pytest.mark.parametrize("department", yaml_result["add_department"])
    def test_add_department(self,department):
        '''
        添加部门测试用例
        :return:
        '''

        Rdepartment = self.main_page.goto_contact().goto_add_department().add_department(department).get_contact_departmentlist(department[0])
        print(Rdepartment)
        assert department == Rdepartment