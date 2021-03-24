# -*- coding:utf-8 -*-
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.by import By
import time, logging
from time import sleep
import os
from selenium.webdriver.common.keys import Keys
import unittest


class officialAccountsContentPO(BasePage):
    """description of class"""
    controls = {
        "添加公众号文章": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/button'),
        "添加公众号文章标识": (By.XPATH, ".//*[text()='添加公众号文章']"),
        "标题": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input'),
        "描述": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]/textarea'),
        "链接": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/span/span/input'),
        "关联项目": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div'),
        "关联项目-搜索项目": (By.XPATH, "/html/body/div[3]/div/div/div/div[1]/input"),
        "关联项目-选择项目": (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div"),

        "关联地区": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[5]/div[2]/div/div/span'),
        "关联地区-搜索区域": (By.XPATH, '//*[@id="rcDialogTitle1"]/div/span/span/input'),
        #  //*[@class="city-list"]/button
        "关联地区-搜索": (By.XPATH, '//*[@id="rcDialogTitle1"]/div/span/span/span/button'),
        "关联地区-全局":(By.XPATH,
                   # "//*[text()='全局']"),
                   "//*[@class='city-list']/button"),
                   # "//*[@class='city-list']/button[@class='ant-btn mb10 btn']"),
                   # "//*[@class='ant-spin-container']/div/button"),
                    # '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/button/span'),
                    # '//*[@class="city-list"]/button'),
                              # '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/button/span'),
        "关联地区-选择第一个区域": (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div/div/div[1]/div[2]/button'),

        # 下面还有个弹窗
        "上传图片": (By.XPATH, "//*[@class='components-common-Uploader-index-module_WAMvg']"),
        "上传图片-保存": (By.XPATH, "//*[text()='确 定']"),
        "保存": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[2]'),
        "编辑": (By.XPATH,
               '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span/button[1]'),
        "删除": (By.XPATH,
               '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[6]/span/button[2]'),
        "删除-确认": (By.XPATH, '/html/body/div[7]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'),

        "请选择项目": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div'),
        "项目查询条件": (By.XPATH, '/html/body/div[4]/div/div/div/div[1]/input'),
        "项目查询条件-第一个": (By.XPATH, '/html/body/div[4]/div/div/div/div[2]/div[1]'),

    }

    def relationProject(self, pro_name):
        """
        选择项目
        pro_name:只支持项目全名称的情况
        :return:
        """
        sleep(2)
        self.find_element(self.controls["关联项目"]).click()
        sleep(2)
        self.find_element(self.controls["关联项目-搜索项目"]).clear()
        sleep(2)
        self.find_element(self.controls["关联项目-搜索项目"]).send_keys(pro_name)
        sleep(1)
        self.find_element(self.controls["关联项目-选择项目"]).click()

    def relationRegion(self):
        """
        选择关联地区
        :return:
        """
        sleep(2)
        self.find_element(self.controls["关联地区"]).click()
        sleep(2)
        self.find_element(self.controls["关联地区-搜索区域"]).clear()
        self.find_element(self.controls["关联地区-搜索区域"]).send_keys(u"全局")
        self.find_element(self.controls["关联地区-搜索"]).click()
        sleep(2)
        self.find_element(self.controls["关联地区-全局"]).click()
        sleep(2)
        # if regionType == u"全局":
        #     sleep(1)
        #     self.find_element(self.controls["关联地区-搜索区域"]).clear()
        #     self.find_element(self.controls["关联地区-搜索区域"]).send_keys(u"全局")
        #     self.find_element(self.controls["关联地区-搜索"]).click()
        #     self.find_element(self.controls["关联地区-全局"]).click()
        #     try:
        #         sleep(2)
        #         print(self.get_page_info())
        #         print(self.find_element(self.controls["关联地区-全局"]).text())
        #         self.find_element(self.controls["关联地区-全局"]).click()
        #
        #     except Exception as e:
        #         print(e)
        # else:
        #     sleep(2)
        #     self.find_element(self.controls["关联地区-搜索区域"]).clear()
        #     self.find_element(self.controls["关联地区-搜索区域"]).send_keys(regionType)
        #     self.find_element(self.controls["关联地区-搜索"]).click()
        #     sleep(2)
        #     self.find_element(self.controls["关联地区-选择第一个区域"]).click()

    def addImage(self):
        """
        新增图片
        :return:
        """
        self.find_element(self.controls["上传图片"]).click()
        sleep(1)
        path = r'C:\Users\zhengw\Desktop\otherFile\200-200.jpg'
        self.send_keys(path)  # 发送文件地址
        self.send_keys("{ENTER}")
        sleep(2)
        # 保存图片
        self.find_element(self.controls["上传图片-保存"]).click()

    def newOfficialAccounts(self,title,content,urlPath,proName):
        ''',title,content,urlPath,proName,regionType
        :return: 新增公众号文章
        '''
        sleep(2)
        self.find_element(self.controls["添加公众号文章"]).click()
        sleep(2)
        contentTitle = self.find_element(self.controls["添加公众号文章标识"]).text
        print(contentTitle)
        if contentTitle == u'添加公众号文章':
            self.find_element(self.controls["标题"]).clear()
            self.find_element(self.controls["标题"]).send_keys(title)
            self.find_element(self.controls["描述"]).clear()
            self.find_element(self.controls["描述"]).send_keys(content)
            self.find_element(self.controls["链接"]).clear()
            self.find_element(self.controls["链接"]).send_keys(urlPath)
        self.relationProject(pro_name=proName)
        self.relationRegion()
        self.addImage()
        self.find_element(self.controls["保存"]).click()





        # try:
        #     self.find_element(self.controls["添加公众号文章"]).click()
        #     sleep(2)
        #     contentTitle = self.find_element(self.controls["添加公众号文章标识"]).text
        #     print(2)
        #
        #     if contentTitle == u'添加公众号文章':
        #         self.find_element(self.controls["标题"]).clear()
        #         self.find_element(self.controls["标题"]).send_keys(title)
        #         self.find_element(self.controls["描述"]).clear()
        #         self.find_element(self.controls["描述"]).send_keys(content)
        #         self.find_element(self.controls["链接"]).clear()
        #         self.find_element(self.controls["链接"]).send_keys(urlPath)
        #     self.relationProject(pro_name=proName)
        #     self.relationRegion(regionType=regionType)
        #     self.addImage()
        #     self.find_element(self.controls["保存"]).click()
        #     pass
        # except Exception as ex:
        #     print(ex)


def updateOfficialAccounts(self, title, content, urlPath, proName, regionType):
    '''
    :return: 更新公众号文章,默认更新第一个
    '''
    sleep(2)
    self.find_element(self.controls["编辑"]).click()
    sleep(2)
    self.find_element(self.controls["公众号文章管理"]).click()
    contentTitle = self.find_element(self.controls["添加公众号文章标识"]).text
    if contentTitle == u'添加公众号文章':
        self.find_element(self.controls["标题"]).clear()
        self.find_element(self.controls["标题"]).send_keys(title)
        self.find_element(self.controls["描述"]).clear()
        self.find_element(self.controls["描述"]).send_keys(content)
        self.find_element(self.controls["链接"]).clear()
        self.find_element(self.controls["链接"]).send_keys(urlPath)
    self.relationProject(pro_name=proName)
    self.relationRegion(regionType=regionType)
    self.addImage()
    self.find_element(self.controls["保存"]).click()


def delOfficialAccounts(self):
    sleep(2)
    self.find_element(self.controls["删除"]).click()
    self.find_element(self.controls["删除-确认"]).click()


def queryOfficialAccounts(self, proName):
    sleep(2)
    self.find_element(self.controls["请选择项目"]).click()
    sleep(1)
    self.find_element(self.controls["项目查询条件"]).send_keys(proName)
    sleep(2)
    self.find_element(self.controls["项目查询条件-第一个"]).click()
