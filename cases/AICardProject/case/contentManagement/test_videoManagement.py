# -*- encoding=utf8 -*-
import sys
import time
import os
import unittest
from ddt import ddt, data
from myweb.tools.getpath import getFilePath
from myweb.utils.config import JsonConfig
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.videoManagementLg import videoManagementLg
from myweb.tools.env_params import get_env_params

@ddt
class test_videoContent(TestCase):
    __author__ = "wangliagnzheng"
    # 当前模块名
    # __module = sys._getframe().f_code.co_name
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image')

    @classmethod
    def setUpClass(cls):
        super(test_videoContent, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.videoManagementLg = videoManagementLg(cls.driver)
        cls.videoManagementLg.into_video_page()

    def test_01_addVideo(self):
        # 新增视频
        if not self._check_case(["C00075"]): return
        params = {
            "videoPath": getFilePath('xjdsp.mp4'),
            "imgPath": getFilePath('th.jpg'),
            "titleName": "新的视频",
            "proName": "全局"
        }
        self.videoManagementLg.addVideo(params)

    def test_02_updateVideo(self):
        # 编辑视频
        if not self._check_case(["C00076"]): return
        params = {
            "videoPath": os.path.join(self.IMAGE_PATH, 'xjdsp.mp4'),
            "imgPath": os.path.join(self.IMAGE_PATH, 'video.jpg'),
            "titleName": "更新视频",
            "proName": "项目"
        }
        #self.videoManagementLg.videoManagement(params)
        time.sleep(3)
        self.videoManagementLg.updateVideo(params)

    @data(
        {"videoName": "更新"},
        {"videoName": "更新视频"}
    )
    def test_03_queryVideo(self, data):
        # 搜索视频
        if not self._check_case(["C00078","C00079"]): return
        params = {
            "videoName": data['videoName']
        }
        self.videoManagementLg.queryVideo(params)

    def test_04_delVideo(self):
        # 删除视频
        if not self._check_case(["C00082"]): return
        self.videoManagementLg.delVideo()

    def test_05_page_turning(self):
        # 翻页
        if not self._check_case(["C00083"]): return
        self.videoManagementLg.page_turning()

    def tearDown(self):
        super(test_videoContent, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_videoContent, cls).tearDownClass()

if __name__ == '__main__':
    unittest.main()


