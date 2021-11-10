#-*- encoding=utf-8 -*-

from myweb.core.BasePage import BasePage
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.areaSettingPO import areaSettingPO
from cases.AICardProject.logic.MenuManager import MenuManager


class areaSettingLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.areaSettingPO = areaSettingPO(driver)

    def into_areaSetting_page(self):
        '''打开系统设置-区域设置'''
        self.MenuManager.choiceMenu("系统设置","系统设置-区域设置")

    def add_area_01_lg(self,var):
        '''新增区域，不关联项目'''
        self.areaSettingPO.add_area_01(var['area_name'])

    def add_area_02_lg(self,var):
        '''新增区域，关联项目'''
        self.areaSettingPO.add_area_02(var['area_name'])

    def edit_area_lg(self,var):
        '''编辑区域'''
        self.areaSettingPO.edit_area(var['area_name'])

    def edit_area_delete_area_lg(self,var):
        '''编辑区域,删除辖区范围'''
        self.areaSettingPO.edit_area_delete_area(var['area_name'])

    def delete_area_lg(self,var):
        '''删除区域'''
        self.areaSettingPO.delete_area(var['area_name'])

    def open_location_matching_settings_lg(self,var):
        '''定位匹配设置-开启定位重定向'''
        self.areaSettingPO.open_location_matching_settings(var['name'])

    def close_location_matching_settings_lg(self,var):
        '''定位匹配设置-关闭定位重定向'''
        self.areaSettingPO.close_location_matching_settings(var['name'])

    def maintained_area_lg(self):
        '''打开已维护项目'''
        self.areaSettingPO.maintained_area()

    def unbound_project_lg(self):
        '''打开未绑定项目'''
        self.areaSettingPO.unbound_project()

    def page_switching_lg(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        self.areaSettingPO.click_next_page()
        self.areaSettingPO.click_previous_page()

    # def click_edit_lg(self,var):
    #     self.areaSettingPO.click_edit(var['checkData'])