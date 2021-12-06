#-*- encoding=utf-8 -*-

from myweb.core.BasePage import BasePage
from time import sleep
from cases.AICardProject.page.settingConfigurationPO.basicInfoPO import BasicInfoPO
from cases.AICardProject.logic.MenuManager import MenuManager

class BasicInfoLg(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.menuManager = MenuManager(driver)
        self.basicInfoPO = BasicInfoPO(driver)

    def into_BasicInfo_page(self):
        '''打开系统设置-基础信息'''
        self.menuManager.choiceMenu("系统设置","系统设置-基础信息")

    def short_for_mini_program_lg(self,var):
        '''小程序简称'''
        self.basicInfoPO.short_for_mini_program(var['name'])

    def corporate_image_chart_lg(self,var):
        '''企业形象图的上传图片、重新上传、删除'''
        self.basicInfoPO.corporate_image_chart(var['path'])

    def corporate_logo_lg(self,var):
        '''企业LOGO的上传图片、重新上传、删除'''
        self.basicInfoPO.corporate_logo(var['path'])

    def authorization_background_image_lg(self,var):
        '''授权背景图的上传图片、重新上传、删除'''
        self.basicInfoPO.authorization_background_image(var['path'])

    def poster_on_moments_lg(self,var):
        '''朋友圈海报（安卓）的上传图片、重新上传、删除'''
        self.basicInfoPO.poster_on_moments(var['path'])

    def workbench_icon_lg(self,var):
        '''工作台图标，开或关，上传图片、重新上传、删除'''
        self.basicInfoPO.workbench_icon(var['path'])

    def map_marker_icon_lg(self,var):
        '''地图标记图标的上传图片、重新上传、删除'''
        self.basicInfoPO.map_marker_icon(var['path'])

    def intelligent_customer_service_lg(self,var):
        '''智能客服：开启或关闭,添加机器人'''
        self.basicInfoPO.intelligent_customer_service(var['parmeter'])

    def delete_robot_lg(self):
        '''智能客服：删除机器人'''
        self.basicInfoPO.delete_robot()

    def intelligent_customer_service_configuration_lg(self,var):
        '''智能客服-机器人配置快捷提问，保存'''
        self.basicInfoPO.intelligent_customer_service_configuration(var['question'])

    def cancel_intelligent_customer_service_configuration_lg(self,var):
        '''智能客服-机器人配置快捷提问，取消保存'''
        self.basicInfoPO.cancel_intelligent_customer_service_configuration(var['question'])

    def number_of_visits_lg(self,var):
        '''浏览人次名称自定义:开或关，自定义名称'''
        self.basicInfoPO.number_of_visits(var['name'])

    def leave_advice_lg(self):
        '''留电通知开或关，勾选置业顾问、行销人员、全民经纪人'''
        self.basicInfoPO.leave_advice()

    def other_settings_01_lg(self):
        '''其他设置，勾选允许查看服务轨迹'''
        self.basicInfoPO.other_settings_01()

    def other_settings_02_lg(self):
        '''其他设置，勾选允许云会员'''
        self.basicInfoPO.other_settings_02()

    def save_lg(self):
        '''保存'''
        self.basicInfoPO.save()

    def cancel_save_lg(self):
        '''取消保存'''
        self.basicInfoPO.cancel_save()