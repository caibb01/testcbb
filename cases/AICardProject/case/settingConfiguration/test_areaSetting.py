#-*- encoding=utf-8 -*-

import os
import unittest
import sys
from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.areaSettingLg import areaSettingLg
from time import sleep
from selenium.webdriver.common.keys import Keys
from  random import randint
from myweb.tools.env_params import get_env_params

@ddt
class test_areaSetting(TestCase):
    __author__ = "lips"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    #登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_areaSetting, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.areaSettingLg = areaSettingLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])


    def setUp(self):
        super(test_areaSetting, self).setUp()

    def test_01_open_location_matching_settings(self):
        '''定位匹配设置-开启定位重定向'''
        self.areaSettingLg.into_areaSetting_page()

    def tearDown(self):
        super(test_areaSetting, self).tearDown()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()