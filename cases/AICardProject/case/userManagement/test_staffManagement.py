#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.userManagementLG.staffManagementLg import staffManagementLg
from myweb.tools.env_params import get_env_params

@ddt
class test_staffManagement(TestCase):
    __author__ = "lips"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_staffManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.staffManagementLg = staffManagementLg(cls.driver)
        cls.env_param = get_env_params()
        # cls.loginLogic.login(username=cls.__login_data['username'],
        #                      password=cls.__login_data['password'],
        #                      orgname=cls.__login_data['orgname'])
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.staffManagementLg.into_staffManagementLg_page()
    def setUp(self):
        super(test_staffManagement, self).setUp()

    @data(
          [{'modelName':'销售团队','check_model_type':'1','check_phone_type': '', 'project_Name':'','project_Type':'','name_or_phone':'18816851537','expectData':'18816851537','flag':'True','msg':"销售团队-未找到该员工",}],
          [{'modelName': '销售团队', 'check_model_type':'2','check_phone_type': '', 'project_Name': '', 'project_Type': '', 'name_or_phone': '李美丽','expectData': '18816851537','flag':'True','msg':"销售团队-未找到该员工"}],
          [{'modelName': '销售团队', 'check_model_type':'3','check_phone_type':'1','project_Name': 'lips3专属测试项目', 'project_Type': 'input', 'name_or_phone': '李美丽','expectData': '18816851537','flag':'True','msg':"销售团队-未找到该员工"}],
          [{'modelName': '销售团队', 'check_model_type': '3', 'check_phone_type': '2', 'project_Name': 'lips3专属测试项目','project_Type': 'input', 'name_or_phone': '李美丽', 'expectData': '18816851537', 'flag': 'True','msg': "销售团队-未找到该员工"}]
          )
    @unpack
    def test_01_sales_team_inquiry(self, data):
        '''销售团队查询'''
        params = {
            'modelName':data['modelName'],
            'parameter': {
                'project_Name':data['project_Name'],
                'project_Type':data['project_Type'],
                'name_or_phone':data['name_or_phone'],
                'check_model_type':data['check_model_type'],
                'check_phone_type':data['check_phone_type']
                          },
            'checkData': {
                'expectData':data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.staffManagementLg.staff_management_inquiry_lg(params)

    @data([{'modelName': '行销团队', 'check_model_type':'1','check_phone_type':'','project_Name': '', 'project_Type': '', 'name_or_phone': '18816851537','expectData': '18816851537','flag':'True','msg':"行销团队-未找到该员工"}],
          [{'modelName': '行销团队', 'check_model_type':'2','check_phone_type':'','project_Name': '', 'project_Type': '', 'name_or_phone': '李紫宁','expectData': '18816851537','flag':'True','msg':"行销团队-未找到该员工"}],
          [{'modelName': '行销团队', 'check_model_type':'3','check_phone_type':'1','project_Name': '1哥伦布多项目333', 'project_Type': 'input', 'name_or_phone': '李紫宁','expectData': '18816851537','flag':'True','msg':"行销团队-未找到该员工"}],
           )
    @unpack
    def test_02_marketing_team_inquiry(self,data):
        '''行销团队查询'''
        params = {
            'modelName': data['modelName'],
            'parameter': {'project_Name': data['project_Name'],
                          'project_Type': data['project_Type'],
                          'name_or_phone': data['name_or_phone'],
                          'check_model_type':data['check_model_type'],
                          'check_phone_type':data['check_phone_type']
                          },
            'checkData': {
                'expectData':data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.staffManagementLg.staff_management_inquiry_lg(params)

    @data([{'modelName': '策划人员', 'check_model_type':'1','check_phone_type':'','project_Name': '', 'project_Type': '', 'name_or_phone': '13117879130','expectData': '13117879130','flag':'True','msg':"策划人员-未找到该员工"}],
          [{'modelName': '策划人员', 'check_model_type':'2','check_phone_type':'','project_Name': '', 'project_Type': '', 'name_or_phone': '刘涛策划','expectData': '13117879130','flag':'True','msg':"策划人员-未找到该员工"}],
          [{'modelName': '策划人员', 'check_model_type':'3','check_phone_type':'1','project_Name': '明源集团宝安中心花园', 'project_Type': 'input', 'name_or_phone': '刘涛策划','expectData': '13117879130','flag':'True','msg':"策划人员-未找到该员工"}],
           )
    @unpack
    def test_03_planning_team_inquiry(self,data):
        '''策划人员查询'''
        params = {
            'modelName': data['modelName'],
            'parameter': {'project_Name': data['project_Name'],
                          'project_Type': data['project_Type'],
                          'name_or_phone': data['name_or_phone'],
                          'check_model_type':data['check_model_type'],
                          'check_phone_type':data['check_phone_type']
                          },
            'checkData': {
                'expectData':data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.staffManagementLg.staff_management_inquiry_lg(params)

    @data(
          [{'modelName': '经纪人团队','check_phone_type':'1', 'name_or_phone': 'AI云店自动注册','expectData': '18816851537','flag':'True','msg':"经纪人团队-未找到该员工"}],
          [{'modelName': '经纪人团队','check_phone_type':'2','name_or_phone': '18816851537','expectData': '18816851537','flag':'True','msg':"经纪人团队-未找到该员工"}],
           )
    @unpack
    def test_04_broker_team_inquiry(self,data):
        '''经纪人团队查询'''
        params = {
            'modelName': data['modelName'],
            'parameter': {
                'name_or_phone': data['name_or_phone'],
                'check_phone_type':data['check_phone_type']
            },
            'checkData': {
                'expectData':data['expectData'],
                'flag': data['flag'],
                'msg': data['msg']
            }
        }
        self.staffManagementLg.broker_team_inquiry_lg(params)

    @data([{'modelName': '销售团队'}],
          [{'modelName': '策划人员'}]
          )
    @unpack
    def test_05_open_project_page(self,data):
        '''销售团队/策划人员团队：打开所属项目页面'''
        params = {
            'modelName': data['modelName']
        }
        self.staffManagementLg.open_project_page_lg(params)

    @data(
          [{'modelName': '行销团队'}]
          )
    @unpack
    def test_06_marketing_team_open_project_page(self, data):
        '''行销团队：打开所属项目页面'''
        params = {
            'modelName': data['modelName']
        }
        self.staffManagementLg.marketing_team_open_project_page_lg(params)


    @data([{'modelName': '销售团队'}],
          [{'modelName': '行销团队'}],
          [{'modelName': '策划人员'}],
          [{'modelName': '经纪人团队'}]
          )
    @unpack
    def test_07_synchronization_personnel_list(self,data):
        '''同步人员名单'''
        params = {
            'modelName': data['modelName']
        }
        self.staffManagementLg.synchronization_personnel_list_lg(params)

    @data([{'modelName': '销售团队'}],
          [{'modelName': '行销团队'}],
          [{'modelName': '策划人员'}],
          [{'modelName': '经纪人团队'}]
          )
    @unpack
    def test_08_enable_of_disable_card(self, data):
        '''判断该员工的卡片是启用还是禁用,弹窗选择确定'''
        params = {
            'modelName': data['modelName']
        }
        self.staffManagementLg.enable_of_disable_card_lg(params)

    @data([{'modelName': '销售团队'}],
          [{'modelName': '行销团队'}],
          [{'modelName': '策划人员'}],
          [{'modelName': '经纪人团队'}]
          )
    @unpack
    def test_09_cancel_enable_of_disable_card(self,data):
        '''判断该员工的卡片是启用还是禁用，弹窗选择取消'''
        params = {
            'modelName': data['modelName']
        }
        self.staffManagementLg.cancel_enable_of_disable_card_lg(params)


    @data([{'modelName': '销售团队'}],
          [{'modelName': '行销团队'}],
          [{'modelName': '策划人员'}],
          [{'modelName': '经纪人团队'}]
          )
    @unpack
    def test_10_page_switching(self,data):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        params = {
                    'modelName': data['modelName']
                }
        self.staffManagementLg.page_switching_lg(params)

    def tearDown(self):
        super(test_staffManagement, self).tearDown()

if __name__ == '__main__':
    unittest.main()