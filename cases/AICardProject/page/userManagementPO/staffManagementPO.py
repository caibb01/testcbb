#-*- coding:utf-8 -*-
from myweb.core.runner import TestCase
from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


from myweb.core.BasePage import BasePage

class staffManagement(BasePage, TestCase):
    control = {
        "用户管理":(By.XPATH,'//ul/li[@class="ant-menu-item sub-item ant-menu-item-selected"]'),
        #销售团队
        "销售团队": (By.XPATH, '//div[@role="tab" and @class="ant-tabs-tab-active ant-tabs-tab"]'),
        "销售团队-项目":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "销售团队-请选择项目":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_21xSF"]/input'),
        "销售团队-项目下拉列表":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_1R0Lp  "]'),
        "销售团队-项目下拉列表-全部":(By.XPATH,'//div[text()="全部"]'),
        "销售团队-模糊查询":(By.XPATH,'//span[@class="ant-form-item-children"]/input'),
        "销售团队-同步人员名单":(By.XPATH,'//div/button[@type="button"]'),
        "销售团队-查询":(By.XPATH,'//div/button[@type="submit"]'),
        "销售团队-已启用":(By.XPATH,'//td/button[@aria-checked="true"]'),
        "销售团队-已禁用":(By.XPATH,'//td/button[@aria-checked="false"]'),
        #启动或禁用该名片
        "销售团队-确定":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "销售团队-取消":(By.XPATH,'//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "销售团队-当前页面手机号列表数据": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[2]'),
        "销售团队-所属项目名称": (By.XPATH, '//table/tbody/tr/td[4][1]/button'),
        "销售团队-所属项目列表数据": (By.XPATH, '//table/tbody/tr/td[4]'),
        "销售团队-所属项目页面的列表": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td'),
        "销售团队-关闭所属项目页面": (By.XPATH, '//button[@class="ant-drawer-close"]'),

        #行销团队
        "行销团队": (By.XPATH, '//div[@class=" ant-tabs-tab"][1]'),
        "行销团队-项目": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "行销团队-请选择项目": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_21xSF"]/input'),
        "行销团队-项目下拉列表": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_1R0Lp  "]'),
        "行销团队-项目下拉列表-全部":(By.XPATH,'//div[text()="全部"]'),
        "行销团队-模糊查询": (By.XPATH, '//span[@class="ant-form-item-children"]/input'),
        "行销团队-同步人员名单": (By.XPATH, '//div/button[@type="button"]'),
        "行销团队-查询": (By.XPATH, '//div/button[@type="submit"]'),
        "行销团队-已启用": (By.XPATH, '//td/button[@aria-checked="true"]'),
        "行销团队-已禁用": (By.XPATH, '//td/button[@aria-checked="false"]'),
        # 启动或禁用该名片
        "行销团队-确定": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "行销团队-取消": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "行销团队-当前页面手机号列表数据": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[4]'),
        "行销团队-所属项目名称":(By.XPATH,'//table/tbody/tr/td[6][1]/button'),
        "行销团队-所属项目列表数据":(By.XPATH,'//table/tbody/tr/td[6]'),
        "行销团队-所属项目页面的列表": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td'),
        "行销团队-关闭所属项目页面": (By.XPATH, '//button[@class="ant-drawer-close"]'),

        #策划人员
        "策划人员": (By.XPATH, '//div[@class=" ant-tabs-tab"][2]'),
        "策划人员-项目": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "策划人员-请选择项目": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_21xSF"]/input'),
        "策划人员-项目下拉列表": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_1R0Lp  "]'),
        "策划人员-项目下拉列表-全部": (By.XPATH, '//div[text()="全部"]'),
        "策划人员-模糊查询": (By.XPATH, '//span[@class="ant-form-item-children"]/input'),
        "策划人员-同步人员名单": (By.XPATH, '//div/button[@type="button"]'),
        "策划人员-查询": (By.XPATH, '//div/button[@type="submit"]'),
        "策划人员-已启用": (By.XPATH, '//td/button[@aria-checked="true"]'),
        "策划人员-已禁用": (By.XPATH, '//td/button[@aria-checked="false"]'),
        # 启动或禁用该名片
        "策划人员-确定": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "策划人员-取消": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "策划人员-当前页面手机号列表数据": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[2]'),
        "策划人员-所属项目名称": (By.XPATH, '//table/tbody/tr/td[4][1]/button'),
        "策划人员-所属项目列表数据": (By.XPATH, '//table/tbody/tr/td[4]'),
        "策划人员-所属项目页面的列表": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[2]/div/div/div/div/div/div/table/tbody/tr/td'),
        "策划人员-关闭所属项目页面": (By.XPATH, '//button[@class="ant-drawer-close"]'),

        #经纪人团队
        "经纪人团队": (By.XPATH, '//div[@class=" ant-tabs-tab"][3]'),
        "经纪人团队-模糊查询": (By.XPATH, '//span[@class="ant-form-item-children"]/input'),
        "经纪人团队-同步人员名单": (By.XPATH, '//div/button[@type="button"]'),
        "经纪人团队-查询": (By.XPATH, '//div/button[@type="submit"]'),
        "经纪人团队-已启用": (By.XPATH, '//td/button[@aria-checked="true"]'),
        "经纪人团队-已禁用": (By.XPATH, '//td/button[@aria-checked="false"]'),
        # 启动或禁用该名片
        "经纪人团队-确定": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),
        "经纪人团队-取消": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn"]'),
        "经纪人团队-当前页面手机号列表数据": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[2]'),

        "错误提示-知道了": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),

        "共计总记录": (By.XPATH, "//span[@class='primary']"),
        "每页条数": (By.XPATH, "//div[@class='ant-select-sm ant-select ant-select-enabled']/div/div/div"),
        "上一页": (By.XPATH, "//li[@title='上一页']"),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input')

    }

    def __init__(self,driver):
        super(staffManagement, self).__init__(driver)

    def switch_to_tab(self,tab_name):
        self.refresh()
        if tab_name == '销售团队':
            self.wait_eleVisible(self.control['销售团队'])
            self.find_element(self.control['销售团队']).click()
        if tab_name == '行销团队':
            self.wait_eleVisible(self.control['行销团队'])
            self.find_element(self.control['行销团队']).click()
        if tab_name == '策划人员':
            self.wait_eleVisible(self.control['策划人员'])
            self.find_element(self.control['策划人员']).click()
        if tab_name == '经纪人团队':
            self.wait_eleVisible(self.control['经纪人团队'])
            self.find_element(self.control['经纪人团队']).click()
            sleep(2)
            self.inquiry(tab_name)
        sleep(2)

    # def select_project(self,modelName,project_Name,project_Type):
    #     # 选择或输入项目
    #
    #     if project_Name != '':
    #         self.wait_eleVisible(self.control[modelName+'-项目'])
    #         self.find_element(self.control[modelName+'-项目']).click()
    #         # 判断查询还是直接点击
    #         i = -1
    #         # 用于判定是否查询到有我们的判定值
    #         numFlag = False
    #         if project_Type == 'input':
    #             self.wait_eleVisible(self.control[modelName+'-请选择项目'])
    #             self.find_element(self.control[modelName+'-请选择项目']).send_keys(project_Name)
    #             sleep(1)
    #             elem = self.find_elements_list(self.control[modelName+'-项目下拉列表'])
    #             for e in elem:
    #                 i += 1
    #                 if fuzz.ratio(e.text, project_Name) > 0:
    #                     numFlag = True
    #                     break
    #         else:
    #             elem = self.find_elements_list(self.control[modelName+'-项目下拉列表'])
    #             for e in elem:
    #                 i += 1
    #                 if e.text == project_Name:
    #                     numFlag = True
    #                     break
    #         sleep(1)
    #         if numFlag:
    #             self.wait_eleVisible(self.control[modelName+'-项目下拉列表'])
    #             ele = self.find_elements(self.control[modelName+'-项目下拉列表'], i)
    #             ele.click()
    #         else:
    #             self.find_element(self.control['用户管理']).click()

    def get_list_model(self,modelName = None,check_mode_type = None):
        '''项目下拉列表，选择第一条项目数据'''
        str_data = "全部"
        if self.is_exist_element(self.control[modelName + '-项目下拉列表']):
            self.wait_eleVisible(self.control[modelName + '-项目下拉列表'])
            list = self.find_elements_list(self.control[modelName + '-项目下拉列表'])
            if len(list) == 0:
                str_data = "全部"
                # return str_data
            elif (check_mode_type == '1') & (len(list) != 0):
                str_data = list[0].text
                # print("str_data:"+str_data)
            elif (check_mode_type == '2') & (len(list) != 0):
                str_data = list[0].text[0:1]
            else:
                str_data = "全部"
                # return str_data
        return str_data

    def get_list_phone(self, modelName=None,check_phone_type=None):
        '''手机号列表，选择第一条手机号数据'''
        str_data = "18816851537"
        if self.is_exist_element(self.control[modelName+'-当前页面手机号列表数据']):
            self.wait_eleVisible(self.control[modelName+'-当前页面手机号列表数据'])
            list = self.find_elements_list(self.control[modelName+'-当前页面手机号列表数据'])
            if len(list) == 0:
                str_data = "18816851537"
            if (check_phone_type == '1') & (len(list) != 0):
                str_data = list[0].text
                # print("str_data:"+str_data)
            elif (check_phone_type != '1') & (len(list) != 0):
                str_data = list[0].text[0:6]
        return str_data

    def select_project(self, modelName,project_Name, project_Type,check_mode_type):
        '''选择或输入项目'''
        self.wait_eleVisible(self.control[modelName + '-项目'])
        self.find_element(self.control[modelName + '-项目']).click()
        project_Name = self.get_list_model(modelName, check_mode_type)
        if project_Name == "全部":
            self.wait_eleVisible(self.control[modelName + '-请选择项目'])
            self.find_element(self.control[modelName + '-请选择项目']).send_keys(project_Name)
            sleep(1)
            self.wait_eleVisible(self.control[modelName + '-项目下拉列表-全部'])
            self.find_element(self.control[modelName + '-项目下拉列表-全部']).click()
        else:
            #判断查询还是直接点击
            i = -1
            # 用于判定是否查询到有我们的判定值
            numFlag = False
            if project_Type == 'input':
                self.wait_eleVisible(self.control[modelName + '-请选择项目'])
                self.find_element(self.control[modelName + '-请选择项目']).send_keys(project_Name)
                sleep(1)
                elem = self.find_elements_list(self.control[modelName + '-项目下拉列表'])
                for e in elem:
                    i += 1
                    if fuzz.ratio(e.text, project_Name) > 0:
                        numFlag = True
                        break
            else:
                elem = self.find_elements_list(self.control[modelName + '-项目下拉列表'])
                for e in elem:
                    i += 1
                    if e.text == project_Name:
                        numFlag = True
                        break
            sleep(1)
            if numFlag:
                self.wait_eleVisible(self.control[modelName + '-项目下拉列表'])
                ele = self.find_elements(self.control[modelName + '-项目下拉列表'], i)
                ele.click()
            else:
                self.find_element(self.control['用户管理']).click()

    def  error_message_prompt(self):
        '''错误提示：failed to connect to all addresses'''
        if self.is_exist_element(self.control['错误提示-知道了']):
            self.find_element(self.control['错误提示-知道了']).click()

    def enable_of_disable_card(self,modelName):
        '''判断该员工的卡片是启用还是禁用,弹窗选择确定'''
        if self.is_exist_element(self.control[modelName+'-已启用']):
            self.find_elements(self.control[modelName+'-已启用'],0).click()
            self.wait_eleVisible(self.control[modelName+'-确定'])
            self.find_element(self.control[modelName+'-确定']).click()
            sleep(3)
            self.find_elements(self.control[modelName + '-已禁用'], 0).click()
            self.wait_eleVisible(self.control[modelName + '-确定'])
            self.find_element(self.control[modelName + '-确定']).click()
            sleep(2)
        else:
            if self.is_exist_element(self.control[modelName+'-已禁用']):
                self.find_elements(self.control[modelName+'-已禁用'],0).click()
                self.wait_eleVisible(self.control[modelName+'-确定'])
                self.find_element(self.control[modelName+'-确定']).click()
                sleep(3)
                self.find_elements(self.control[modelName + '-已启用'], 0).click()
                self.wait_eleVisible(self.control[modelName + '-确定'])
                self.find_element(self.control[modelName + '-确定']).click()
                sleep(2)

    def cancel_enable_of_disable_card(self,modelName):
        '''判断该员工的卡片是启用还是禁用，弹窗选择取消'''
        if self.is_exist_element(self.control[modelName+'-已启用']):
            self.find_elements(self.control[modelName+'-已启用'],0).click()
            self.wait_eleVisible(self.control[modelName+'-取消'])
            self.find_element(self.control[modelName+'-取消']).click()
            sleep(3)
            # self.find_elements(self.control[modelName + '-已禁用'], 0).click()
            # self.wait_eleVisible(self.control[modelName + '-取消'])
            # self.find_element(self.control[modelName + '-取消']).click()
            # sleep(2)
        else:
            if self.is_exist_element(self.control[modelName+'-已禁用']) :
                self.find_elements(self.control[modelName + '-已禁用'], 0).click()
                self.wait_eleVisible(self.control[modelName + '-取消'])
                self.find_element(self.control[modelName + '-取消']).click()
                sleep(3)
                # self.find_elements(self.control[modelName + '-已启用'], 0).click()
                # self.wait_eleVisible(self.control[modelName + '-取消'])
                # self.find_element(self.control[modelName + '-取消']).click()
                # sleep(2)


    def input_name_or_phone(self,modelName,check_phone_type):
        '''模糊查询：输入姓名或手机号搜索'''
        self.wait_eleVisible(self.control[modelName+'-模糊查询'])
        self.find_element(self.control[modelName+'-模糊查询']).click()
        self.find_element(self.control[modelName+'-模糊查询']).send_keys(self.get_list_phone(modelName,check_phone_type))

    def inquiry(self,modelName):
        '''点击查询按钮'''
        self.wait_eleVisible(self.control[modelName+'-查询'])
        self.find_element(self.control[modelName+'-查询']).click()

    def synchronization_personnel_list(self,modelName):
        '''同步人员名单'''
        self.wait_eleVisible(self.control[modelName+'-同步人员名单'])
        self.find_element(self.control[modelName+'-同步人员名单']).click()
        sleep(3)

    def contrast_list_data(self,modelName,checkData):
        '''判断查询的值是否在列表'''
        flag = False
        typeBolle = True
        while(typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.control[modelName+'-当前页面手机号列表数据'])
            for b in bodyContent:
                b.click()
                if b.text == checkData['expectData'] :
                    flag = True
                    break
            sleep(1)
            typeBolle = self.check_next_clickable()
            if typeBolle:
                '''点击下一页'''
                self.find_element(self.control['下一页']).click()
        self.check_assert(checkData['flag'],flag,checkData['msg'])
        return  flag

    def check_assert(self,checkflag,flag,message):
        '''断言封装'''
        if checkflag == 'True':
            self.assertTrue(flag,msg= message)
        else:
            self.assertFalse(flag,msg= message)


    def staff_management_inquiry(self,modelName,parameter = None):
        '''销售团队/行销团队/策划团队查询'''
        # 选择或输入项目
        if parameter['check_model_type'] != "":
            self.select_project(modelName,parameter['project_Name'],parameter['project_Type'],parameter['check_model_type'])
        sleep(3)
        #模糊查询输入姓名或手机号
        if parameter['check_phone_type'] != "":
            self.input_name_or_phone(modelName,parameter['check_phone_type'])
        sleep(3)
        #点击查询
        self.inquiry(modelName)
        sleep(3)

    # def broker_team_inquiry(self,modelName,parameter = None):
    #     '''经纪人团队查询'''
    #     # 模糊查询输入姓名或手机号
    #     if parameter['name_or_phone'] != '':
    #         sleep(1)
    #         self.input_name_or_phone(modelName,parameter['name_or_phone'])
    #     sleep(2)
    #     # 点击查询
    #     self.inquiry(modelName)

    def broker_team_inquiry(self,modelName,parameter = None):
        '''经纪人团队查询'''
        # 模糊查询输入姓名或手机号
        if len(parameter['check_phone_type']) != 0:
            self.input_name_or_phone(modelName, parameter['check_phone_type'])
        sleep(2)
        # 点击查询
        self.inquiry(modelName)
        sleep(3)

    # def sales_team_inquiry(self,parameter = None):
    #     '''销售团队查询'''
    #     # 选择或输入项目
    #     self.select_project(parameter['project_Name'],parameter['project_Type'])
    #     sleep(2)
    #     #模糊查询输入姓名或手机号
    #     if parameter['name_or_phone'] != '':
    #         sleep(1)
    #         self.input_name_or_phone(parameter['name_or_phone'])
    #     sleep(2)
    #     #点击查询
    #     self.inquiry()
    #
    # def marketing_team_inquiry(self,parameter = None):
    #     '''行销团队查询'''
    #     # 选择或输入项目
    #     self.select_project(parameter['project_Name'], parameter['project_Type'])
    #     sleep(2)
    #     # 模糊查询输入姓名或手机号
    #     if parameter['name_or_phone'] != '':
    #         sleep(1)
    #         self.input_name_or_phone(parameter['name_or_phone'])
    #     sleep(2)
    #     # 点击查询
    #     self.inquiry()
    #
    # def planning_team_inquiry(self,parameter = None):
    #     '''策划人员查询'''
    #     # 选择或输入项目
    #     self.select_project(parameter['project_Name'], parameter['project_Type'])
    #     sleep(2)
    #     # 模糊查询输入姓名或手机号
    #     if parameter['name_or_phone'] != '':
    #         sleep(1)
    #         self.input_name_or_phone(parameter['name_or_phone'])
    #     sleep(2)
    #     # 点击查询
    #     self.inquiry()

    def open_project_page(self,modelName):
        '''销售团队/策划人员团队：打开所属项目页面'''
        self.error_message_prompt()
        sleep(2)
        l = self.find_elements_list(self.control[modelName + '-所属项目名称'])
        if len(l) != 0:
            strValue = self.find_elements(self.control[modelName + '-所属项目名称'], 0).text
            listValue = strValue.split('，')
            sleep(2)
            self.find_elements(self.control[modelName + '-所属项目名称'], 0).click()
            sleep(2)
        list = self.find_elements_list(self.control[modelName + '-所属项目页面的列表'])
        if len(list) != 0:
            project_name = self.find_elements(self.control[modelName + '-所属项目页面的列表'], 0).text
            sleep(2)
            self.assertIn(str(project_name), strValue, msg='所属项目页面没有找到项目名称')
            sleep(2)
            self.wait_eleVisible(self.control[modelName + '-关闭所属项目页面'])
            self.find_element(self.control[modelName + '-关闭所属项目页面']).click()

    def marketing_team_open_project_page(self):
        '''行销团队：打开所属项目页面'''
        self.error_message_prompt()
        sleep(2)
        l = self.find_elements_list(self.control['行销团队-所属项目名称'])
        if len(l) != 0:
            strValue = self.find_elements(self.control['行销团队-所属项目名称'], 0).text
            listValue = strValue.split('，')
            sleep(2)
            self.find_elements(self.control['行销团队-所属项目名称'], 0).click()
            sleep(2)
        list = self.find_elements_list(self.control['行销团队-所属项目页面的列表'])
        if len(list) != 0:
            project_name = self.find_elements(self.control['行销团队-所属项目页面的列表'], 0).text
            sleep(2)
            self.assertIn(str(project_name), strValue, msg='所属项目页面没有找到项目名称')
            sleep(2)
            self.wait_eleVisible(self.control['行销团队-关闭所属项目页面'])
            self.find_element(self.control['行销团队-关闭所属项目页面']).click()
        
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
                self.wait_eleVisible(self.control['跳转至第几页'])
                self.find_element(self.control['跳转至第几页']).send_keys(page + 1)
                sleep(2)
                self.find_element(self.control['共计总记录']).click()
                #self.send_keys("{ENTER}")
                sleep(2)
                while(self.is_exist_element(self.control['获取可点击的上一页'])):
                    sleep(1)
                    self.find_element(self.control['上一页']).click()