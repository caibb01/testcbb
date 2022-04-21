#-*- encoding=utf8 -*-
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.contentManagementPO.miniProgramLivePO import miniProgramLive


class miniProgramLiveLg():
    def __init__(self,driver):
        #super(miniProgramLiveLg,self).__init__(driver)
        self.driver = driver
        self.miniProgramLivePO = miniProgramLive(driver)
        self.MenuManager = MenuManager(driver)

    def into_miniProgramLive_page(self):
        '''打开内容管理-小程序直播'''
        self.MenuManager.choiceMenu("内容管理", "内容管理-小程序直播")

    def check_title_lg(self,var):
        '''检查小程序直播页面的标题'''
        self.miniProgramLivePO.check_title(var['checkData'])

    def open_mini_Program_Live_lg(self):
        '''开启小程序直播'''
        self.miniProgramLivePO.open_mini_Program_Live()

    def close_mini_Program_Live_lg(self):
        '''关闭小程序直播'''
        self.miniProgramLivePO.close_mini_Program_Live()

    def mini_Program_Live_documentation_lg(self):
        '''打开小程序直播说明文档'''
        self.miniProgramLivePO.mini_Program_Live_documentation()