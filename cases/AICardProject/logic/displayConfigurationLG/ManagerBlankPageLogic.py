# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
import sys
from cases.AICardProject.page.LoginPage import LoginPage
from cases.AICardProject.page.displayConfigurationPO.ManagerBlankPagePage import ManagerBlankPagePage
from cases.AICardProject.logic.MenuManager import MenuManager
from time import sleep


class ManagerBlankPageLogic(BasePage):

    def __init__(self, driver):
        super(ManagerBlankPageLogic, self).__init__(driver)
        self.loginPage = LoginPage(driver)
        self.managerBlankPagePage = ManagerBlankPagePage(driver)
        self.menuManager = MenuManager(driver)

    def into_manageBlankPage_page(self):
        self.menuManager.choiceMenu("展示配置", "展示配置-新页面")

    def insert_blankPage(self, params):
        self.managerBlankPagePage.insert_blankPage(params)

    def delete_blankPage(self, params):
        self.managerBlankPagePage.delete_blankPage(params)

    def edit_blankPage(self, params):
        self.managerBlankPagePage.edit_blankPage(params)

    def into_blankPage_edit_page(self, page_name, relation_project, **kwargs):
        self.managerBlankPagePage.into_blankPage_edit_page(page_name, relation_project, **kwargs)
