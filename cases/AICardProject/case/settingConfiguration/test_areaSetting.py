import os
import sys
import unittest

from myweb.core.runner import My4wTestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.areaSettingLg import AreaSettingLg
from selenium import webdriver
import time

class test_areaSetting(My4wTestCase):
    __author__ = "yeting"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 当前用例数据绝对路径
    __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
                               '%s.json' % __module)

    def setUp(self):
        super(test_areaSetting, self).setUp()
        self.driver = webdriver.Chrome(r"D:\AICar\WebTestProject\chromedriver.exe")
        self.loginLogic = LoginLogic(self.driver)
        self.areaSettingLg = AreaSettingLg(self.driver)
        self.loginLogic.login(username='yktest', password='yk_123456', orgname='gzminjieadmin_test')
        self.loginLogic.logincheck()
        self.loginLogic.openAI()

    def tearDown(self):
        super(test_areaSetting, self).tearDown()
        self.driver.close()

    @unittest.skip("")
    def test_case_01_add_area(self):
        self.areaSettingLg.add_area()
        time.sleep(3)

    @unittest.skip("")
    def test_case_02_edit_area(self):
        self.areaSettingLg.edit_area()
        time.sleep(3)

    @unittest.skip("")
    def test_case_03_delete_area(self):
        self.areaSettingLg.delete_area()
        time.sleep(3)

    @unittest.skip("")
    def test_case_04_location_matching(self):
        self.areaSettingLg.location_pattern()
        time.sleep(3)


    def test_case_05_operate_area(self):
        """新增区域-编辑区域-删除区域"""
        self.areaSettingLg.operate_area()
        time.sleep(3)