# -*- encoding=utf8 -*-
import unittest

from myweb.core.runner import My4wTestCase
from myweb.utils.runner import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.miniProgramJumpLg import miniProgramJumpLg

from selenium import webdriver
import os, sys
import time

class test_miniProgramJump(My4wTestCase):
    __author__ = "yeting"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 当前用例数据绝对路径
    __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
                               '%s.json' % __module)
    def setUp(self):
        super(test_miniProgramJump, self).setUp()
        self.driver = webdriver.Chrome(r"D:\AICar\WebTestProject\chromedriver.exe")
        self.loginLogic = LoginLogic(self.driver)
        self.miniProgramJumpLg = miniProgramJumpLg(self.driver)
        self.loginLogic.login(username='yktest', password='yk_123456', orgname='gzminjieadmin_test')
        self.loginLogic.logincheck()
        self.loginLogic.openAI()

    def tearDown(self):
        super(test_miniProgramJump, self).tearDown()
        self.driver.close()

    @unittest.skip("")
    def test_case_01_add_program(self):
        """
        添加小程序
        """
        self.miniProgramJumpLg.add_program()
        time.sleep(3)

    @unittest.skip("")
    def test_case_02_delete_program(self):
        """
        删除小程序
        """
        self.miniProgramJumpLg.delete_program()
        time.sleep(3)

    def test_case_03_add_and_delete_program(self):
        """
        添加并删除小程序
        """
        self.miniProgramJumpLg.add_program()
        self.miniProgramJumpLg.delete_program()
        time.sleep(3)

    if __name__ == '__main__':
        import unittest
        unittest.main()