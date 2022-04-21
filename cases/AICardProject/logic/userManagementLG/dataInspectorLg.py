#-*- encoding=utf8 -*-
from time import sleep
import unittest
from myweb.core.BasePage import BasePage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.userManagementPO.dataInspectorPO import dataInspector


class dataInspectorLg():
    def __init__(self,driver):
        #super(dataInspectorLg,self).__init__(driver)
        self.driver = driver
        self.dataInspectorPO = dataInspector(driver)
        self.MenuManager = MenuManager(driver)

    def into_dataInspector_page(self):
        '''打开用户管理-数据查阅人'''
        self.MenuManager.choiceMenu("用户管理", "用户管理-数据查阅人")

    def inquiry_lg(self,var):
        '''输入姓名/手机号进行查询'''
        self.dataInspectorPO.inquiry(var['parameter'])
        sleep(2)
        self.dataInspectorPO.refresh()

    def confirm_delete_lg(self,var):
        '''确认删除数据查阅人'''
        print('var:',var)
        self.dataInspectorPO.inquiry(var['parameter'])
        sleep(2)
        self.dataInspectorPO.confirm_delete()
        sleep(2)
        self.dataInspectorPO.refresh()

    def synchronization_lg(self):
        '''同步数据查阅人'''
        self.dataInspectorPO.synchronization()
        sleep(2)
        self.dataInspectorPO.refresh()

    def add_lg(self,var):
        '''新增数据查阅人'''
        self.dataInspectorPO.add(var)

    def cancel_delete_lg(self,var):
        '''取消删除数据查阅人'''
        self.dataInspectorPO.inquiry(var['parameter'])
        sleep(2)
        self.dataInspectorPO.cancel_delete()
        sleep(2)
        self.dataInspectorPO.refresh()

    def click_detailed_description_lg(self):
        '''点击详细说明'''
        self.dataInspectorPO.click_detailed_description()

    def page_switching_lg(self):
        '''切换每页显示条数，切换下一页/上一页/跳至x页'''
        self.dataInspectorPO.click_next_page()
        self.dataInspectorPO.click_previous_page()