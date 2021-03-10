# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from cases.AICardProject.page.LoginPage import LoginPage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.marketingBusinessCenterPO.PopupManagementPage import PopupManagementPage
from time import sleep


class PopupManagementLogic(BasePage):

    def __init__(self, driver):
        super(PopupManagementLogic, self).__init__(driver)
        self.loginPage = LoginPage(driver)
        self.popupManagementPage = PopupManagementPage(driver)
        self.menuManager = MenuManager(driver)

    def into_popupManagement_page(self):
        self.menuManager.choiceMenu("营销业务中心", "营销业务中心-弹窗管理")

    def insert_popup(self, params):
        self.popupManagementPage.insert_popup(params)

    def delete_popup(self, params):
        self.popupManagementPage.delete_popup(params)

    def editor_popup(self, params):
        self.popupManagementPage.editor_popup(params)



