# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.miniProgramJumpPO import MiniProgramJumpPO
from cases.AICardProject.logic.MenuManager import MenuManager


class miniProgramJumpLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.miniProgramJumpPO = MiniProgramJumpPO(driver)


    def add_program(self):
        '''
        添加小程序
        :return:
        '''
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-小程序跳转")
        self.miniProgramJumpPO.add_mini_program(contentName=u"添加小程序测试", miniProgramId='wxc02b67a84146b966')

    def delete_program(self):
        '''
        删除小程序
        :return:
        '''
        self.MenuManager.choiceMenu(firstLevelMenu="系统设置", SecondaryMenu="系统设置-小程序跳转")
        self.miniProgramJumpPO.delete_mini_program()

