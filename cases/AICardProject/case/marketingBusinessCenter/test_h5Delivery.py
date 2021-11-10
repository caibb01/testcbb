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
        {'name': "ui" + now_time, 'project': "全局"}
    )
    def test_case_01_save_h5(self, data):
        # 新增h5
        self.test_code = ["C00188"]
        params = {
            'name': data['name'],
            'project': data['project']
        }
        self.h5DeliveryLg.save_h5(params)
        time.sleep(6)

    def test_case_02_h5_detail(self):
        # 查看h5
        self.test_code = ["C00189"]
        self.h5DeliveryLg.h5_detail()
        time.sleep(3)

    def test_case_03_customer_detail(self):
        # 导出客户明细
        self.test_code = ["C00190"]
        self.h5DeliveryLg.customer_detail()
        time.sleep(3)

    def test_case_04_copy_link(self):
        # 复制链接
        self.test_code = ["C00191"]
        self.h5DeliveryLg.copy_link()
        time.sleep(3)

    @data(
        {'name': "ui"}
    )
    def test_case_05_search_h5(self, data):
        # 列表查询
        self.test_code = ["C00194","C00195"]
        params = {
            'name': data['name']
        }
        self.h5DeliveryLg.search_h5(params)
        time.sleep(6)

    def test_case_06_delete_h5(self):
        # 删除h5
        self.test_code = ["C00197"]
        self.h5DeliveryLg.delete_h5()
        time.sleep(3)

    def test_case_07_page_turning(self):
        # 翻页
        self.test_code = ["C00198"]
        self.h5DeliveryLg.page_turning()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        super(test_h5Delivery, cls).tearDownClass()
        cls.driver.close()


if __name__ == '__main__':
    unittest.main()