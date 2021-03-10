# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.basicInfoPO import BasicInfoPO
from cases.AICardProject.logic.MenuManager import MenuManager

class BasicInfoLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.menuManager = MenuManager(driver)
        self.basicInfoPO = BasicInfoPO(driver)

    def portrait_pic_upload(self):
        """企业形象图：上传图片、重新上传、删除图片"""
        self.menuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-基础信息")
        self.basicInfoPO.portrait_upload()
        self.basicInfoPO.portrait_reUpload()
        self.basicInfoPO.portrait_delete()

    def logo_pic_upload(self):
        """企业LOGO：上传图片、重新上传、删除图片"""
        self.menuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-基础信息")
        self.basicInfoPO.logo_upload()
        self.basicInfoPO.logo_reUpload()
        self.basicInfoPO.logo_delete()

    def bg_pic_upload(self):
        """授权背景图：上传图片、重新上传、删除图片"""
        self.menuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-基础信息")
        self.basicInfoPO.bgPic_upload()
        self.basicInfoPO.bgPic_reUpload()
        self.basicInfoPO.bgPic_delete()

    def all_pic_upload(self):
        """三个图片区域：上传图片、重新上传、删除图片"""
        self.menuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-基础信息")
        self.basicInfoPO.portrait_upload()
        self.basicInfoPO.portrait_reUpload()
        self.basicInfoPO.portrait_delete()

        self.basicInfoPO.logo_upload()
        self.basicInfoPO.logo_reUpload()
        self.basicInfoPO.logo_delete()

        self.basicInfoPO.bgPic_upload()
        self.basicInfoPO.bgPic_reUpload()
        self.basicInfoPO.bgPic_delete()


    def save_all_info(self):
        self.basicInfoPO.save_info()
