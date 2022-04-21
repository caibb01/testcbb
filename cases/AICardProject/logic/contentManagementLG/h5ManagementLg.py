#-*- coding:utf-8 -*-

from cases.AICardProject.page.contentManagementPO.h5ManagementPO import H5ManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class H5ManagementLg():
    def __init__(self, driver):
        self.driver = driver
        self.h5ManagementPO = H5ManagementPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_h5Link_page(self):
        # 打开内容管理-H5链接
        self.MenuManager.choiceMenu("内容管理", "内容管理-H5链接")
        sleep(3)

    def save_h5Link(self, var):
        # 新增h5链接
        self.h5ManagementPO.save_h5Link(params=var)

    def edit_h5Link(self, var):
        # 编辑h5链接
        self.h5ManagementPO.edit_h5Link(params=var)

    def delete_h5Link(self):
        # 删除h5链接
        self.h5ManagementPO.delete_h5Link()

    def search_h5Link(self, var):
        # H5链接搜索
        self.h5ManagementPO.search_h5Link(parameter=var)

    def save_and_search(self, var):
        # 新增h5链接(包括搜索)
        self.h5ManagementPO.save_and_search(params=var)

    def page_turning(self):
        # 点击下一页
        self.h5ManagementPO.click_next()
        sleep(2)
        # 点击上一页
        self.h5ManagementPO.click_previous()
        sleep(2)
        # 点击跳页
        self.h5ManagementPO.jump_page()