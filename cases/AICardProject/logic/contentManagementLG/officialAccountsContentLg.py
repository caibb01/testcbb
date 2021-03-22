#coding:utf-8
# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
import sys
from cases.AICardProject.page.contentManagementPO.officialAccountsContentPO import officialAccountsContentPO
from time import sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class officialAccountsContentLg(BasePage):
    def __init__(self, driver):
        # super(articleContentPO, self).__init__(driver)
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.officialAccountsContentPO = officialAccountsContentPO(driver)

    def officialAccounts(self):
        self.MenuManager.choiceMenu(firstLevelMenu="内容管理", SecondaryMenu="内容管理-公众号文章")
        self.officialAccountsContentPO.newOfficialAccounts(title="公众号自动化测试",content="公众号文章自动化测试内容",
                                                           urlPath="111",proName="哥伦布多项目3")
        self.officialAccountsContentPO.queryOfficialAccounts(proName=u"哥伦布多项目3")
        self.officialAccountsContentPO.updateOfficialAccounts(title=u"公众号文章自动化测试",contentu=u"公众号文章自动化测试内容",
                                                           urlPath=u"111",proName=u"哥伦布多项目3",regionType=u"深圳")
        self.officialAccountsContentPO.queryOfficialAccounts(proName=u"哥伦布多项目3")
        self.officialAccountsContentPO.delOfficialAccounts()
