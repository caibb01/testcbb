# -*- encoding=utf8 -*-
import os, sys, datetime
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from myweb.tools.util import get_time
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.PopupManagementLogic import PopupManagementLogic


class PopupManagementCase(TestCase):
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
        super(PopupManagementCase, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.popupManagementLogic = PopupManagementLogic(cls.driver)
        cls.loginLogic.login(username=cls.__login_data['username'],
                             password=cls.__login_data['password'],
                             orgname=cls.__login_data['orgname'])
        cls.loginLogic.logincheck()
        # 进入AI云店页面
        cls.loginLogic.openAI()
        # 进入弹窗管理页面
        cls.popupManagementLogic.into_popupManagement_page()

    def setUp(self):
        super(PopupManagementCase, self).setUp()
        if self._need_delete:
            # 倒序循环，每次删掉最末尾
            for need_del in reversed(self._need_delete):
                self.popupManagementLogic.delete_popup(need_del)
                self._need_delete.remove(need_del)

    def tearDown(self):
        super(PopupManagementCase, self).tearDown()
        if self._need_delete:
            # 倒序循环，每次删掉最末尾
            for need_del in reversed(self._need_delete):
                self.popupManagementLogic.delete_popup(need_del)
                self._need_delete.remove(need_del)

    def test_insert_main_page_popup(self):
        """
        新增弹窗用例----首页
        """
        params = {
            "popup_name": "UI自动化测试新增弹窗",
            "project_relation_name": "全局",
            "control_page": ["首页", "集团首页"],
            "jump_page": ["按类型", "项目楼盘", "全部"],
            "condition": "每次进入",
            "start_and_end_time": self._get_start_time_and_end_time(start_time=1, end_time=2),
            "image_path": os.path.join(self.__image_path, 'penguin01.jpg'),
        }
        self.popupManagementLogic.insert_popup(params=params)
        self._need_delete.append(params)

    def test_insert_area_popup(self):
        """
        新增弹窗用例----区域
        """
        params = {
            "popup_name": "UI自动化测试新增弹窗",
            "project_relation_name": "全局",
            "control_page": ["区域", "百色"],
            "jump_page": ["按类型", "项目楼盘", "全部"],
            "condition": "每次进入",
            "start_and_end_time": self._get_start_time_and_end_time(start_time=1, end_time=2),
            "image_path": os.path.join(self.__image_path, 'penguin02.jpg'),
        }
        self.popupManagementLogic.insert_popup(params=params)
        self._need_delete.append(params)

    def test_insert_project_popup(self):
        """
        新增弹窗用例----项目
        """
        params = {
            "popup_name": "UI自动化测试新增弹窗",
            "project_relation_name": "全局",
            "control_page": ["项目", "自动化测试"],
            "jump_page": ["按类型", "项目楼盘", "全部"],
            "condition": "每次进入",
            "start_and_end_time": self._get_start_time_and_end_time(start_time=1, end_time=2),
            "image_path": os.path.join(self.__image_path, 'penguin03.jpg'),
        }
        self.popupManagementLogic.insert_popup(params=params)
        self._need_delete.append(params)

    def test_editor_area_popup(self):
        """
        编辑弹窗用例----区域
        """
        params = {
            "popup_name": "UI自动化测试新增弹窗",
            "project_relation_name": "全局",
            "control_page": ["区域", "百色"],
            "jump_page": ["按类型", "项目楼盘", "全部"],
            "condition": "每次进入",
            "start_and_end_time": self._get_start_time_and_end_time(start_time=1, end_time=2),
            "image_path": os.path.join(self.__image_path, 'penguin01.jpg'),
        }
        self.popupManagementLogic.insert_popup(params=params)
        params2 = {
            "popup_name_old": params["popup_name"],
            "popup_name": "UI自动化测试编辑弹窗",
        }
        self.popupManagementLogic.editor_popup(params=params2)
        self._need_delete.append(params)
        self._need_delete.append(params2)

    def test_delete_area_popup(self):
        """
        删除弹窗用例----区域
        """
        params = {
            "popup_name": "UI自动化测试删除弹窗",
            "project_relation_name": "全局",
            "control_page": ["区域", "百色"],
            "jump_page": ["按类型", "项目楼盘", "全部"],
            "condition": "每次进入",
            "start_and_end_time": self._get_start_time_and_end_time(start_time=1, end_time=2),
            "image_path": os.path.join(self.__image_path, 'penguin01.jpg'),
        }
        self.popupManagementLogic.insert_popup(params)
        self.popupManagementLogic.delete_popup(params)

    def _get_start_time_and_end_time(self, start_time, end_time):
        """
        给定开始时间距离今天的日期，和结束时间距离今天的日期,得到格式化后的时间
        :param start_time: 今天距离开始时间差的天数
        :param end_time: 今天距离结束时间差的天数
        :param format: 时间格式
        :return:
        """
        start_time = get_time(True, days=start_time)
        end_time = get_time(True, days=end_time)
        return [start_time, end_time]


if __name__ == '__main__':
    import unittest

    unittest.main()
