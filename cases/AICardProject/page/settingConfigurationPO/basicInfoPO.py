#-*- coding:utf-8 -*-

from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from myweb.core.runner import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from myweb.core.BasePage import BasePage

class BasicInfoPO(BasePage):
    controls = {
        "基础信息": (By.XPATH,'.//*[text()="基础信息"]'),
        "小程序简称":(By.XPATH,'//div[@class="ant-row ant-form-item"]/div[@class="ant-col ant-col-12 ant-form-item-control-wrapper"]/div/span/input'),

        "企业形象图-上传图片": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/span/div/span/div/span/div/div/i'),
        "企业形象图-重新上传": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "企业形象图-删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[2]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "企业LOGO-上传图片": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[3]/div[2]/div/span/div/span/div/span/div/div/i'),
        "企业LOGO-重新上传": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[3]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "企业LOGO-删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[3]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "授权背景图-上传图片": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[4]/div[2]/div/span/div/span/div/span/div/div/i'),
        "授权背景图-上传图片2": (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[4]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "授权背景图-重新上传": (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[4]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "授权背景图-删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[4]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "朋友圈海报-上传图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[5]/div[2]/div/span/div/span/div/span/div/div/i'),
        "朋友圈海报-重新上传":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[5]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "朋友圈海报-删除":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[5]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "工作台图标-开或关":(By.XPATH,'//*[@id="allow_workspace_icon"]/span'),
        "工作台图标-上传图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[7]/div[2]/div/span/div/span/div/span/div/div/i'),
        "工作台图标-重新上传":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[7]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "工作台图标-删除":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[7]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "地图标记图标-上传图片":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[8]/div[2]/div/span/div/span/div/span/div/div/i'),
        "地图标记图标-重新上传":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[8]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[1]'),
        "地图标记图标-删除":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/form/div[8]/div[2]/div/span/div/span/div/span/div/div/div[2]/i[2]'),

        "裁剪框-确定": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[@class="ant-btn ant-btn-primary"]'),
        "裁剪框-取消": (By.XPATH, '//button[@class="ant-btn"]'),
        "裁剪框-关闭": (By.XPATH, '//span[@class="ant-modal-close-x"]/i'),

        "智能客服-开或关":(By.XPATH,'//*[@id="enable_customer_service"]/span'),
        #列表
        "机器人-添加":(By.XPATH,'//div[@class="ant-row-flex ant-row-flex-middle"]/div[5]/span[1]/i'),
        "机器人名字":(By.XPATH,'//input[@placeholder="请填写机器人名字"  and @value=""]'),
        "机器人ID":(By.XPATH,'//input[@placeholder="请填写机器人ID"  and @value=""]'),
        #列表
        "机器人-删除": (By.XPATH, '//div[@class="ant-row-flex ant-row-flex-middle"]/div[5]/span[2]/i'),
        "机器人-确认删除":(By.XPATH,'//div[@class="ant-popover-buttons"]/button[@class="ant-btn ant-btn-primary ant-btn-sm"]'),
        #列表
        "机器人配置":(By.XPATH,'//div[@class="ant-col"]/button'),
        #列表
        "快捷提问-添加":(By.XPATH,'//div[@class="ant-col ant-col-4"]/span[@class="components-common-plusAndMinus-index-module_1I6Kf"][1]/i'),
        "快捷提问-输入":(By.XPATH,'//div[@class="ant-col ant-col-15"]/input[@class="ant-input"]'),
        "快捷提问-删除": (By.XPATH,'//div[@class="ant-col ant-col-4"]/span[@class="components-common-plusAndMinus-index-module_1I6Kf"][2]/i'),
        "快捷提问-保存":(By.XPATH,'//div[@class="ant-modal-footer"]/div/button[@class="ant-btn ant-btn-primary"]'),
        "快捷提问-取消":(By.XPATH,'//button[@class="ant-btn"]'),
        "快捷提问-关闭":(By.XPATH,'//span[@class="ant-modal-close-x"]/i'),

        "浏览人次名称自定义-开或关":(By.XPATH,'//*[@id="enable_wanna_buy_text"]/span'),
        "浏览人次自定义":(By.XPATH,'//div/div[@class="ant-col ant-col-11 ant-form-item-control-wrapper"]/div/span/input'),
        "浏览人次自定义-输入框置灰":(By.XPATH,'//div/div[@class="ant-col ant-col-11 ant-form-item-control-wrapper"]/div/span/input[@disabled]'),

        "留电通知-开或关":(By.XPATH,'//*[@id="allow_sms_notification"]/span'),
        "最少配置一个通知对象":(By.XPATH,'//div[@class="ant-form-explain"]'),
        "置业顾问":(By.XPATH,'//*[@id="allow_sms_seller_types"]/label[1]/span[1]/input'),
        "行销人员":(By.XPATH,'//*[@id="allow_sms_seller_types"]/label[2]/span[1]/input'),
        "全民经纪人":(By.XPATH,'//*[@id="allow_sms_seller_types"]/label[3]/span[1]/input'),

        "其他设置-允许查看服务轨迹":(By.XPATH,'//*[@id="allow_view_track"]'),
        "其他设置-云会员":(By.XPATH,'//*[@id="enable_vip"]'),
        "保存": (By.XPATH, '//div/button[@class="ant-btn ant-btn-primary"]'),
        "取消":(By.XPATH,'//div/button[@class="ant-btn ml10"]'),
        #服务器繁忙中，请稍后再试！
        "错误提示-知道了":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]')

    }

    def short_for_mini_program(self,name):
        '''小程序简称'''
        self.wait_eleVisible(self.controls["小程序简称"])
        self.find_element(self.controls["小程序简称"]).click()
        self.find_element(self.controls["小程序简称"]).send_keys(Keys.CONTROL, 'a')
        self.find_element(self.controls["小程序简称"]).send_keys("")
        sleep(2)
        self.find_element(self.controls["小程序简称"]).send_keys(name)
        sleep(2)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def corporate_image_chart(self,path):
        '''企业形象图的上传图片、重新上传、删除'''
        sleep(2)
        if self.is_exist_element(self.controls["企业形象图-上传图片"]):
            self.find_element(self.controls["企业形象图-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        else:
            # if self.is_exist_element(self.controls["企业形象图-删除"]):
            self.find_element(self.controls["企业形象图-删除"]).click()
            sleep(2)
            self.find_element(self.controls["企业形象图-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def corporate_logo(self,path):
        '''企业LOGO的上传图片、重新上传、删除'''
        sleep(2)
        if self.is_exist_element(self.controls["企业LOGO-上传图片"]):
            self.find_element(self.controls["企业LOGO-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        else:
        # if self.is_exist_element(self.controls["企业LOGO-删除"]):
            self.find_element(self.controls["企业LOGO-删除"]).click()
            sleep(2)
            self.find_element(self.controls["企业LOGO-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def authorization_background_image(self,path):
        '''授权背景图的上传图片、重新上传、删除'''
        sleep(2)
        if self.is_exist_element(self.controls["授权背景图-上传图片"]):
            self.find_element(self.controls["授权背景图-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        elif self.is_exist_element(self.controls["授权背景图-删除"]):
            self.find_element(self.controls["授权背景图-删除"]).click()
            sleep(2)
            self.find_element(self.controls["授权背景图-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        else:
            if self.is_exist_element(self.controls["授权背景图-上传图片2"]):
                self.find_element(self.controls["授权背景图-上传图片"]).click()
                sleep(2)
                self.upload(path)
                sleep(2)
                self.find_element(self.controls["裁剪框-确定"]).click()
                sleep(2)

        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def poster_on_moments(self,path):
        '''朋友圈海报（安卓）的上传图片、重新上传、删除'''
        sleep(2)
        if self.is_exist_element(self.controls["朋友圈海报-上传图片"]):
            self.find_element(self.controls["朋友圈海报-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            # self.find_element(self.controls["裁剪框-确定"]).click()
            # sleep(3)
        else:
        # if self.is_exist_element(self.controls["朋友圈海报（安卓）-删除"]):
            self.find_element(self.controls["朋友圈海报-删除"]).click()
            sleep(2)
            self.find_element(self.controls["朋友圈海报-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(3)
            # self.find_element(self.controls["裁剪框-确定"]).click()
            # sleep(3)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def workbench_icon(self,path):
        '''工作台图标，开或关，上传图片、重新上传、删除'''
        self.find_element(self.controls["工作台图标-开或关"]).click()
        if self.find_element(self.controls["工作台图标-开或关"]).text == "关":
            sleep(2)
            self.find_element(self.controls["工作台图标-开或关"]).click()
            if self.is_exist_element(self.controls["工作台图标-上传图片"]):
                self.find_element(self.controls["工作台图标-上传图片"]).click()
                sleep(2)
                self.upload(path)
                sleep(2)
                self.find_element(self.controls["裁剪框-确定"]).click()
                sleep(2)
            else:
            # if self.is_exist_element(self.controls["工作台图标-删除"]):
                self.find_element(self.controls["工作台图标-删除"]).click()
                sleep(2)
                self.find_element(self.controls["工作台图标-上传图片"]).click()
                sleep(2)
                self.upload(path)
                sleep(2)
                self.find_element(self.controls["裁剪框-确定"]).click()
                sleep(2)
        else:
            sleep(2)
            if self.is_exist_element(self.controls["工作台图标-上传图片"]):
                self.find_element(self.controls["工作台图标-上传图片"]).click()
                sleep(2)
                self.upload(path)
                sleep(2)
                self.find_element(self.controls["裁剪框-确定"]).click()
                sleep(2)
            else:
            # if self.is_exist_element(self.controls["工作台图标-删除"]):
                self.find_element(self.controls["工作台图标-删除"]).click()
                sleep(2)
                self.find_element(self.controls["工作台图标-上传图片"]).click()
                sleep(2)
                self.upload(path)
                sleep(2)
                self.find_element(self.controls["裁剪框-确定"]).click()
                sleep(2)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def map_marker_icon(self,path):
        '''地图标记图标的上传图片、重新上传、删除'''
        sleep(2)
        if self.is_exist_element(self.controls["地图标记图标-上传图片"]):
            self.find_element(self.controls["地图标记图标-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        else:
        # if self.is_exist_element(self.controls["地图标记图标-删除"]):
            self.find_element(self.controls["地图标记图标-删除"]).click()
            sleep(2)
            self.find_element(self.controls["地图标记图标-上传图片"]).click()
            sleep(2)
            self.upload(path)
            sleep(2)
            self.find_element(self.controls["裁剪框-确定"]).click()
            sleep(2)
        # self.find_element(self.controls["保存"]).click()
        # sleep(2)

    def intelligent_customer_service(self,parmeter):
        '''智能客服：开启或关闭,添加机器人'''
        sleep(2)
        self.find_element(self.controls["智能客服-开或关"]).click()
        if self.find_element(self.controls["智能客服-开或关"]).text == "关闭":
            self.find_element(self.controls["智能客服-开或关"]).click()
            sleep(2)
            # 添加机器人
            self.find_elements(self.controls["机器人-添加"], 0).click()
            self.wait_eleVisible(self.controls["机器人名字"])
            self.find_element(self.controls["机器人名字"]).click()
            self.find_element(self.controls["机器人名字"]).send_keys(parmeter['name'])
            sleep(2)
            self.wait_eleVisible(self.controls["机器人ID"])
            self.find_element(self.controls["机器人ID"]).click()
            self.find_element(self.controls["机器人ID"]).send_keys(parmeter['id'])
        else:
            # 添加机器人
            self.find_elements(self.controls["机器人-添加"],0).click()
            self.wait_eleVisible(self.controls["机器人名字"])
            self.find_element(self.controls["机器人名字"]).click()
            self.find_element(self.controls["机器人名字"]).send_keys(parmeter['name'])
            sleep(2)
            self.wait_eleVisible(self.controls["机器人ID"])
            self.find_element(self.controls["机器人ID"]).click()
            self.find_element(self.controls["机器人ID"]).send_keys(parmeter['id'])
        sleep(2)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def intelligent_customer_service_configuration(self,question):
        '''智能客服-机器人配置快捷提问,保存'''
        sleep(2)
        if self.find_element(self.controls["智能客服-开或关"]).text == "关闭":
            self.find_element(self.controls["智能客服-开或关"]).click()
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人配置"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人配置"],nums-1).click()
            sleep(2)
            elem = self.find_elements_list(self.controls['快捷提问-输入'])
            nums = int(len(elem))
            print(nums)
            if nums > 2:
                self.find_elements(self.controls["快捷提问-添加"], 0).click()
                self.find_elements(self.controls['快捷提问-输入'],1).click()
                self.find_element(self.controls['快捷提问-输入',1]).send_keys(question)
            else:
                self.find_element(self.controls['快捷提问-输入']).click()
                self.find_element(self.controls['快捷提问-输入']).send_keys(question)
            sleep(2)
            self.find_element(self.controls["快捷提问-保存"]).click()
        else:
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人配置"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人配置"], nums - 1).click()
            sleep(2)
            elem = self.find_elements_list(self.controls['快捷提问-输入'])
            nums = int(len(elem))
            print(nums)
            if nums > 2:
                self.find_elements(self.controls["快捷提问-添加"], 0).click()
                self.find_elements(self.controls['快捷提问-输入'], 1).click()
                self.find_element(self.controls['快捷提问-输入', 1]).send_keys(question)
            else:
                self.find_element(self.controls['快捷提问-输入']).click()
                self.find_element(self.controls['快捷提问-输入']).send_keys(question)
            sleep(2)
            self.find_element(self.controls["快捷提问-保存"]).click()
        sleep(2)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def cancel_intelligent_customer_service_configuration(self,question):
        '''智能客服-机器人配置快捷提问，取消保存'''
        sleep(2)
        if self.find_element(self.controls["智能客服-开或关"]).text == "关闭":
            self.find_element(self.controls["智能客服-开或关"]).click()
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人配置"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人配置"],nums-1).click()
            sleep(2)
            elem = self.find_elements_list(self.controls['快捷提问-输入'])
            nums = int(len(elem))
            print(nums)
            if nums > 2:
                self.find_elements(self.controls["快捷提问-添加"], 0).click()
                self.find_elements(self.controls['快捷提问-输入'],1).click()
                self.find_element(self.controls['快捷提问-输入',1]).send_keys(question)
            else:
                self.find_element(self.controls['快捷提问-输入']).click()
                self.find_element(self.controls['快捷提问-输入']).send_keys(question)
            sleep(2)
            self.find_element(self.controls["快捷提问-取消"]).click()
        else:
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人配置"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人配置"], nums - 1).click()
            sleep(2)
            elem = self.find_elements_list(self.controls['快捷提问-输入'])
            nums = int(len(elem))
            print(nums)
            if nums > 2:
                self.find_elements(self.controls["快捷提问-添加"], 0).click()
                self.find_elements(self.controls['快捷提问-输入'], 1).click()
                self.find_element(self.controls['快捷提问-输入', 1]).send_keys(question)
            else:
                self.find_element(self.controls['快捷提问-输入']).click()
                self.find_element(self.controls['快捷提问-输入']).send_keys(question)
            sleep(2)
            self.find_element(self.controls["快捷提问-取消"]).click()
        sleep(2)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def delete_robot(self):
        '''智能客服：删除机器人'''
        if self.find_element(self.controls["智能客服-开或关"]).text == "关闭":
            self.find_element(self.controls["智能客服-开或关"]).click()
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人-删除"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人-删除"], nums - 1).click()
            sleep(2)
            self.find_element(self.controls["机器人-确认删除"]).click()
            sleep(2)
            self.find_element(self.controls["保存"]).click()
            sleep(2)
        else:
            sleep(2)
            elem = self.find_elements_list(self.controls["机器人-删除"])
            nums = int(len(elem))
            self.find_elements(self.controls["机器人-删除"], nums - 1).click()
            sleep(2)
            self.find_element(self.controls["机器人-确认删除"]).click()
            sleep(2)
            self.find_element(self.controls["保存"]).click()
            sleep(2)

    def number_of_visits(self,name):
        '''浏览人次名称自定义:开或关，自定义名称'''
        sleep(2)
        self.find_element(self.controls["浏览人次名称自定义-开或关"]).click()
        sleep(2)
        if self.find_element(self.controls["浏览人次名称自定义-开或关"]).text == "关":
            self.find_element(self.controls["浏览人次名称自定义-开或关"]).click()
            self.find_element(self.controls["浏览人次自定义"]).click()
            self.find_element(self.controls["浏览人次自定义"]).send_keys(Keys.CONTROL, 'a')
            self.find_element(self.controls["浏览人次自定义"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["浏览人次自定义"]).send_keys(name)
        else:
            self.find_element(self.controls["浏览人次自定义"]).click()
            self.find_element(self.controls["浏览人次自定义"]).send_keys(Keys.CONTROL, 'a')
            self.find_element(self.controls["浏览人次自定义"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["浏览人次自定义"]).send_keys(name)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def leave_advice(self):
        '''留电通知开或关，勾选置业顾问、行销人员、全民经纪人'''
        sleep(2)
        self.find_element(self.controls["留电通知-开或关"]).click()
        if self.find_element(self.controls["留电通知-开或关"]).text == "关":
            self.find_element(self.controls["留电通知-开或关"]).click()
            self.find_element(self.controls["置业顾问"]).click()
            self.find_element(self.controls["行销人员"]).click()
            self.find_element(self.controls["全民经纪人"]).click()
        else:
            self.find_element(self.controls["置业顾问"]).click()
            self.find_element(self.controls["行销人员"]).click()
            self.find_element(self.controls["全民经纪人"]).click()
            sleep(2)
        if self.is_exist_element(self.controls["最少配置一个通知对象"]):
            self.find_element(self.controls["置业顾问"]).click()
            self.find_element(self.controls["行销人员"]).click()
            self.find_element(self.controls["全民经纪人"]).click()
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def other_settings_01(self):
        '''其他设置，勾选允许查看服务轨迹'''
        sleep(2)
        self.find_element(self.controls["其他设置-允许查看服务轨迹"]).click()

    def other_settings_02(self):
        '''其他设置，勾选允许云会员'''
        sleep(2)
        self.find_element(self.controls["其他设置-云会员"]).click()

    def save(self):
        '''保存'''
        sleep(2)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def cancel_save(self):
        '''取消保存'''
        sleep(2)
        self.find_element(self.controls["取消"]).click()

    def error(self):
        if self.is_exist_element(self.controls["错误提示-知道了"]):
           self.find_element(self.controls["错误提示-知道了"]).click()