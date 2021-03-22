#coding:utf-8
# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
import sys
from cases.AICardProject.page.contentManagementPO.videoManagementPO import videoManagementPO
from time import sleep
from cases.AICardProject.logic.MenuManager import MenuManager
import os

class videoManagementLg(BasePage):
    def __init__(self, driver):
        # super(articleContentPO, self).__init__(driver)
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.videoManagementPO = videoManagementPO(driver)

    def videoManagement(self):
        # current_dir = os.path.abspath(os.path.dirname(__file__))
        # print(current_dir)
        voidPath=r'D:\AICar\WebTestProject\cases\AICardProject\data\image\xjdsp.mp4'
        imgPath=r'D:\AICar\WebTestProject\cases\AICardProject\data\image\video.jpg'
        self.MenuManager.choiceMenu(firstLevelMenu="内容管理", SecondaryMenu="内容管理-视频管理")
        self.videoManagementPO.addVideo(titlename="视频新增自动化测试",voidPath=voidPath,imgPath=imgPath,proName="全局")
        self.videoManagementPO.queryVideo(videoName="视频新增自动化测试")
        self.videoManagementPO.updateVideo(titlename="update视频新增自动化测试",voidName=voidPath,imgName=imgPath,proName='哥伦布多项目3')
        self.videoManagementPO.delVideo()
