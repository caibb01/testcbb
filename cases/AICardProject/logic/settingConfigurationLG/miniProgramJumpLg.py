#-*- encoding=utf-8 -*-

from myweb.core.BasePage import BasePage
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.miniProgramJumpPO import MiniProgramJumpPO
from cases.AICardProject.logic.MenuManager import MenuManager


class miniProgramJumpLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.miniProgramJumpPO = MiniProgramJumpPO(driver)

    def into_miniProgramJump_page(self):
        '''打开系统设置-小程序跳转'''
        self.MenuManager.choiceMenu("系统设置", "系统设置-小程序跳转")

    def add_mini_program_lg(self,var):
        """新增小程序"""
        self.miniProgramJumpPO.add_mini_program(var['parameter'])
        self.miniProgramJumpPO.contrast_list_data(var['checkData'])

    def cancel_add_mini_program_lg(self,var):
        """新增小程序，取消保存"""
        self.miniProgramJumpPO.cancel_add_mini_program(var['parameter'])
        self.miniProgramJumpPO.contrast_list_data(var['checkData'])

    def delete_mini_program_lg(self,var):
        """删除小程序"""
        self.miniProgramJumpPO.delete_mini_program()
        self.miniProgramJumpPO.contrast_list_data(var['checkData'])