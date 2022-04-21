# -*- encoding=utf8 -*-
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.ManageRoleLogic import ManageRoleLogic
import os, sys, datetime
import unittest


class test_manageRoleCase(TestCase):
    __author__ = "chenyz01"
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
        super(test_manageRoleCase, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.manageRoleLogic = ManageRoleLogic(cls.driver)
        cls.loginLogic.login(username=cls.__login_data['username'],
                             password=cls.__login_data['password'],
                             orgname=cls.__login_data['orgname'])
        cls.loginLogic.logincheck()
        # 进入AI云店页面
        cls.loginLogic.openAI()
        # 进入弹窗管理页面
        cls.manageRoleLogic.into_manageRole_page()

    def setUp(self):
        super(test_manageRoleCase, self).setUp()
        # 初始化置业顾问页面-关闭保护期开关
        self.manageRoleLogic.setUp_sales_info()
        self.manageRoleLogic.setUp_marketing_info()
        self.manageRoleLogic.setUp_broker_info()
        self.manageRoleLogic.setUp_guest_info()

    # def test_01_sales_open_customer_protection_switch(self):
    #     """
    #     进入置业顾问tab，打开保护期开关，将保护期设置为3小时
    #     """
    #     params = {
    #         'customer_protection_switch': True,
    #         'customer_protection_time': '3',
    #         "button": '确定'
    #     }
    #     self.manageRoleLogic.switch_to_tab('置业顾问')
    #     self.manageRoleLogic.editor_sales_info(params=params)

    # def test_02_marketing_open_customer_protection_switch(self):
    #     """
    #     进入行销人员tab，打开保护期开关，将保护期设置为3小时
    #     """
    #     params = {
    #         'customer_protection_switch': True,
    #         'customer_protection_time': '2',
    #         "button": '确定'
    #     }
    #     self.manageRoleLogic.switch_to_tab('行销人员')
    #     self.manageRoleLogic.editor_marketing_info(params=params)

    # def test_03_broker_open_protection_switch(self):
    #     """
    #     进入全民营销tab
    #     1、打开总开关，设置统一身份名为<全民营销>，拓客保护期为<1>小时
    #     2、打开项目楼盘报备入口，设置入口名称<忙着赚钱>，跳转方式为<Pass全民营销>
    #     :return:
    #     """
    #     params = {
    #         'marketing': {
    #             'switch': True,
    #             'show_identity': '全民营销',
    #             'protection_time': '5',
    #             'button': '确定'
    #         },
    #         'recommend_entry': {
    #             'switch': True,
    #             'entry_name': '立享佣金',
    #             'jump_way': 'Pass全民营销',
    #             'button': '确定'
    #         },
    #         'card': {
    #             'switch': True,
    #             'options': ['老业主'],
    #             'button': '确定'
    #         },
    #         'get_phone_number_become_broker': True
    #     }
    #     self.manageRoleLogic.switch_to_tab('全民营销')
    #     self.manageRoleLogic.editor_broker_info(params=params)

    # def test_04_guest_open_protection_switch(self):
    #     """
    #     进入访客tab
    #     1、打开拓客保护期开关，设置保护期为<5>小时
    #     2、打开购房进程状态信息呈现
    #     :return:
    #     """
    #     params = {
    #             'protection': {
    #                 'switch': True,
    #                 'protection_time': '5',
    #                 'button': '确定'
    #                 },
    #             'house_buying_process': True
    #         }

    #     self.manageRoleLogic.switch_to_tab('访客')
    #     self.manageRoleLogic.editor_guest_info(params=params)
    def tearDown(self):
        super(test_manageRoleCase, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_manageRoleCase, cls).tearDownClass()


if __name__ == '__main__':
    import unittest
    unittest.main()
