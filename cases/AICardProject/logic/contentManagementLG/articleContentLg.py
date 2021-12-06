# coding=utf-8
from myweb.core.BasePage import BasePage
from cases.AICardProject.page.contentManagementPO.articleContentPO import articleContent, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class articleContentLg(BasePage):
    def __init__(self, driver):
        super(articleContentLg, self).__init__(driver)
        self.driver = driver
        self.articleContentPO = articleContent(driver)
        self.MenuManager = MenuManager(driver)

    def into_article_page(self):
        # 打开内容管理-原创文章
        self.MenuManager.choiceMenu("内容管理", "内容管理-原创文章")
        sleep(3)

    def addArticle(self, var):
        """
        添加一个原创文章
        titleName: 要新增的文章标题
        content: 需要新增的文章内同
        imagePath : 文章封面图片路径
        """
        self.articleContentPO.operation_new_Function(titleName=var["titleName"], content=var["content"], imagePath=var["imagePath"])

    def editArticle(self, var):
        """
        编辑原创文章
        queryTitle: 要搜索的文章标题
        newTitle: 新的标题
        newContent: 新的文章内容
        newQueryTitle ：编辑后搜索的文章标题
        """
        self.articleContentPO.operation_query_Function(queryTitle=var['queryTitle'])
        sleep(3)
        self.articleContentPO.operation_update_Function(newTitle=var["newTitle"], newContent=var["newContent"])
        sleep(3)
        self.articleContentPO.operation_query_Function(queryTitle=var['newQueryTitle'])

    def postArticleEdit(self, var):
        """
        发布文章并进行编辑
        newQueryTitle: 要搜索的文章标题
        postNewTitle: 发布后的新的标题
        postNewContent: 发布后的新文章内容
        pastNewQueryTitle: 编辑后搜索文章标题
        """
        self.articleContentPO.operation_state_Function()
        sleep(3)
        self.articleContentPO.operation_query_Function(queryTitle=var['newQueryTitle'])
        sleep(3)
        self.articleContentPO.operation_update_Function(newTitle=var["postNewTitle"], newContent=var["postNewContent"])
        sleep(3)
        self.articleContentPO.operation_query_Function(queryTitle=var['pastNewQueryTitle'])

    def saveArticle(self, var):
        """
        新建原创文章-开启活动
        """
        self.articleContentPO.save_article(params=var)

    def closeArticle(self, var):
        """
        关闭文章
        """
        self.articleContentPO.close_article(publish_status=var)

    def apply_list(self, var):
        """
        报名列表
        """
        self.articleContentPO.apply_list(params=var)

    def page_turning(self):
        # 点击下一页
        self.articleContentPO.click_next()
        sleep(2)
        # 点击上一页
        self.articleContentPO.click_previous()
        sleep(2)
        # 点击跳页
        self.articleContentPO.jump_page()