#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from fuzzywuzzy import fuzz
from selenium.webdriver.common.keys import Keys

class H5ManagementPO(BasePage):
    control = {
        "内容管理目录": (By.XPATH, '//*[text()="内容管理"]'),
        # 添加
        "添加按钮": (By.XPATH, '//div[@class="page-manager-h5 pages-manager_h5-index-module_3B3T3"]/div[2]/div[2]/button'),
        "标题输入框": (By.XPATH, '//div/div[1]/div[2]/input[@class="ant-input inp"]'),
        "描述输入框": (By.XPATH, '//textarea[@class="ant-input fs-12"]'),
        "链接输入框": (By.XPATH, '//div/div[3]/div[2]/input[@class="ant-input inp"]'),
        "类型下拉框": (By.XPATH, '//div[@class="ant-select ant-select-enabled"]'),
        "类型下拉列表": (By.XPATH, '//div[@title="其他"]'),
        "关联项目下拉框": (By.XPATH, '//div/div[5]/div[2]/div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "选择项目下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        #"选择项目下拉列表": (By.XPATH,'//ul[@role="listbox"]/li'),
        "搜索项目": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "关联地区下拉框": (By.XPATH, '//span[text()="请选择地区"]'),
        "编辑-关联地区下拉框": (By.XPATH, '//span[text()="全局"]'),
        "关联地区选择框": (By.XPATH, '//div[@class="city-list"]'),
        "选择关联地区": (By.XPATH, '//div[@class="city-list"]/button'),
        "搜索城市": (By.XPATH, '//input[@placeholder="输入城市名进行搜索"]'),
        "搜索城市按钮": (By.XPATH, '//button[@class="ant-btn ant-input-search-button ant-btn-primary"]'),
        "保存": (By.XPATH, '//div/button[2][@class="ant-btn ant-btn-primary"]'),
        "取消": (By.XPATH, '//div/button[1][@class="ant-btn"]'),
        "关闭弹窗": (By.XPATH, '//button[@class="ant-modal-close"]'),

        # 列表查询
        "链接类型下拉框": (By.XPATH, '//div[@class="flex-default fs-12"]/div'),
        "链接类型搜索框": (By.XPATH, '//input[@placeholder="请输入关键字"]'),
        "链接类型下拉列表": (By.XPATH, '//div[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]/div/div[2]'),
        "列表-关联项目下拉框": (By.XPATH, '//div[@class="flex-default fs-12 ml20"]/div'),
        "关联项目搜索框": (By.XPATH, '//div[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]/div/div[1]/input'),
        "关联项目下拉列表": (By.XPATH, '//div[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]/div/div[2]'),

        # 编辑
        "编辑按钮": (By.XPATH, '//table/tbody/tr[1]/td[6]/span/button[1]'),

        # 删除
        "删除按钮": (By.XPATH, '//table/tbody/tr[1]/td[6]/span/button[2]'),
        "确定按钮": (By.XPATH, '//button[@class="ant-btn ant-btn-danger"]'),
        "取消按钮": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[@class="ant-btn"]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
    }

    def __init__(self, driver):
        super(H5ManagementPO, self).__init__(driver)

    def save_h5Link(self, params=None):
        # 添加h5链接
        # 点击添加按钮
        self.click_add_button()
        sleep(2)
        # 输入标题
        if params['title'] != '':
            self.input_title(params['title'])
        sleep(1)
        # 输入描述
        if params['description'] != '':
            self.input_description(params['description'])
        sleep(1)
        # 输入链接
        if params['link'] != '':
            self.input_link(params['link'])
        sleep(1)
        # 选择关联项目
        self.input_project()
        sleep(1)
        # 选择关联地区
        self.save_input_region()
        sleep(1)
        # 点击保存按钮
        self.click_save_button()

    def save_and_search(self, params=None):
        # 添加h5链接(包括搜索)
        # 点击添加按钮
        self.click_add_button()
        sleep(2)
        # 输入标题
        if params['title'] != '':
            self.input_title(params['title'])
        sleep(1)
        # 输入描述
        if params['description'] != '':
            self.input_description(params['description'])
        sleep(1)
        # 输入链接
        if params['link'] != '':
            self.input_link(params['link'])
        sleep(1)
        # 选择关联项目
        if params['project_name'] != '':
            self.wait_eleVisible(self.control['关联项目下拉框'])
            self.find_element(self.control['关联项目下拉框']).click()
            sleep(1)
            ele = self.control['搜索项目']
            self.wait_eleVisible(ele)
            self.find_element(ele).click()
            self.find_element(ele).send_keys(params['project_name'])
            sleep(1)
            i = -1
            i += 1
            self.find_elements(self.control['选择项目下拉列表'], i).click()
            sleep(1)
        # 选择关联地区
        if params['region_name'] != '':
            self.wait_eleVisible(self.control['关联地区下拉框'])
            self.find_element(self.control['关联地区下拉框']).click()
            sleep(1)
            ele = self.control['搜索城市']
            self.wait_eleVisible(ele)
            self.find_element(ele).click()
            self.find_element(ele).send_keys(params['region_name'])
            self.find_element(self.control['搜索城市按钮']).click()
            sleep(2)
            self.wait_eleVisible(self.control['关联地区选择框'])
            self.find_element((self.control['选择关联地区'])).click()
            sleep(1)
        # 点击保存按钮
        self.click_save_button()

    def edit_h5Link(self, params=None):
        # 编辑h5链接
        # 点击编辑按钮
        self.click_edit_button()
        sleep(2)
        # 输入标题
        if params['title'] != '':
            self.input_title(params['title'])
        # 输入描述
        if params['description'] != '':
            self.input_description(params['description'])
        # 输入链接
        if params['link'] != '':
            self.input_link(params['link'])
        # 选择关联项目
        self.input_project()
        sleep(2)
        # 选择关联地区
        self.edit_input_region()
        sleep(2)
        # 点击保存按钮
        self.click_save_button()

    def delete_h5Link(self):
        # 删除h5链接
        # 点击删除按钮
        self.wait_eleVisible(self.control['删除按钮'])
        self.find_element(self.control['删除按钮']).click()
        sleep(2)
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()

    def search_h5Link(self, parameter=None):
        # H5链接搜索
        if parameter['link_type'] != "":
            i = -1
            #用于判定是否查询到有我们的判定值
            numFalg = False
            # 点击链接类型下拉框
            self.wait_eleVisible(self.control['链接类型下拉框'])
            self.find_element(self.control['链接类型下拉框']).click()
            sleep(2)
            if parameter['search_type'] == 'input':
                type_search_box = self.control['链接类型搜索框']
                self.wait_eleVisible(type_search_box)
                self.find_element(type_search_box).click()
                self.find_element(type_search_box).send_keys(parameter['link_type'])
                sleep(2)
                # i += 1
                # self.find_elements(self.control['链接类型下拉列表'], i).click()
                elem = self.find_elements_list(self.control['链接类型下拉列表'])
                for e in elem:
                    if fuzz.ratio(e.text, parameter['link_type']) > 0:
                        numFalg = True
                        break
                    i += 1
            else:
                i += 1
                self.find_elements(self.control['链接类型下拉列表'], i).click()
                # elem = self.find_elements_list(self.control['链接类型下拉列表'])
                # for e in elem:
                #     if e.text == parameter['link_type']:
                    #     numFalg = True
                    #     break
                    # i += 1
                # i += 1
                # ele = self.find_elements(self.control['链接类型下拉列表'], i)
                # ele.click()
            if numFalg:
                self.wait_eleVisible(self.control['链接类型下拉列表'])
                ele = self.find_elements(self.control['链接类型下拉列表'], i)
                ele.click()
            else:
                self.find_element(self.control['内容管理目录']).click()
            sleep(2)

        if parameter['project_name'] != '':
            i = -1
            #用于判定是否查询到有我们的判定值
            numFalg = False
            # 点击链接类型下拉框
            self.wait_eleVisible(self.control['列表-关联项目下拉框'])
            self.find_element(self.control['列表-关联项目下拉框']).click()
            sleep(2)
            if parameter['search_type'] == 'input':
                project_search_box = self.control['关联项目搜索框']
                self.wait_eleVisible(project_search_box)
                self.find_element(project_search_box).click()
                self.find_element(project_search_box).send_keys(parameter['project_name'])
                sleep(2)
                # i += 1
                # self.find_elements(self.control['关联项目下拉列表'], i).click()
                elem = self.find_elements_list(self.control['关联项目下拉列表'])
                for e in elem:
                    if fuzz.ratio(e.text, parameter['project_name']) > 0:
                        numFalg = True
                        break
                    i += 1
            else:
                i += 1
                self.find_elements(self.control['关联项目下拉列表'], i).click()
                # elem = self.find_elements_list(self.control['关联项目下拉列表'])
                # for e in elem:
                #     if e.text == parameter['project_name']:
                    #     numFalg = True
                    #     break
                    # i += 1
                # i += 1
                # ele = self.find_elements(self.control['关联项目下拉列表'], i)
                # ele.click()
            if numFalg:
                self.wait_eleVisible(self.control['关联项目下拉列表'])
                ele = self.find_elements(self.control['关联项目下拉列表'], i)
                ele.click()
            else:
                self.find_element(self.control['内容管理目录']).click()
            sleep(2)

    def click_add_button(self):
        # 点击添加按钮
        self.wait_eleVisible(self.control['添加按钮'])
        self.find_element(self.control['添加按钮']).click()

    def click_edit_button(self):
        # 点击编辑按钮
        self.wait_eleVisible(self.control['编辑按钮'])
        self.find_element(self.control['编辑按钮']).click()

    def input_title(self, title=None):
        # 输入标题
        self.wait_eleVisible(self.control['标题输入框'])
        ele = self.find_element(self.control['标题输入框'])
        ele.click()
        ele.clear()
        ele.send_keys(title)

    def input_description(self, description=None):
        # 输入描述
        self.wait_eleVisible(self.control['描述输入框'])
        ele = self.find_element(self.control['描述输入框'])
        ele.click()
        ele.clear()
        ele.send_keys(description)

    def input_link(self, link=None):
        # 输入链接
        self.wait_eleVisible(self.control['链接输入框'])
        ele = self.find_element(self.control['链接输入框'])
        ele.click()
        ele.clear()
        ele.send_keys(link)

    def input_project(self):
        # 选择关联项目
        i = -1
        self.wait_eleVisible(self.control['关联项目下拉框'])
        self.find_element(self.control['关联项目下拉框']).click()
        sleep(1)
        i += 1
        self.wait_eleVisible(self.control['选择项目下拉列表'])
        ele = self.find_elements(self.control['选择项目下拉列表'], 0)
        ele.click()

    def save_input_region(self):
        # 选择关联地区
        self.wait_eleVisible(self.control['关联地区下拉框'])
        self.find_element(self.control['关联地区下拉框']).click()
        sleep(5)

        self.wait_eleVisible(self.control['关联地区选择框'])
        self.find_element(self.control['选择关联地区']).click()

    def edit_input_region(self):
        # 选择关联地区
        self.wait_eleVisible(self.control['编辑-关联地区下拉框'])
        self.find_element(self.control['编辑-关联地区下拉框']).click()
        sleep(5)

        self.wait_eleVisible(self.control['关联地区选择框'])
        self.find_element(self.control['选择关联地区']).click()

    def click_save_button(self):
        # 点击保存按钮
        self.wait_eleVisible(self.control['保存'])
        self.find_element(self.control['保存']).click()

    def click_cancel_button(self):
        # 点击取消按钮
        self.wait_eleVisible(self.control['取消'])
        self.find_element(self.control['取消']).click()

    def click_close_button(self):
        # 点击关闭按钮
        self.wait_eleVisible(self.control['关闭弹窗'])
        self.find_element(self.control['关闭弹窗']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        self.refresh()
        while (self.check_button_clickable()):
            nextNum = len(self.find_elements_list(self.control['下一页']))
            if nextNum > 1:
                self.find_elements(self.control['下一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.control['获取可点击的下一页']).click()

    def check_button_previous_page(self):
        # 检查上一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['上一页'])
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        while(self.check_button_previous_page()):
            nextNum = len(self.find_elements_list(self.control['上一页']))
            if nextNum > 1:
                self.find_elements(self.control['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.control['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data/number_page)
        if page > 1:
            self.wait_eleVisible(self.control['跳转至第几页'])
            self.find_element(self.control['跳转至第几页']).send_keys(page+1)
            sleep(2)
            self.find_element(self.control['跳转至第几页']).send_keys(Keys.ENTER)
            sleep(2)

    def total_data(self):
        '''获取当前查询共计总记录'''
        if self.is_exist_element(self.control['共计总记录']):
            return self.find_element(self.control['共计总记录']).text
        return 1

    def number_page(self):
        '''获取每页的条数'''
        if self.is_exist_element(self.control['每页条数']):
            return self.find_element(self.control['每页条数']).text
        return 1
