# coding=utf-8
from myweb.core.BasePage import BasePage
from cases.AICardProject.page.contentManagementPO.recommendArticlePO import RecommendArticle, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class RecommendArticleLg(BasePage):
    def __init__(self, driver):
        super(RecommendArticleLg, self).__init__(driver)
        self.driver = driver
        self.recommendArticlePO = RecommendArticle(driver)
        self.MenuManager = MenuManager(driver)

    def into_article_page(self):
        # 打开内容管理-推荐文章
        self.MenuManager.choiceMenu("内容管理", "内容管理-推荐文章")
        sleep(3)

    def addArticle(self, var):
        """
        添加推荐文章
        """
        self.recommendArticlePO.save_article(params=var)

    def editArticle(self, var):
        """
        编辑推荐文章
        """
        self.recommendArticlePO.update_article(params=var)

    def publishArticle(self, var):
        """
        发布文章
        """
        self.recommendArticlePO.publish_article(publish_status=var)

    def closeArticle(self, var):
        """
        关闭文章
        """
        self.recommendArticlePO.close_article(publish_status=var)

    def apply_list(self, var):
        """
        报名列表
        """
        self.recommendArticlePO.apply_list(params=var)

    def copy_article_link(self, var):
        """
        复制公众号文章
        """
        self.recommendArticlePO.copy_article_link(link=var)

    def search_article(self, var):
        """
        查询文章
        """
        self.recommendArticlePO.search_article(keywords=var)

    def page_turning(self):
        # 点击下一页
        self.recommendArticlePO.click_next()
        sleep(2)
        # 点击上一页
        self.recommendArticlePO.click_previous()
        sleep(2)
        # 点击跳页
        self.recommendArticlePO.jump_page()