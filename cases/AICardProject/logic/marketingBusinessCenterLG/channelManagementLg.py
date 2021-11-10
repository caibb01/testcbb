#-*- coding:utf-8 -*-

from cases.AICardProject.page.marketingBusinessCenterPO.channelManagementPO import ChannelManagementPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class ChannelManagementLg():
    def __init__(self, driver):
        self.driver = driver
        self.channelManagementPO = ChannelManagementPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_channel_page(self):
        # 营销业务中心-渠道管理
        self.MenuManager.choiceMenu("营销业务中心", "营销业务中心-渠道管理")
        sleep(2)

    def save_channel(self, var):
        # 新增渠道码
        self.channelManagementPO.save_channel(params=var)

    def edit_channel(self, var):
        # 编辑渠道码
        self.channelManagementPO.edit_channel(params=var)

    def get_channel_code(self):
        # 获取渠道码
        self.channelManagementPO.get_channel_code()

    def copy_link(self):
        # 复制链接
        self.channelManagementPO.copy_link()

    def guest_detail(self):
        # 下载新客明细
        self.channelManagementPO.guest_detail()

    def exposure_detail(self):
        # 下载曝光明细
        self.channelManagementPO.guest_detail()

    def search_channel(self, var):
        # 列表查询
        self.channelManagementPO.search_channel(params=var)

    def delete_channel(self):
        # 删除渠道码
        self.channelManagementPO.delete_channel()

    def page_turning(self):
        # 点击下一页
        self.channelManagementPO.click_next()
        sleep(1)
        # 点击上一页
        self.channelManagementPO.click_previous()
        sleep(1)
        # 点击跳页
        self.channelManagementPO.jump_page()


    def single_path_code(self):
        # 获取单个路径码
        self.channelManagementPO.single_path_code()

    def batch_code(self):
        # 获取批量码
        self.channelManagementPO.batch_code()

    def switch_to_tab(self, var):
        # 切换tab
        self.channelManagementPO.switch_to_tab(tab_name=var)