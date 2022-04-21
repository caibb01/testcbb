#-*- encoding=utf8 -*-

import os
import unittest

from ddt import ddt,data
from time import sleep
from myweb.core.runner import TestCase
from myweb.utils.config import JsonConfig
from myweb.utils.excelUtil import ExcelUtil
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.userManagementLG.clientStandingBookLg import clientStandingBookLg
from myweb.tools.env_params import get_env_params

EXCEL_ROOT_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'excel')
EXCEL_PATH = os.path.join(EXCEL_ROOT_PATH, 'client_standing_book.xls')

excel_group_customer = ExcelUtil(EXCEL_PATH, 'group_customer_inquiry')
excel_regional_customer = ExcelUtil(EXCEL_PATH, 'regional_customer_inquiry')
excel_project_customer = ExcelUtil(EXCEL_PATH, 'project_customer_inquiry')
excel_booking_customer = ExcelUtil(EXCEL_PATH, 'booking_customer_inquiry')
excel_business_relationship = ExcelUtil(EXCEL_PATH, 'review_business_relationship')
excel_topological_graph = ExcelUtil(EXCEL_PATH,'review_topological_graph')
excel_export_list = ExcelUtil(EXCEL_PATH,'export_list')
excel_click_next_page = ExcelUtil(EXCEL_PATH,'click_next_page')
excel_click_previous_page = ExcelUtil(EXCEL_PATH,'click_previous_page')

@ddt
class test_clientStandingBook(TestCase):
    __author__ = "lips"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data','loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_clientStandingBook,cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.clientStandingBookLg = clientStandingBookLg(cls.driver)
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
        cls.clientStandingBookLg.into_clientStandingBook_page()

    def setUp(self):
        super(test_clientStandingBook, self).setUp()

    @data(*excel_group_customer.next())
    def test_01_group_cusromer_inquiry(self, data):
        '''查询集团客户'''
        params = {
            'modelName': data['model'],
            'parameter': {
                'phone': str(data['phone']),
                'startDate': data['startDate'],
                'endDate': data['endDate'],
                'userIntent': data['userIntent'],
                #1为精确查询，2为模糊查询
                'check_phone_type':data['check_phone_type']
            },
            'checkData': {
                #查找列表标准值
                'standardData': data['standardData'],
                'expectResult': data['expectResult'],
                'msg': data['msg']
            }
        }
        self.clientStandingBookLg.group_cusromer_inquiry_lg(params)

    @data(*excel_regional_customer.next())
    def test_02_regional_customer_inquiry(self, data):
        '''查询区域客户'''
        params = {
            'modelName': data['model'],
            'parameter': {
                'phone': str(data['phone']),
                'region_Name': data['region_Name'],
                'startDate': data['startDate'],
                'endDate': data['endDate'],
                'userIntent': data['userIntent'],
                'check_regional_type':data['check_regional_type'],
                'check_phone_type':data['check_phone_type']
            },
            'checkData': {
                'standardData': data['standardData'],
                'expectResult': data['expectResult'],
                'msg': data['msg']
            }
        }
        self.clientStandingBookLg.regional_customer_inquiry_lg(params)

    @data(*excel_project_customer.next())
    def test_03_project_customer_inquiry(self, data):
        '''查询项目用户'''
        params = {
            'modelName': data['model'],
            'parameter': {
                'phone': str(data['phone']),
                'project_Type': data['project_Type'],
                'project_Name': data['project_Name'],
                'startDate': data['startDate'],
                'endDate': data['endDate'],
                'userIntent': data['userIntent'],
                'check_project_type': data['check_project_type'],
                'check_phone_type': data['check_phone_type']
            },
            'checkData': {
                'standardData': data['standardData'],
                'expectResult': data['expectResult'],
                'msg': data['msg']
            }
        }
        self.clientStandingBookLg.project_customer_inquiry_lg(params)

    @data(*excel_booking_customer.next())
    def test_04_booking_customer_inquiry(self, data):
        '''查询预约用户'''
        params = {
            'modelName': data['model'],
            'parameter': {
                'project_Type': data['project_Type'],
                'project_Name': data['project_Name'],
                'selectType': data['selectType'],
                'Name_or_phone': data['Name_or_phone'],
                'startDate': data['startDate'],
                'endDate': data['endDate'],
                'startDate1': data['startDate1'],
                'endDate1': data['endDate1'],
                'check_project_type': data['check_project_type'],
                'check_phone_type': data['check_phone_type'],
                'check_name_type':data['check_name_type']
            },
            'checkData': {
                'standardData': data['standardData'],
                'expectResult': data['expectResult'],
                'msg': data['msg']
            }
        }
        self.clientStandingBookLg.booking_customer_inquiry_lg(params)

    @data(*excel_business_relationship.next())
    def test_05_review_business_relationship_table(self,data):
        '''查看业务关系表，关闭业务关系表'''
        params = {
        "modelName" : data['model'],
        "standardName" : data['standardName']
        }
        self.clientStandingBookLg.review_business_relationship_table_lg(params)


    @data(*excel_topological_graph.next())
    def test_06_review_topological_graph(self,data):
        '''查看来去拓扑图,关闭拓扑图'''
        params = {
        'modelName' : data['model']
        }
        self.clientStandingBookLg.review_topological_graph_lg(params)

    @data(*excel_export_list.next())
    def test_07_export_list(self,data):
        '''导出列表并下载'''
        params = {
            'modelName' : data['model']
        }
        self.clientStandingBookLg.export_list_lg(params)


    def test_08_review_customer_detail(self):
        '''预约客户-查看客户列表的详情'''
        params = {
            'modelName': '预约客户'

        }
        self.clientStandingBookLg.review_customer_detail_lg(params)

    def test_09_export_booking_customer_list(self):
        '''导出预约客户列表'''
        params = {
            'modelName': '预约客户'
        }
        self.clientStandingBookLg.export_booking_customer_list_lg(params)

    @data(*excel_click_previous_page.next())
    def test_10_page_switching(self,data):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        params = {
            'modelName': data['model']
        }
        self.clientStandingBookLg.page_switching_lg(params)

    def tearDown(self):
        super(test_clientStandingBook, self).tearDown()
    @classmethod
    def tearDownClass(cls):
        super(test_clientStandingBook, cls).tearDownClass()
if __name__ == '__main__':
    import unittest
    unittest.main()