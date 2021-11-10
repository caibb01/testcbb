#-*- encoding=utf8 -*-
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.displayConfigurationPO.StartupPagePO import StartupPage


class StartupPageLg():
    def __init__(self,driver):
        #super(StartupPageLg,self).__init__(driver)
        self.driver=driver
        self.StartupPagePO = StartupPage(driver)
        self.MenuManager = MenuManager(driver)

    def into_StartupPage(self):
        '''打开展示配置-启动页'''
        self.MenuManager.choiceMenu("展示配置","展示配置-启动页")

    def upload_still_image_lg(self,var):
        '''启动页配置，上传静态图片，预览，保存，刷新页面'''
        self.StartupPagePO.upload_still_image(var['path'])

    def upload_dynamic_image_lg(self,var):
        '''启动页配置，上传动态图片，预览，保存，刷新页面'''
        self.StartupPagePO.upload_dynamic_image(var['path'])

    def upload_image_refresh_page_lg(self,var):
        '''启动页配置，上传图片，刷新'''
        self.StartupPagePO.upload_image_refresh_page(var['path'])

    def upload_images_larger_than_2M_lg(self,var):
        '''启动页配置，上传大于2M的图片'''
        self.StartupPagePO.upload_images_larger_than_2M(var['path'])

    # def upload_other_formats_lg(self,var):
    #     '''上传除jpg、jpeg、png和gif格式的图片'''
    #     self.StartupPagePO.upload_other_formats(var['path'])
    def select_image_fill_mode_lg(self):
        '''选择图片填充模式'''
        self.StartupPagePO.select_image_fill_mode()

    def open_startup_page_lg(self):
        '''开启启动页图片'''
        self.StartupPagePO.open_startup_page()

    def close_startup_page_lg(self):
        '''关闭启动页图片'''
        self.StartupPagePO.close_startup_page()


