#-*- coding:utf-8 -*-

import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.labelManagementLg import LabelManagementLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
import datetime
from myweb.tools.env_params import get_env_params

@ddt
class test_LabelManagement(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')

    @classmethod
    def setUpClass(cls):
        super(test_LabelManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.labelManagementLg = LabelManagementLg(cls.driver)
        cls.loginLogic.login(url = cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.labelManagementLg.into_label_page()

    def test_case_01_switch_to_tab(self):
        # 切换标签页
        if not self._check_case(["C00101"]): return
        self.labelManagementLg.switch_to_tab("报名活动")
        self.labelManagementLg.switch_to_tab("优惠券")
        self.labelManagementLg.switch_to_tab("原创文章")
        self.labelManagementLg.switch_to_tab("公众号文章")
        self.labelManagementLg.switch_to_tab("活动中心")
        self.labelManagementLg.switch_to_tab("项目楼盘")
        time.sleep(3)

    @data(
        {'label_name': "JK标签", 'project_name': "全局"}
    )
    def test_case_02_new_label(self, data):
        # 项目楼盘-新增标签
        if not self._check_case(["C00102"]): return
        params = {
            'label_name': data['label_name'],
            'project_name': data['project_name']
        }
        self.labelManagementLg.new_label(params)
        time.sleep(3)

    def test_case_03_del_association(self):
        # 删除关联关系
        if not self._check_case(["C00103"]): return
        self.labelManagementLg.del_association()
        time.sleep(3)

    def test_case_04_label_sort(self):
        # 关联数据排序
        if not self._check_case(["C00104"]): return
        self.labelManagementLg.label_sort()
        time.sleep(3)

    def test_case_05_del_label(self):
        # 删除标签
        if not self._check_case(["C00105"]): return
        self.labelManagementLg.del_label()
        time.sleep(3)
    @data(
        {"city_name": "全局"}
    )
    def test_case_06_add_association(self, data):
        # 添加关联关系
        if not self._check_case(["C00106","C00107"]): return
        params = {
            "city_name": data["city_name"]
        }
        self.labelManagementLg.add_association(params)
        time.sleep(3)

    def test_case_07_page_turning(self):
        # 点击上一页
        if not self._check_case(["C00108"]): return
        self.labelManagementLg.page_turning()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        super(test_LabelManagement, cls).tearDownClass()
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()