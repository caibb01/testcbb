#-*- encoding=utf8 -*-

import os,sys
import unittest

from ddt import ddt,data,unpack
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.displayConfigurationLG.StartupPageLogic import StartupPageLg
from myweb.tools.env_params import get_env_params

@ddt
class test_StartupPage(TestCase):
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
        super(test_StartupPage, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.StartupPageLogic = StartupPageLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.StartupPageLogic.into_StartupPage()

    def setUp(self):
        super(test_StartupPage, self).setUp()

    @data([{'path':os.path.join(__image_path, '07.jpg')}])
    @unpack
    def test_01_upload_still_image_lg(self,data):
        '''启动页配置，上传静态图片，预览，保存，刷新页面'''
        if not self._check_case(["C00203","C00206"]): return
        params = {
            'path': data['path']
        }
        self.StartupPageLogic.upload_still_image_lg(params)

    @data([{'path': os.path.join(__image_path, '06.gif')}])
    @unpack
    def test_02_upload_dynamic_image_lg(self,data):
        '''启动页配置，上传动态图片，预览，保存，刷新页面'''
        if not self._check_case(["C00204"]): return
        params = {
            'path': data['path']
        }
        self.StartupPageLogic.upload_dynamic_image_lg(params)

    @data([{'path': os.path.join(__image_path, '07.jpg')}])
    @unpack
    def test_03_upload_image_refresh_page_lg(self,data):
        '''启动页配置，上传图片，刷新'''
        if not self._check_case(["C00205"]): return
        params = {
            'path': data['path']
        }
        self.StartupPageLogic.upload_image_refresh_page_lg(params)

    @data([{'path': os.path.join(__image_path, '08.jpg')}])
    @unpack
    def test_04_upload_images_larger_than_2M_lg(self,data):
        '''启动页配置，上传大于2M的图片'''
        if not self._check_case(["C00207"]): return
        params = {
            'path': data['path']
        }
        self.StartupPageLogic.upload_images_larger_than_2M_lg(params)

    def test_05_select_image_fill_mode(self):
        '''选择图片填充模式'''
        self.StartupPageLogic.select_image_fill_mode_lg()

    def test_06_open_startup_page(self):
        '''开启启动页图片'''
        self.StartupPageLogic.open_startup_page_lg()

    def test_07_close_startup_page(self):
        '''关闭启动页图片'''
        self.StartupPageLogic.close_startup_page_lg()

    def tearDown(self):
        super(test_StartupPage, self).tearDown()

if __name__ == '__main__':
    unittest.main()