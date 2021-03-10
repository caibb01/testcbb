# -*- encoding=utf8 -*-
from util.runner import My4wTestCase
from util.config import JsonConfig, conf
from cases.AICardProject.logic.LoginLogic import LoginLogic
from selenium import webdriver
import os, sys
import time


class AICardTestCase(My4wTestCase):
    __author__ = "zero"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 当前用例数据绝对路径
    __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
                               '%s.json' % __module)
    # 获取用例数据
    __data = JsonConfig(__data_path).get()

    def setUp(self):
        super(AICardTestCase, self).setUp()
        self.driver = webdriver.Chrome(conf['driverPath'])
        self.loginLogic = LoginLogic(self.driver)

    def test_case_01(self):
        """
        AI名片测试用例
        """
        self.loginLogic.login(username=self.__data['username'],
                              password=self.__data['password'],
                              orgname=self.__data['orgname'])
        self.loginLogic.logincheck()
        self.loginLogic.openAI()
        time.sleep(3)


if __name__ == '__main__':
    import unittest

    unittest.main()
