# -*- encoding=utf8 -*-
from myweb.core.runner import My4wTestCase
from myweb.utils.runner import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.imageContentLg import imageContentLg

from selenium import webdriver
import os, sys
import time


class test_imageContent(My4wTestCase):
    __author__ = "zero"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 当前用例数据绝对路径
    __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
                               '%s.json' % __module)
    # # 获取用例数据
    # __data = JsonConfig(__data_path).get()

    def setUp(self):
        super(test_imageContent, self).setUp()
        self.driver = webdriver.Chrome(r"/Users/sean/Desktop/WebTestProject/chromedriver")
        self.loginLogic = LoginLogic(self.driver)
        self.imageContentLg = imageContentLg(self.driver)

    def test_case_01(self):
        """
        AI名片测试用例
        """
        self.loginLogic.login(username='yktest', password='yk_123456', orgname='gzminjieadmin_test')
        # self.loginLogic.login(username=self.__data['username'],
        #                       password=self.__data['password'],
        #                       orgname=self.__data['orgname'])
        self.loginLogic.logincheck()
        self.loginLogic.openAI()
        self.imageContentLg.newContent()
        time.sleep(3)


if __name__ == '__main__':
    import unittest
    unittest.main()
