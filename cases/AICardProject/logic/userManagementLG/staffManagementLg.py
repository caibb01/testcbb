#-*- encoding=utf8 -*-
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.userManagementPO.staffManagementPO import staffManagement


class staffManagementLg():
    def __init__(self,driver):
        #super(staffManagementLg,self).__init__(driver)
        self.driver=driver
        self.staffManagementPO = staffManagement(driver)
        self.MenuManager = MenuManager(driver)

    def into_staffManagementLg_page(self):
        '''打开用户管理-员工管理'''
        self.MenuManager.choiceMenu("用户管理","用户管理-员工管理")

    def staff_management_inquiry_lg(self,var):
        '''销售团队/行销团队/策划团队查询'''
        #切换销售团队/行销团队/策划团队/经纪人团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        #查询
        self.staffManagementPO.staff_management_inquiry(var['modelName'],var['parameter'])
        #对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.staffManagementPO.contrast_list_data(var['modelName'],var['checkData'])

    def broker_team_inquiry_lg(self,var):
        '''经纪人团队查询'''
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.broker_team_inquiry(var['modelName'],var['parameter'])
        # 对比列表中的数据，当前页没有找到点击下一页继续找，直到最后一页
        #self.staffManagementPO.contrast_list_data(var['modelName'],var['checkData'])

    def enable_of_disable_card_lg(self,var):
        '''判断该员工的卡片是启用还是禁用,弹窗选择确定'''
        # 切换销售团队/行销团队/策划团队/经纪人团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.enable_of_disable_card(var['modelName'])

    def cancel_enable_of_disable_card_lg(self,var):
        '''判断该员工的卡片是启用还是禁用，弹窗选择取消'''
        # 切换销售团队/行销团队/策划团队/经纪人团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.cancel_enable_of_disable_card(var['modelName'])


    def page_switching_lg(self,var):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        sleep(2)
        # 切换销售团队/行销团队/策划团队/经纪人团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.click_next_page()
        self.staffManagementPO.click_previous_page()

    def open_project_page_lg(self,var):
        '''销售团队/策划人员团队：打开所属项目页面'''
        # 切换销售团队/行销团队/策划团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.open_project_page(var['modelName'])

    def marketing_team_open_project_page_lg(self,var):
        '''行销团队：打开所属项目页面'''
        # 切换行销团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.marketing_team_open_project_page()

    def synchronization_personnel_list_lg(self,var):
        '''同步人员名单'''
        # 切换销售团队/行销团队/策划团队/经纪人团队的Tab
        self.staffManagementPO.switch_to_tab(var['modelName'])
        self.staffManagementPO.synchronization_personnel_list(var['modelName'])

    def project_lg(self):
        '''打开所属项目页面'''
        self.staffManagementPO.open_project_page()