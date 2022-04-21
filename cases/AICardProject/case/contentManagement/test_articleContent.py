# -*- encoding=utf8 -*-
import os
import sys
from myweb.tools.getpath import getFilePath
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.articleContentLg import articleContentLg
from time import sleep
from myweb.tools.env_params import get_env_params

class test_articleContent(TestCase):
    __author__ = "wangliangzheng"
    # __module = sys._getframe().f_code.co_name
    # 图片文件路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image')
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    _need_delete = []

    @classmethod
    def setUpClass(cls):
        super(test_articleContent, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url = cls.env_param['url'],
                             username= cls.env_param['username'],
                             password= cls.env_param['password'],
                             orgname= cls.env_param['orgname'])
        cls.loginLogic.logincheck( cls.env_param['loginuser'])
        cls.loginLogic.openAI( cls.env_param['ai_xpath'])
        cls.articleContentLg = articleContentLg(cls.driver)
        cls.articleContentLg.into_article_page()

    def setUp(self):
        super(test_articleContent, self).setUp()

    def test_01_addArticle(self):
        """
        新增文章
        self.articleContentLg.newContent()
        time.sleep(3)
        """
        if not self._check_case(["C00041","C00043","C00048"]): return
        params = {
            "titleName": "新的文章呀",
            "content": "全局",
            "imagePath": getFilePath("200.jpg")
        }
        self.articleContentLg.addArticle(params)
        sleep(3)

    def test_02_saveArticle(self):
        """
        新建原创文章-开启活动
        """
        if not self._check_case(["C00045","C00046"]): return
        params = {
            "title": "JK标题",
            "content": "JK内容",
            "imagePath": getFilePath("200.jpg"),
            "button_name": "活动按钮名称",
            "start_time": "2021/08/18 00:00",
            "end_time": "2021/12/31 23:59",
        }
        self.articleContentLg.saveArticle(params)
        sleep(3)

    def test_03_exitArticle(self):
        """
        编辑文章
        """
        if not self._check_case(["C00049","C00055"]): return
        params = {
            "queryTitle": "新的文章呀",
            "newTitle": "新的标题",
            "newContent": "新的文章内容",
            "newQueryTitle": "新的标题"
        }
        self.articleContentLg.editArticle(params)
        sleep(3)

    def test_04_postArticleEdit(self):
        """
        发布文章后进行编辑
        """
        if not self._check_case(["C00051"]): return
        params = {
            "newQueryTitle": "新的标题",
            "postNewTitle": "发布后的新的标题",
            "postNewContent": "发布后的新文章内容",
            "pastNewQueryTitle": "发布后的新的标题"
        }
        self.articleContentLg.postArticleEdit(params)
        sleep(3)

    def test_05_closeArticle(self):
        """
        关闭文章
        """
        if not self._check_case(["C00052"]): return
        params = "已发布"
        self.articleContentLg.closeArticle(params)
        sleep(3)

    def test_06_apply_list(self):
        """
        报名列表
        """
        if not self._check_case(["C00059"]): return
        params = {
            'publish_status': "全部",
            'title': "JK",
            'phone_number': 13800000000
        }
        self.articleContentLg.apply_list(params)
        sleep(3)

    def test_07_page_turning(self):
        # 翻页
        if not self._check_case(["C00061"]): return
        self.articleContentLg.page_turning()
        sleep(3)


    # @classmethod
    # def tearDownClass(cls):
    #     super(test_articleContent, cls).tearDownClass()
    #     cls.driver.close()
    #     # if self._need_delete:
    #     #     # 倒序循环，每次删掉最末尾
    #     #     for need_del in reversed(self._need_delete):
    #     #         self.managerBlankPageLogic.delete_blankPage(need_del)
    #     #         self._need_delete.remove(need_del)

    def tearDown(self):
        super(test_articleContent, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_articleContent, cls).tearDownClass()

if __name__ == '__main__':
    import unittest
    unittest.main()
