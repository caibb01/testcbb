# coding=utf-8
from cases.AICardProject.page.contentManagementPO.officialAccountsManagementPO import OfficialAccountsManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class OfficialAccountsManagementLg():
    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.officialAccountsContentPO = OfficialAccountsManagementPO(driver)

    def into_officialAccounts_page(self):
        # 打开内容管理-公众号文章
        self.MenuManager.choiceMenu("内容管理", "内容管理-公众号文章")
        sleep(3)

    def newOfficialAccounts(self, var):
        # 新增公众号文章
        self.officialAccountsContentPO.newOfficialAccounts(params=var)

    def updateOfficialAccounts(self, var):
        # 编辑公众号文章
        self.officialAccountsContentPO.updateOfficialAccounts(params=var)

    def delOfficialAccounts(self):
        # 删除公众号文章
        self.officialAccountsContentPO.delOfficialAccounts()

    def queryOfficialAccounts(self, var):
        # 搜索公众号文章
        self.officialAccountsContentPO.queryOfficialAccounts(proName=var)

    def page_turning(self):
        # 点击下一页
        self.officialAccountsContentPO.click_next()
        sleep(2)
        # 点击上一页
        self.officialAccountsContentPO.click_previous()
        sleep(2)
        # 点击跳页
        self.officialAccountsContentPO.jump_page()