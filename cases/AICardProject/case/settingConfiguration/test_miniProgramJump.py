# -*- encoding=utf8 -*-

import os,sys
import unittest

from ddt import ddt,data,unpack
from time import sleep
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from myweb.utils.excelUtil import ExcelUtil
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.settingConfigurationLG.miniProgramJumpLg import miniProgramJumpLg
from random import randint
from myweb.tools.env_params import get_env_params
@ddt
class test_miniProgramJump(TestCase):
    __author__ = "lips"
    # 当前模块名
    __module = sys._getframe().f_code.co_name
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_miniProgramJump, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.miniProgramJumpLg = miniProgramJumpLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.miniProgramJumpLg.into_miniProgramJump_page()

    def setUp(self):
        super(test_miniProgramJump, self).setUp()

    contentName = "test"+ str(randint(100,1000))
    miniProgramId = "wxc02b67a8414"+ str(randint(10000,99999))
    miniProgramId2 = "wxfd936776387" + str(randint(10000, 99999))
    @data([{'contentName': contentName,'miniProgramId':miniProgramId,'miniProgramId2':miniProgramId2,'expectData':contentName,'flag':'True','msg':'新增失败'}])
    @unpack
    def test_01_add_mini_program(self,data):
        """新增小程序,保存"""
        if not self._check_case(["C00166"]): return
        params = {
            'parameter':{
                'contentName': data['contentName'],
                'miniProgramId': data['miniProgramId'],
                'miniProgramId2': data['miniProgramId2']
            },
            'checkData': {
                'expectData': data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.miniProgramJumpLg.add_mini_program_lg(params)

    contentName2 = "test2" + str(randint(100, 1000))
    miniProgramId = "wx68406315e5e" + str(randint(10000, 99999))
    @data([{'contentName2': contentName2, 'miniProgramId': miniProgramId,'expectData': contentName2, 'flag': 'Flase', 'msg': '新增成功'}])
    @unpack
    def test_02_cancel_add_mini_program(self, data):
        """新增小程序，取消保存"""
        if not self._check_case(["C00168"]): return
        params = {
            'parameter': {
                'contentName2': data['contentName2'],
                'miniProgramId': data['miniProgramId']
            },
            'checkData': {
                'expectData': data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.miniProgramJumpLg.cancel_add_mini_program_lg(params)

    @data([{'expectData': contentName, 'flag': 'False','msg': '删除失败'}])
    @unpack
    def test_03_delete_mini_program(self,data):
        """删除小程序"""
        if not self._check_case(["C00169"]): return
        params = {
            'checkData': {
                'expectData': data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.miniProgramJumpLg.delete_mini_program_lg(params)

    def tearDown(self):
        super(test_miniProgramJump, self).tearDown()


if __name__ == '__main__':
        unittest.main()