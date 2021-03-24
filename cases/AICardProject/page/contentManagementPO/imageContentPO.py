#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class imageContentPO(BasePage):
    controls = {
        "上传图片按钮": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[1]/button'),
        "新增图片标识": (By.XPATH, ".//*[text()='新增图片']"),
        "标题内容": (By.XPATH, '//*[@id="title"]'),
        "关联类型-全局": (By.XPATH, '//*[@id="publish_range"]/label[1]/span[1]/input'),
        "关联类型-项目": (By.XPATH, '//*[@id="publish_range"]/label[2]/span[1]/input'),
        "点击关联项目": (By.XPATH, '//*[@id="relation_ids"]/div/div/div'),
        # "点击关联项目": (By.XPATH, '//*[@id="relation_ids"]/div/div/div'),

        "点击上传图片": (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/span/div/div/div[1]/div/div/div/input'),
        "确认保存": (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]'),
        "获取上传图片名称": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[1]/div[1]'),
        "获取第一个详情": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[1]'),
        "编辑图片标识": (By.XPATH, ".//*[text()='编辑图片']"),

        "删除图片": (By.XPATH, "//*[@class='pages-manager_image-modal-edit-index-module_2mq2l']/i"),
        "再次上传图片": (By.XPATH,
                   '/html/body/div[5]/div/div[2]/div/div[2]/div[2]/form/div[4]/div[2]/div/span/div/div/div[1]/div/div/div/input'),
"ant-modal-confirm-btns"
        "获取第一个删除": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[@class="ant-btn pages-manager_image-content-component-item-image-index-module_1ppYW ant-btn-default"]'),
                              # '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[2]/span'),
        "点击删除": (By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[2]'),
                 # '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]/div[2]/button[@class="ant-btn pages-manager_image-content-component-item-image-index-module_1ppYW ant-btn-default"]'),

        "删除-确定": (By.XPATH, '//*[@class="ant-modal-confirm-btns"]/button[@class="ant-btn ant-btn-primary"]'),

    }
    def newImage(self, contentName):
        sleep(2)
        self.find_element(self.controls["上传图片按钮"]).click()
        sleep(2)
        content =self.find_element(self.controls["新增图片标识"]).text
        try:
            if content == u"新增图片":
                self.find_element(self.controls["标题内容"]).clear()
                self.find_element(self.controls["标题内容"]).send_keys(contentName)
                self.find_element(self.controls["关联类型-全局"]).click()
                self.find_element(self.controls["点击上传图片"]).click()
                sleep(1)
                path = r'C:\Users\zhengw\Desktop\otherFile\200-200.jpg'
                self.send_keys(path)  # 发送文件地址
                self.send_keys("{ENTER}")
                sleep(2)
                self.find_element(self.controls["确认保存"]).click()
            else:
                return u"页面打开失败！"
        except Exception as err:
            return err

    def updateImage(self,contentName,contentNewName):
        sleep(2)
        getImageName= self.find_element(self.controls["获取上传图片名称"]).text
        if getImageName==contentName:
            self.find_element(self.controls["获取第一个详情"]).click()
            sleep(2)
            content = self.find_element(self.controls["编辑图片标识"]).text
            sleep(1)
            if content == u"编辑图片":
                self.find_element(self.controls["标题内容"]).clear()
                self.find_element(self.controls["标题内容"]).send_keys(contentNewName)
                self.find_element(self.controls["关联类型-全局"]).click()
                # self.find_element(self.controls["删除图片"]).click()
                # sleep(1)
                # self.find_element(self.controls["再次上传图片"]).click()
                # sleep(1)
                # path = r'C:\Users\zhengw\Desktop\otherFile\200-200.jpg'
                # self.send_keys(path)  # 发送文件地址
                # self.send_keys("{ENTER}")
                sleep(2)
                self.find_element(self.controls["确认保存"]).click()

            else:
                return u"页面打开失败！"


    def delImage(self,contentNewName):
        sleep(2)
        # self.find_element(self.controls["点击删除"]).click()
        # sleep(2)
        # self.find_element(self.controls["删除-确定"]).click()
        getImageName= self.find_element(self.controls["获取上传图片名称"]).text
        # print(getImageName)
        if getImageName == contentNewName:
            print(self.find_element(self.controls["点击删除"]))
            self.find_element(self.controls["点击删除"]).click()
            sleep(2)
            self.find_element(self.controls["删除-确定"]).click()
        sleep(2)
