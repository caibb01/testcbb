#coding:utf-8
#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class videoManagementPO(BasePage):
    controls = {
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "搜索": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/button[1]'),
        "新增视频": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/button[2]'),
        "取页面-新增视频信息": (By.XPATH, '//*[@id="rcDialogTitle4"]'),
        "视频描述": (By.XPATH, '//*[@id="title"]'),
        "点击上传": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/div[2]/div/span/div/span/div[1]/span/button'),
        "添加图片": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/div[2]/div/span/div/div/div/div/div/div/input'),
        "选择权限关联项目": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/span/div/div/span'),
        "选择权限关联项目-输入搜索": (By.XPATH, '/html/body/div[3]/div/div/div/div[1]/input'),
        # "选择权限关联项目-输入搜索": (By.CLASS_NAME, '//*[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "选择权限关联项目-选择搜索": (By.XPATH, '/html/body/div[3]/div/div/div/div[2]/div'),
        "勾选-我已阅读并同意": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div[2]/label/span[1]/input'),
        "确认": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'),
        "编辑": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[5]/span/button[1]'),
        "删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[5]/span/button[2]'),
        "删除-确认": (By.XPATH,
                  # ".//*[@class='ant-modal-confirm-body-wrapper']/div/button[@class='ant-btn ant-btn-primary']")
                  # '//*[text()="确定"]'),
                  '/html/body/div[6]/div/div[2]/div/div[2]/div[3]/div/button[2]/span'),
    }
    def getProInfo(self,proName):
        """
        下拉选择项目
        :param proName:
        :return:
        """
        print(proName)
        sleep(2)
        self.find_element(self.controls["选择权限关联项目"]).click()
        sleep(1)
        self.find_element(self.controls["选择权限关联项目-输入搜索"]).clear()
        sleep(1)
        self.find_element(self.controls["选择权限关联项目-输入搜索"]).send_keys(proName)
        sleep(2)
        self.find_element(self.controls["选择权限关联项目-选择搜索"]).click()

    def uploadVideo(self,path):
        """
        新增视频
        :return:
        """
        sleep(2)
        self.find_element(self.controls["点击上传"]).click()
        sleep(2)
        self.send_keys(path)  # 发送文件地址
        self.send_keys("{ENTER}")


    def uploadImg(self,path):
        """
        新增图片
        :return:
        """
        sleep(2)
        self.find_element(self.controls["添加图片"]).click()
        sleep(2)
        self.send_keys(path)  # 发送文件地址
        self.send_keys("{ENTER}")
        sleep(2)

    def addVideo(self,titlename,voidPath,imgPath,proName):
        sleep(2)
        self.find_element(self.controls["新增视频"]).click()
        sleep(2)
        # 由于这里选择项目会出错，这里的所以将顺序修改到这里
        self.getProInfo(proName=proName)
        self.find_element(self.controls["视频描述"]).clear()
        self.find_element(self.controls["视频描述"]).send_keys(titlename)
        # 上传视频
        self.uploadVideo(voidPath)
        # 视频上传有进度情况，增加等待时间
        sleep(20)
        # 上传图片
        self.uploadImg(imgPath)
        self.find_element(self.controls["勾选-我已阅读并同意"]).click()
        sleep(2)
        self.find_element(self.controls["确认"]).click()

    #修改和更新用的同一个
    def updateVideo(self,titlename,voidName,imgName,proName):
        sleep(2)
        self.find_element(self.controls["编辑"]).click()
        sleep(2)
        self.getProInfo(proName=proName)
        self.find_element(self.controls["视频描述"]).clear()
        self.find_element(self.controls["视频描述"]).send_keys(titlename)
        # 上传视频
        # self.uploadVideo(voidName)
        # # 视频上传有进度情况，增加等待时间
        # sleep(30)
        # 上传图片
        # self.uploadImg(imgName)
        self.find_element(self.controls["勾选-我已阅读并同意"]).click()
        self.find_element(self.controls["确认"]).click()

    def delVideo(self):
        sleep(2)
        self.refresh()
        sleep(2)
        self.find_element(self.controls["删除"]).click()
        sleep(2)
        self.find_element(self.controls["删除-确认"]).click()

    def queryVideo(self,videoName):
        sleep(2)
        self.find_element(self.controls["输入查询条件"]).clear()
        self.find_element(self.controls["输入查询条件"]).send_keys(videoName)
        self.find_element(self.controls["搜索"]).click()

