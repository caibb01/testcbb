# -*- coding:utf-8 -*-
import unittest
from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class StartupPage(BasePage):
    controls = {
        "启动页": (By.XPATH, './/*[text()="启动页"]'),
        "上传图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/span/div/span/div/div/i'),
        "确定":(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]'),
        "取消":(By.XPATH,'//button[@class="ant-btn"]'),
        "重新上传图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/span/div/span/div/div/div[2]/i[1]'),
        "删除图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/span/div/span/div/div/div[2]/i[2]'),
        #图片填充模式列表：裁剪填充/拉伸填充/完全展示
        "图片填充模式":(By.XPATH,'//input[@class="ant-radio-input"]'),
        "关":(By.XPATH,'//span[contains(text(), "关")]/parent::button'),
        "开启启动页图片":(By.XPATH,'//button[@class="ant-switch"]'),
        "开": (By.XPATH, '//span[contains(text(), "开")]/parent::button'),
        "关闭启动页图片":(By.XPATH,'//button[@class="ant-switch ant-switch-checked"]'),
        "保存":(By.XPATH,'//span[contains(text(), "保 存")]/parent::button'),
        "知道了": (By.XPATH, '//span[contains(text(), "知道了")]/parent::button')
    }

    def __init__(self, driver):
        super(StartupPage, self).__init__(driver)

    def upload_still_image(self,path):
        '''启动页配置，上传静态图片，预览，保存，刷新页面'''
        sleep(2)
        if self.is_exist_element(self.controls["上传图片"]):
            self.find_element(self.controls["上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        elif self.is_exist_element(self.controls["重新上传图片"]):
            self.find_element(self.controls["重新上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        if self.is_exist_element(self.controls["保存"]):
           self.find_element(self.controls["保存"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["知道了"]):
            self.find_element(self.controls["知道了"]).click()
        sleep(3)
        self.refresh()
        sleep(2)

    def upload_dynamic_image(self,path):
        '''启动页配置，上传动态图片，预览，保存，刷新页面'''
        sleep(2)
        if self.is_exist_element(self.controls["上传图片"]):
            self.find_element(self.controls["上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        elif self.is_exist_element(self.controls["删除图片"]):
            self.find_element(self.controls["删除图片"]).click()
            if self.is_exist_element(self.controls["上传图片"]):
                self.find_element(self.controls["上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        if self.is_exist_element(self.controls["保存"]):
           self.find_element(self.controls["保存"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["知道了"]):
            self.find_element(self.controls["知道了"]).click()
        sleep(3)
        self.refresh()
        sleep(2)

    def upload_image_refresh_page(self,path):
        '''启动页配置，上传图片，刷新'''
        sleep(2)
        if self.is_exist_element(self.controls["上传图片"]):
            self.find_element(self.controls["上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        elif self.is_exist_element(self.controls["重新上传图片"]):
            self.find_element(self.controls["重新上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["知道了"]):
            self.find_element(self.controls["知道了"]).click()
        sleep(3)
        self.refresh()
        sleep(2)

    def upload_images_larger_than_2M(self,path):
        '''启动页配置，上传大于2M的图片'''
        sleep(2)
        if self.is_exist_element(self.controls["上传图片"]):
            self.find_element(self.controls["上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
        elif self.is_exist_element(self.controls["重新上传图片"]):
            self.find_element(self.controls["重新上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["确定"]).click()
        sleep(3)
        if self.is_exist_element(self.controls["知道了"]):
            self.find_element(self.controls["知道了"]).click()

    # def upload_other_formats(self,path):
    #     '''上传除jpg、jpeg、png和gif格式的图片'''
    #     if self.is_exist_element(self.controls["上传图片"]):
    #         self.find_element(self.controls["上传图片"]).click()
    #         sleep(2)
    #         self.upload(path)
    #         sleep(2)
    #         self.find_element(self.controls["确定"]).click()
    #         sleep(2)
    #     elif self.is_exist_element(self.controls["重新上传图片"]):
    #         self.find_element(self.controls["重新上传图片"]).click()
    #         sleep(2)
    #         self.upload(path)
    #         sleep(2)
    #         self.find_element(self.controls["确定"]).click()
    #     sleep(3)
    #     if self.is_exist_element(self.controls["知道了"]):
    #         self.find_element(self.controls["知道了"]).click()

    def select_image_fill_mode(self):
        '''选择图片填充模式'''
        sleep(2)
        mode = self.find_elements_list(self.controls["图片填充模式"])
        for i in range(len(mode)):
            sleep(2)
            mode[i].click()
        if self.is_exist_element(self.controls["保存"]):
           self.find_element(self.controls["保存"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["知道了"]):
            self.find_element(self.controls["知道了"]).click()
        sleep(2)

    def open_startup_page(self):
        '''开启启动页图片'''
        sleep(2)
        if self.find_element(self.controls["关"]).text == "关":
            self.find_element(self.controls["开启启动页图片"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["保存"]):
               self.find_element(self.controls["保存"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["知道了"]):
                self.find_element(self.controls["知道了"]).click()
            sleep(2)
        else:
            self.find_element(self.controls["关闭启动页图片"]).click()
            sleep(2)
            self.find_element(self.controls["开启启动页图片"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["保存"]):
                self.find_element(self.controls["保存"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["知道了"]):
                self.find_element(self.controls["知道了"]).click()
            sleep(2)

    def close_startup_page(self):
        '''关闭启动页图片'''
        sleep(2)
        if self.find_element(self.controls["开"]).text == "开":
            self.find_element(self.controls["关闭启动页图片"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["保存"]):
                self.find_element(self.controls["保存"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["知道了"]):
                self.find_element(self.controls["知道了"]).click()
            sleep(2)
        else:
            self.find_element(self.controls["开启启动页图片"]).click()
            sleep(2)
            self.find_element(self.controls["关闭启动页图片"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["保存"]):
                self.find_element(self.controls["保存"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["知道了"]):
                self.find_element(self.controls["知道了"]).click()
            sleep(2)



