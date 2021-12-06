#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.userManagementLG.dataInspectorLg import dataInspectorLg
from myweb.tools.env_params import get_env_params

@ddt
class test_dataInspector(TestCase):
    __author__ = "lips"
    #登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_dataInspector, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.dataInspectorLg = dataInspectorLg(cls.driver)
        cls.env_param = get_env_params()
        # cls.loginLogic.login(username=cls.__login_data['username'],
        #                      password=cls.__login_data['password'],
        #                      orgname=cls.__login_data['orgname'])
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.dataInspectorLg.into_dataInspector_page()

    def setUp(self):
        super(test_dataInspector, self).setUp()


    @data([{'check_type': '1'}],
          [{'check_type': '2'}])
    @unpack
    def test_01_inquiry(self,data):
        '''输入姓名/手机号进行查询'''
        params = {
            'parameter': {
                'check_type': data['check_type']
            }
        }
        self.dataInspectorLg.inquiry_lg(params)

    #@data([{'name_or_phone':'18816851537'}])
    @data([{'check_type': '1'}])
    @unpack
    def test_02_confirm_delete(self,data):
        '''确认删除数据查阅人'''
        params = {
            'parameter': {
                #'name_or_phone': data['name_or_phone']
                'check_type': data['check_type']
            }
        }
        self.dataInspectorLg.confirm_delete_lg(params)

    def test_03_synchronization(self):
        '''同步数据查阅人'''
        self.dataInspectorLg.synchronization_lg()

   # @data([{'phone': '18816851537'}])
    @data([{'check_type': '1'}])
    @unpack
    def test_04_add(self,data):
        '''新增数据查阅人'''
        params = {
            #'phone': data['phone']
            'check_type': data['check_type']
        }
        self.dataInspectorLg.add_lg(params)

    @data([{'name_or_phone': '15707519537','check_type': '1' }])
    @unpack
    def test_05_cancel_delete(self,data):
        '''取消删除数据查阅人'''
        params = {
            'parameter': {
                'name_or_phone': data['name_or_phone'],
                'check_type': data['check_type']
            }

        }
        self.dataInspectorLg.cancel_delete_lg(params)

    def test_06_click_detailed_description(self):
        '''点击详细说明'''
        self.dataInspectorLg.click_detailed_description_lg()

    def test_07_page_switching(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        self.dataInspectorLg.page_switching_lg()

    def tearDown(self):
        super(test_dataInspector, self).tearDown()

if __name__ == '__main__':
    unittest.main()