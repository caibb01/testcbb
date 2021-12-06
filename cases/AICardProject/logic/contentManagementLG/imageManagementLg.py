# coding=utf-8
from cases.AICardProject.page.contentManagementPO.imageManagementPO import imageManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager


class imageManagementLg():

    def __init__(self, driver):
        self.driver = driver
        self.MenuManager = MenuManager(driver)
        self.imageManagementPO = imageManagementPO(driver)

    def into_imageManagement_page(self):
        # 打开内容管理-图片管理
        self.MenuManager.choiceMenu("内容管理", "内容管理-图片管理")
        sleep(2)

    def upload_image(self, var):
        # 上传图片
        self.imageManagementPO.upload_image(params=var)

    def image_detail(self, var):
        # 查看图片详情
        self.imageManagementPO.image_detail(params=var)

    def delete_image(self):
        # 删除图片
        self.imageManagementPO.delete_image()

    def page_turning(self):
        # 翻页
        # 点击下一页
        self.imageManagementPO.click_next()
        sleep(2)
        # 点击上一页
        self.imageManagementPO.click_previous()
        sleep(2)
        # 点击跳页
        self.imageManagementPO.jump_page()
