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
        cls.areaSettingLg.into_areaSetting_page()

    def setUp(self):
        super(test_areaSetting, self).setUp()

    @data([{'name': '全国首页O'}])
    @unpack
    def test_01_open_location_matching_settings(self, data):
        '''定位匹配设置-开启定位重定向'''
        self.test_code = ["C00131"]
        params = {
            'name': data['name']
        }
        self.areaSettingLg.open_location_matching_settings_lg(params)
        sleep(3)

    @data([{'name': '全国首页C'}])
    @unpack
    def test_02_close_location_matching_settings(self, data):
        '''定位匹配设置-关闭定位重定向'''
        self.test_code = ["C00132"]
        params = {
            'name': data['name']
        }
        self.areaSettingLg.close_location_matching_settings_lg(params)
        sleep(3)

    rand = 'test_'+str(randint(100,999))
    @data([{'area_name': rand}])
    @unpack
    def test_03_add_area_01(self,data):
        '''新增区域,不关联项目'''
        self.test_code = ["C00133"]
        params = {
                'area_name':data['area_name']
        }
        self.areaSettingLg.add_area_01_lg(params)
        sleep(3)

    rand2 = 'test2_' + str(randint(100, 999))
    @data([{'area_name': rand2}])
    @unpack
    def test_04_add_area_02(self, data):
        '''新增区域,关联项目'''
        self.test_code = ["C00134"]
        params = {
            'area_name': data['area_name']
        }
        self.areaSettingLg.add_area_02_lg(params)
        sleep(3)

    @data([{'area_name': rand}])
    @unpack
    def test_05_edit_area(self,data):
        '''编辑区域'''
        self.test_code = ["C00135","C00136"]
        params = {
                'area_name': data['area_name']
        }
        self.areaSettingLg.edit_area_lg(params)
        sleep(3)

    @data([{'area_name': rand}])
    @unpack
    def test_06_edit_area_delete_area(self,data):
        '''编辑区域,删除辖区范围'''
        self.test_code = ["C00137"]
        params = {
            'area_name': data['area_name']
        }
        self.areaSettingLg.edit_area_delete_area_lg(params)
        sleep(3)

    @data([{'area_name': rand}],
          [{'area_name': rand2}])
    @unpack
    def test_07_delete_area(self,data):
        '''删除区域'''
        self.test_code = ["C00138"]
        #新增区域
        params = {
            'area_name': data['area_name']
        }
        # self.areaSettingLg.add_area_lg(params)
        # sleep(3)
        #删除区域
        self.areaSettingLg.delete_area_lg(params)
        sleep(3)

    def test_08_unbound_project(self):
        '''打开未绑定项目'''
        self.test_code = ["C00139"]
        self.areaSettingLg.unbound_project_lg()
        sleep(3)

    def test_09_page_switching(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        self.test_code = ["C00140"]
        self.areaSettingLg.unbound_project_lg()
        self.areaSettingLg.page_switching_lg()
        sleep(3)
        self.areaSettingLg.maintained_area_lg()
        self.areaSettingLg.page_switching_lg()


    def tearDown(self):
        super(test_areaSetting, self).tearDown()

if __name__ == '__main__':
    unittest.main()