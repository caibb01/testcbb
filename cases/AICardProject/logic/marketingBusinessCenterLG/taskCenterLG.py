#-*- coding:utf-8 -*-

from cases.AICardProject.page.marketingBusinessCenterPO.taskCenterPO import TaskCenterPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class TaskCenterLg():
    def __init__(self, driver):
        self.driver = driver
        self.taskCenterPO = TaskCenterPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_taskCenter_page(self):
        # 打开营销业务中心-任务中心
        self.MenuManager.choiceMenu("营销业务中心", "营销业务中心-任务中心")
        sleep(2)

    def save_task(self, var):
        # 新增任务
        self.taskCenterPO.save_task(params=var)

    def edit_task(self, var):
        # 编辑任务
        self.taskCenterPO.edit_task(params=var)

    def check_progress(self):
        # 查看进展
        self.taskCenterPO.check_progress()

    def view_ranking_list(self):
        # 查看排行榜
        self.taskCenterPO.view_ranking_list()

    def search_task(self, var):
        # 列表搜索
        self.taskCenterPO.search_task(params=var)

    def click_next(self):
        # 点击下一页
        self.taskCenterPO.click_next()

    def click_previous(self):
        # 点击上一页
        self.taskCenterPO.click_previous()

    def jump_page(self):
        # 点击跳页
        self.taskCenterPO.jump_page()

    def delete_task(self):
        # 删除任务
        self.taskCenterPO.delete_task()


