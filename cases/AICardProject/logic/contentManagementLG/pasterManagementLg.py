# coding=utf-8
import time
from myweb.core.BasePage import BasePage
from cases.AICardProject.page.contentManagementPO.pasterManagementPO import pasterManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class pasterManagementLg(BasePage):
    def __init__(self, driver):
        super(pasterManagementLg, self).__init__(driver)
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.pasterManagementPO = pasterManagementPO(driver)

    def into_poster_page(self):
        # 打开内容管理-海报管理
        self.MenuManager.choiceMenu("内容管理", "内容管理-海报管理")
        sleep(5)

    def addPaster(self, var):
        """
        新增一个海报
        title: 海报标题
        imagePath: 图片地址
        """
        self.pasterManagementPO.addPaster(title=var['title'], imagePath=var['imagePath'])

    def editPaster(self, var):
        """
        编辑一个海报
        pasterTitle: 需要编辑的海报
        newTitle: 海报标题
        imagePath: 图片地址
        """
        time.sleep(2)
        self.pasterManagementPO.editPaster(newtitle=var['newTitle'],
                                           imagePath=var['imagePath'])

    def delPaster(self):
        """
        删除一个海报
        saerchTitle: 需要删除海报的名字
        """
        self.pasterManagementPO.delPaster()
        # self.refresh()
        time.sleep(5)

    def addSort(self, var):
        """
        添加一个分类
        sortTitle: 创建海报的名字
        """
        self.pasterManagementPO.addSort(sortTitle=var['sortTitle'])

    def search_poster(self, var):
        # 搜索海报
        self.pasterManagementPO.search_poster(poster_title=var['poster_title'])

    def poster_page_turning(self):
        # 海报列表翻页
        self.refresh()
        # 点击下一页
        self.pasterManagementPO.click_next()
        # 点击上一页
        self.pasterManagementPO.click_previous()
        # 跳页
        self.pasterManagementPO.jump_page()

    def sort_page_turning(self):
        # 海报分类翻页
        # 点击下一页
        self.pasterManagementPO.click_next()
        # 点击上一页
        self.pasterManagementPO.click_previous()
        # 跳页
        self.pasterManagementPO.jump_page()

    def edit_sort(self, var):
        # 编辑分类
        self.pasterManagementPO.edit_sort(sort_title=var['sort_title'])

    def del_sort(self):
        # 删除分类
        self.pasterManagementPO.del_sort()

    def search_sort(self, var):
        # 搜索分类
        self.pasterManagementPO.search_sort(keywords=var['keywords'])