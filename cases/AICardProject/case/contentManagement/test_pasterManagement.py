# -*- encoding=utf8 -*-
import os
import unittest
from myweb.tools.getpath import getFilePath
from myweb.utils.config import JsonConfig
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.pasterManagementLg import pasterManagementLg, sleep
from ddt import ddt, data
from myweb.tools.env_params import get_env_params
import datetime

@ddt
class test_pasterContent(TestCase):
    __author__ = "wangliagnzheng"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()



    @classmethod
    def setUpClass(cls):

        super(test_pasterContent, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.pasterManagementLg = pasterManagementLg(cls.driver)
        cls.pasterManagementLg.into_poster_page()

        now_time = datetime.datetime.now().strftime('%H%M%S')
        # 海报标题
        cls.title = "海报" + now_time
        # 海报分类
        cls.sort = "分类" + now_time

    def test_01_addPaster(self):
        if not self._check_case(["C00114","C00115"]): return
        # 新增海报
        params = {
            "title": self.title,
            "imagePath": getFilePath('th.jpg'),
        }
        self.pasterManagementLg.addPaster(params)
        sleep(3)

    def test_02_editPaster(self):
        if not self._check_case(["C00116"]): return
        # 编辑海报
        params = {
            # "pasterTitle": self.title,
            "newTitle": "新的海报",
            "imagePath": getFilePath('video.jpg')
        }
        self.pasterManagementLg.editPaster(params)
        sleep(3)

    def test_03_delPaster(self):
        if not self._check_case(["C00119"]): return
        # 删除海报
        # params = {
        #     "searchTitle": "新的海报"
        # }
        self.pasterManagementLg.delPaster()
        sleep(3)

    def test_04_search_poster(self):
        # 搜索海报
        if not self._check_case(["C00120","C00121","C00122","C00123","C00124"]): return
        params = {
            "poster_title": "海报"
        }
        self.pasterManagementLg.search_poster(params)
        sleep(3)

    def test_05_poster_page_turning(self):
        # 海报列表翻页
        if not self._check_case(["C00127"]): return
        self.pasterManagementLg.poster_page_turning()
        sleep(3)

    def test_06_addSort(self):
        # 新增分类
        if not self._check_case(["C00128"]): return
        params = {
            "sortTitle": self.sort
        }
        self.pasterManagementLg.addSort(params)
        sleep(3)

    def test_07_edit_sort(self):
        # 编辑分类
        if not self._check_case(["C00129"]): return
        params = {
            "sort_title": "编辑后的分类"
        }
        self.pasterManagementLg.edit_sort(params)
        sleep(3)

    def test_08_del_sort(self):
        # 删除分类
        if not self._check_case(["C00130"]): return
        self.pasterManagementLg.del_sort()
        sleep(3)

    def test_09_sort_page_turning(self):
        # 海报分类翻页
        if not self._check_case(["C00132"]): return
        self.pasterManagementLg.sort_page_turning()
        sleep(3)

    @data(
        {"keywords": "分类"},
        {"keywords": "自动化分类"},
    )
    def test_10_search_sort(self, data):
        # 搜索分类
        if not self._check_case(["C00133","C00134"]): return
        params = {
            "keywords": data['keywords']
        }
        self.pasterManagementLg.search_sort(params)
        sleep(3)


    @classmethod
    def tearDownclass(cls):
        super(test_pasterContent, cls).tearDownclass()
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()
