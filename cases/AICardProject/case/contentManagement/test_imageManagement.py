# -*- encoding=utf8 -*-
import os
import unittest
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.imageManagementLg import imageManagementLg
import time
from myweb.utils.config import JsonConfig
from ddt import ddt, data
import datetime
from myweb.tools.env_params import get_env_params

@ddt
class test_ImageManagement(TestCase):
    __author__ = "zhouyh"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image', 'th.jpg')


    @classmethod
    def setUpClass(cls):
        super(test_ImageManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.imageManagementLg = imageManagementLg(cls.driver)
        cls.loginLogic.login(url = cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.imageManagementLg.into_imageManagement_page()

    @data(
        {'title': "JK图片" + now_time, "path": IMAGE_PATH}
    )
    def test_case_01_upload_image(self, data):
        # 上传图片
        if not self._check_case(["C00054"]): return
        params = {
            'title': data['title'],
            'path': data['path']
        }
        self.imageManagementLg.upload_image(params)
        time.sleep(3)

    @data(
        {'title': "JK图片" + now_time, "path": IMAGE_PATH}
    )
    def test_case_02_image_detail(self, data):
        # 图片详情
        if not self._check_case(["C00055"]): return
        params = {
            'title': data['title'],
            'path': data['path']
        }
        self.imageManagementLg.image_detail(params)
        time.sleep(3)

    def test_case_03_delete_image(self):
        # 删除图片
        if not self._check_case(["C00056"]): return
        self.imageManagementLg.delete_image()
        time.sleep(3)

    def test_case_04_page_turning(self):
        # 翻页
        if not self._check_case(["C00057"]): return
        self.imageManagementLg.page_turning()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        super(test_ImageManagement, cls).tearDownClass()
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
