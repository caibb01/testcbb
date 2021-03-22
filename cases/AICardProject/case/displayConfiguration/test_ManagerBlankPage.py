# -*- encoding=utf8 -*-
from myweb.core.runner import My4wTestCase
from myweb.utils.runner import JsonConfig
from myweb.tools.util import get_time
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.displayConfigurationLG.ManagerBlankPageLogic import ManagerBlankPageLogic
import os, sys, datetime
import unittest


class ManagerBlankPageCase(My4wTestCase):
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
        super(ManagerBlankPageCase, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.managerBlankPageLogic = ManagerBlankPageLogic(cls.driver)
        cls.loginLogic.login(username=cls.__login_data['username'],
                             password=cls.__login_data['password'],
                             orgname=cls.__login_data['orgname'])
        cls.loginLogic.logincheck()
        # 进入AI云店页面
        cls.loginLogic.openAI()
        # 进入弹窗管理页面
        cls.managerBlankPageLogic.into_manageBlankPage_page()

    def setUp(self):
        super(ManagerBlankPageCase, self).setUp()

    def tearDown(self):
        super(ManagerBlankPageCase, self).tearDown()
        if self._need_delete:
            # 倒序循环，每次删掉最末尾
            for need_del in reversed(self._need_delete):
                self.managerBlankPageLogic.delete_blankPage(need_del)
                self._need_delete.remove(need_del)

    def test_01_insert_blankPage(self):
        """
        新增新页面
        """
        params = {
            'page_name': 'UI自动新增%s' % get_time(True, format='%Y%m%d'),
            'desc': '描述',
            'relation_project': '全局',
            'background_img': os.path.join(self.__image_path, 'penguin01.jpg'),
            'share_img': os.path.join(self.__image_path, 'penguin01.jpg'),
            'business_relation': ['项目', '云来逸宅'],
            'button': '保存'
        }
        print(params)
        self._need_delete.append(params)
        self.managerBlankPageLogic.insert_blankPage(params)

    def test_02_update_blankPage(self):
        """
        编辑页面信息
        1、新增空白页
        2、进入编辑界面
        3、修改页面基础配置/修改页面配置
        """
        insert_params = {
            'page_name': 'UI自动编辑%s' % get_time(True, format='%Y%m%d'),
            'desc': '描述',
            'relation_project': '全局',
            'background_img': os.path.join(self.__image_path, 'penguin01.jpg'),
            'share_img': os.path.join(self.__image_path, 'penguin01.jpg'),
            'business_relation': ['项目', '哥伦布5勿动项目'],
            'button': '保存'
        }
        params = {
            # 用于搜索时查询具体是哪个空白页
            'blank_page': {
                'page_name': insert_params['page_name'],
                'relation_project': insert_params['relation_project'],
                'desc': insert_params['desc']
            },
            # 空白页基础配置
            'page_base_config': {
                'page_name': 'UI自动被编辑%s' % get_time(True, format='%Y%m%d'),
                'desc': '描述',
                'relation_project': '全局',
                'background_img': os.path.join(self.__image_path, 'penguin02.jpg'),
                'share_img': os.path.join(self.__image_path, 'penguin02.jpg'),
                'business_relation': ['项目', '哥伦布多项目3gg'],
                'button': '保存'
            },
            # 空白页页面配置
            'page_config': {
                # 默认/透明/隐藏/渐现/浮动渐现
                'header_style': '浮动渐现',
                # 白色/藏青色
                'module_color': '藏青色',
                'button': '保存'
            }
        }
        # 新增和修改时的名字可能会不一样，这里因为修改了名字，所以还原时清除的是修改的名字
        self._need_delete.append(params['page_base_config'])
        self.managerBlankPageLogic.insert_blankPage(insert_params)
        self.managerBlankPageLogic.into_blankPage_edit_page(page_name=insert_params['page_name'],
                                                            relation_project=insert_params['relation_project'],
                                                            desc=insert_params['desc'])
        self.managerBlankPageLogic.edit_blankPage(params)

    # def test_03_module_blankPage(self):
    #     """
    #     组件化配置空白页
    #     """
    #     params = [
    #         # 大图组件
    #         {"module": {"name": "大图"},
    #          "component": {"jump_type": ["标签", "项目楼盘", "云客后台"],
    #                        "poster_img": os.path.join(self.__image_path, 'penguin02.jpg')}},
    #         {}
    #     ]


if __name__ == '__main__':
    import unittest

    unittest.main()
