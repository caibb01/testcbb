#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class MiniProgramJumpPO(BasePage):
    controls = {
        "新增": (By.XPATH, '//a[@ng-click="addMiniApp()"]'),
        "添加小程序-小程序名称": (By.XPATH, '//td[@i="body"]//input[@ng-model="fields.relation_mini_app_nick"]'),
        "添加小程序-小程序ID": (By.XPATH, '//td[@i="body"]//input[@ng-model="fields.relation_mini_app_id"]'),
        "添加小程序-确定": (By.XPATH, '//button[text()="确定"]'),
        "添加小程序-取消": (By.XPATH, '//button[text()="取消"]'),
        "添加小程序-右上角取消": (By.XPATH, '//button[@title="取消"]'),
        "添加小程序-关联小程序已存在": (By.XPATH, '//div[@class="loading-con"]'),
        "删除": (By.XPATH, '//a[@ng-click="deleteMiniApp(item)"]'),
        "删除-确定": (By.XPATH, '//button[@i-id="ok"]'),
        "删除-取消": (By.XPATH, '//button[@i-id="cancel"]'),
        "删除-右上角取消": (By.XPATH, '//button[@title="取消"]')
    }

    def delete_mini_program(self):
        """删除小程序"""
        sleep(2)
        num = len(self.find_elements_list(self.controls["删除-确定"]))
        self.find_elements(self.controls["删除"], num-1).click()
        sleep(2)
        self.find_element(self.controls["删除-确定"]).click()

    def add_mini_program(self, contentName, miniProgramId):
        """增加小程序"""
        sleep(2)
        self.find_element(self.controls["新增"]).click()
        sleep(2)
        self.find_element(self.controls["添加小程序-小程序名称"]).send_keys(contentName)
        self.find_element(self.controls["添加小程序-小程序ID"]).send_keys(miniProgramId)
        self.find_element(self.controls["添加小程序-确定"]).click()

        # # 如果添加的小程序已存在，关闭添加小程序输入框
        # if len(self.find_elements_list(self.controls["添加小程序-关联小程序已存在"])) != 0:
        #     sleep(2)
        #     self.find_element(self.controls["添加小程序-取消"]).click()

