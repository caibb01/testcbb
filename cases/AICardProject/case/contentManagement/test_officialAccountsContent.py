#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.officialAccountsManagementLg import OfficialAccountsManagementLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
from faker import Faker
from myweb.tools.env_params import get_env_params
import datetime

@ddt
class test_officialAccounts(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取假数据
    fakeinfo = Faker(locale="zh_CN")
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')
    # 获取图片路径
    image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image', 'th.jpg')
    new_image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image', '01.jpg')


    @classmethod
    def setUpClass(cls):
        super(test_officialAccounts, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.officialAccountsManagementLg = OfficialAccountsManagementLg(cls.driver)
        cls.loginLogic.login(url = cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.officialAccountsManagementLg.into_officialAccounts_page()

    @data(
        {'title': "UI测试" + now_time, 'content': fakeinfo.text(20), 'url': 'uitest',
         "project_name": '全局', 'city_name': '全局', 'path': image_path}
    )
    def test_case_01_newOfficialAccounts(self, data):
        # 新增公众号文章
        if not self._check_case(["C00029"]): return
        params = {
            'title': data['title'],
            'content': data['content'],
            'url': data['url'],
            'project_name': data['project_name'],
            'city_name': data['city_name'],
            'path': data['path'],
        }
        self.officialAccountsManagementLg.newOfficialAccounts(params)
        time.sleep(3)

    @data(
        {'title': "UI测试" + now_time, 'content': fakeinfo.text(20), 'url': 'uitest',
         "project_name": '全局', 'city_name': '全局', 'path': new_image_path}
    )
    def test_case_02_updateOfficialAccounts(self, data):
        # 编辑公众号文章
        if not self._check_case(["C00030"]): return
        params = {
            'title': data['title'],
            'content': data['content'],
            'url': data['url'],
            'project_name': data['project_name'],
            'city_name': data['city_name'],
            'path': data['path'],
        }
        self.officialAccountsManagementLg.updateOfficialAccounts(params)
        time.sleep(3)

    def test_case_03_delOfficialAccounts(self):
        # 删除公众号文章
        if not self._check_case(["C00031"]): return
        self.officialAccountsManagementLg.delOfficialAccounts()
        time.sleep(3)


    def test_case_04_queryOfficialAccounts(self):
        # 搜索公众号文章
        if not self._check_case(["C00032","C00033"]): return
        self.officialAccountsManagementLg.queryOfficialAccounts("全局")
        time.sleep(3)

    def test_case_05_page_turning(self):
        # 翻页
        if not self._check_case(["C00036"]): return
        self.officialAccountsManagementLg.page_turning()


    @classmethod
    def tearDownClass(cls):
        super(test_officialAccounts, cls).tearDownClass()
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()