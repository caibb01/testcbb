#-*- coding:utf-8 -*-

from cases.AICardProject.page.marketingBusinessCenterPO.commentsPO import CommentsPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class CommentsLg():
    def __init__(self, driver):
        self.driver = driver
        self.commentsPO = CommentsPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_comments_page(self):
        # 打开营销业务中心-评论
        self.MenuManager.choiceMenu("营销业务中心", "营销业务中心-评论")
        sleep(2)

    def save_comments(self, var):
        # 新增评论
        self.commentsPO.save_comments(params=var)

    def reply_comments(self, var):
        # 回复评论
        self.commentsPO.reply_comments(params=var)

    def reply_histroy(self):
        # 查看回复历史
        self.commentsPO.reply_histroy()

    def search_comments(self, var):
        # 列表查询
        self.commentsPO.search_comments(params=var)

    def click_next(self):
        # 点击下一页
        self.commentsPO.click_next()

    def click_previous(self):
        # 点击上一页
        self.commentsPO.click_previous()

    def jump_page(self):
        # 点击跳页
        self.commentsPO.jump_page()

    def delete_comments(self):
        # 删除评论
        self.commentsPO.delete_comments()