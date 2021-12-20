#-*- coding:utf-8 -*-

from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from myweb.core.runner import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from myweb.core.BasePage import BasePage

class ComplianceConfiguration(BasePage,TestCase):
    control =  {
        "合规配置": (By.XPATH, './/*[text()="合规配置"]'),
        "关联项目":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "请选择项目":(By.XPATH,'//div/input[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "项目列表":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_1R0Lp  "]'),
        "合同展示":(By.XPATH,'//div[@class="ant-col ant-col-10"]/button'),
        "确认开启合同展示-确定":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "确认开启合同展示-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "请先开启合同展示-知道了":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "默认同意":(By.XPATH,'//div[@class="ant-col ant-col-10"]/button'),
        "确认开启默认同意-确定":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "确认开启默认同意-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "增加协议":(By.XPATH,'//div[@class="right"]/button[@class="ant-btn ant-btn-primary"]'),
        "协议名称":(By.XPATH,'//span[@class="ant-form-item-children"]/input'),
        "关联类型-全局":(By.XPATH,'//div[@class="ant-radio-group ant-radio-group-outline"]/label/span/input[@value="GLOBAL"]'),
        "关联类型-项目":(By.XPATH,'//div[@class="ant-radio-group ant-radio-group-outline"]/label/span/input[@value="PROJECT"]'),
        "关联项目-输入":(By.XPATH,'//div[@class="ant-select-selection__placeholder"]'),
        "关联项目-列表":(By.XPATH,'//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]/li'),
        "协议内容-上传":(By.XPATH,'//span[@class="ant-upload"]/button[@class="ant-btn ant-btn-primary"]'),
        "协议内容-删除鼠标":(By.XPATH,'//div[@class="ant-upload-list-item-info"]/span'),
        "协议内容-删除":(By.XPATH,'//span[@class="ant-upload-list-item-card-actions "]/a/i'),
        "新增协议-确定":(By.XPATH,'//div[@class="ant-modal-footer"]/div/button[@class="ant-btn ant-btn-primary"]'),
        "新增协议-取消":(By.XPATH,'//div[@class="ant-modal-footer"]/div/button[@class="ant-btn"]'),
        "新增协议-关闭":(By.XPATH,'//span[@class="ant-modal-close-x"]/i'),
        #列表
        "编辑":(By.XPATH,'//button[@class="ant-btn fs-12 blue ant-btn-link ant-btn-sm"]'),
        # 列表
        "删除":(By.XPATH,'//button[@class="ant-btn fs-12 light ant-btn-link ant-btn-sm"]'),
        "删除-确认":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "删除-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),

        "发布协议":(By.XPATH,'//div[@class="pages-protocol_setting-index-module_1-pVX"]/button'),
        "发布协议-确定":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "发布协议-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),

        "协议名称列表":(By.XPATH,'//tbody/tr/td[1]'),
        "blank":(By.XPATH,'//div[@class="ant-modal-body"]')
    }

    def __init__(self,driver):
        super(ComplianceConfiguration, self).__init__(driver)

    def select_project(self,projectName):
        '''选择项目'''
        self.wait_eleVisible(self.control["关联项目"])
        self.find_element(self.control["关联项目"]).click()
        self.find_element(self.control["请选择项目"]).click()
        i = -1
        # 用于判定是否查询到有我们的判定值
        numFlag = False
        elem = self.find_elements_list(self.control["项目列表"])
        for e in elem:
            i += 1
            if e.text == projectName:
                numFlag = True
                break
        if numFlag:
            self.wait_eleVisible(self.control["项目列表"])
            ele = self.find_elements(self.control["项目列表"], i)
            ele.click()
        else:
            self.wait_eleVisible(self.control["项目列表"])
            ele = self.find_elements(self.control["项目列表"], 0)
            ele.click()
        self.refresh()

    def input_project(self,projectName):
        '''输入项目'''
        sleep(2)
        self.wait_eleVisible(self.control["关联项目"])
        self.find_element(self.control["关联项目"]).click()
        self.find_element(self.control["请选择项目"]).click()
        sleep(2)
        self.find_element(self.control["请选择项目"]).send_keys(projectName)
        i = -1
        # 用于判定是否查询到有我们的判定值
        numFlag = False
        elem = self.find_elements_list(self.control["项目列表"])
        for e in elem:
            i += 1
            if fuzz.ratio(e.text,projectName) > 0:
                numFlag = True
                break
        if numFlag:
            self.wait_eleVisible(self.control["项目列表"])
            ele = self.find_elements(self.control["项目列表"], i)
            ele.click()
        else:
            self.refresh()
        sleep(2)
        self.refresh()
        sleep(2)

    def contract_show(self):
        '''开启和关闭合同展示'''
        sleep(2)
        self.wait_eleVisible(self.control['合同展示'])
        self.find_elements(self.control["合同展示"],0).click()
        self.find_element(self.control["确认开启合同展示-确定"]).click()

    def implied_consent(self):
        '''开启和关闭默认同意'''
        self.wait_eleVisible(self.control['默认同意'])
        self.find_elements(self.control["默认同意"],1).click()
        if self.is_exist_element(self.control["请先开启合同展示-知道了"]):
            self.find_element(self.control["请先开启合同展示-知道了"]).click()
            self.find_element(self.control["合同展示"]).click()
            self.find_element(self.control["确认开启合同展示-确定"]).click()
            self.find_element(self.control["默认同意"]).click()
            self.find_element(self.control["确认开启默认同意-确定"]).click()
        else:
            self.find_element(self.control["确认开启默认同意-确定"]).click()

    def increase_agreement(self,name,type,projectName,filePath):
        '''增加协议'''
        self.refresh()
        self.find_element(self.control["增加协议"]).click()
        sleep(2)
        self.find_element(self.control["协议名称"]).click()
        self.find_element(self.control["协议名称"]).send_keys(name)
        #选择管理类型：全局/项目
        if type == "全局":
            self.find_element(self.control["关联类型-全局"]).click()
        else:
            self.find_element(self.control["关联类型-项目"]).click()
            sleep(2)
            self.find_element(self.control["关联项目-输入"]).click()
            sleep(2)
            self.find_element(self.control["关联项目-输入"]).text == projectName
            sleep(2)
            i = -1
            # 用于判定是否查询到有我们的判定值
            numFlag = False
            elem = self.find_elements_list(self.control["关联项目-列表"])
            for e in elem:
                i += 1
                if e.text == projectName:
                    numFlag = True
                    break
            if numFlag:
                self.wait_eleVisible(self.control["关联项目-列表"])
                ele = self.find_elements(self.control["关联项目-列表"], i)
                ele.click()
                self.find_element(self.control["blank"]).click()
            else:
                self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
                sleep(2)
                self.switch_to_active_element().send_keys(Keys.ENTER)
                sleep(2)
                self.find_element(self.control["blank"]).click()
        #上传文件
        self.find_element(self.control["协议内容-上传"]).click()
        sleep(2)
        self.upload(filePath)
        sleep(2)
        self.find_element(self.control["新增协议-确定"]).click()
        sleep(2)

    def edit_agreement(self,name,filePath):
        '''编辑协议'''
        self.refresh()
        typeBolle = True
        countNum = 0
        while(typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.control["协议名称列表"])
            for b in bodyContent:
                if b.text == name:
                    print("909090:",b.text,"===",name)
                    flag = True
                    typeBolle = False
                    break
                countNum += 1
        self.wait_eleVisible(self.control['编辑'])
        self.find_elements(self.control['编辑'], countNum).click()
        #删除协议
        sleep(2)
        self.move_mouse_to_element(self.control['协议内容-删除鼠标'])
        self.wait_eleVisible(self.control['协议内容-删除'])
        self.find_element(self.control['协议内容-删除']).click()
        #重新上传协议
        self.wait_eleVisible(self.control['协议内容-上传'])
        self.find_element(self.control["协议内容-上传"]).click()
        sleep(2)
        self.upload(filePath)
        sleep(2)
        self.find_element(self.control["新增协议-确定"]).click()
        sleep(2)


    def delete_agreement(self,name):
        '''删除协议'''
        self.refresh()
        typeBolle = True
        flag = False
        countNum = 0
        sleep(2)
        while (typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.control["协议名称列表"])
            for b in bodyContent:
                if b.text == name:
                    typeBolle = False
                    flag = True
                    break
                countNum += 1
            if countNum == len(bodyContent):
                typeBolle = False
        if flag:
            self.wait_eleVisible(self.control['删除'])
            self.find_elements(self.control['删除'], countNum).click()
            sleep(2)
            if self.is_exist_element(self.control["删除-确认"]):
                self.find_element(self.control["删除-确认"]).click()
        sleep(2)

    def publishing_agreement(self):
        '''发布协议'''
        self.find_element(self.control["发布协议"]).click()
        self.find_element(self.control["发布协议-确定"]).click()

















