#-*- encoding=utf8 -*-
import time
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.ComplianceConfigurationPO import ComplianceConfiguration


class ComplianceConfigurationLg():
    def __init__(self,driver):
        #super(ComplianceConfigurationLg,self).__init__(driver)
        self.driver=driver
        self.ComplianceConfigurationPO = ComplianceConfiguration(driver)
        self.MenuManager = MenuManager(driver)

    def into_complianceConfigurationLg_page(self):
        '''打开合规配置'''
        self.MenuManager.choiceMenu("合规配置")

    def select_project_lg(self, var):
        '''选择项目'''
        self.ComplianceConfigurationPO.select_project(var['projectName'])

    def input_project_lg(self,var):
        '''输入项目'''
        self.ComplianceConfigurationPO.input_project(var['projectName'])

    def contract_show_lg(self):
        '''开启和关闭合同展示'''
        self.ComplianceConfigurationPO.contract_show()

    def implied_consent_lg(self):
        '''开启和关闭默认同意'''
        self.ComplianceConfigurationPO.implied_consent()

    def increase_agreement_lg(self,var):
        '''增加协议'''
        self.ComplianceConfigurationPO.increase_agreement(var['name'],var['type'],var['projectName'],var['filePath'])

    def edit_agreement_lg(self,var):
        '''编辑协议'''
        self.ComplianceConfigurationPO.edit_agreement(var["name"],var["filePath"])

    def delete_agreement_lg(self,var):
        '''删除协议'''
        self.ComplianceConfigurationPO.delete_agreement(var["name"])

    def publishing_agreement_lg(self):
        '''发布协议'''
        self.ComplianceConfigurationPO.publishing_agreement()

    def add_authorized_protocol_lg(self, var):
        """增加授权协议"""
        self.ComplianceConfigurationPO.add_authorized_protocol(var['protocol_name'], var['filePath'])

    def edit_authorized_protocol_lg(self):
        """编辑授权协议"""
        self.ComplianceConfigurationPO.edit_authorized_protocol()

    def delete_authorized_protocol_lg(self, var):
        """删除授权协议"""
        self.ComplianceConfigurationPO.delete_authorized_protocol(var['protocol_name'])

    def publish_authorized_protocol_lg(self):
        """发布授权协议"""
        self.ComplianceConfigurationPO.publish_authorized_protocol()

