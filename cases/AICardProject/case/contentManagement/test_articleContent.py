# -*- encoding=utf8 -*-
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.articleContentLg import articleContentLg

from selenium import webdriver
import os, sys
import time


class test_articleContent(TestCase):
    __author__ = "zhengw"
    # 当前模块名
    # __module = sys._getframe().f_code.co_name
    # # 当前用例数据绝对路径
    # __data_path = os.path.join(os.path.split(os.path.dirname(os.path.abspath(__file__)))[0], 'data',
    #                            '%s.json' % __module)
    # # # 获取用例数据
    # # __data = JsonConfig(__data_path).get()
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 图片文件路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image')
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    _need_delete = []


    @classmethod
    def setUpClass(cls):
        super(test_articleContent, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.articleContentLg = articleContentLg(cls.driver)
        cls.loginLogic.login(username=cls.__login_data['username'],
                             password=cls.__login_data['password'],
                             orgname=cls.__login_data['orgname'])
        cls.loginLogic.logincheck()
        cls.loginLogic.openAI()

    def setUp(self):
        super(test_articleContent, self).setUp()

    def test_case_01(self):
        """
        新增文章，编辑文章，发布文章，编辑文章，关闭文章
        """
        self.articleContentLg.newContent()
        time.sleep(3)

    def tearDown(self):
        super(test_articleContent, self).tearDown()
        # if self._need_delete:
        #     # 倒序循环，每次删掉最末尾
        #     for need_del in reversed(self._need_delete):
        #         self.managerBlankPageLogic.delete_blankPage(need_del)
        #         self._need_delete.remove(need_del)

if __name__ == '__main__':
    import unittest
    unittest.main()
