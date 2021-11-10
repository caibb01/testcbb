# -*- coding:utf-8 -*-
import unittest
from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class projectManagement(BasePage):
    control = {
        "项目管理": (By.XPATH, '//span[text()="项目管理"]'),
        "项目系统名称":(By.XPATH,'//span[@class="ant-form-item-children"]/div/div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "请选择项目":(By.XPATH,'//input[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "项目列表":(By.XPATH,'//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]/div'),
        "项目列表-全部": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_1R0Lp components-common-SelectTree-index-module_fI8Ra components-common-SelectTree-index-module_fI8Ra"]'),
        #"所属城市":(By.XPATH,'//input[@class="ant-input ant-cascader-input "]'),
        "所属城市":(By.XPATH,'//div[@class="ant-col ant-form-item-control-wrapper"]/div[@class="ant-form-item-control"]/span/div/span'),
        "所属城市-第一个列表":(By.XPATH,'//li[@class="ant-cascader-menu-item ant-cascader-menu-item-expand"]'),
        "所属城市-第二个列表":(By.XPATH,'//li[@class="ant-cascader-menu-item"]'),
        "所属城市-删除图标":(By.XPATH,'//i[@class="anticon anticon-close-circle ant-cascader-picker-clear"]'),
        "发布状态":(By.XPATH,'//div[@class="ant-select ant-select-enabled"]/div/div[@class="ant-select-selection__rendered"]'),
        "发布状态列表":(By.XPATH,'//ul[@class="ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical"]/li'),
        "查询":(By.XPATH,'//span[@class="ant-form-item-children"]/button[@class="ant-btn ant-btn-primary"]'),

        "项目系统名称-列表":(By.XPATH,'//tbody/tr/td[2]/div'),
        "发布状态-已发布":(By.XPATH,'//tbody/tr[1]/td[5]/button[@class="ant-switch ant-switch-checked"]'),
        "发布状态-已关闭":(By.XPATH,'//tbody/tr[1]/td[5]/button[@class="ant-switch"]'),
        "发布状态-列表": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[5]/button/span'),
        "发布状态-文案":(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div/div/table/tbody/tr/td[5]/button/span'),
        "提示弹窗-确认":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "提示弹窗-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        #错误提示:项目已被禁用，请联系明源顾问;当前项目未关联区域，请将项目关联区域之后，再执行发布操作;
        "错误提示-知道了":(By.XPATH,'//div/button[@class="ant-btn ant-btn-primary"]'),
        #操作-编辑列表
        "操作-编辑":(By.XPATH,'//tbody/tr/td[6]/button[@class="ant-btn ant-btn-link ant-btn-sm"][1]'),
        #操作-接待列表
        "操作-接待列表":(By.XPATH,'//tr/td[6]/button[@class="ant-btn ant-btn-link ant-btn-sm"][2]'),
        "项目接待列表设置页面-关闭":(By.XPATH,'//i[@class="anticon anticon-close"]'),
        "输入框":(By.XPATH,'//input[@class="ant-input"]'),
        "输入框搜索":(By.XPATH,'//span[@class="ant-input-suffix"]'),
        "隐藏列表":(By.XPATH,'//i[@class="anticon anticon-eye"]'),
        "已经隐藏列表":(By.XPATH,'//i[@class="anticon anticon-eye-invisible"]'),
        "checkbox列表":(By.XPATH,'//input[@class="ant-checkbox-input"]'),
        "还未选中的checkbox列表":(By.XPATH,'//span[@class="ant-checkbox"]/input[@class="ant-checkbox-input"]'),
        "选中的checkBox列表":(By.XPATH,'//span[@class="ant-checkbox ant-checkbox-checked"]/input[@class="ant-checkbox-input"]'),
        "人员列表":(By.XPATH,'//li[@class="ant-list-item"]/div[3]'),
        "操作-上移":(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/button[1]'),
        "操作-下移":(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/button[2]'),
        "操作-删除":(By.XPATH,'/html/body/div[3]/div/div[2]/div/div/div[2]/div[1]/div[2]/div/div/div/div/div/div/table/tbody/tr/td[3]/button[3]'),
        "项目接待列表设置页面-保存":(By.XPATH,'//div/button[@class="ant-btn ant-btn-primary"]'),
        "项目接待列表设置页面-取消": (By.XPATH, '//div/button[@class="ant-btn"]'),
        "温馨提示确认":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "关闭项目接待页面":(By.XPATH,'//button[@class="ant-drawer-close"]'),
        #操作-复制页面路径列表
        "操作-复制页面路径":(By.XPATH,'//tr/td[6]/button[@class="ant-btn ant-btn-link ant-btn-sm" ][3]'),

        "共计":(By.XPATH,'//li[@class="ant-pagination-total-text"]'),

        "共计总记录": (By.XPATH, '//li[@class="ant-pagination-total-text"]/div/span'),
        "每页条数": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/ul/li[11]/div[1]/div/div/div'),
        "上一页": (By.XPATH, "//li[@title='上一页']"),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input')
    }

    def __init__(self, driver):
        super(projectManagement, self).__init__(driver)

    count_sum = 0
    def publish_multiple_projects(self,publishStatus):
        '''发布项目(包含项目已关联区域，未关联区域，项目被禁用)'''
        flag = False
        self.count_sum += 1
        sleep(3)
        if self.is_exist_element(self.control["发布状态-列表"]):
            list = self.find_elements_list(self.control["发布状态-列表"])
            count = 0
            for l in list:
                sleep(2)
                count += 1
                if l.text != publishStatus :
                    # print("publishStatus:",l.text)
                    l.click()
                    if self.is_exist_element(self.control['提示弹窗-确认']):
                        sleep(2)
                        self.wait_eleVisible(self.control['提示弹窗-确认'])
                        self.find_element(self.control['提示弹窗-确认']).click()
                    if self.is_exist_element(self.control["错误提示-知道了"]):
                        sleep(2)
                        self.find_element(self.control["错误提示-知道了"]).click()

                if (count == len(list))&(self.count_sum <3) :
                    if self.check_next_clickable():
                        #点击下一页
                        self.find_element(self.control['下一页']).click()
                        sleep(2)
                        self.publish_multiple_projects(publishStatus)
        self.refresh()
        sleep(3)

    def publish_project(self):
        '''发布项目'''
        sleep(3)
        if self.is_exist_element(self.control["发布状态-列表"]):
            self.find_elements(self.control["发布状态-列表"], 0).click()
            if self.is_exist_element(self.control["错误提示-知道了"]):
                self.find_element(self.control["错误提示-知道了"]).click()
            else:
                self.wait_eleVisible(self.control['提示弹窗-确认'])
                self.find_element(self.control['提示弹窗-确认']).click()
        self.refresh()
        sleep(3)


    # def select_publish_status(self):
    #     '''选择发布状态'''
    #     self.wait_eleVisible(self.control['发布状态'])
    #     self.find_element(self.control['发布状态']).click()
    #     i = 0
    #     s = self.find_elements_list(self.control['发布状态列表'])
    #     #for i in s:
    #     for i in range(0,len(s)):
    #         if i != 0 :
    #             self.find_element(self.control['发布状态']).click()
    #         sleep(2)
    #         self.find_elements(self.control['发布状态列表'],i).click()
    #         sleep(2)
    #         self.find_element(self.control['查询']).click()
    #         sleep(3)
    #     self.refresh()
    #     sleep(2)

    def select_publish_status(self,publishStatus):
        '''选择发布状态'''
        self.refresh()
        self.wait_eleVisible(self.control['发布状态'])
        self.find_element(self.control['发布状态']).click()
        sleep(2)
        s = self.find_elements_list(self.control['发布状态列表'])
        for i in s:
            # if i != 0:
            #     self.find_element(self.control['发布状态']).click()
            if i.text == publishStatus:
                sleep(2)
                i.click()
                break
        self.find_element(self.control['查询']).click()
        sleep(2)

    def select_publish_status_01(self,publishStatus):
        '''选择发布状态'''
        self.wait_eleVisible(self.control['发布状态'])
        self.find_element(self.control['发布状态']).click()
        sleep(3)
        s = self.find_elements_list(self.control['发布状态列表'])
        for i in s:
            sleep(2)
            # if i != 0:
            #     self.find_element(self.control['发布状态']).click()
            if i.text == publishStatus:
                sleep(2)
                i.click()
                break
        self.find_element(self.control['查询']).click()
        sleep(3)
        self.refresh()
        sleep(3)

    def edit_project(self):
        '''编辑项目'''
        sleep(2)
        handle = self.driver.current_window_handle
        if self.is_exist_element(self.control['操作-编辑']):
            self.find_elements(self.control['操作-编辑'],0).click()
            sleep(2)
            self.driver.switch_to_window(handle)
            sleep(1)
        self.refresh()
        sleep(3)

    def get_list_project(self,check_project_type = None):
        '''项目下拉列表，选择第一条项目数据'''
        str_data = ""
        self.wait_eleVisible(self.control['项目列表'])
        list = self.find_elements_list(self.control['项目列表'])
        if len(list) == 0:
            str_data = "全部"
        elif (check_project_type == '1') & (len(list) != 0):
            str_data = list[1].text
            print("str_data:"+str_data)
        elif (check_project_type == '2') & (len(list) != 0):
            str_data = list[1].text[0:1]
            print("str_data2:" + str_data)
        else:
            str_data = "全部"
        return str_data

    def select_project(self,parameter):
        # 选择或输入系统项目名称
        if parameter['project_Name'] != '':
            self.wait_eleVisible(self.control['项目系统名称'])
            self.find_element(self.control['项目系统名称']).click()
            project_Name = self.get_list_project(parameter['check_project_type'])
            # if project_Name == "全部":
            #     self.wait_eleVisible(self.control['请选择项目'])
            #     self.find_element(self.control['请选择项目']).send_keys(project_Name)
            #     sleep(1)
            #     self.wait_eleVisible(self.control['项目列表-全部'])
            #     self.find_element(self.control['项目列表-全部']).click()
            # else:
            # 判断查询还是直接点击
            i = -1
            # 用于判定是否查询到有我们的判定值
            numFlag = False
            if parameter['project_Type'] == 'input':
                self.wait_eleVisible(self.control['请选择项目'])
                self.find_element(self.control['请选择项目']).send_keys(project_Name)
                sleep(1)
                elem = self.find_elements_list(self.control['项目列表'])
                for e in elem:
                    i += 1
                    if fuzz.ratio(e.text, project_Name) > 0:
                        numFlag = True
                        break
            else:
                elem = self.find_elements_list(self.control['项目列表'])
                for e in elem:
                    i += 1
                    if e.text == project_Name:
                        numFlag = True
                        break
            sleep(1)
            if numFlag:
                self.wait_eleVisible(self.control['项目列表'])
                ele = self.find_elements(self.control['项目列表'], i)
                ele.click()
            else:
                self.find_element(self.control['项目管理']).click()
        sleep(2)
        self.refresh()
        sleep(3)

    def select_project_01(self,parameter):
        # 选择或输入系统项目名称
        if parameter['project_Name'] != '':
            self.wait_eleVisible(self.control['项目系统名称'])
            self.find_element(self.control['项目系统名称']).click()
            project_Name = self.get_list_project(parameter['check_project_type'])
            # if project_Name == "全部":
            #     self.wait_eleVisible(self.control['请选择项目'])
            #     self.find_element(self.control['请选择项目']).send_keys(project_Name)
            #     sleep(1)
            #     self.wait_eleVisible(self.control['项目列表-全部'])
            #     self.find_element(self.control['项目列表-全部']).click()
            # else:
            # 判断查询还是直接点击
            i = -1
            # 用于判定是否查询到有我们的判定值
            numFlag = False
            if parameter['project_Type'] == 'input':
                self.wait_eleVisible(self.control['请选择项目'])
                self.find_element(self.control['请选择项目']).send_keys(project_Name)
                sleep(1)
                elem = self.find_elements_list(self.control['项目列表'])
                for e in elem:
                    i += 1
                    if fuzz.ratio(e.text, project_Name) > 0:
                        numFlag = True
                        break
            else:
                elem = self.find_elements_list(self.control['项目列表'])
                for e in elem:
                    i += 1
                    if e.text == project_Name:
                        numFlag = True
                        break
            sleep(1)
            if numFlag:
                self.wait_eleVisible(self.control['项目列表'])
                ele = self.find_elements(self.control['项目列表'], i)
                ele.click()
            else:
                self.find_element(self.control['项目管理']).click()
        sleep(2)

    def select_city(self):
        '''根据所属城市，查询项目'''
        self.wait_eleVisible(self.control['所属城市'])
        self.find_element(self.control['所属城市']).click()
        sleep(2)
        self.find_elements(self.control['所属城市-第一个列表'],2).click()
        self.wait_eleVisible(self.control['所属城市-第二个列表'])
        self.find_elements(self.control['所属城市-第二个列表'],1).click()
        # self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        # sleep(2)
        # self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        # sleep(2)
        # self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)
        self.find_element(self.control['查询']).click()
        sleep(2)
        self.refresh()
        sleep(3)

    def select_city_01(self):
        '''根据所属城市，查询项目'''
        self.wait_eleVisible(self.control['所属城市'])
        self.find_element(self.control['所属城市']).click()
        sleep(2)
        self.find_elements(self.control['所属城市-第一个列表'],2).click()
        self.wait_eleVisible(self.control['所属城市-第二个列表'])
        self.find_elements(self.control['所属城市-第二个列表'],1).click()
        sleep(2)

    def close_project(self):
        '''关闭项目'''
        if self.is_exist_element(self.control['发布状态-已发布']):
            self.find_element(self.control['发布状态-已发布']).click()
            self.wait_eleVisible(self.control['提示弹窗-确认'])
            self.find_element(self.control['提示弹窗-确认']).click()
        else:
            self.find_element(self.control['发布状态-已关闭']).click()
            self.wait_eleVisible(self.control['提示弹窗-确认'])
            self.find_element(self.control['提示弹窗-确认']).click()
            sleep(2)
            self.find_element(self.control['发布状态-已发布']).click()
            self.wait_eleVisible(self.control['提示弹窗-确认'])
            self.find_element(self.control['提示弹窗-确认']).click()
            sleep(2)
            self.find_element(self.control['发布状态-已关闭']).click()
            self.wait_eleVisible(self.control['提示弹窗-确认'])
            self.find_element(self.control['提示弹窗-确认']).click()

    def reception_list(self):
        '''打开接待列表，勾选checkbox'''
        # if self.is_exist_element(self.control['发布状态-已关闭']):
        #     self.find_element(self.control['发布状态-已关闭']).click()
        #     self.wait_eleVisible(self.control['提示弹窗-确认'])
        #     self.find_element(self.control['提示弹窗-确认']).click()
        if self.is_exist_element(self.control['操作-接待列表']):
            sleep(2)
            if len(self.find_elements_list(self.control['操作-接待列表'])) != 0 :
                sleep(2)
                self.wait_eleVisible(self.control['操作-接待列表'])
                self.find_elements(self.control['操作-接待列表'], 0).click()
            sleep(2)
            if len(self.find_elements_list(self.control['checkbox列表'])) != 0:
                sleep(2)
                # self.wait_eleVisible(self.control['checkbox列表'])
                # self.find_elements(self.control['checkbox列表'], 0).click()
                self.change_checkbox()
                sleep(2)
                for i in range(0,3):
                    sleep(2)
                    self.find_elements(self.control['checkbox列表'], 0).click()

            self.save_reception_list()
            sleep(2)
            self.find_element(self.control['关闭项目接待页面']).click()
            self.refresh()
            sleep(3)
    #选中的checkbox置为未选中，再置为选中前4个
    def change_checkbox(self):
        if len(self.find_elements_list(self.control['选中的checkBox列表'])) >0 :
            for checkbox in self.find_elements_list(self.control['选中的checkBox列表']):
                checkbox.click();

        if len(self.find_elements_list(self.control['已经隐藏列表'])) >0:
            for eyeDIsable in self.find_elements_list(self.control['已经隐藏列表']) :
                eyeDIsable.click()

        # for i in range(3):
        #     self.find_elements(self.control('还未选中的checkbox列表'),i).click()



    def reception_list_people_search(self):
        '''项目接待列表-人员搜索'''
        '''打开接待列表'''
        sleep(2)
        if self.is_exist_element(self.control['操作-接待列表']):
            self.find_elements(self.control['操作-接待列表'], 0).click()
            sleep(2)
            '''获取接待列表'''
            self.wait_eleVisible(self.control["人员列表"])
            list = self.find_elements_list(self.control["人员列表"])
            # print("list:",list[0].text)
            one_str = int(list[0].text.find('('))+1
            twe_str = int(list[0].text.find(')'))
            # print("123131:",one_str,"---",twe_str)
            str = list[0].text[one_str:twe_str]
            self.find_element(self.control['输入框']).click()
            self.find_element(self.control['输入框']).send_keys(str)
            sleep(2)
            self.find_element(self.control['输入框搜索']).click()
            sleep(2)
            self.find_element(self.control['关闭项目接待页面']).click()
            self.refresh()
            sleep(3)


    def reception_list_people_hide(self):
        '''项目接待列表-人员隐藏'''
        '''打开接待列表'''
        sleep(2)
        if self.is_exist_element(self.control['操作-接待列表']):
            self.find_elements(self.control['操作-接待列表'], 0).click()
            sleep(2)
            # one_box = self.find_elements_list(self.control['checkbox列表'])
            # two_box = self.find_elements_list(self.control['还未选中的checkbox列表'])
            # a = len(one_box) - len(two_box)
            #
            # if a > 0 & (a < len(one_box)):
            #     self.wait_eleVisible(self.control["隐藏列表"])
            #     self.find_elements(self.control["隐藏列表"], a).click()

            self.change_checkbox()
            self.find_elements(self.control["隐藏列表"], 0).click()

            sleep(2)
            self.save_reception_list()
            sleep(2)
            self.find_element(self.control['关闭项目接待页面']).click()
            self.refresh()
            sleep(3)

    def reception_list_people_sort(self):
        '''项目接待列表-人员排序'''
        '''打开接待列表'''
        sleep(2)

        if self.is_exist_element(self.control['操作-接待列表']):
            if len(self.find_elements_list(self.control['操作-接待列表'])) != 0:
                self.wait_eleVisible(self.control['操作-接待列表'])
                self.find_elements(self.control['操作-接待列表'], 0).click()

            self.change_checkbox()
            sleep(2)
            for i in range(0, 3):
                sleep(2)
                self.find_elements(self.control['checkbox列表'], 0).click()
            sleep(2)

            if (self.is_exist_element(self.control["操作-上移"])):
                list1 = self.find_elements_list(self.control["操作-上移"])
                print('list1:',list1)
                if (len(list1) < 2 ):
                    for i in range(0,2):
                        sleep(2)
                        self.find_elements(self.control["还未选中的checkbox列表"],0).click()
                        if i > len(self.find_elements_list(self.control["操作-上移"])):
                            break
            else:
                for i in range(0, 2):
                    sleep(2)
                    self.find_elements(self.control["还未选中的checkbox列表"], 0).click()
            # 上移
            sleep(2)
            if self.is_exist_element(self.control['操作-上移']):
                self.wait_eleVisible(self.control['操作-上移'])
                #print("cccc=",len(self.find_elements_list(["操作-上移"])))
                # self.wait_eleVisible(self.control["操作-上移"])
                self.find_elements(self.control["操作-上移"], 1).click()
            if self.is_exist_element(self.control['操作-下移']):
                self.wait_eleVisible(self.control['操作-下移'])
                # 下移
                # self.wait_eleVisible(self.control["操作-下移"])
                sleep(2)
                self.find_elements(self.control["操作-下移"], 0).click()
            sleep(2)
            self.save_reception_list()
            sleep(2)
            self.find_element(self.control['关闭项目接待页面']).click()
            self.refresh()
            sleep(3)

    def reception_list_remove_personnel(self):
        '''项目接待列表-删除人员'''
        sleep(2)
        if self.is_exist_element(self.control['操作-接待列表']):
            if len(self.find_elements_list(self.control['操作-接待列表'])) != 0:
                self.wait_eleVisible(self.control['操作-接待列表'])
                self.find_elements(self.control['操作-接待列表'], 0).click()
            if self.is_exist_element(self.control["操作-删除"]):
                self.wait_eleVisible(self.control["操作-删除"])
                self.find_elements(self.control["操作-删除"], 0).click()
                sleep(2)
                self.save_reception_list()
                sleep(2)
            self.find_element(self.control['关闭项目接待页面']).click()
            self.refresh()
            sleep(3)

    def save_reception_list(self):
        '''项目接待列表-保存'''
        sleep(2)
        self.wait_eleVisible(self.control['项目接待列表设置页面-保存'])
        self.find_element(self.control['项目接待列表设置页面-保存']).click()
        sleep(2)
        self.wait_eleVisible(self.control['温馨提示确认'])
        self.find_element(self.control['温馨提示确认']).click()

    def copy_page_path(self):
        '''复制页面路径'''
        sleep(2)
        if self.is_exist_element(self.control['操作-复制页面路径']):
            self.find_elements(self.control['操作-复制页面路径'], 0).click()
            sleep(2)

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
                sleep(3)
                self.find_element(self.control['获取可点击的下一页']).click()
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
                # self.send_keys("{ENTER}")
                self.find_element(self.control['共计总记录']).click()
                sleep(2)
                while (self.is_exist_element(self.control['获取可点击的上一页'])):
                    sleep(1)
                    self.find_element(self.control['上一页']).click()
                    sleep(2)