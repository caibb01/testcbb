#-*- coding:utf-8 -*-

import os
import unittest

import ddt as ddt

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.channelManagementLg import ChannelManagementLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
import datetime
from random import randint
from myweb.tools.env_params import get_env_params

@ddt
class test_channelManagement(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')

    @classmethod
    def setUpClass(cls):
        super(test_channelManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.channelManagementLg = ChannelManagementLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.channelManagementLg.into_channel_page()

    @data(
        {'channel_name': "JK渠道码" + now_time, 'channel_input': randint(1, 100)}
    )
    def test_case_01_save_channel(self, data):
        # 新增渠道码
        if not self._check_case(["C00144"]): return
        params = {
            'channel_name': data['channel_name'],
            'channel_input': data['channel_input']
        }
        self.channelManagementLg.save_channel(params)
        time.sleep(10)

    @data(
        {'channel_input': randint(1, 100)}
    )
    def test_case_02_edit_channel(self, data):
        # 编辑渠道码
        if not self._check_case(["C00145"]): return
        params = {
            'channel_input': data['channel_input']
        }
        self.channelManagementLg.edit_channel(params)
        time.sleep(6)

    def test_case_03_get_channel_code(self):
        # 获取渠道码
        if not self._check_case(["C00146"]): return
        self.channelManagementLg.get_channel_code()
        time.sleep(3)

    def test_case_04_copy_link(self):
        # 复制链接
        if not self._check_case(["C00147"]): return
        self.channelManagementLg.copy_link()
        time.sleep(3)

    def test_case_05_guest_detail(self):
        # 下载新客明细
        if not self._check_case(["C00148"]): return
        self.channelManagementLg.guest_detail()
        time.sleep(5)

    def test_case_06_exposure_detail(self):
        # 下载曝光明细
        if not self._check_case(["C00149"]): return
        self.channelManagementLg.exposure_detail()
        time.sleep(5)

    @data(
        {'channel_name': "JK"}
    )
    def test_case_07_search_channel(self, data):
        # 列表查询
        if not self._check_case(["C00150","C00151","C00152","C00153","C00154"]): return
        params = {
            'channel_name': data['channel_name']
        }
        self.channelManagementLg.search_channel(params)
        time.sleep(6)

    def test_case_08_delete_channel(self):
        # 删除渠道码
        if not self._check_case(["C00155"]): return
        self.channelManagementLg.delete_channel()
        time.sleep(3)

    def test_case_09_page_turning(self):
        # 点击下一页
        if not self._check_case(["C00156"]): return
        self.channelManagementLg.page_turning()
        time.sleep(3)


    def test_case_10_single_path_code(self):
        # 获取单个路径码
        if not self._check_case(["C00158","C00159"]): return
        self.channelManagementLg.switch_to_tab('获取路径码')
        self.channelManagementLg.single_path_code()
        time.sleep(3)

    def test_case_11_batch_code(self):
        # 获取批量码
        if not self._check_case(["C00161"]): return
        self.channelManagementLg.switch_to_tab('获取批量码')
        self.channelManagementLg.batch_code()
        time.sleep(3)

    def tearDown(self):
        super(test_channelManagement, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_channelManagement, cls).tearDownClass()


if __name__ == '__main__':
    unittest.main()
