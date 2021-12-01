#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.h5ManagementLg import H5ManagementLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
from faker import Faker
from myweb.tools.env_params import get_env_params

@ddt
class test_H5Management(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取假数据
    fakeinfo = Faker(locale="zh_CN")


    @classmethod
    def setUpClass(cls):
        super(test_H5Management, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.h5ManagementLg = H5ManagementLg(cls.driver)
        cls.loginLogic.login(url = cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.h5ManagementLg.into_h5Link_page()

    @data(
        {'title': fakeinfo.text(5), 'description': fakeinfo.text(20), 'link': 'https://test-qmyxcg.myscrm.com.cn'}
    )
    def test_case_01_save_h5Link(self, data):
        # 新增H5链接(直接选择项目和城市)
        if not self._check_case(["C00088"]): return
        params = {
            'title': data['title'],
            'description': data['description'],
            'link': data['link']
        }
        self.h5ManagementLg.save_h5Link(params)
        time.sleep(3)

    @data(
        {'title': fakeinfo.text(5), 'description': fakeinfo.text(20), 'link': 'https://test-qmyxcg.myscrm.com.cn'}
    )

    def test_case_02_edit_h5Link(self, data):
        # 编辑h5链接
        if not self._check_case(["C00089"]): return
        params = {
            'title': data['title'],
            'description': data['description'],
            'link': data['link']
        }
        self.h5ManagementLg.edit_h5Link(params)
        time.sleep(3)

    def test_case_03_delete_h5Link(self):
        # 删除h5链接
        if not self._check_case(["C00090"]): return
        self.h5ManagementLg.delete_h5Link()
        time.sleep(3)

    # @data(
    #     {'title': fakeinfo.text(5), 'description': fakeinfo.text(20),
    #       'link': 'https://test-qmyxcg.myscrm.com.cn',
    #       'project_name': "云", 'region_name': '北京'}
    # )
    # def test_case_04_save_and_search(self, data):
    #     # 新增h5链接(包括搜索项目和城市)
    #     params = {
    #         'title': data['title'],
    #         'description': data['description'],
    #         'link': data['link'],
    #         'project_name': data['project_name'],
    #         'region_name': data['region_name']
    #     }
    #     self.h5ManagementLg.save_and_search(params)
    #     time.sleep(3)

    @data(
        {'link_type': "PaaS版全民营销", 'search_type': "choose", 'project_name': '全局'},
        {'link_type': "PaaS版全民营销", 'search_type': "input", 'project_name': '全局'}
    )
    def test_case_04_search_h5Link(self, data):
        # 列表搜索
        if not self._check_case(["C00091","C00092","C00093"]): return
        params = {
            'link_type': data['link_type'],
            'search_type': data['search_type'],
            'project_name': data['project_name']
        }
        self.h5ManagementLg.search_h5Link(params)
        time.sleep(3)

    def test_case_05_page_turning(self):
        # 翻页
        if not self._check_case(["C00096"]): return
        self.h5ManagementLg.page_turning()


    @classmethod
    def tearDownClass(cls):
        super(test_H5Management, cls).tearDownClass()
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()