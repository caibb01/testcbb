#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.miniProgramLiveLg import miniProgramLiveLg

from myweb.tools.env_params import get_env_params

@ddt
class test_miniProgramLive(TestCase):
    __author__ = "lips"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_miniProgramLive, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.miniProgramLiveLg = miniProgramLiveLg(cls.driver)
        cls.loginLogic.login(url = cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.miniProgramLiveLg.into_miniProgramLive_page()

    def setUp(self):
        super(test_miniProgramLive, self).setUp()

    # @data([{'expectData': '小程序直播','msg':"未打开小程序直播页面"}]
    #       )
    # @unpack
    # def test_01_check_title(self,data):
    #     '''检查小程序直播页面的标题'''
    #     params = {
    #         'checkData': {
    #             'expectData': data['expectData'],
    #             'msg': data['msg']
    #         }
    #     }
    #     self.miniProgramLiveLg.check_title_lg(params)

    def test_02_open_mini_Program_Live(self):
        '''开启小程序直播'''
        if not self._check_case(["C00140"]): return
        self.miniProgramLiveLg.open_mini_Program_Live_lg()

    def test_03_close_mini_Program_Live(self):
        '''关闭小程序直播'''
        if not self._check_case(["C00141"]): return
        self.miniProgramLiveLg.close_mini_Program_Live_lg()

    def test_04_mini_Program_Live_documentation(self):
        '''打开小程序直播说明文档'''
        if not self._check_case(["C00142"]): return
        self.miniProgramLiveLg.mini_Program_Live_documentation_lg()

    def tearDown(self):
        super(test_miniProgramLive, self).tearDown()


    @classmethod
    def tearDownClass(cls):
        super(test_miniProgramLive, cls).tearDownClass()

if __name__ == '__main__':
    unittest.main()