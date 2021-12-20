# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep


class MenuManager(BasePage):
    """
    菜单选择菜单统一管理
    """
    controls = {
        "首页": (By.XPATH, ".//*[text()='首页']"),
        # 因为存在个人中心首页的概念所以只能只能用xpath定位，而不能用文字
        "配置页-首页": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div/a[1]/div/div'),
        "配置页-首页配置": (By.XPATH, ".//*[text()='首页配置']"),
        "配置页-项目配置": (By.XPATH, ".//*[text()='项目配置']"),
        "配置页-个人中心": (By.XPATH, ".//*[text()='个人中心']"),
        "配置页-颜色": (By.XPATH, ".//*[text()='颜色']"),
        "内容管理": (By.XPATH, ".//*[text()='内容管理']"),
        "内容管理-项目管理": (By.XPATH, ".//*[text()='项目管理']"),
        "内容管理-公众号文章": (By.XPATH, ".//*[text()='公众号文章']"),
        "内容管理-原创文章": (By.XPATH, ".//*[text()='原创文章']"),
        "内容管理-图片管理": (By.XPATH, ".//*[text()='图片管理']"),
        "内容管理-视频管理": (By.XPATH, ".//*[text()='视频管理']"),
        "内容管理-H5链接": (By.XPATH, ".//*[text()='H5链接']"),
        "内容管理-标签管理": (By.XPATH, ".//*[text()='标签管理']"),
        "内容管理-海报管理": (By.XPATH, ".//*[text()='海报管理']"),
        "内容管理-小程序直播": (By.XPATH, ".//*[text()='小程序直播']"),
        "数据中心": (By.XPATH, ".//*[text()='数据中心']"),
        "营销业务中心": (By.XPATH, ".//*[text()='营销业务中心']"),
        "营销业务中心-弹窗管理": (By.XPATH, ".//*[text()='弹窗管理']"),
        "营销业务中心-渠道管理": (By.XPATH, ".//*[text()='一渠一码（原渠道管理）']"),
        "营销业务中心-任务中心": (By.XPATH, ".//span[text()='任务中心']"),
        "营销业务中心-预约看房管理": (By.XPATH, ".//*[text()='预约看房管理']"),
        "营销业务中心-角色功能管理": (By.XPATH, ".//*[text()='角色功能管理']"),
        "营销业务中心-评论": (By.XPATH, ".//span[text()='评论']"),
        "营销业务中心-H5单页": (By.XPATH, ".//span[text()='H5单页']"),
        "活动中心": (By.XPATH, ".//*[text()='活动中心']"),
        "活动中心-报名活动": (By.XPATH, ".//*[text()='报名活动']"),
        "活动中心-优惠券": (By.XPATH, ".//*[text()='优惠券']"),
        "活动中心-更多活动": (By.XPATH, ".//*[text()='更多活动']"),
        "用户管理": (By.XPATH, ".//*[text()='用户管理']"),
        "用户管理-客户台账": (By.XPATH, ".//*[text()='客户台账']"),
        "用户管理-员工管理": (By.XPATH, ".//*[text()='员工管理']"),
        "用户管理-数据查阅人":(By.XPATH,".//*[text()='数据查阅人']"),
        "用户管理-客群管理":(By.XPATH,".//*[text()='客群管理']"),
        "展示配置": (By.XPATH, ".//*[text()='展示配置']"),
        "展示配置-小程序首页": (By.XPATH, ".//*[text()='小程序首页']"),
        "展示配置-项目页": (By.XPATH, ".//*[text()='项目页']"),
        "展示配置-新页面": (By.XPATH, ".//*[text()='新页面']"),
        "展示配置-个人中心": (By.XPATH, ".//*[text()='个人中心']"),
        "展示配置-启动页": (By.XPATH, ".//*[text()='启动页']"),
        "展示配置-底部菜单栏": (By.XPATH, ".//*[text()='底部菜单栏']"),
        "展示配置-颜色配置": (By.XPATH, ".//*[text()='颜色配置']"),
        "合规配置": (By.XPATH, ".//*[text()='合规配置']"),
        "系统设置": (By.XPATH, ".//*[text()='系统设置']"),
        "系统设置-区域设置": (By.XPATH, ".//*[text()='区域设置']"),
        "系统设置-基础信息": (By.XPATH, ".//*[text()='基础信息']"),
        "系统设置-小程序跳转": (By.XPATH, ".//*[text()='小程序跳转']")
    }

    def __init__(self, driver):
        # super(MenuManager, self).__init__(driver)
        # self.MenuManager = MenuManager(driver)
        self.driver = driver

    def choiceMenu(self, firstLevelMenu="", SecondaryMenu=""):
        """
        :param firstLevelMenu: 一级菜单
        :param SecondaryMenu: 二级菜单
        :return:
        用来统一维护选择菜单入口
        1、判断是不是都为空，不为空则正常点击
        2、如果存在一个为空则直接点击
        3、两个都不为空则直接点击
        """
        if firstLevelMenu != "" and SecondaryMenu != "":
            self.find_element(self.controls[firstLevelMenu]).click()
            self.find_element(self.controls[SecondaryMenu]).click()
        elif firstLevelMenu != "" and SecondaryMenu == "":
            self.find_element(self.controls[firstLevelMenu]).click()
        else:
            return u"输入格式不正确！"
