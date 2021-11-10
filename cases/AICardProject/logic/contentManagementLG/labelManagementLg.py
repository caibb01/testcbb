#-*- coding:utf-8 -*-

from cases.AICardProject.page.contentManagementPO.labelManagementPO import LabelManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class LabelManagementLg():
    def __init__(self, driver):
        self.driver = driver
        self.labelManagementPO = LabelManagementPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_label_page(self):
        # 内容管理-标签管理
        self.MenuManager.choiceMenu("内容管理", "内容管理-标签管理")
        sleep(2)

    def switch_to_tab(self, var):
        # 切换tab
        self.labelManagementPO.switch_to_tab(tab_name=var)

    def new_label(self, var):
        # 新增标签
        self.labelManagementPO.new_label(params=var)

    def add_association(self, var):
        # 添加关联关系
        self.labelManagementPO.add_association(params=var)

    def del_association(self):
        # 删除关联关系
        self.labelManagementPO.del_association()

    def del_label(self):
        # 删除标签
        self.labelManagementPO.del_label()

    def label_sort(self):
        # 关联数据排序
        self.labelManagementPO.label_sort()

    # def click_next(self):
    #     # 点击下一页
    #     self.labelManagementPO.click_next()
    #
    # def click_previous(self):
    #     # 点击上一页
    #     self.labelManagementPO.click_previous()

    def page_turning(self):
        # 点击下一页
        self.labelManagementPO.click_next()
        sleep(1)
        # 点击上一页
        self.labelManagementPO.click_previous()
