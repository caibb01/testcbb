#-*- coding:utf-8 -*-
from myweb.core.runner import TestCase
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class MiniProgramJumpPO(BasePage,TestCase):
    controls = {
        "小程序跳转": (By.XPATH, './/*[text()="小程序跳转"]'),

        "新增": (By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'),
        "添加小程序-小程序名称": (By.XPATH, '//div[@class="ant-row"]/div[@class="ant-col ant-col-20 right"]/input[@class="ant-input inp w-400"]'),
        "添加小程序-小程序ID": (By.XPATH, '//div[@class="ant-row mt10"]/div/input'),
        "添加小程序-保存": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[@class="ant-btn ant-btn-primary"]'),
        "添加小程序-取消": (By.XPATH, '//button[@class="ant-btn"]'),
        "添加小程序-关闭": (By.XPATH, '//span[@class="ant-modal-close-x"]'),
        #错误提示：关联小程序已经存在
        "添加小程序-关联小程序已存在": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        #列表
        "删除": (By.XPATH,'//button[@class="ant-btn fs-12 red ant-btn-link ant-btn-sm"]'),
        "删除-确定": (By.XPATH, '//button[@class="ant-btn ant-btn-danger"]'),
        "删除-取消": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "删除-右上角取消": (By.XPATH, '//button[@title="取消"]'),

        #断言
        #小程序自定义名称列表
        "小程序自定义名称列表":(By.XPATH,'//td[2]/div[@class="text-overflow w-200"]'),
        #小程序ID列表
        "小程序ID列表":(By.XPATH,'//td[3]/div[@class="text-overflow w-200"]')
    }

    def add_mini_program(self,parameter=None):
        """新增小程序，保存"""
        self.wait_eleVisible(self.controls["新增"])
        self.find_element(self.controls["新增"]).click()
        sleep(2)
        self.find_element(self.controls["添加小程序-小程序名称"]).click()
        self.find_element(self.controls["添加小程序-小程序名称"]).send_keys(parameter['contentName'])
        sleep(2)
        self.find_element(self.controls["添加小程序-小程序ID"]).click()
        self.find_element(self.controls["添加小程序-小程序ID"]).send_keys(parameter['miniProgramId'])
        self.find_element(self.controls["添加小程序-保存"]).click()
        if self.is_exist_element(self.controls["添加小程序-关联小程序已存在"]):
            self.find_element(self.controls["添加小程序-关联小程序已存在"]).click()
            sleep(2)
            self.find_element(self.controls["添加小程序-小程序ID"]).click()
            self.find_element(self.controls["添加小程序-小程序ID"]).send_keys(parameter['miniProgramId2'])
            self.find_element(self.controls["添加小程序-保存"]).click()

    def cancel_add_mini_program(self,parameter=None):
        """新增小程序，取消保存"""
        sleep(2)
        self.find_element(self.controls["新增"]).click()
        sleep(2)
        self.find_element(self.controls["添加小程序-小程序名称"]).click()
        self.find_element(self.controls["添加小程序-小程序名称"]).send_keys(parameter['contentName2'])
        sleep(2)
        self.find_element(self.controls["添加小程序-小程序ID"]).click()
        self.find_element(self.controls["添加小程序-小程序ID"]).send_keys(parameter['miniProgramId'])
        self.find_element(self.controls["添加小程序-取消"]).click()

    def delete_mini_program(self):
        """删除小程序"""
        sleep(2)
        num = len(self.find_elements_list(self.controls["删除"]))
        self.find_elements(self.controls["删除"], num-1).click()
        sleep(2)
        self.find_element(self.controls["删除-确定"]).click()

    def contrast_list_data(self,checkData):
        '''判断新增的值是否在列表'''
        flag = False
        typeBolle = True
        countNum = 0
        while(typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.controls["小程序自定义名称列表"])
            for b in bodyContent:
                if b.text == checkData['expectData']:
                    flag = True
                    break
                countNum += 1
            sleep(2)
            if countNum >= len(bodyContent):
                typeBolle = False
        self.check_assert(checkData['flag'],flag,checkData['msg'])
        return  flag

    #断言封装
    def check_assert(self,checkflag,flag,message):
        if checkflag == 'True' :
            self.assertTrue(flag,msg= message)
        else:
            self.assertFalse(flag,msg= message)