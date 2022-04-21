#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class manageAppointmentpage(BasePage):
    control = {
        # 预约设置
        "预约看房": (By.XPATH, '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[1]'),
        "预约交房": (By.XPATH, '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[1]'),

        # 预约看房
        "项目选择": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[1]/div[1]//div[@class="ant-col ant-form-item-control-wrapper"][1]'),
        "预约看房文案": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[1]/div[1]//label[@title="用户是否可线上预约看房"]'),
        "预约看房开关": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[1]/div[1]//span[@class="ant-switch-inner"]'),
        "约看项目预约二维码": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[1]/div[1]//button[@class="ant-btn ant-btn-primary"]'),
        "页面设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[1]/div[2]/button'),
        "约看预约须知设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[2]/div[1]'),
        "预约看房须知输入框": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/div/div/div/textarea'),
        "约看确定": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/div/div/div[2]/button[1]'),
        "约看取消": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/div/div/div[2]/button[2]'),
        "约看填写字段设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[2]/div[2]'),
        "约看自定义字段": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]//div[@class="ant-spin-container"]/div/div/div[last()]'),
        "约看陪同人员信息填写开关": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/form/div[1]/div[2]/div/span/button'),
        "约看陪同人员限制": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/form/div[2]/div/div/span'),
        "越看复制当前设置到其他项目": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/div[2]/button'),
        "约看接待量设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[2]/div[3]'),
        "约看预约可选时间": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[3]/div/div/div/form/div/div[2]/div/span'),
        "约看可选时间列表": (By.XPATH, '//ul[@role="listbox"]/li'),
        "约看可预约日期设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[2]/div[4]'),
        "约看预约时间输入框": (By.XPATH, '//div[@class="ant-input-number-input-wrap"]/input'),
        "约看资格验证设置": (By.XPATH, '//div[@role="tabpanel"][1]/div[2]/div[2]/div[5]'),
        "约看预约客户资格验证开关": (By.XPATH, '//div[@class="ant-row mt30 mb30"]/div[2]/button'),

        # 预约交房
        "预约交房文案": (By.XPATH, '//div[@class="ant-col ant-form-item-label"]/label[@title="用户是否可线上预约交房"]'),
        "约交预约须知设置": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[2]/div[1]'),
        "约交填写字段设置": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[2]/div[2]'),
        "约交接待量设置": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[2]/div[3]'),
        "约交可预约日期设置": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[2]/div[4]'),
        "约交资格验证设置": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[2]/div[5]'),
        "预约交房开关": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[1]/div[1]//span[@class="ant-switch-inner"]'),
        "约交项目预约二维码": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[1]/div[1]//button[@class="ant-btn ant-btn-primary"]'),
        "预约交房须知输入框": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/div/div/div/textarea'),
        "约交确定": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/div/div/div[2]/button[1]'),
        "约交取消": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/div/div/div[2]/button[2]'),
        "约交自定义字段": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]//div[@class="ant-spin-container"]/div/div/div[last()]'),
        "约交陪同人员信息填写开关": (By.XPATH, '//div[@role="tabpanel"][3]/div[2]/div[3]/div/form/div[1]/div[2]/div/span/button'),
        "约交陪同人员限制": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/form/div[2]/div/div/span'),
        "约交复制当前设置到其他项目": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/div[2]/button'),
        "约交预约可选时间": (By.XPATH, '//div[@role="tabpanel"][2]/div[2]/div[3]/div/div/div/form/div/div[2]/div/span'),
        "约交可选时间列表": (By.XPATH, '//ul[@role="listbox"]/li'),
        "约交预约时间输入框": (By.XPATH, '//div[@class="ant-input-number-input-wrap"]/input'),
    }

    def __init__(self, driver):
        super(manageAppointmentpage, self).__init__(driver)

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

