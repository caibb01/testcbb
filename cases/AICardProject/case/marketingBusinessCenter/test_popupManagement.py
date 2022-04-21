import datetime
import os
import time
import unittest
from ddt import data, ddt
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.PopupManagementLg import PopupManagementLg
from myweb.core.runner import TestCase
from myweb.tools.env_params import get_env_params
from myweb.utils.config import JsonConfig


@ddt
class test_popup_Management(TestCase):
    __author__ = "mabb01"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image',
                              'th.jpg')

    @classmethod
    def setUpClass(cls):
        super(test_popup_Management, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.PopupManagementLg = PopupManagementLg(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])

    @data(
        {
            "path": IMAGE_PATH,
        }
    )
    def test_case_01_new_marketing_popup(self, data):
        if not self._check_case(["C00267"]): return
        params = {
            "path": data['path'],
            "associated_items": "mbb新建营销弹窗勿动",
            "entry_name": "全局",
            "start_date": "2022/04/02 00:00",
            "end_date": "2060/04/02 23:59",

        }
        # 进入预约管理-弹窗管理
        self.PopupManagementLg.into_popup_management_lg()
        # 新建营销弹窗
        self.PopupManagementLg.new_marketing_popup_lg(params)

    def test_case_02_edit_marketing_popup(self):
        if not self._check_case(["C00269"]): return
        params = {
            "modify marketing pop-up name": "mbb编辑后的营销弹窗",
        }
        # 编辑营销弹窗
        self.PopupManagementLg.edit_marketing_popup_lg(params)
        self.driver.refresh()
        time.sleep(2)


    def test_case_03_search_marketing_popup(self):
        if not self._check_case(["C00271"]): return
        params = {
            "key_word": "mbb",
            "project_name": "全局",

        }
        # 输入关联项目进行搜索
        self.PopupManagementLg.select_item_lg(params)
        # 输入关键词搜索营销弹窗
        self.PopupManagementLg.search_marketing_popup_lg(params)


    def test_case_04_delete_marketing_popup(self):
        if not self._check_case(["C00270"]): return
        # 删除营销弹窗
        self.PopupManagementLg.delete_marketing_popup_lg()
        self.driver.refresh()


    def test_case_05_access_authorization_popup(self):
        # 进入授权弹窗
        self.PopupManagementLg.access_authorization_popup_lg()

    @data(
        {
            "path": IMAGE_PATH}
    )
    def test_case_06_add_authorization_popup(self, data):
        if not self._check_case(["C00272"]): return

        params = {
            "path": data['path'],
            "authorization_popup_name": "mbb新建授权弹窗勿动",
        }
        # 新增授权弹窗
        self.PopupManagementLg.add_authorization_popup_lg(params)

    def test_case_07_edit_authorization_popup(self):
        if not self._check_case(["C00274"]): return

        # 编辑授权弹窗
        self.PopupManagementLg.edit_authorization_popup_lg()

    def test_case_08_keyword_search(self):
        if not self._check_case(["C00276"]): return
        params = {
            "authorization_pop-up_keyword": "mbb新建授权弹窗勿动",

        }

        # 输入关键字搜索授权弹窗
        self.PopupManagementLg.keyword_search_lg(params)

    def test_case_09_delete_authorization_popup(self):
        if not self._check_case(["C00275"]): return
        # 删除授权弹窗
        self.PopupManagementLg.delete_authorization_popup_lg()

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        super(test_popup_Management, cls).tearDownClass()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
