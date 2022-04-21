#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.taskCenterLG import TaskCenterLg
import time
from myweb.utils.config import JsonConfig

import datetime
from myweb.tools.env_params import get_env_params
from ddt import ddt, data
@ddt
class test_taskCenter(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.
                                              join(os.path.abspath(__file__), "../../..")), 'data', 'image', 'th.jpg')


    @classmethod
    def setUpClass(cls):
        super(test_taskCenter, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.taskCenterLg = TaskCenterLg(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.taskCenterLg.into_taskCenter_page()

    @data(
        {'title': "JK任务" + now_time, 'start_time': "2051-07-31 23:59", 'perform_cycle': 3,
         'perform_index': 3, "path": IMAGE_PATH}
    )
    def test_case_01_save_task(self, data):
        # 新增任务
        params = {
            'title': data['title'],
            'perform_cycle': data['perform_cycle'],
            'perform_index': data['perform_index'],
            'start_time': data['start_time'],
            'path': data['path']
        }
        self.taskCenterLg.save_task(params)
        time.sleep(3)

    @data(
        {'title': "JK任务" + now_time, "path": IMAGE_PATH}
    )
    def test_case_02_edit_task(self, data):
        # 编辑任务
        params = {
            'title': data['title'],
            'path': data['path']
        }
        self.taskCenterLg.edit_task(params)
        time.sleep(3)

    def test_case_03_check_progress(self):
        # 查看进展
        self.taskCenterLg.check_progress()
        time.sleep(3)

    def test_case_04_delete_task(self):
        # 删除任务
        self.taskCenterLg.delete_task()
        time.sleep(3)

    @data(
        {'keywords': "JK"}
    )
    def test_case_05_search_task(self, data):
        params = {
            'keywords': data['keywords']
        }
        # 列表搜索
        self.taskCenterLg.search_task(params)
        time.sleep(3)

    def test_case_06_click_next(self):
        # 点击下一页
        self.taskCenterLg.click_next()
        time.sleep(3)

    def test_case_07_click_previous(self):
        # 点击上一页
        self.taskCenterLg.click_previous()
        time.sleep(3)

    def test_case_08_jump_page(self):
        # 跳页
        self.taskCenterLg.jump_page()
        time.sleep(3)

    def test_case_09_view_ranking_list(self):
        # 查看排行榜
        self.taskCenterLg.view_ranking_list()
        time.sleep(3)
    def tearDown(self):
        super(test_taskCenter, self).tearDown()
    @classmethod
    def tearDownClass(cls):
        super(test_taskCenter, cls).tearDownClass()

if __name__ == '__main__':
    unittest.main()
