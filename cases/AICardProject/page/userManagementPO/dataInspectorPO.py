#-*- coding:utf-8 -*-
import unittest
from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage

class dataInspector(BasePage):
    control = {
        "数据查阅人":(By.XPATH,'.//*[text()="数据查阅人"]'),
        "数据查阅人-电话列表":(By.XPATH,'//div[@class="pages-manager_data_review-UserCard-index-module_37sbF"]'),
        "数据查阅人-说明列表":(By.XPATH,'//div[@class="pages-manager_data_review-UserCard-index-module_1V2Y9"]/span'),
        "详细说明":(By.XPATH,'//div[@class="mr10"]/a'),
        "请输入姓名或手机号":(By.XPATH,'//span[@class="ant-input-search w-250 h-32 ant-input-search-enter-button ant-input-group-wrapper"]/span[@class="ant-input-wrapper ant-input-group"]/input'),
        "查询":(By.XPATH,'//span[@class="ant-input-group-addon"]/button'),
        "新增":(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]'),
        "新增-请输入用户手机号":(By.XPATH,'//span[@class="ant-input-search ant-input-search-enter-button ant-input-group-wrapper"]/span/input'),
        "新增-搜索":(By.XPATH,'//div[2]/div/div/span/span/span/button'),
        "新增-关闭":(By.XPATH,'//span[@class="ant-modal-close-x"]/i'),
        #错误提示-找不到该集团用户/获取小程序码失败/用户已经存在,请不要重新添加
        "错误提示-知道了":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@type="button" and @class="ant-btn ant-btn-primary"]'),
        "获取绑定小程序码":(By.XPATH,'//button[@class="ant-btn pages-manager_data_review-UserCard-index-module_1ZOup ant-btn-primary"]'),
        "同步":(By.XPATH,'//button[@class="ant-btn ant-btn-default"]'),
        #点击同步后，列表的数据，检查电话号栏目
        "同步后的数据":(By.XPATH,'//div[@class="pages-manager_data_review-UserCard-index-module_37sbF"]'),
        "删除":(By.XPATH,'//i[@class="anticon anticon-delete pages-manager_data_review-UserCard-index-module_1Qw6P"]'),
        #操作确认，确定删除该用户？
        "确定":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),

        "共计总记录": (By.XPATH, "//span[@class='primary']"),
        "每页条数": (By.XPATH, '//div[@class="ant-select-selection__rendered"]/div'),
        "上一页": (By.XPATH, "//li[@title='上一页']"),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input')
    }
    
    def __init__(self,driver):
        super(dataInspector, self).__init__(driver)

    def get_list(self,check_type):
        str_data = ""
        self.wait_eleVisible(self.control["数据查阅人-电话列表"])
        list = self.find_elements_list(self.control["数据查阅人-电话列表"])
        if len(list) == 0 :
            str_data = "18816851537"
        if (check_type == '1') & len(list) != 0 :
            str_data = list[0].text
            # print("str_data:"+str_data)
        else:
            str_data = list[0].text[0:6]
        return str_data

    def inquiry(self,parameter):
        '''输入姓名/手机号进行查询'''
        self.wait_eleVisible(self.control['请输入姓名或手机号'])
        sleep(2)
        self.find_element(self.control['请输入姓名或手机号']).click()
        sleep(2)
        #self.find_element(self.control['请输入姓名或手机号']).send_keys(parameter['name_or_phone'])
        self.find_element(self.control['请输入姓名或手机号']).send_keys(self.get_list(parameter['check_type']))
        sleep(2)
        self.find_element(self.control['查询']).click()
        # sleep(2)
        #断言
        #self.find_element(self.control['同步后的数据']).text


    def add(self,parameter):
        '''新增数据查阅人'''
        self.wait_eleVisible(self.control['新增'])
        self.find_element(self.control['新增']).click()
        self.wait_eleVisible(self.control['新增-请输入用户手机号'])
        self.find_element(self.control['新增-请输入用户手机号']).click()
        self.find_element(self.control['新增-请输入用户手机号']).send_keys(self.get_list(parameter['check_type']))
        sleep(2)
        self.wait_eleVisible(self.control['新增-搜索'])
        self.find_element(self.control['新增-搜索']).click()
        sleep(2)
        if self.is_exist_element(self.control['获取绑定小程序码']):
            self.find_element(self.control['获取绑定小程序码']).click()
        sleep(2)
        #错误提示，用户已存在，请不要重新添加。
        if self.is_exist_element(self.control['错误提示-知道了']):
            self.find_element(self.control['错误提示-知道了']).click()
        self.wait_eleVisible(self.control['新增-关闭'])
        self.find_element(self.control['新增-关闭']).click()

    def confirm_delete(self):
        '''确认删除数据查阅人'''
        sleep(2)
        if self.is_exist_element(self.control['删除']):
            self.find_element(self.control['删除']).click()
            if self.is_exist_element(self.control['确定']):
                self.find_element(self.control['确定']).click()

    def cancel_delete(self):
        '''取消删除数据查阅人'''
        sleep(2)
        if self.is_exist_element(self.control['删除']):
            self.find_element(self.control['删除']).click()
            if self.is_exist_element(self.control['取消']):
                self.find_element(self.control['取消']).click()

    def click_detailed_description(self):
        '''点击详细说明'''
        sleep(2)
        handle = self.driver.current_window_handle
        self.find_element(self.control['详细说明']).click()
        sleep(2)
        self.driver.switch_to_window(handle)
        sleep(1)

    def synchronization(self):
        '''同步数据查阅人'''
        sleep(2)
        self.find_element(self.control['同步']).click()
        # sleep(2)
        # 断言
        # self.find_element(self.control['同步后的数据']).text

    def refresh_page(self):
        '''刷新页面'''
        self.refresh()

    def check_next_clickable(self):
        '''检查下一页按钮是否可点击'''
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next_page(self):
        '''点击下一页'''
        flag = True
        count = 0
        while (flag):
            sleep(2)
            if self.is_exist_element(self.control['获取可点击的下一页']):
                self.find_element(self.control['下一页']).click()
                count += 1
                if count > 8:
                    flag = False
            else:
                flag = False

    def check_previous_clickable(self):
        '''检查上一页按钮是否可点击'''
        button_clickable = self.is_exist_element(self.control['获取可点击的上一页'])
        return button_clickable

    def total_data(self):
        '''获取当前查询共计总记录'''
        if self.is_exist_element(self.control['共计总记录']):
            return self.find_element(self.control['共计总记录']).text
        return 1

    def Number_page(self):
        '''获取每页的条数'''
        if self.is_exist_element(self.control['每页条数']):
            return self.find_element(self.control['每页条数']).text
        return 1

    def click_previous_page(self):
        '''点击上一页'''
        sleep(2)
        # total_data = int(self.total_data())
        # number_page = int(self.Number_page())
        # page = int(total_data/number_page)
        # if page > 10:
        #
        page = 10
        if page > 1:
            if self.is_exist_element(self.control['跳转至第几页']):
                sleep(2)
                # self.wait_eleVisible(self.control['跳转至第几页'])
                self.find_element(self.control['跳转至第几页']).send_keys(page + 1)
                sleep(2)
                self.send_keys("{ENTER}")
                sleep(2)
                while(self.is_exist_element(self.control['获取可点击的上一页'])):
                    sleep(1)
                    self.find_element(self.control['上一页']).click()