# -*- encoding=utf8 -*-
import os
import sys
from myweb.tools.getpath import getFilePath
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.recommendArticleLg import RecommendArticleLg
from time import sleep
from myweb.tools.env_params import get_env_params
import datetime
from faker import Faker
from ddt import ddt, data

@ddt
class test_recommendArticle(TestCase):
    __author__ = "zhouyihui"
    # __module = sys._getframe().f_code.co_name
    # 图片文件路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image')
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    _need_delete = []
    # 获取当前时间戳
    now_time = datetime.datetime.now().strftime('%H%M%S')
    # 获取假数据
    fakeinfo = Faker(locale="zh_CN")

    @classmethod
    def setUpClass(cls):
        super(test_recommendArticle, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url = cls.env_param['url'],
                             username= cls.env_param['username'],
                             password= cls.env_param['password'],
                             orgname= cls.env_param['orgname'])
        cls.loginLogic.logincheck( cls.env_param['loginuser'])
        cls.loginLogic.openAI( cls.env_param['ai_xpath'])
        cls.recommendArticleLg = RecommendArticleLg(cls.driver)
        cls.recommendArticleLg.into_article_page()

    def setUp(self):
        super(test_recommendArticle, self).setUp()

    @data(
        {'title': "UI" + now_time, 'content': fakeinfo.text(20),'imagePath': getFilePath("200.jpg"),
         "button_name":"活动按钮名称" , "start_time": "2022/01/01 00:00", "end_time": "2022/12/31 23:59",
         "share_copy":"分享文案"}
    )
    def test_01_saveArticle(self, data):
        """
        新建文章
        """
        # if not self._check_case(["C00043","C00045","C00046"]): return
        params = {
            "title": data['title'],
            "content": data['content'],
            "imagePath": data['imagePath'],
            "button_name": data['button_name'],
            "start_time": data['start_time'],
            "end_time": data['end_time'],
            "share_copy":data['share_copy']
        }
        self.recommendArticleLg.addArticle(params)
        sleep(3)


    @data(
        {'title': "new", 'phone_number': fakeinfo.text(20)}
    )
    def test_02_apply_list(self, data):
        """
        报名列表
        """
        # if not self._check_case(["C00059"]): return
        params = {
            'title': data['title'],
            'phone_number': data['phone_number']
        }
        self.articleContentLg.apply_list(params)
        sleep(3)


    @data(
        {'newTitle': "new" + now_time, 'newContent': fakeinfo.text(20)}
    )
    def test_03_editArticle(self, data):
        """
        编辑文章
        """
        # if not self._check_case(["C00041","C00048","C00049"]): return
        params = {
            "newTitle": data['newTitle'],
            "newContent": data['newContent']
        }
        self.recommendArticleLg.editArticle(params)
        sleep(3)

    def test_04_publishArticle(self):
        """
        发布文章
        """
        # if not self._check_case(["C00051"]): return
        self.recommendArticleLg.publishArticle("待发布")
        sleep(3)

    def test_05_closeArticle(self):
        """
        关闭文章
        """
        # if not self._check_case(["C00052"]): return
        self.recommendArticleLg.closeArticle("已发布")
        sleep(3)

    def test_06_copy_article_link(self):
        """
        复制公众号文章
        """
        # if not self._check_case(["C00052"]): return
        self.recommendArticleLg.copy_article_link("s/q_B-jKqSXMFgWdx6GjYYNg")
        sleep(3)

    def test_07_search_article(self):
        """
        查询文章
        """
        # if not self._check_case(["C00055"]): return
        self.recommendArticleLg.search_article("UI")
        sleep(3)

    def test_08_page_turning(self):
        # 翻页
        # if not self._check_case(["C00061"]): return
        self.articleContentLg.page_turning()
        sleep(3)

    def tearDown(self):
        super(test_recommendArticle, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_recommendArticle, cls).tearDownClass()

if __name__ == '__main__':
    import unittest
    unittest.main()
