#-*- encoding=utf8 -*-
import os
import unittest

from ddt import ddt,data,unpack
from myweb.utils.config import JsonConfig

from myweb.core.runner import TestCase
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.ComplianceConfigurationLg import ComplianceConfigurationLg
from  random import randint
from myweb.tools.env_params import get_env_params

@ddt
class test_ComplianceConfiguration(TestCase):
    __author__ = "lips"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    # 获取pdf路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../..")), 'data', 'pdf')

    @classmethod
    def setUpClass(cls):
        super(test_ComplianceConfiguration, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.ComplianceConfigurationLg = ComplianceConfigurationLg(cls.driver)
        # cls.loginLogic.login(username=cls.__login_data['username'],
        #                      password=cls.__login_data['password'],
        #                      orgname=cls.__login_data['orgname'])
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.ComplianceConfigurationLg.into_complianceConfigurationLg_page()
    def setUp(self):
        super(test_ComplianceConfiguration, self).setUp()

    name1 = 'test_' + str(randint(100, 999))
    @data([{'projectName':'云来逸宅1+1+edit'}])
    @unpack
    def test_01_select_project(self, data):
        '''选择项目'''
        params = {
            'projectName':data['projectName'],
        }
        self.ComplianceConfigurationLg.select_project_lg(params)

    @data([{'projectName': 'lips3专属测试项目'}])
    @unpack
    def test_02_input_project(self, data):
        '''选择项目'''
        params = {
            'projectName': data['projectName'],
        }
        self.ComplianceConfigurationLg.input_project_lg(params)

    def test_03_contract_show(self):
        '''开启和关闭合同展示'''
        self.ComplianceConfigurationLg.contract_show_lg()

    # def test_04_implied_consent(self):
    #     '''开启和关闭默认同意'''
    #     self.ComplianceConfigurationLg.implied_consent_lg()


    @data([{'name': name1,'type':'全局','projectName':'首开四期4哥伦布','filePath':os.path.join(__image_path, '1.pdf')}])
    @unpack
    def test_05_increase_agreement(self, data):
        '''增加协议'''
        params = {
            'name': data['name'],
            'type':data['type'],
            'projectName':data['projectName'],
            'filePath':data['filePath']
        }
        self.ComplianceConfigurationLg.increase_agreement_lg(params)

    @data([{'name': name1, 'filePath': os.path.join(__image_path, '2.pdf')}]
          )
    @unpack
    def test_06_edit_agreement(self, data):
        '''编辑协议'''
        params = {
            'name': data['name'],
            #'type': data['type'],
            #'projectName': data['projectName'],
            'filePath': data['filePath']
        }
        self.ComplianceConfigurationLg.edit_agreement_lg(params)

    @data([{'name': name1}])
    @unpack
    def test_07_delete_agreement(self, data):
        '''删除协议'''
        params = {
            'name': data['name']
        }
        self.ComplianceConfigurationLg.delete_agreement_lg(params)

    def test_08_publishing_agreement(self):
        '''发布协议'''
        self.ComplianceConfigurationLg.publishing_agreement_lg()

    def tearDown(self):
        super(test_ComplianceConfiguration, self).tearDown()

if __name__ == '__main__':
    unittest.main()