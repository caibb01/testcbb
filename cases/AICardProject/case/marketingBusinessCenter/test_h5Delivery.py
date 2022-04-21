#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.h5DeliveryLg import H5DeliveryLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
import datetime
from random import randint
from myweb.tools.env_params import get_env_params

@ddt
class test_h5Delivery(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')

    @classmethod
    def setUpClass(cls):
        super(test_h5Delivery, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.h5DeliveryLg = H5DeliveryLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.h5DeliveryLg.into_h5_page()


    @data(
        {'name': "ui" + now_time, 'project': "全局", "channel_into":100}
    )
    def test_case_01_save_h5(self, data):
        # 新增h5
        if not self._check_case(["C00223"]): return
        params = {
            'name': data['name'],
            'project': data['project'],
            'channel_into': data['channel_into']
        }
        self.h5DeliveryLg.save_h5(params)
        time.sleep(6)

    def test_case_02_edit_h5(self):
        # 编辑h5
        if not self._check_case(["C00224"]): return
        self.h5DeliveryLg.edit_h5(200)
        time.sleep(3)

    def test_case_03_customer_detail(self):
        # 导出客户明细
        if not self._check_case(["C00225"]): return
        self.h5DeliveryLg.customer_detail()
        time.sleep(3)

    def test_case_04_copy_link(self):
        # 复制链接
        if not self._check_case(["C00226"]): return
        self.h5DeliveryLg.copy_link()
        time.sleep(3)

    @data(
        {'name': "ui"}
    )
    def test_case_05_search_h5(self, data):
        # 列表查询
        if not self._check_case(["C00229","C00230"]): return
        params = {
            'name': data['name']
        }
        self.h5DeliveryLg.search_h5(params)
        time.sleep(6)

    def test_case_06_delete_h5(self):
        # 删除h5
        if not self._check_case(["C00234"]): return
        self.h5DeliveryLg.delete_h5()
        time.sleep(3)

    def test_case_07_page_turning(self):
        # 翻页
        if not self._check_case(["C00235"]): return
        self.h5DeliveryLg.page_turning()
        time.sleep(3)

    def tearDown(self):
        super(test_h5Delivery, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_h5Delivery, cls).tearDownClass()


if __name__ == '__main__':
    unittest.main()