#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.commentsLg import CommentsLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
from faker import Faker
from myweb.tools.env_params import get_env_params

@ddt
class test_Comments(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image', 'th.jpg')
    # 获取假数据
    fakeinfo = Faker(locale="zh_CN")

    @classmethod
    def setUpClass(cls):
        super(test_Comments, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.commentsLg = CommentsLg(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.commentsLg.into_comments_page()

    @data(
        {'project_name': "项目", 'nick_name': fakeinfo.name(), 'comments': fakeinfo.text(10), "path": IMAGE_PATH}
    )
    def test_case_01_save_comments(self, data):
        # 新增评论
        params = {
            'project_name': data['project_name'],
            'nick_name': data['nick_name'],
            'comments': data['comments'],
            'path': data['path']
        }
        self.commentsLg.save_comments(params)
        time.sleep(3)

    @data(
        {'reply_content': fakeinfo.text(10)}
    )
    def test_case_02_reply_comments(self, data):
        # 回复评论
        params = {
            'reply_content': data['reply_content']
        }
        self.commentsLg.reply_comments(params)
        time.sleep(3)

    def test_case_03_delete_comments(self):
        # 删除评论
        self.commentsLg.delete_comments()
        time.sleep(3)

    def test_case_04_click_next(self):
        # 点击下一页
        self.commentsLg.click_next()
        time.sleep(3)

    def test_case_05_click_previous(self):
        # 点击上一页
        self.commentsLg.click_previous()
        time.sleep(3)

    def test_case_06_jump_page(self):
        # 点击跳页
        self.commentsLg.jump_page()
        time.sleep(3)

    @data(
        {'start_date': '2021/08/01', 'end_date': '2021/12/31', 'project_name': "项目"}
    )
    def test_case_07_search_comments(self, data):
        # 列表查询
        params = {
            'start_date': data['start_date'],
            'end_date': data['end_date'],
            'project_name': data['project_name']
        }
        self.commentsLg.search_comments(params)
        time.sleep(3)

    def test_case_08_reply_histroy(self):
        # 查看回复历史
        self.commentsLg.reply_histroy()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        super(test_Comments, cls).tearDownClass()
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()