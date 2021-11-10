#-*- coding:utf-8 -*-

from cases.AICardProject.page.marketingBusinessCenterPO.h5DeliveryPO import H5DeliveryPO, sleep
from cases.AICardProject.logic.MenuManager import MenuManager

class H5DeliveryLg():
    def __init__(self, driver):
        self.driver = driver
        self.h5DeliveryPO = H5DeliveryPO(driver)
        self.MenuManager = MenuManager(driver)

    def into_h5_page(self):
        # 营销业务中心-H5单页
        self.MenuManager.choiceMenu("营销业务中心", "营销业务中心-H5单页")
        sleep(3)

    def save_h5(self, var):
        # 新增h5
        self.h5DeliveryPO.save_h5(params=var)

    def h5_detail(self):
        # 查看h5
        self.h5DeliveryPO.h5_detail()

    def customer_detail(self):
        # 导出客户明细
        self.h5DeliveryPO.customer_detail()

    def copy_link(self):
        # 复制链接
        self.h5DeliveryPO.copy_link()

    def delete_h5(self):
        # 删除h5
        self.h5DeliveryPO.delete_h5()

    def search_h5(self, var):
        # 列表查询
        self.h5DeliveryPO.search_h5(params=var)

    def page_turning(self):
        # 点击下一页
        self.h5DeliveryPO.click_next()
        sleep(1)
        # 点击上一页
        self.h5DeliveryPO.click_previous()
        sleep(1)
        # 点击跳页
        self.h5DeliveryPO.jump_page()
