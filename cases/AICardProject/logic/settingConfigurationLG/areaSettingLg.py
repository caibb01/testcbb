# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.areaSettingPO import AreaSettingPO
from cases.AICardProject.logic.MenuManager import MenuManager


class AreaSettingLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.areaSettingPO = AreaSettingPO(driver)

    def add_area(self):
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-区域设置")
        self.areaSettingPO.add_area()

    def edit_area(self):
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-区域设置")
        self.areaSettingPO.edit_area()

    def delete_area(self):
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-区域设置")
        self.areaSettingPO.delete_area()

    def operate_area(self):
        """新增区域-编辑区域-删除区域"""
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-区域设置")
        self.areaSettingPO.add_area()
        self.areaSettingPO.edit_area()
        self.areaSettingPO.delete_area()

    def location_pattern(self):
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-区域设置")
        self.areaSettingPO.location_matching_settings()