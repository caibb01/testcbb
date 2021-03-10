# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from time import sleep
from cases.AICardProject.page.contentManagementPO.imageContentPO import imageContentPO
from cases.AICardProject.logic.MenuManager import MenuManager


class imageContentLg(BasePage):
    def __init__(self, driver):
        # super(articleContentPO, self).__init__(driver)
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.imageContentPO = imageContentPO(driver)


    def newContent(self):
        '''
        新增文章，编辑文章，发布文章，编辑文章，关闭文章
        :return:
        '''
        self.MenuManager.choiceMenu(firstLevelMenu="内容管理", SecondaryMenu="内容管理-图片管理")
        self.imageContentPO.newImage(contentName=u"图片上传测试")
        self.imageContentPO.updateImage(contentName=u"图片上传测试",contentNewName=u"修改图片上传测试")
        self.imageContentPO.delImage(contentNewName = u"修改图片上传测试")
        # contentNewName = u"修改图片上传测试"
