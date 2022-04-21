# -*- encoding=utf8 -*-

import os, sys
import unittest

from ddt import ddt, data, unpack
from time import sleep
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from myweb.utils.excelUtil import ExcelUtil
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.basicInfoLg import BasicInfoLg
from random import randint
from myweb.tools.env_params import get_env_params


@ddt
class test_basicInfo(TestCase):
    __author__ = "lips"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    # 获取图片路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image')

    @classmethod
    def setUpClass(cls):
        super(test_basicInfo, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.BasicInfoLg = BasicInfoLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.BasicInfoLg.into_BasicInfo_page()

    def setUp(self):
        super(test_basicInfo, self).setUp()

    @data([{'name': '测试名片' + str(randint(100, 1000))}])
    @unpack
    def test_01_short_for_mini_program(self, data):
        '''小程序简称'''
        if not self._check_case(["C00176"]): return
        params = {
            'name': data['name']
        }
        self.BasicInfoLg.short_for_mini_program_lg(params)

    @data([{'path': os.path.join(__image_path, '01.jpg')}])
    @unpack
    def test_02_corporate_image_chart(self, data):
        '''企业形象图的上传图片、重新上传、删除'''
        if not self._check_case(["C00177"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.corporate_image_chart_lg(params)

    @data([{'path': os.path.join(__image_path, '02.jpg')}])
    @unpack
    def test_03_corporate_logo(self, data):
        '''企业LOGO的上传图片、重新上传、删除'''
        if not self._check_case(["C00178"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.corporate_logo_lg(params)

    @data([{'path': os.path.join(__image_path, '03.jpg')}])
    @unpack
    def test_04_authorization_background_image(self, data):
        '''授权背景图的上传图片、重新上传、删除'''
        if not self._check_case(["C00179"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.authorization_background_image_lg(params)

    @data([{'path': os.path.join(__image_path, '04.jpg')}])
    @unpack
    def test_05_poster_on_moments(self, data):
        '''朋友圈海报（安卓）的上传图片、重新上传、删除'''
        if not self._check_case(["C00180"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.poster_on_moments_lg(params)

    @data([{'path': os.path.join(__image_path, '05.jpg')}])
    @unpack
    def test_06_workbench_icon(self, data):
        '''工作台图标，开或关，上传图片、重新上传、删除'''
        if not self._check_case(["C00181"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.workbench_icon_lg(params)

    @data([{'path': os.path.join(__image_path, 'penguin01.jpg')}])
    @unpack
    def test_07_map_marker_icon(self, data):
        '''地图标记图标的上传图片、重新上传、删除'''
        if not self._check_case(["C00182"]): return
        params = {
            'path': data['path']
        }
        self.BasicInfoLg.map_marker_icon_lg(params)

    @data([{'name': 'test' + str(randint(100, 1000)), 'id': 'Wol0R7aVOlKlwEImE9O09V34QpPHhi'}])
    @unpack
    def test_08_intelligent_customer_service(self, data):
        '''智能客服：开启或关闭,添加机器人'''
        if not self._check_case(["C00183"]): return
        params = {
            'parmeter': {
                'name': data['name'],
                'id': data['id']
            }
        }
        self.BasicInfoLg.intelligent_customer_service_lg(params)

    @data([{'question': 'test' + str(randint(100000, 999999))}]
          )
    @unpack
    def test_09_intelligent_customer_service_configuration(self, data):
        '''智能客服-机器人配置快捷提问,保存'''
        if not self._check_case(["C00184"]): return
        params = {
            'question': data['question']
        }
        self.BasicInfoLg.intelligent_customer_service_configuration_lg(params)

    @data([{'question': 'test' + str(randint(100000, 999999))}]
          )
    @unpack
    def test_10_cancel_intelligent_customer_service_configuration(self, data):
        '''智能客服-机器人配置快捷提问，取消保存'''
        if not self._check_case(["C00186"]): return
        params = {
            'question': data['question']
        }
        self.BasicInfoLg.cancel_intelligent_customer_service_configuration_lg(params)

    def test_11_delete_robot(self):
        '''智能客服：删除机器人'''
        if not self._check_case(["C00187"]): return
        self.BasicInfoLg.delete_robot_lg()

    @data([{'name': 't' + str(randint(100, 999))}])
    @unpack
    def test_12_number_of_visits(self, data):
        '''浏览人次名称自定义:开或关，自定义名称'''
        if not self._check_case(["C00188", "C00189", "C00190"]): return
        params = {
            'name': data['name']
        }
        self.BasicInfoLg.number_of_visits_lg(params)

    def test_13_leave_advice(self):
        '''留电通知开或关，勾选置业顾问、行销人员、全民经纪人'''
        if not self._check_case(["C00191", "C00192"]): return
        self.BasicInfoLg.leave_advice_lg()

    def test_14_other_settings_01(self):
        '''其他设置，勾选允许查看服务轨迹'''
        if not self._check_case(["C00195"]): return
        self.BasicInfoLg.other_settings_01_lg()

    def test_15_other_settings_02(self):
        '''其他设置，勾选允许云会员'''
        if not self._check_case(["C00196"]): return
        self.BasicInfoLg.other_settings_02_lg()

    def test_16_save(self):
        '''保存'''
        if not self._check_case(["C00197"]): return
        self.BasicInfoLg.save_lg()

    def test_17_cancel_save(self):
        '''取消保存'''
        if not self._check_case(["C00198"]): return
        self.BasicInfoLg.cancel_save_lg()

    def tearDown(self):
        super(test_basicInfo, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_basicInfo, cls).tearDownClass()


if __name__ == '__main__':
    unittest.main()
