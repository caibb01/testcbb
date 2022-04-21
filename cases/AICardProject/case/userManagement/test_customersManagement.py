#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.userManagementLG.customersManagementLg import customersManagementLg
from myweb.tools.env_params import get_env_params
@ddt
class test_customersManagement(TestCase):
    __author__ = "lips"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_customersManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.customersManagementLg = customersManagementLg(cls.driver)
        cls.env_param = get_env_params()
        # cls.loginLogic.login(username=cls.__login_data['username'],
        #                      password=cls.__login_data['password'],
        #                      orgname=cls.__login_data['orgname'])
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.customersManagementLg.into_customersManagement_page()

    def setUp(self):
        super(test_customersManagement, self).setUp()

    @data([{'expectData': '客群管理','msg':"未打开客群管理页面"}]
          )
    @unpack
    def test_01_check_title(self,data):
        '''检查客群管理页面的标题'''
        params = {
            'checkData': {
                'expectData': data['expectData'],
                'msg': data['msg']
            }
        }
        self.customersManagementLg.check_title_lg(params)

    def tearDown(self):
        super(test_customersManagement, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_customersManagement, cls).tearDownClass()


if __name__ == '__main__':
    unittest.main()