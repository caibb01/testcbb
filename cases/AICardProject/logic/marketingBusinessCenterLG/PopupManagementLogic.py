# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
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
        """
        新增一个弹窗
        image_path              :图片地址
        start_and_end_time      :开始时间
        condition               :触发条件
        jump_page               :跳转页面
        control_page            :生效页面
        project_relation_name   :关联项目
        popup_name              :弹窗名称
        """
        self.popupManagementPage.insert_popup(params)

    def delete_popup(self, params):
        """
        删除弹窗管理
        popup_name：弹窗名
        """
        self.popupManagementPage.delete_popup(params)

    def editor_popup(self, params):
        """
        编辑弹窗管理
        start_and_end_time      :开始时间
        condition               :触发条件
        jump_page               :跳转页面
        control_page            :生效页面
        project_relation_name   :关联项目
        popup_name_old          :需要编辑的弹窗名称
        popup_name              :新的弹窗名
        image_path              :图片地址
        """
        self.popupManagementPage.editor_popup(params)
