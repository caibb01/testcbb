# -*- coding:utf-8 -*-

from myweb.core.runner import TestCase
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class miniProgramLive(BasePage,TestCase):
    control = {
        "小程序直播": (By.XPATH, '//span[text()="小程序直播"]'),
        "小程序直播断言":(By.XPATH,'//span[@class="ant-breadcrumb-link"]/a[text()="小程序直播"]'),
        "关闭小程序直播":(By.XPATH,'//button[@class="ant-switch ant-switch-checked"]'),
        "关闭小程序直播-文案（开）": (By.XPATH, '//button[@class="ant-switch ant-switch-checked"]/span'),
        "提示弹窗-确定":(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]'),
        "提示弹窗-取消": (By.XPATH, '//button[@class="ant-btn"]'),
        "开启小程序直播": (By.XPATH, '//button[@class="ant-switch"]'),
        "开启小程序直播-文案(关)": (By.XPATH, '//button[@class="ant-switch"]/span'),
        "小程序直播说明文档":(By.XPATH,'//div[@class="ant-col ant-col-10"]/a')
    }

    def __init__(self, driver):
        super(miniProgramLive, self).__init__(driver)

    def check_title(self,checkData):
        '''检查小程序直播页面的标题'''
        sleep(2)
        actualResult = self.find_element(self.control['小程序直播断言']).text
        self.assertIn(actualResult,checkData['expectData'],msg=checkData['msg'])

    def open_mini_Program_Live(self):
        '''开启小程序直播'''
        if self.is_exist_element(self.control['开启小程序直播']):
            self.find_element(self.control['开启小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()
        else:
            self.find_element(self.control['关闭小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()
            sleep(2)
            self.find_element(self.control['开启小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()


    def close_mini_Program_Live(self):
        '''关闭小程序直播'''
        if self.is_exist_element(self.control['关闭小程序直播']):
            self.find_element(self.control['关闭小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()
        else:
            self.find_element(self.control['开启小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()
            sleep(2)
            self.find_element(self.control['关闭小程序直播']).click()
            self.wait_eleVisible(self.control['提示弹窗-确定'])
            self.find_element(self.control['提示弹窗-确定']).click()

    def mini_Program_Live_documentation(self):
        '''打开小程序直播说明文档'''
        sleep(2)
        handle = self.driver.current_window_handle
        self.find_element(self.control['小程序直播说明文档']).click()
        sleep(2)
        self.driver.switch_to_window(handle)
        sleep(1)