#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig
from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.contentManagementLG.projectManagementLg import projectManagementLg
from myweb.tools.env_params import get_env_params

@ddt
class test_projectManagement(TestCase):
    __author__ = "lips"
    #登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_projectManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.projectManagementLg = projectManagementLg(cls.driver)
        # cls.loginLogic.login(username=cls.__login_data['username'],
        #                      password=cls.__login_data['password'],
        #                      orgname=cls.__login_data['orgname'])
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.projectManagementLg.into_projectManagement_page()

    def setUp(self):
        super(test_projectManagement, self).setUp()

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_01_close_project(self, data):
        '''关闭项目'''
        if not self._check_case(["C00007"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.close_project_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_02_publish_project(self,data):
        '''发布项目(包含项目已关联区域，未关联区域，项目被禁用)'''
        if not self._check_case(["C00001","C00002","C00004","C00006"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.publish_multiple_projects_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_03_edit_project(self, data):
        '''编辑项目'''
        if not self._check_case(["C00008"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.edit_project_lg(params)


    @data([{'project_Type': '','project_Name':'明源集团宝安中心花园','check_project_type':'1',}],
          [{'project_Type': 'input','project_Name':'云来逸宅','check_project_type':'2',}])
    @unpack
    def test_04_select_project(self,data):
        '''选择或输入系统项目名称'''
        if not self._check_case(["C00009","C00010"]): return
        params = {
            'parameter': {
                'project_Type': data['project_Type'],
                'project_Name':data['project_Name'],
                'check_project_type':data['check_project_type']
            }
        }
        self.projectManagementLg.select_project_lg(params)

    def test_05_select_city(self):
        '''根据所属城市，查询项目'''
        if not self._check_case(["C00011"]): return
        self.projectManagementLg.select_city_lg()

    @data([{'publishStatus': '全部'}],
          [{'publishStatus': '待发布'}],
          [{'publishStatus': '已发布'}],
          [{'publishStatus': '已关闭'}]
          )
    @unpack
    def test_06_select_publish_status(self,data):
        '''根据发布状态，查询项目'''
        if not self._check_case(["C00012"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.select_publish_status_lg(params)

    @data(
          [{'publishStatus': '已发布','project_Type': '','project_Name':'明源集团宝安中心花园','check_project_type':'1',}]
          )
    @unpack
    def test_07_query(self,data):
        '''根据项目系统名称、所属城市、发布状态，查询项目'''
        if not self._check_case(["C00013"]): return
        params = {
            'publishStatus': data['publishStatus'],
            'parameter': {
                'project_Type': data['project_Type'],
                'project_Name': data['project_Name'],
                'check_project_type': data['check_project_type']
            }
        }
        self.projectManagementLg.query_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_08_reception_list(self,data):
        '''打开接待列表，项目接待列表-人员选择,勾选checkbox'''
        if not self._check_case(["C00014","C00016","C00020"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.reception_list_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_09_reception_list_people_search(self,data):
        '''项目接待列表-人员搜索'''
        if not self._check_case(["C00015"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.reception_list_people_search_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_11_reception_list_people_hide(self,data):
        '''项目接待列表-人员隐藏'''
        if not self._check_case(["C00017"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.reception_list_people_hide_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_12_reception_list_people_sort(self,data):
        '''项目接待列表-人员排序'''
        if not self._check_case(["C00018"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.reception_list_people_sort_lg(params)

    @data([{'publishStatus': '已发布'}])
    @unpack
    def test_13_reception_list_remove_personnel(self,data):
        '''项目接待列表-删除人员'''
        if not self._check_case(["C00019"]): return
        params = {
            'publishStatus': data['publishStatus']
        }
        self.projectManagementLg.reception_list_remove_personnel_lg(params)

    # @data([{'publishStatus': '已发布'}])
    # @unpack
    # def test_14_save_reception_list(self,data):
    #     '''项目接待列表-保存'''
    #     params = {
    #         'publishStatus': data['publishStatus']
    #     }
    #     self.projectManagementLg.save_reception_list_lg(params)

    def test_15_copy_page_path(self):
        '''复制页面路径'''
        if not self._check_case(["C00021"]): return
        self.projectManagementLg.copy_page_path_lg()

    def test_16_page_switching(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        if not self._check_case(["C00022"]): return
        self.projectManagementLg.page_switching_lg()

    def tearDown(self):
        super(test_projectManagement, self).tearDown()

if __name__ == '__main__':
    unittest.main()



