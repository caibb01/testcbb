import os
import sys
import unittest

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.basicInfoLg import BasicInfoLg
from selenium import webdriver
import time

class test_basicInfo(TestCase):
    __author__ = "yeting"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 当前用例数据绝对路径
    __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
                               '%s.json' % __module)

    def setUp(self):
        super(test_basicInfo, self).setUp()
        self.driver = webdriver.Chrome(r"D:\AICar\WebTestProject\chromedriver.exe")
        self.loginLogic = LoginLogic(self.driver)
        self.basicInfoLg = BasicInfoLg(self.driver)
        self.loginLogic.login(username='yktest', password='yk_123456', orgname='gzminjieadmin_test')
        self.loginLogic.logincheck()
        self.loginLogic.openAI()

    def tearDown(self):
        super(test_basicInfo, self).tearDown()
        self.driver.close()

    @unittest.skip("")
    def test_case_01_portrait_pic_upload(self):
        self.basicInfoLg.portrait_pic_upload()
        self.basicInfoLg.save_all_info()
        time.sleep(3)

    @unittest.skip("")
    def test_case_02_logo_pic_upload(self):
        self.basicInfoLg.logo_pic_upload()
        self.basicInfoLg.save_all_info()
        time.sleep(3)

    @unittest.skip("")
    def test_case_03_bg_pic_upload(self):
        self.basicInfoLg.bg_pic_upload()
        self.basicInfoLg.save_all_info()
        time.sleep(3)

    def test_case_04_all_pic_upload(self):
        self.basicInfoLg.all_pic_upload()
        self.basicInfoLg.save_all_info()
        time.sleep(3)

    if __name__ == '__main__':
        import unittest
        unittest.main()