#-*- coding:utf-8 -*-

from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from myweb.core.runner import TestCase
from selenium.webdriver.common.action_chains import ActionChains

from myweb.core.BasePage import BasePage

class clientStandingBook(BasePage,TestCase):
    control =  {
        "用户管理目录": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/ul/li[6]/div/span'),
        #集团客户
        "选择集团客户": (By.XPATH, "//div[@class='components-manager_customer-tabs-index-module_1TcjH']/a[1]/div"),
        "集团客户-客户电话": (By.XPATH, "//span/input[@class='ant-input']"),
        '集团客户-移动到日期选择框': (By.XPATH, '//span[@class="ant-calendar-picker-input ant-input"]'),
        '集团客户-日期删除按钮': (By.XPATH, '//i[@aria-label="图标: close-circle"]'),
        "集团客户-注册时间段-开始时间": (By.XPATH, "//span/input[1][@class='ant-calendar-range-picker-input']"),
        "集团客户-注册时间段-开始时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-left"]/div/div/input[@placeholder = "开始时间"]'),
        "集团客户-注册时间段-结束时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-right"]/div/div/input[@placeholder = "结束时间"]'),
        "集团客户-用户意向点击":(By.XPATH,'//div[@class="ant-select-selection__placeholder"]'),
        "集团客户-用户意向选择":(By.XPATH,'//ul[@role="listbox"]/li'),
        "集团客户-用户意向删除":(By.XPATH,'//span[@class="ant-select-selection__clear"]'),
        "集团客户-查询": (By.XPATH, "//button[@class='ant-btn ml5 ant-btn-primary']"),
        "集团客户-点击业务关系表": (By.XPATH, '//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[1]/button'),
        "集团客户-业务关系表列表": (By.XPATH,'//tbody[@class="ant-table-tbody"]/tr[@class="ant-table-row ant-table-row-level-0"]/td[@style="text-align: center;"]'),
        "集团客户-关闭业务关系表": (By.XPATH, "//button[@class='ant-modal-close']"),
        "集团客户-查看来去拓扑图": (By.XPATH, "//div[@class = 'ant-table-fixed-right']/div/div/table/tbody/tr/td[2]/button"),
        "集团客户-关闭来去拓扑图": (By.XPATH, '//span[@class="ant-modal-close-x"]/i'),
        "集团客户-来去拓扑图页面": (By.XPATH, "//div[text()='来去拓扑图']"),
        "集团客户-查看用户意向":(By.XPATH,'//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[3]/button'),
        "集团客户-关闭用户意向":(By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/button/span/i'),
        "集团客户-查看用户意向页面":(By.XPATH,"//div[text()='用户意向标签']"),
        "集团客户-导出列表": (By.XPATH, "//div[@class='right']/button[@class = 'ant-btn ant-btn-primary']"),
        "集团客户-导出": (By.XPATH, "//div[@class='tc']/button"),
        "集团客户-下载":(By.XPATH,'//button[@class="ant-btn ant-btn-link"]'),
        "业务关系表":(By.XPATH,'//div[@class="ant-modal-title"]'),
        "来去拓扑图":(By.XPATH,'//div[@class="ant-modal-title"]'),
        # 区域客户
        "选择区域客户": (By.XPATH, "//div[@class='components-manager_customer-tabs-index-module_1TcjH']/a[2]/div"),
        "区域客户-客户电话": (By.XPATH, "//span/input[@class='ant-input']"),
        "区域名称": (By.XPATH, "//div[@class='w-350 ant-select ant-select-enabled']"),
        "区域名称下拉列表": (By.XPATH, "//ul[@role='listbox']/li/ul/li"),
        '区域客户-移动到日期选择框': (By.XPATH, '//span[@class="ant-calendar-picker-input ant-input"]'),
        '区域客户-日期删除按钮': (By.XPATH, '//i[@aria-label="图标: close-circle"]'),
        "区域客户-注册时间段-开始时间": (By.XPATH, "//span/input[1][@class='ant-calendar-range-picker-input']"),
        "区域客户-注册时间段-开始时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-left"]/div/div/input[@placeholder = "开始时间"]'),
        "区域客户-注册时间段-结束时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-right"]/div/div/input[@placeholder = "结束时间"]'),
        "区域客户-用户意向点击": (By.XPATH, '//div[@class="ant-select ant-select-enabled ant-select-allow-clear"]/div/div/div[@class="ant-select-selection__placeholder"]'),
        "区域客户-用户意向选择": (By.XPATH, '//ul[@role="listbox"]/li[@role="option"]'),
        "区域客户-用户意向删除": (By.XPATH, '//span[@class="ant-select-selection__clear"]'),
        "区域客户-查询": (By.XPATH, "//button[@class='ant-btn ml5 ant-btn-primary']"),
        "区域客户-点击业务关系表": (By.XPATH,'//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[1]/button'),
        "区域客户-业务关系表列表": (By.XPATH,'//tbody[@class="ant-table-tbody"]/tr[@class="ant-table-row ant-table-row-level-0"]/td[@style="text-align: center;"]'),
        "区域客户-关闭业务关系表": (By.XPATH, "//button[@class='ant-modal-close']"),
        "区域客户-查看来去拓扑图": (By.XPATH, "//div[@class = 'ant-table-fixed-right']/div/div/table/tbody/tr/td[2]/button"),
        "区域客户-关闭来去拓扑图": (By.XPATH, '//div[@class="ant-modal-content"]/button/span/i'),
        "区域客户-来去拓扑图页面": (By.XPATH, "//div[text()='来去拓扑图']"),
        "区域客户-查看用户意向": (By.XPATH, '//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[3]/button'),
        "区域客户-关闭用户意向": (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/button/span/i'),
        "区域客户-查看用户意向页面": (By.XPATH, "//div[text()='用户意向标签']"),
        "区域客户-导出列表": (By.XPATH, "//div[@class='right']/button[@class = 'ant-btn ant-btn-primary']"),
        "区域客户-导出": (By.XPATH, "//div[@class='tc']/button"),
        "区域客户-下载":(By.XPATH,'//button[@class="ant-btn ant-btn-link"]'),
        # 项目客户
        "选择项目客户": (By.XPATH, "//div[@class='components-manager_customer-tabs-index-module_1TcjH']/a[3]"),
        "项目客户-客户电话": (By.XPATH, "//span/input[@class='ant-input']"),
        "项目客户-项目名称": (By.XPATH, '//div[@class="mt20 flex-align-center"]/div/div'),
        #项目名称下拉列表输入查询
        "项目客户-项目名称查询": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_3Qmax"]/div/input'),
        '项目客户-项目名称下拉列表': (By.XPATH, '//div[@class="components-common-SelectTree-index-module_1R0Lp  "]'),
        '项目客户-移动到日期选择框': (By.XPATH, '//span[@class="ant-calendar-picker-input ant-input"]'),
        '项目客户-日期删除按钮': (By.XPATH, '//i[@aria-label="图标: close-circle"]'),
        "项目客户-注册时间段-开始时间": (By.XPATH, "//span/input[1][@class='ant-calendar-range-picker-input']"),
        "项目客户-注册时间段-开始时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-left"]/div/div/input[@placeholder = "开始时间"]'),
        "项目客户-注册时间段-结束时间输入框": (By.XPATH,'//div[@class = "ant-calendar-range-part ant-calendar-range-right"]/div/div/input[@placeholder = "结束时间"]'),
        "项目客户-用户意向点击": (By.XPATH,'//div[@class="ant-select ant-select-enabled ant-select-allow-clear"]/div/div/div[@class="ant-select-selection__placeholder"]'),
        "项目客户-用户意向选择": (By.XPATH, '//ul[@role="listbox"]/li'),
        "项目客户-用户意向删除": (By.XPATH, '//span[@class="ant-select-selection__clear"]'),
        "项目客户-查询": (By.XPATH, "//button[@class='ant-btn ml5 ant-btn-primary']"),

        "项目客户-点击业务关系表": (By.XPATH, '//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[1]/button'),
        "项目客户-业务关系表列表": (By.XPATH,'//tbody[@class="ant-table-tbody"]/tr[@class="ant-table-row ant-table-row-level-0"]/td[@style="text-align: center;"]'),
        "项目客户-关闭业务关系表": (By.XPATH, "//button[@class='ant-modal-close']"),
        "项目客户-查看来去拓扑图": (By.XPATH, "//div[@class = 'ant-table-fixed-right']/div/div/table/tbody/tr/td[2]/button"),
        "项目客户-关闭来去拓扑图": (By.XPATH, '//div[@class="ant-modal-content"]/button/span/i'),
        "项目客户-来去拓扑图页面": (By.XPATH, "//div[text()='来去拓扑图']"),
        "项目客户-查看用户意向": (By.XPATH, '//div[@class = "ant-table-fixed-right"]/div/div/table/tbody/tr/td[3]/button'),
        "项目客户-关闭用户意向": (By.XPATH, '/html/body/div[5]/div/div[2]/div/div[2]/button/span/i'),
        "项目客户-查看用户意向页面": (By.XPATH, "//div[text()='用户意向标签']"),

        "项目客户-导出列表": (By.XPATH, "//div[@class='right']/button[@class = 'ant-btn ant-btn-primary']"),
        "项目客户-导出": (By.XPATH, "//div[@class='tc']/button"),
        "项目客户-导出状态": (By.XPATH, "//div[@class='ant-table-content']/div[@class='ant-table-body']/table/tbody/tr[1]/td[4]/div"),
        "导出状态-创建时间": (By.XPATH, "//div[@class='ant-table-content']/div[@class='ant-table-body']/table/tbody/tr[1]/td[2]/div"),
        #"项目客户-下载": (By.XPATH, "//tbody/tr[1]/td[6]/span/a"),
        "项目客户-下载":(By.XPATH,'//button[@class="ant-btn ant-btn-link"]'),
        #"项目客户-下载": (By.XPATH, '//button/span[text()="下载"]'),
        "项目客户-导出页面关闭": (By.XPATH, "//button[@class='ant-modal-close']/span"),

        #预约客户
        "选择预约客户": (By.XPATH, "//div[@class='components-manager_customer-tabs-index-module_1TcjH']/a[4]/div"),
        "预约客户-项目名称": (By.XPATH, '//div[@class="ant-form-item-control has-success"]/span/div'),
        # 项目名称下拉列表输入查询
        "预约客户-输入项目点击":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "预约客户-输入项目名称":(By.XPATH,'//div[@class="components-common-SelectTree-index-module_21xSF"]/input'),
        "预约客户-项目名称下拉列表": (By.XPATH, "//div[@class='components-common-SelectTree-index-module_1R0Lp  ']"),
        "预约客户-查询客户/电话-选择按钮": (By.XPATH, '//span[@class="ant-input-group-addon"]/div/div'),
        "预约客户-客户姓名":(By.XPATH,'//li[@title="客户姓名"]'),
        "预约客户-客户手机":(By.XPATH,'//li[@title="客户手机"]'),
        "预约客户-客户姓名/客户手机": (By.XPATH, "//span/input[@class='ant-input']"),
        #列表
        '预约客户-移动到日期选择框': (By.XPATH, '//span[@class="ant-calendar-picker-input ant-input"]'),
        #列表
        '预约客户-日期删除按钮': (By.XPATH,'//i[@aria-label="图标: close-circle"]'),
        "预约客户-看房时间-开始时间": (By.XPATH, '//*[@id="look_house_times"]/span/input[1]'),
        "预约客户-看房时间-开始时间输入框": (By.XPATH,'//input[@class="ant-calendar-input " and @placeholder="开始时间" ]'),
        "预约客户-看房时间-结束时间输入框": (By.XPATH,'//input[@class="ant-calendar-input " and @placeholder="结束时间" ]'),
        "预约客户-预约时间-开始时间": (By.XPATH, "//span[@id='appoint_times']/span/input[1]"),
        "预约客户-预约时间-开始时间输入框": (By.XPATH, '//input[@class="ant-calendar-input " and @placeholder="开始时间" ]'),
        "预约客户-预约时间-结束时间输入框": (By.XPATH, '//input[@class="ant-calendar-input " and @placeholder="结束时间" ]'),
        "预约客户-查询": (By.XPATH, "//button[@type='submit']"),
        "预约客户-导出": (By.XPATH, "//div[@class='right']/button[@class = 'ant-btn ant-btn-primary']"),
        "预约客户-查看详情": (By.XPATH, "//tbody/tr/td[8]/button"),
        "预约客户-判断预约客户明细": (By.XPATH, '//div[@class="ant-drawer-title"]'),
        "关闭预约客户明细页面": (By.XPATH, "//button[@aria-label='Close']"),
        "预约客户-共计总记录":(By.XPATH,'//li[@class="ant-pagination-total-text"]/div/span'),
        "预约客户-导出列表": (By.XPATH, "//div[@class='right']/button[@class = 'ant-btn ant-btn-primary']"),

        "错误提示-知道了": (By.XPATH, "//div[@class='ant-modal-confirm-btns']/button"),

        #手机号列表的数据
        "当前页面列表数据": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr/td[3]/div'),
        #姓名列表的数据
        "当前页面姓名列表数据": (By.XPATH, '//table/tbody/tr/td[2]'),


        "共计总记录":(By.XPATH,"//span[@class='primary']"),
        "每页条数": (By.XPATH, "//div[@class='ant-select-sm ant-select ant-select-enabled']/div/div/div"),
        "上一页":(By.XPATH,"//li[@title='上一页']"),
        "下一页":(By.XPATH,'//li[@title="下一页"]'),
        "获取可点击的下一页":(By.XPATH,'//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页":(By.XPATH,'//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input')
    }
    def __init__(self,driver):
        super(clientStandingBook, self).__init__(driver)

    #项目客户-项目名称选择第一个
    def get_list_project(self, check_project_type=None):
        str_data = "1"
        if self.is_exist_element(self.control['项目客户-项目名称下拉列表']):
            self.wait_eleVisible(self.control['项目客户-项目名称下拉列表'])
            list = self.find_elements_list(self.control['项目客户-项目名称下拉列表'])
            if len(list) == 0:
                self.refresh()
            if (check_project_type == '1') & (len(list) != 0):
                str_data = list[0].text
            else:
                str_data = list[0].text[0:1]
        return str_data

    #预约看房-项目名称选择第一个
    def get_booking_customer_list_project(self, check_project_type=None):
          str_data = ""
          if self.is_exist_element(self.control['预约客户-项目名称下拉列表']) :
              self.wait_eleVisible(self.control['预约客户-项目名称下拉列表'])
              list = self.find_elements_list(self.control['预约客户-项目名称下拉列表'])
              if len(list) == 0:
                    self.refresh()
                    sleep(2)
              if (check_project_type == '1') & (len(list) != 0):
                    str_data = list[1].text
              else:
                    str_data = list[1].text[0:1]
              print("str_date:",str_data)
              return str_data


    # 区域名称选择第一个
    def get_list_regional(self, check_regional_type=None):
        str_data = ""
        self.wait_eleVisible(self.control['区域名称下拉列表'])
        list = self.find_elements_list(self.control['区域名称下拉列表'])
        if len(list) == 0:
            str_data = "全部"
            return str_data
        if (check_regional_type == '1') & (len(list) != 0):
            str_data = list[0].text
            # print("str_data:"+str_data)
        else:
            str_data = list[0].text[0:1]
        return str_data

    # 电话列表选择第一个
    def get_list_phone(self, check_phone_type=None):
        str_data = ""
        #self.wait_eleVisible(self.control['当前页面列表数据'])
        sleep(2)
        list = self.find_elements_list(self.control['当前页面列表数据'])
        if len(list) == 0:
            str_data = "18816851537"
            return str_data

        if (check_phone_type == '1') & (len(list) != 0):
            str_data = list[0].text
            if  str_data == "":
                for i in range(1,len(list)):
                    str_data = list[i].text
                    if str_data != "":
                        break
            # print("str_data:"+str_data)
        elif (check_phone_type != '1') & (len(list) != 0):
            str_data = list[0].text[0:6]
            if  str_data == "":
                for i in range(1,len(list)):
                    str_data = list[i].text[0:6]
                    if str_data != "":
                        break
        return str_data

    # 姓名列表选择第一个
    def get_list_name(self, check_name_type=None):
        str_data = ""
#        self.wait_eleVisible(self.control['当前页面姓名列表数据'])
        sleep(2)
        list = self.find_elements_list(self.control['当前页面姓名列表数据'])
        if len(list) == 0:
            str_data = "云"
            return str_data
        if (check_name_type == '1') & (len(list) != 0):
            str_data = list[0].text
            if str_data == "":
                for i in range(1, len(list)):
                    str_data = list[i].text
                    if str_data != "":
                        break
            # print("str_data:"+str_data)
        elif (check_name_type != '1') & (len(list) != 0):
            str_data = list[0].text[0:1]
            if str_data == "":
                for i in range(1, len(list)):
                    str_data = list[i].text[0:6]
                    if str_data != "":
                        break
        return str_data

    # def group_customer_inquiry(self,parameter = None):
    #     '''集团客户--查询'''
    #     #输入电话号码
    #     if  parameter['phone'] != '':
    #         sleep(1)
    #         self.input_phone(parameter['phone'],'集团客户-')
    #     #输入注册时间段
    #     sleep(1)
    #     if parameter['startDate'] != '':
    #         self.input_registration_date(parameter['startDate'],parameter['endDate'],'集团客户-')
    #     print('userIntent:',parameter['userIntent'])
    #     self.user_intent(parameter['userIntent'],'集团客户-用户意向点击','集团客户-用户意向选择','集团客户-用户意向删除')
    #
    #     #点击查询
    #     sleep(1)
    #     self.inquire('集团客户-')
    #     sleep(1)

    def group_customer_inquiry(self,parameter = None,checkData = None):
        '''集团客户--查询'''
        #输入电话号码
        if  parameter['phone'] != '':
            sleep(1)
            phone = self.get_list_phone(parameter['check_phone_type'])
            self.input_phone(phone,'集团客户-')
        #输入注册时间段
        sleep(1)
        if parameter['startDate'] != '':
            self.input_registration_date(parameter['startDate'],parameter['endDate'],'集团客户-')
        # print('userIntent:',parameter['userIntent'])
        self.user_intent(parameter['userIntent'],'集团客户-用户意向点击','集团客户-用户意向选择','集团客户-用户意向删除')
        #点击查询
        self.inquire('集团客户-')
        sleep(3)
        self.contrast_list_data(checkData,phone)


    # def regional_customer_inquiry(self, parameter=None):
    #     '''区域客户--查询'''
    #     # 输入电话号码
    #     if parameter['phone'] != '':
    #         sleep(1)
    #         self.input_phone(parameter['phone'],'区域客户-')
    #     #选择区域名称
    #     if parameter['region_Name'] != '':
    #         self.wait_eleVisible(self.control['区域名称'])
    #         self.find_element(self.control['区域名称']).click()
    #         sleep(1)
    #         elem = self.find_elements_list(self.control['区域名称下拉列表'])
    #         i = 0
    #         for e in elem:
    #             if e.text == parameter['region_Name']:
    #                 break
    #             i += 1
    #         sleep(1)
    #         if i != len(elem):
    #             ele = self.find_elements(self.control['区域名称下拉列表'], i)
    #             ele.click()
    #         else:
    #             ele = self.find_elements(self.control['区域名称下拉列表'], 0)
    #             ele.click()
    #         sleep(2)
    #     # 输入注册时间段
    #     sleep(1)
    #     if parameter['startDate'] != '':
    #         self.input_registration_date(parameter['startDate'], parameter['endDate'],'区域客户-')
    #     ##选择用户意向
    #
    #     # 点击查询
    #     sleep(1)
    #     self.inquire('区域客户-')
    #     sleep(1)

    def regional_customer_inquiry(self, parameter=None,checkData = None):
        '''区域客户--查询'''
        # 输入电话号码
        if parameter['phone'] != '':
            sleep(1)
            phone = self.get_list_phone(parameter['check_phone_type'])
            self.input_phone(phone,'区域客户-')
        #选择区域名称
        if parameter['region_Name'] != '':
            self.wait_eleVisible(self.control['区域名称'])
            self.find_element(self.control['区域名称']).click()
            sleep(1)
            elem = self.find_elements_list(self.control['区域名称下拉列表'])
            i = 0
            region_Name = self.get_list_regional(parameter['check_regional_type'])
            for e in elem:
                if e.text == region_Name:
                    break
                i += 1
            sleep(1)
            if i != len(elem):
                ele = self.find_elements(self.control['区域名称下拉列表'], i)
                ele.click()
            else:
                ele = self.find_elements(self.control['区域名称下拉列表'], 0)
                ele.click()
            sleep(2)
        # 输入注册时间段
        sleep(1)
        if parameter['startDate'] != '':
            self.input_registration_date(parameter['startDate'], parameter['endDate'],'区域客户-')
        ##选择用户意向
        self.user_intent(parameter['userIntent'], '区域客户-用户意向点击', '区域客户-用户意向选择', '区域客户-用户意向删除')
        # 点击查询
        self.inquire('区域客户-')
        sleep(3)
        self.contrast_list_data(checkData,phone)

    # def project_customer_inquiry(self, parameter=None):
    #     '''项目客户-查询'''
    #     # 输入电话号码
    #     if parameter['phone'] != '':
    #         sleep(1)
    #         phone = self.get_list_phone(parameter['check_phone_type'])
    #         self.input_phone(phone,'项目客户-')
    #     #输入项目名称
    #     if parameter['project_Name'] != '':
    #         self.wait_eleVisible(self.control['项目客户-项目名称'])
    #         self.find_element(self.control['项目客户-项目名称']).click()
    #         #判断查询还是直接点击
    #         i = -1
    #         #用于判定是否查询到有我们的判定值
    #         numFalg = False
    #         # 判断查询还是直接点击
    #         if parameter['project_Type'] == 'input':
    #             #标记是否查询到数据
    #             self.wait_eleVisible(self.control['项目客户-项目名称查询'])
    #             self.find_element(self.control['项目客户-项目名称查询']).send_keys(parameter['project_Name'])
    #             sleep(1)
    #             elem = self.find_elements_list(self.control['项目客户-项目名称下拉列表'])
    #             project_Name = self.get_list_project(parameter['check_project_type'])
    #             for e in elem:
    #                 i += 1
    #                 if fuzz.ratio(e.text,project_Name) > 0 :
    #                     numFalg = True
    #                     break
    #         else:
    #             elem = self.find_elements_list(self.control['项目客户-项目名称下拉列表'])
    #             project_Name = self.get_list_project(parameter['check_project_type'])
    #             for e in elem:
    #                 i += 1
    #                 if e.text == project_Name:
    #                     numFalg = True
    #                     break
    #         sleep(1)
    #         if numFalg :
    #             self.wait_eleVisible(self.control['项目客户-项目名称下拉列表'])
    #             ele = self.find_elements(self.control['项目客户-项目名称下拉列表'], i)
    #             ele.click()
    #         else:
    #             self.find_element(self.control['用户管理目录']).click()
    #         sleep(2)
    #     # 输入注册时间段
    #     sleep(1)
    #     if parameter['startDate'] != '':
    #         self.input_registration_date(parameter['startDate'], parameter['endDate'],'项目客户-')
    #     # 选择用户意向
    #     self.user_intent(parameter['userIntent'], '项目客户-用户意向点击', '项目客户-用户意向选择', '项目客户-用户意向删除')
    #
    #     # 点击查询
    #     sleep(1)
    #     self.inquire('项目客户-')
    #     sleep(1)

    def project_customer_inquiry(self, parameter=None,checkData = None):
        '''项目客户-查询'''
        # 输入电话号码
        if parameter['phone'] != '':
            phone = self.get_list_phone(parameter['check_phone_type'])
            self.input_phone(phone,'项目客户-')
        #输入项目名称
        if parameter['project_Name'] != '':
            self.wait_eleVisible(self.control['项目客户-项目名称'])
            self.find_element(self.control['项目客户-项目名称']).click()
            project_Name = self.get_list_project(parameter['check_project_type'])
            #判断查询还是直接点击
            i = -1
            #用于判定是否查询到有我们的判定值
            numFalg = False
            # 判断查询还是直接点击
            if parameter['project_Type'] == 'input':
                #标记是否查询到数据
                self.wait_eleVisible(self.control['项目客户-项目名称查询'])
                self.find_element(self.control['项目客户-项目名称查询']).send_keys(project_Name)
                sleep(1)
                elem = self.find_elements_list(self.control['项目客户-项目名称下拉列表'])
                for e in elem:
                    i += 1
                    if fuzz.ratio(e.text,project_Name) > 0 :
                        numFalg = True
                        break
            else:
                elem = self.find_elements_list(self.control['项目客户-项目名称下拉列表'])
                for e in elem:
                    i += 1
                    if e.text == project_Name:
                        numFalg = True
                        break
            sleep(1)
            if numFalg :
                self.wait_eleVisible(self.control['项目客户-项目名称下拉列表'])
                ele = self.find_elements(self.control['项目客户-项目名称下拉列表'], i)
                ele.click()
            else:
                self.find_element(self.control['用户管理目录']).click()
            sleep(2)
        # 输入注册时间段
        sleep(1)
        if parameter['startDate'] != '':
            self.input_registration_date(parameter['startDate'], parameter['endDate'],'项目客户-')
        # 选择用户意向
        self.user_intent(parameter['userIntent'], '项目客户-用户意向点击', '项目客户-用户意向选择', '项目客户-用户意向删除')
        # 点击查询
        self.inquire('项目客户-')
        sleep(3)
        self.contrast_list_data(checkData,phone)

    # def booking_customer_inquiry(self, parameter=None):
    #     '''预约客户-查询'''
    #     sleep(1)
    #     i = 0
    #     #选择项目名称
    #     if parameter['project_Name'] != '':
    #         self.wait_eleVisible(self.control['预约客户-项目名称'])
    #         self.find_element(self.control['预约客户-项目名称']).click()
    #         #用于判定是否查询到有我们的判定值
    #         numFalg = False
    #         # 判断查询还是直接点击
    #         if parameter['project_Type'] == 'input':
    #             #标记是否查询到数据
    #             self.wait_eleVisible(self.control['预约客户-项目名称'])
    #             self.find_element(self.control['预约客户-输入项目名称']).send_keys(parameter['project_Name'])
    #             sleep(2)
    #             self.find_element(self.control['预约客户-项目名称']).click()
    #             elem = self.find_elements_list(self.control['预约客户-项目名称下拉列表'])
    #             project_Name = self.get_list_project(parameter['check_project_type'])
    #             for e in elem:
    #                 if fuzz.ratio(e.text,project_Name) > 0 :
    #                     numFalg = True
    #                     break
    #                 i += 1
    #
    #         else:
    #             sleep(1)
    #             elem = self.find_elements_list(self.control['预约客户-项目名称下拉列表'])
    #             project_Name = self.get_list_project(parameter['check_project_type'])
    #             for e in elem:
    #                 if e.text == project_Name:
    #                     numFalg = True
    #                     break
    #                 i += 1
    #         sleep(1)
    #         if numFalg :
    #             self.wait_eleVisible(self.control['项目客户-项目名称下拉列表'])
    #             ele = self.find_elements(self.control['项目客户-项目名称下拉列表'], i)
    #             ele.click()
    #         else:
    #             self.find_element(self.control['用户管理目录']).click()
    #         sleep(2)
    #     #客户姓名/客户手机列表选择
    #     if parameter['Name_or_phone'] != '':
    #         self.find_element(self.control['预约客户-查询客户/电话-选择按钮']).click()
    #         sleep(2)
    #         #输入客户姓名/客户手机，根据参数定义
    #         if parameter['selectType'] == 'customerName':
    #             # 选择客户姓名
    #             if self.is_exist_element(self.control['预约客户-客户姓名']):
    #                 self.find_element(self.control['预约客户-客户姓名']).click()
    #         else:
    #             # 输入电话号码
    #             sleep(1)
    #             if self.is_exist_element(self.control['预约客户-客户手机']):
    #                 self.find_element(self.control['预约客户-客户手机']).click()
    #         #输入客户姓名/电话
    #         self.find_element(self.control['预约客户-客户姓名/客户手机']).send_keys(parameter['Name_or_phone'])
    #     # 输入看房时间
    #     if parameter['startDate'] != '':
    #         sleep(1)
    #         self.move_mouse_to_element(self.control['看房时间-开始时间'])
    #         # move_ele = self.find_element(self.control['预约客户-移动到日期选择框'])
    #         # ActionChains(self.driver).move_to_element(move_ele).perform()
    #         sleep(3)
    #         self.wait_eleVisible(self.control['日期删除按钮'])
    #         self.find_element(self.control['日期删除按钮']).click()
    #         self.wait_eleVisible(self.control['看房时间-开始时间'])
    #         self.find_element(self.control['看房时间-开始时间']).click()
    #         sleep(3)
    #         self.find_element(self.control['注册时间段-开始时间输入框']).send_keys(parameter['startDate'])
    #         self.find_element(self.control['注册时间段-开始时间输入框']).send_keys(parameter['endDate'])
    #         sleep(2)
    #         self.find_element(self.control['用户管理目录']).click()
    #         sleep(1)
    #     # 输入预约时间
    #     if parameter['startDate1'] != '':
    #         self.move_mouse_to_element(self.control['预约时间-开始时间'])
    #         # move_ele = self.find_element(self.control['移动到日期选择框'])
    #         # ActionChains(self.driver).move_to_element(move_ele).perform()
    #         sleep(3)
    #         self.find_elements(self.control['日期删除按钮'],1).click()
    #         self.find_elements(self.control['注册时间段-开始时间'],1).click()
    #         sleep(3)
    #         self.find_element(self.control['注册时间段-开始时间输入框']).send_keys(parameter['startDate'])
    #         self.find_element(self.control['注册时间段-结束时间输入框']).send_keys(parameter['endDate'])
    #         sleep(2)
    #         self.find_element(self.control['用户管理目录']).click()
    #         sleep(1)
    #     # 点击查询
    #     sleep(1)
    #     if self.is_exist_element(self.control['预约客户-查询']):
    #         self.find_element(self.control['预约客户-查询']).click()
    #     sleep(1)

    def booking_customer_inquiry(self, parameter=None,checkData = None):
        '''预约客户-查询'''
        sleep(3)
        #选择项目名称
        if (parameter['project_Name'] != '') & (self.is_exist_element(self.control['预约客户-项目名称'])):
            sleep(2)
            self.wait_eleVisible(self.control['预约客户-项目名称'])
            self.find_element(self.control['预约客户-项目名称']).click()
            project_Name = self.get_booking_customer_list_project(parameter['check_project_type'])
            #用于判定是否查询到有我们的判定值
            i = 0
            numFalg = False
            # 判断查询还是直接点击
            if parameter['project_Type'] == 'input':
                #标记是否查询到数据
                sleep(2)
                self.wait_eleVisible(self.control['预约客户-输入项目名称'])
                print("project_Name:", project_Name)
                self.find_element(self.control['预约客户-输入项目名称']).send_keys(project_Name)
                sleep(2)
                # self.find_element(self.control['预约客户-项目名称']).click()
                elem = self.find_elements_list(self.control['预约客户-项目名称下拉列表'])
                for e in elem:
                    if fuzz.ratio(e.text,project_Name) > 0 :
                        numFalg = True
                        break
                    i += 1
            else:
                sleep(1)
                elem = self.find_elements_list(self.control['预约客户-项目名称下拉列表'])
                for e in elem:
                    if e.text == project_Name:
                        numFalg = True
                        break
                    i += 1
            sleep(1)
            if numFalg :
                self.wait_eleVisible(self.control['预约客户-项目名称下拉列表'])
                ele = self.find_elements(self.control['预约客户-项目名称下拉列表'], i)
                ele.click()
            else:
                self.find_element(self.control['用户管理目录']).click()
            sleep(2)
        #客户姓名/客户手机列表选择
        if parameter['Name_or_phone'] != '':
            self.find_element(self.control['预约客户-查询客户/电话-选择按钮']).click()
            phone = self.get_list_phone(parameter['check_phone_type'])
            name = self.get_list_name(parameter['check_name_type'])
            sleep(2)
            #输入客户姓名/客户手机，根据参数定义
            if parameter['selectType'] == 'customerName':
                # 选择客户姓名
                if self.is_exist_element(self.control['预约客户-客户姓名']):
                    self.find_element(self.control['预约客户-客户姓名']).click()
                    # 输入客户姓名/电话
                    self.find_element(self.control['预约客户-客户姓名/客户手机']).send_keys(name)
            elif self.is_exist_element(self.control['预约客户-客户手机']):
                # 输入电话号码
                self.find_element(self.control['预约客户-客户手机']).click()
                # 输入客户姓名/电话
                self.find_element(self.control['预约客户-客户姓名/客户手机']).send_keys(phone)
        # 输入看房时间
        if parameter['startDate'] != '':
            self.wait_eleVisible(self.control["预约客户-移动到日期选择框"])
            e = self.find_elements(self.control["预约客户-移动到日期选择框"],0)
            icon = self.find_elements(self.control["预约客户-日期删除按钮"], 0)
            ActionChains(self.driver).move_to_element(e).click(icon).perform()
            sleep(3)
            self.wait_eleVisible(self.control['预约客户-看房时间-开始时间'])
            self.find_element(self.control['预约客户-看房时间-开始时间']).click()
            sleep(3)
            self.find_element(self.control['预约客户-看房时间-开始时间输入框']).send_keys(parameter['startDate'])
            self.find_element(self.control['预约客户-看房时间-结束时间输入框']).send_keys(parameter['endDate'])
            sleep(2)
            self.find_element(self.control['用户管理目录']).click()
            sleep(1)
        # 输入预约时间
        if parameter['startDate1'] != '':
            self.wait_eleVisible(self.control["预约客户-移动到日期选择框"])
            e = self.find_elements(self.control["预约客户-移动到日期选择框"], 1)
            icon = self.find_elements(self.control["预约客户-日期删除按钮"], 1)
            ActionChains(self.driver).move_to_element(e).click(icon).perform()
            self.wait_eleVisible(self.control['预约客户-预约时间-开始时间'])
            self.find_element(self.control['预约客户-预约时间-开始时间']).click()
            sleep(3)
            start_ele = self.find_element(self.control['预约客户-预约时间-开始时间输入框'])
            end_ele = self.find_element(self.control['预约客户-预约时间-结束时间输入框'])
            start_ele.send_keys(parameter['startDate1'])
            sleep(2)
            end_ele.send_keys(parameter['endDate1'])
            sleep(2)
            self.find_element(self.control['用户管理目录']).click()
            sleep(1)
        # 点击查询
        if self.is_exist_element(self.control['预约客户-查询']):
            self.find_element(self.control['预约客户-查询']).click()
        sleep(3)
        self.contrast_list_data(checkData,phone)

    #公共方法
    def switch_to_tab(self,tab_name):
        self.refresh()
        if tab_name == '集团客户':
            self.wait_eleVisible(self.control['选择集团客户'])
            self.find_element(self.control['选择集团客户']).click()
        if tab_name == '区域客户':
            self.wait_eleVisible(self.control['选择区域客户'])
            self.find_element(self.control['选择区域客户']).click()
        if tab_name == '项目客户':
            self.wait_eleVisible(self.control['选择项目客户'])
            self.find_element(self.control['选择项目客户']).click()
        if tab_name == '预约客户':
            self.wait_eleVisible(self.control['选择预约客户'])
            self.find_element(self.control['选择预约客户']).click()
        sleep(2)

    def error_message_prompt(self):
        '''项目客户：查看来去拓扑图，错误提示：record not found;
           导出列表-导出-下载时，错误提示：bigCategory不能为空；
           预约客户：查看详情，错误提示：请求用户获取用户信息失败;'''
        sleep(2)
        if self.is_exist_element(self.control['错误提示-知道了']):
            self.find_element(self.control['错误提示-知道了']).click()


    def input_phone(self, phone=None,mode = None):
        '''
        输入客户电话（适用于集团客户、区域客户、项目客户）
        :param phone:
        :return:
        '''
        self.wait_eleVisible(self.control[mode+'客户电话'])
        self.find_element(self.control[mode+'客户电话']).click()
        self.find_element(self.control[mode+'客户电话']).send_keys(phone)

    def input_registration_date(self,startDate=None,endDate=None,mode = None):
        '''
        输入注册时间段：开始时间-结束时间（适用于集团客户、区域客户、项目客户）
        :param startDate:
        :param endDate:
        :return:
        '''
        self.wait_eleVisible(self.control[mode+'移动到日期选择框'])
        self.move_mouse_to_element(self.control[mode + '移动到日期选择框'])
        sleep(3)
        self.wait_eleVisible(self.control[mode + '日期删除按钮'])
        self.find_element(self.control[mode + '日期删除按钮']).click()
        self.wait_eleVisible(self.control[mode + '注册时间段-开始时间'])
        self.find_element(self.control[mode + '注册时间段-开始时间']).click()
        sleep(3)
        start_ele = self.find_element(self.control[mode + '注册时间段-开始时间输入框'])
        end_ele = self.find_element(self.control[mode + '注册时间段-结束时间输入框'])
        start_ele.send_keys(startDate)
        sleep(2)
        end_ele.send_keys(endDate)
        sleep(2)
        self.find_element(self.control['用户管理目录']).click()
        sleep(1)

    def inquire(self,mode = None):
        '''点击查询按钮（适用于集团客户、区域客户、项目客户）'''
        self.wait_eleVisible(self.control[mode + '查询'])
        self.find_element(self.control[mode + '查询']).click()

    def export_list(self,mode = None):
        '''点击导出列表按钮（适用于集团客户、区域客户、项目客户）'''
        sleep(1)
        self.error_message_prompt()
        # 点击导出列表
        self.wait_eleVisible(self.control[mode+'导出列表'])
        self.find_element(self.control[mode+'导出列表']).click()


    def get_reportList(self):
        '''获取导出列表第一条记录的导出状态（适用于集团客户、区域客户、项目客户）'''
        reportStatus = ''
        self.wait_eleVisible(self.control['项目客户-导出状态'])
        reportStatus=self.find_element(self.control['项目客户-导出状态']).text
        return reportStatus

    def export_function(self,mode = None):
        '''导出客户列表，导出并下载'''
        start_time = self.find_element(self.control['导出状态-创建时间']).text
        self.wait_eleVisible(self.control[mode + '导出'])
        self.find_element(self.control[mode + '导出']).click()
        # 识别导出列表第一条记录的导出状态
        sleep(2)
        end_time = self.find_element(self.control['导出状态-创建时间']).text
        self.assertFalse(start_time == end_time,'导出不成功')
        reportStatus = self.get_reportList()
        sleep(1)
        while (reportStatus != '导出成功'):
            sleep(1)
            reportStatus = self.get_reportList()
        sleep(2)
        self.wait_eleVisible(self.control[mode+'下载'])
        self.find_element(self.control[mode+'下载']).click()
        sleep(2)
        self.error_message_prompt()
        sleep(1)
        self.wait_eleVisible(self.control['项目客户-导出页面关闭'])
        self.find_element(self.control['项目客户-导出页面关闭']).click()

    # def review_business_relationship_table(self,links = None,mode = None):
    #     '''查看业务关系表（适用于集团客户、区域客户、项目客户）'''
    #     sleep(2)
    #     self.wait_eleVisible(self.control[mode + '点击业务关系表'])
    #     self.find_elements(self.control[mode + '点击业务关系表'],links).click()
    #     self.error_message_prompt()

    def review_business_relationship_table(self,mode = None):
        '''查看业务关系表（适用于集团客户、区域客户、项目客户）'''
        sleep(2)
        if self.is_exist_element(self.control[mode + '点击业务关系表']):
            self.wait_eleVisible(self.control[mode + '点击业务关系表'])
            self.find_elements(self.control[mode + '点击业务关系表'],0).click()
            self.error_message_prompt()
            self.assertTrue(self.is_exist_element(self.control['业务关系表']),'关系列表不存在')



    def close_business_relationship_table(self,mode = None):
        '''关闭关系表（适用于集团客户、区域客户、项目客户）'''
        sleep(2)
        if self.is_exist_element(self.control[mode+'关闭业务关系表']):
            self.wait_eleVisible(self.control[mode+'关闭业务关系表'])
            self.find_element(self.control[mode +'关闭业务关系表']).click()

    # def review_topological_graph(self,links = None,mode = None):
    #     '''查看来去拓扑图'''
    #     sleep(2)
    #     self.wait_eleVisible(self.control[mode+'查看来去拓扑图'])
    #     self.find_elements(self.control[mode + '查看来去拓扑图'],links).click()
    #     self.error_message_prompt()
    #     sleep(2)
    #     flag = self.assert_element(mode+'来去拓扑图页面')
    #     return flag

    def review_topological_graph(self,mode = None):
        '''查看来去拓扑图'''
        sleep(2)
        if self.is_exist_element(self.control[mode+'查看来去拓扑图']):
            self.wait_eleVisible(self.control[mode+'查看来去拓扑图'])
            self.find_elements(self.control[mode + '查看来去拓扑图'],0).click()
            self.error_message_prompt()
            self.assertTrue(self.is_exist_element(self.control['来去拓扑图']), '关系列表不存在')

    def close_topological_graph(self,mode = None):
        '''关闭来去拓扑图'''
        sleep(1)
        if self.is_exist_element(self.control[mode +'关闭来去拓扑图']):
            self.wait_eleVisible(self.control[mode +'关闭来去拓扑图'])
            self.find_element(self.control[mode + '关闭来去拓扑图']).click()

    # def review_customer_detail(self,line = None,var = None):
    #     '''查看预约客户列表详情'''
    #     if line > 1 :
    #         print("line:",line)
    #         self.find_elements(self.control['预约客户-查看详情'],line).click()
    #         sleep(1)
    #         self.error_message_prompt()
    #         sleep(2)
    #         flag = self.assert_element('预约客户-判断预约客户明细')
    #         #self.check_assert(flag,var['flag'],var['msg'])
    #         self.error_message_prompt()
    #         return flag

    def review_customer_detail(self,line = None,var = None):
        '''查看预约客户列表详情'''
        if self.is_exist_element(self.control['预约客户-查看详情']):
            self.find_elements(self.control['预约客户-查看详情'], 0).click()
            sleep(1)
            self.error_message_prompt()
            self.assertTrue(self.is_exist_element(self.control['预约客户-判断预约客户明细']),'查看预约客户列表详情失败')


    def close_customer_detail(self):
        '''关闭预约客户明细页面'''
        if self.is_exist_element(self.control['关闭预约客户明细页面']):
           self.find_element(self.control['关闭预约客户明细页面']).click()

    def assert_element(self,elementName = None):
        '''断言元素是否存在页面'''
        flag = self.is_exist_element(self.control[elementName])
        return flag

    def contrast_businessRelationshipTable_data(self,parameter = None,mode = None):
        '''业务关系表-判断输入的值是否在列表'''
        sleep(2)
        flag = False
        typeBolle = True
        while (typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.control[mode +'业务关系表列表'])
            for b in bodyContent:
                if b.text == parameter['standardData']:
                    flag = True
                    break
            sleep(1)
            if flag :
                break
            else:
                typeBolle = self.check_button_clickable()
                if typeBolle:
                    self.click_next()
        return flag

    def contrast_list_data(self,checkData = None,standardData = None):
        '''判断输入的值是否在列表,并返回第几个'''
        flag = False
        typeBolle = True
        countNum = 0
        while (typeBolle):
            sleep(2)
            bodyContent = self.find_elements_list(self.control['当前页面列表数据'])
            #print('len(bodyContent):',len(bodyContent))
            countNum = 0
            for b in bodyContent:
                # print(countNum,":",checkData['standardData'])
                # print(countNum,":",b.text)
                if b.text == standardData:
                    flag = True
                    break
                countNum += 1
            sleep(1)
            if flag:
                typeBolle = False
            else:
                typeBolle = self.is_exist_element(self.control['获取可点击的下一页'])
                if typeBolle:
                    self.click_next_page()
            if countNum == len(bodyContent):
                countNum = countNum - 1
        self.public_assert(flag,checkData['expectResult'],checkData['msg'])
        return flag,countNum

    def public_assert(self,actualResult,expectResult,message):
        #
        #预期结果为true，实际结果为flase时，断言提示message
        if expectResult == 'True' :
            self.assertTrue(actualResult,msg= message)
        #预期结果为false，实际结果为true时，断言提示message
        else:
            self.assertFalse(actualResult,msg= message)

    # def check_button_clickable(self):
    #     #     '''检查下一页按钮是否可点击'''
    #     #     nextNum = self.find_elements_list(self.control['下一页'])
    #     #     for i in range(int(len(nextNum)-1)):
    #     #         self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
    #     #         #print('i.is_enabled()',nextNum[i].get_attribute('title'))
    #     #     #print('++++++++++:',int(len(self.find_elements_list(self.control['下一页']))))
    #     #     button_clickable= self.is_exist_element(self.control['获取可点击的下一页'])
    #     #     #print('check_test:',button_clickable)
    #     #     return button_clickable

    def check_next_clickable(self):
        '''检查下一页按钮是否可点击'''
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    # def click_next(self):
    #     '''点击下一页'''
    #     nextNum = len(self.find_elements_list(self.control['下一页']))
    #     if nextNum > 2:
    #         self.find_elements(self.control['下一页'], int(len(nextNum) - 1)).click()
    #     else:
    #         if self.is_exist_element(self.control['获取可点击的下一页']):
    #             self.find_element(self.control['获取可点击的下一页']).click()

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

    # def check_button_previous_page(self):
    #     '''检查上一页按钮是否可点击'''
    #     nextNum = self.find_elements_list(self.control['上一页'])
    #     for i in range(int(len(nextNum)-1)):
    #         self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
    #         #print('i.is_enabled()',nextNum[i].get_attribute('title'))
    #     #print('++++++++++:',int(len(self.find_elements_list(self.control['上一页']))))
    #     button_clickable= self.is_exist_element(self.control['获取可点击的上一页'])
    #     #print('check_test:',button_clickable)
    #     return button_clickable

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

    # def click_previous_page(self):
    #     '''点击上一页'''
    #     sleep(2)
    #     total_data = int(self.total_data())
    #     number_page = int(self.Number_page())
    #     page = int(total_data/number_page)
    #     if page > 1:
    #         self.wait_eleVisible(self.control['跳转至第几页'])
    #         self.find_element(self.control['跳转至第几页']).send_keys(page+1)
    #         sleep(2)
    #         self.find_element(self.control['用户管理目录']).click()
    #         sleep(2)
    #         #获取可点击的上一页
    #         while(self.check_button_previous_page()):
    #             sleep(1)
    #             nextNum = self.find_elements_list(self.control['上一页'])
    #             #print('nextNum:', len(nextNum))
    #             if self.is_exist_element(self.control['上一页']):
    #                 self.find_elements(self.control['上一页'], int(len(nextNum) - 1)).click()

    def click_previous_page(self):
        '''点击上一页'''
        sleep(2)
        # total_data = int(self.total_data())
        # number_page = int(self.Number_page())
        # page = int(total_data/number_page)
        # if page > 10:
        #
        page = 10
        if (page > 1) & (self.is_exist_element(self.control['跳转至第几页'])):
            if self.is_exist_element(self.control['跳转至第几页']) :
                self.wait_eleVisible(self.control['跳转至第几页'])
                self.find_element(self.control['跳转至第几页']).send_keys(page + 1)
                sleep(2)
                #self.send_keys("{ENTER}")
                self.find_element(self.control['共计总记录']).click()
                sleep(2)
                while(self.is_exist_element(self.control['获取可点击的上一页'])):
                    sleep(1)
                    self.find_element(self.control['上一页']).click()

    def click_blank(self):
        '''点击页面的空白处'''
        ActionChains(self.driver).move_by_offset(10, 10).click().perform()


    def user_intent(self,userIntent,userClick,userSelect,userDel):
        '''用户意向选择'''
        if userIntent != '':
            #选择用户意向
            self.find_element(self.control[userClick]).click()
            sleep(2)
            self.wait_eleVisible(self.control[userSelect])
            listUser = self.find_elements_list(self.control[userSelect])
            i = 0
            # print("leg：",len(listUser))
            for user in listUser :
                sleep(2)
                # print("000:",userIntent,"----",user.text)
                if userIntent in user.text :
                    user.click()
                # else:
                #     i += 1
        #else:
            # 选择用户意向
            # self.find_element(self.control[userClick]).click()
            # sleep(2)
            # self.find_elements(self.control[userSelect],0).click()
            # sleep(2)
            # self.find_element(self.control[userDel]).click()




