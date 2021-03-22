# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
import sys
from cases.AICardProject.page.contentManagementPO.articleContentPO import articleContent
from time import sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class articleContentLg(BasePage):
    def __init__(self, driver):
        super(articleContentLg, self).__init__(driver)
        self.driver = driver
        self.articleContentPO = articleContent(driver)
        self.MenuManager = MenuManager(driver)

    def newContent(self):
        '''
        新增文章，编辑文章，发布文章，编辑文章，关闭文章
        :return:
        '''
        self.MenuManager.choiceMenu(firstLevelMenu="内容管理", SecondaryMenu="内容管理-原创文章")
        # self.articleContentPO.select_Menu()
        self.articleContentPO.operation_new_Function(titleName=u'云店自动化测试', content=u'文章内容')
        self.articleContentPO.operation_query_Function(u'云店自动化测试')
        self.articleContentPO.operation_update_Function(u'test_update云店自动化测试', u'test_update云店自动化测试内容文章')
        self.articleContentPO.operation_query_Function(u'test_update云店自动化测试')
        self.articleContentPO.operation_state_Function()
        self.articleContentPO.operation_query_Function(u'test_update云店自动化测试')
        self.articleContentPO.operation_update_Function(u'test_up_s云店自动化测试1', u'test_up_s云店自动化测试内容文章')
        self.articleContentPO.operation_query_Function(u'test_up_s云店自动化测试1')
        self.articleContentPO.operation_state_Function()




