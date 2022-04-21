#-*- coding:utf-8 -*-
from unittest import TestCase
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.keys import Keys

class areaSettingPO(BasePage,TestCase):
    controls = {
        "区域设置":(By.XPATH,'.//*[text()="区域设置"]'),
        "区域名称列表":(By.XPATH,'//tr[@class="ant-table-row ant-table-row-level-0"]/td[2]/span'),
        "编辑列表":(By.XPATH,'//tr[@class="ant-table-row ant-table-row-level-0"]/td[6]/button[1]/span'),
        "删除列表":(By.XPATH,'//tr[@class="ant-table-row ant-table-row-level-0"]/td[6]/button[2]'),
        "已维护区域":(By.XPATH,'//div[text()="已维护区域"]'),
        "未绑定项目":(By.XPATH,'//div[text()="未绑定项目"]'),
        "选中标签": (By.XPATH, '//div[@class="ant-tabs-tab-active ant-tabs-tab"]'),
        "未选中的标签": (By.XPATH, '//div[@class=" ant-tabs-tab"]'),

        "新增区域": (By.XPATH, '//span[text()="新增区域"]//parent::button[@type="button"]'),
        "区域名称": (By.XPATH, '//input[@id="regionName"]'),
        "区域首字母": (By.XPATH, '//div[@id="initials"]//div[@role="combobox"]'),
        "区域首字母-删除": (By.XPATH, '//i[@class="anticon anticon-close-circle ant-select-clear-icon"]'),
        "辖区范围":(By.XPATH,'//span[@class="ant-cascader-picker-label"]'),
        "辖区范围-删除":(By.XPATH,'//i[@class="anticon anticon-close-circle ant-cascader-picker-clear"]'),
        "辖区范围+":(By.XPATH,'//div[@class="pages-region-modules-regionModal-form-module_3QyQk"]/span[1]/i'),
        "辖区范围-": (By.XPATH, '//div[@class="pages-region-modules-regionModal-form-module_3QyQk"]/span[2]/i'),
        "辖区范围-确认删除":(By.XPATH,'//div[@class="ant-popover-inner-content"]/div/button[@class="ant-btn ant-btn-primary ant-btn-sm"]'),
        "辖区范围下拉框":(By.XPATH,'//div[@class="ant-cascader-menus  ant-cascader-menus-placement-topLeft "]/div/ul/li'),
        "新增区域-关联项目": (By.XPATH, '//div[@class="ant-select-show-arrow ant-select ant-select-enabled"]/div/div/div'),
        # 返回1个或多个删除项目按钮
        "关联项目-删除项目": (By.XPATH, '//i[@class="anticon anticon-close ant-select-remove-icon"]'),
        #确定列表
        "确定": (By.XPATH, '//span[text()="确 定"]/parent::button'),
        #"确定":(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]'),

        "取消":(By.XPATH,'//button[@class="ant-btn"]'),
        "关闭弹窗":(By.XPATH,'//span[@class="ant-modal-close-x"]/i'),

        "编辑": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/table/tbody/tr/td/button[1]'),
        "删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[1]/div/div/div/div/div[3]/div/div/table/tbody/tr/td/button[2]'),
        "删除-确认": (By.XPATH, '//button[@class="ant-btn ant-btn-danger"]'),
        "删除-取消":(By.XPATH,'//button[@class="ant-btn"]'),
        "定位匹配设置": (By.XPATH, '//button[@class="ant-btn ml15 ant-btn-primary"]'),
        "定位匹配设置-开启定位重定向": (By.XPATH, '//button[@class="ant-switch" and @aria-checked="false" ]'),
        "定位匹配设置-默认名称":(By.XPATH,'//input[@class="ant-input pages-region-modules-positionModal-index-module_ApVl9"]'),
        "定位匹配设置-关闭定位重定向":(By.XPATH,'//button[@class="ant-switch ant-switch-checked" and @aria-checked="true" ]'),
        "定位匹配设置-取消":(By.XPATH,'//button[@class="ant-btn"]'),
        "定位匹配设置-确定":(By.XPATH,'//button[@class="ant-btn ant-btn-primary"]'),
        "定位匹配设置-关闭":(By.XPATH,'//i[@class="anticon anticon-close ant-modal-close-icon"]'),
        #例：辖区:广东省深圳市南山区已经被区域:深圳南山关联过，不允许重复关联
        "错误提示":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "blank": (By.XPATH, '//div[@class="ant-modal-body"]'),
        "新建区域":(By.XPATH,'//div[@id="rcDialogTitle0"]'),

        "共计总记录": (By.XPATH, "//span[@class='primary']"),
        "每页条数": (By.XPATH, "//div[@class='ant-select-sm ant-select ant-select-enabled']/div/div/div"),
        "上一页": (By.XPATH, "//li[@title='上一页']"),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
        "错误提示知道了":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button'),
        "区域首字母文本":(By.XPATH,'//label[@title="区域首字母"]')
    }

    def add_area_01(self,area_name):
        '''新增区域，不关联项目'''
        self.wait_eleVisible(self.controls["已维护区域"])
        self.find_element(self.controls["已维护区域"]).click()
        self.wait_eleVisible(self.controls["新增区域"])
        self.find_element(self.controls["新增区域"]).click()
        self.wait_eleVisible(self.controls["区域名称"])
        sleep(2)
        self.find_element(self.controls["区域名称"]).click()
        self.find_element(self.controls["区域名称"]).send_keys(area_name)
        sleep(2)
        self.wait_eleVisible(self.controls["区域首字母"])
        self.find_element(self.controls["区域首字母"]).click()
        self.switch_to_active_element().send_keys(Keys.ENTER)
        self.find_element(self.controls['区域首字母文本']).click()
        # self.wait_eleVisible(self.controls["新增区域-关联项目"])
        # self.find_element(self.controls["新增区域-关联项目"]).click()
        # self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        # sleep(2)
        # self.switch_to_active_element().send_keys(Keys.ENTER)
        # self.find_element(self.controls['区域首字母文本']).click()
        flag = True
        check_flag = False
        i = 1
        while(flag):
            self.wait_eleVisible(self.controls["辖区范围"])
            self.find_element(self.controls["辖区范围"]).click()
            sleep(1)
            if self.is_exist_element(self.controls["辖区范围-删除"]):
                self.find_element(self.controls["辖区范围-删除"]).click()
                self.find_element(self.controls["辖区范围"]).click()
            for a in range(i):
                self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
            self.switch_to_active_element().send_keys(Keys.ENTER)
            self.find_element(self.controls['区域首字母文本']).click()
            #self.find_element((self.controls['blank'])).click()
            # self.wait_eleVisible(self.controls["确定"])
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["错误提示知道了"]):
                i=i+1
                self.find_element(self.controls["错误提示知道了"]).click()
            else:
                check_flag = True
                flag = False
            if i > 34 :
                flag = False
                self.find_element(self.controls["取消"]).click()
        self.assertTrue(check_flag,msg="未成功新增区域")

    def add_area_02(self,area_name):
        '''新增区域，关联项目'''
        sleep(2)
        self.wait_eleVisible(self.controls["已维护区域"])
        self.find_element(self.controls["已维护区域"]).click()
        self.wait_eleVisible(self.controls["新增区域"])
        self.find_element(self.controls["新增区域"]).click()
        self.wait_eleVisible(self.controls["区域名称"])
        sleep(2)
        self.find_element(self.controls["区域名称"]).click()
        self.find_element(self.controls["区域名称"]).send_keys(area_name)
        sleep(2)
        self.wait_eleVisible(self.controls["区域首字母"])
        self.find_element(self.controls["区域首字母"]).click()
        # sleep(2)
        # self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        self.find_element(self.controls['区域首字母文本']).click()
        self.wait_eleVisible(self.controls["新增区域-关联项目"])
        self.find_element(self.controls["新增区域-关联项目"]).click()
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        self.find_element(self.controls['区域首字母文本']).click()
        flag = True
        check_flag = False
        i = 1
        while(flag):
            # self.wait_eleVisible(self.controls['辖区范围下拉框'])
            # list = self.find_elements_list(self.controls['辖区范围下拉框'])
            # list[i].click()
            self.wait_eleVisible(self.controls["辖区范围"])
            self.find_element(self.controls["辖区范围"]).click()
            sleep(1)
            if self.is_exist_element(self.controls["辖区范围-删除"]):
                self.find_element(self.controls["辖区范围-删除"]).click()
                self.find_element(self.controls["辖区范围"]).click()
            for a in range(i):
                self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
            self.switch_to_active_element().send_keys(Keys.ENTER)
            self.find_element(self.controls['区域首字母文本']).click()
            #self.find_element((self.controls['blank'])).click()
            # self.wait_eleVisible(self.controls["确定"])
            sleep(2)
            self.find_element(self.controls["确定"]).click()
            sleep(2)
            if self.is_exist_element(self.controls["错误提示知道了"]):
                i=i+1
                self.find_element(self.controls["错误提示知道了"]).click()
            else:
                check_flag = True
                flag = False
            if i > 34 :
                flag = False
        self.assertTrue(check_flag,msg="未成功新增区域")

    def edit_area(self,area_name):
        '''编辑区域'''
        self.click_edit(area_name)
        sleep(2)
        self.wait_eleVisible(self.controls['辖区范围+'])
        self.find_element(self.controls['辖区范围+']).click()
        flag = True
        check_flag = False
        i = 1
        while (flag):
            self.wait_eleVisible(self.controls["辖区范围"])
            self.find_elements(self.controls["辖区范围"],1).click()
            sleep(1)
            if len(self.find_elements_list(self.controls["辖区范围-删除"])) > 1:
                self.find_elements(self.controls["辖区范围-删除"],1).click()
                self.find_elements(self.controls["辖区范围"],1).click()
            for a in range(i+1):
                self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)

            self.switch_to_active_element().send_keys(Keys.ENTER)

            self.find_element(self.controls['区域首字母文本']).click()
            #self.find_element((self.controls['blank'])).click()
            sleep(2)
            if (self.find_elements(self.controls["辖区范围"],1).text in self.find_elements(self.controls["辖区范围"], 0).text  ):
                i += 1
            else:
                # self.wait_eleVisible(self.controls["确定"])
                sleep(2)
                self.find_element(self.controls["确定"]).click()
                sleep(2)
                if self.is_exist_element(self.controls["错误提示知道了"]):
                    i = i + 1
                    self.find_element(self.controls["错误提示知道了"]).click()
                else:
                    check_flag = True
                    flag = False
                if i > 34:
                    flag = False
        self.refresh_page()

    def edit_area_delete_area(self,area_name):
        '''编辑区域,删除辖区范围'''
        self.click_edit(area_name)
        sleep(2)
        if len(self.find_elements_list(self.controls["辖区范围-"])) > 1:
            self.find_elements(self.controls["辖区范围-"], 1).click()
            self.wait_eleVisible(self.controls["辖区范围-确认删除"])
            self.find_element(self.controls["辖区范围-确认删除"]).click()
        # self.wait_eleVisible(self.controls["确定"])
        sleep(2)
        self.find_element(self.controls["确定"]).click()


    def delete_area(self,area_name):
        '''删除区域'''
        self.click_delete(area_name)
        self.wait_eleVisible(self.controls["删除-确认"])
        self.find_element(self.controls["删除-确认"]).click()

    def open_location_matching_settings(self,name):
        '''定位匹配设置-开启定位重定向'''
        self.wait_eleVisible(self.controls["已维护区域"])
        self.find_element(self.controls["已维护区域"]).click()
        self.wait_eleVisible(self.controls["定位匹配设置"])
        self.find_element(self.controls["定位匹配设置"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["定位匹配设置-开启定位重定向"]):
            #开启定位重定向
            self.find_element(self.controls["定位匹配设置-开启定位重定向"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(Keys.CONTROL, 'a')
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(name)
        elif self.is_exist_element(self.controls["定位匹配设置-关闭定位重定向"]):
            #关闭定位重定向
            self.find_element(self.controls["定位匹配设置-关闭定位重定向"]).click()
            sleep(2)
            self.find_element(self.controls["定位匹配设置-开启定位重定向"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(Keys.CONTROL,'a')
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(name)
        sleep(2)
        self.find_element(self.controls["定位匹配设置-确定"]).click()


    def close_location_matching_settings(self,name):
        '''定位匹配设置-关闭定位重定向'''
        self.wait_eleVisible(self.controls["已维护区域"])
        self.find_element(self.controls["已维护区域"]).click()
        self.wait_eleVisible(self.controls["定位匹配设置"])
        self.find_element(self.controls["定位匹配设置"]).click()
        sleep(2)
        if self.is_exist_element(self.controls["定位匹配设置-关闭定位重定向"]):
            #关闭定位重定向
            self.find_element(self.controls["定位匹配设置-关闭定位重定向"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(Keys.CONTROL, 'a')
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(name)

        elif self.is_exist_element(self.controls["定位匹配设置-开启定位重定向"]):
            #开启定位重定向
            self.find_element(self.controls["定位匹配设置-开启定位重定向"]).click()
            sleep(2)
            self.find_element(self.controls["定位匹配设置-关闭定位重定向"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).click()
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(Keys.CONTROL, 'a')
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys("")
            sleep(2)
            self.find_element(self.controls["定位匹配设置-默认名称"]).send_keys(name)
        sleep(2)
        self.find_element(self.controls["定位匹配设置-确定"]).click()

    def maintained_area(self):
        '''打开已维护项目'''
        #self.wait_eleVisible(self.controls["已维护区域"])
        self.find_element(self.controls["已维护区域"]).click()

    def unbound_project(self):
        '''打开未绑定项目'''
        self.wait_eleVisible(self.controls["未绑定项目"])
        self.find_element(self.controls["未绑定项目"]).click()
        #断言

    def error_message_prompt(self):
        '''例：辖区:广东省深圳市南山区已经被区域:深圳南山关联过，不允许重复关联'''
        if self.is_exist_element(self.controls['错误提示']):
            self.find_element(self.controls['错误提示']).click()

    def check_next_clickable(self):
        '''检查下一页按钮是否可点击'''
        button_clickable = self.is_exist_element(self.controls['获取可点击的下一页'])
        return button_clickable

    def click_next_page(self):
        '''点击下一页'''
        flag = True
        count = 0
        while (flag):
            sleep(2)
            if self.is_exist_element(self.controls['获取可点击的下一页']):
                self.find_element(self.controls['下一页']).click()
                count += 1
                if count > 8:
                    flag = False
            else:
                flag = False

    def check_previous_clickable(self):
        '''检查上一页按钮是否可点击'''
        button_clickable = self.is_exist_element(self.controls['获取可点击的上一页'])
        return button_clickable

    def total_data(self):
        '''获取当前查询共计总记录'''
        if self.is_exist_element(self.controls['共计总记录']):
            return self.find_element(self.controls['共计总记录']).text
        return 1

    def Number_page(self):
        '''获取每页的条数'''
        if self.is_exist_element(self.controls['每页条数']):
            return self.find_element(self.controls['每页条数']).text
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
            if self.is_exist_element(self.controls['跳转至第几页']):
                sleep(2)
                self.find_element(self.controls['跳转至第几页']).send_keys(page + 1)
                sleep(2)
                #self.send_keys("{ENTER}")
                self.find_element(self.controls['共计总记录']).click()
                sleep(2)
                while(self.is_exist_element(self.controls['获取可点击的上一页'])):
                    sleep(1)
                    self.find_element(self.controls['上一页']).click()

    def click_blank(self):
        '''点击页面的空白处'''
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()

    #点击编辑
    def click_edit(self,name):
        #获取下拉列表
        typeBolle = True
        countNum = 0
        while (typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.controls['区域名称列表'])
            countNum = 0
            for b in bodyContent:
                if b.text == name:
                    flag = True
                    break
                countNum += 1

            sleep(1)
            if flag:
                break
            typeBolle = self.check_next_button_clickable()
            if typeBolle:
                self.click_next()
        #self.wait_eleVisible(self.controls['编辑'])
#        print("countNum:",countNum)
        self.find_elements(self.controls['编辑'], countNum).click()

    #点击删除
    def click_delete(self, name):
        # 获取下拉列表
        typeBolle = True
        countNum = 0
        while (typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.controls['区域名称列表'])
            countNum = 0
            for b in bodyContent:
                if b.text == name:
                    flag = True
                    break
                countNum += 1

            sleep(1)
            if flag:
                break
            typeBolle = self.check_next_button_clickable()
            if typeBolle:
                self.click_next()
        #self.wait_eleVisible(self.controls['删除'])
        sleep(2)
        self.find_elements(self.controls['删除'], countNum).click()

    def refresh_page(self):
        '''刷新页面'''
        self.refresh()
