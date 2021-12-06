#-*- encoding=utf8 -*-
from time import sleep

import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.page.userManagementPO.customersManagementPO import customersManagement
from cases.AICardProject.logic.MenuManager import MenuManager


class customersManagementLg():
    def __init__(self,driver):
        #super(customersManagementLg,self).__init__(driver)
        self.driver=driver
        self.customersManagementPO = customersManagement(driver)
        self.MenuManager = MenuManager(driver)

    def into_customersManagement_page(self):
        '''打开用户管理-客群管理'''
        self.MenuManager.choiceMenu("用户管理","用户管理-客群管理")

    def check_title_lg(self,var):
        '''检查客群管理页面的标题'''
        self.customersManagementPO.check_title(var['checkData'])