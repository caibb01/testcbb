# coding=utf-8
import time
from myweb.core.BasePage import BasePage
from cases.AICardProject.page.contentManagementPO.videoManagementPO import videoManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class videoManagementLg(BasePage):
    def __init__(self, driver):
        # super(articleContentPO, self).__init__(driver)
        super(videoManagementLg, self).__init__(driver)
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.videoManagementPO = videoManagementPO(driver)

    #def videoManagement(self,var):
        # current_dir = os.path.abspath(os.path.dirname(__file__))
        # print(current_dir)

    def into_video_page(self):
        # 打开内容管理-视频管理
        self.MenuManager.choiceMenu("内容管理", "内容管理-视频管理")
        sleep(3)

    def addVideo(self, var):
        """ 添加一个视频
            titleName: 视频标题
            videoPath：视频文件地址
            imgPath：图片文件地址
            proName：项目名
        """
        # self.MenuManager.choiceMenu(firstLevelMenu="内容管理", SecondaryMenu="内容管理-视频管理")
        self.videoManagementPO.addVideo(titleName="自动化测试视频", voidPath=var["videoPath"], imgPath=var["imgPath"], proName="全局")

        self.videoManagementPO.queryVideo(videoName="自动化测试视频")
        #self.videoManagementPO.updateVideo(titleName="update视频新增自动化测试", voidName=var["videoPath"], imgName=var["imgPath"], proName='体验项目')
        #self.videoManagementPO.addVideo(titleName=var["titleName"], voidPath=var["videoPath"], imgPath=var["imgPath"], proName=var["proName"])
        time.sleep(3)

    def queryVideo(self, var):
        """ 查询一个视频
            videoName: 要查询的视频名
        """
        self.videoManagementPO.queryVideo(videoName=var["videoName"])
        time.sleep(3)

    def updateVideo(self, var):
        """ 更新视频
            titleNmae: 更新后的标题
            proName: 更新后的项目名
        """
        self.videoManagementPO.updateVideo(titleName=var["titleName"], proName=var["proName"])
        time.sleep(3)

    def delVideo(self):
        """ 删除首个视频
        """
        self.videoManagementPO.delVideo()

        time.sleep(3)

    def page_turning(self):
        # 点击下一页
        self.videoManagementPO.click_next()
        sleep(2)
        # 点击上一页
        self.videoManagementPO.click_previous()
        sleep(2)
        # 点击跳页
        self.videoManagementPO.jump_page()
