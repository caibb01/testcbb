# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from cases.AICardProject.page.LoginPage import LoginPage
from cases.AICardProject.logic.MenuManager import MenuManager
from cases.AICardProject.page.marketingBusinessCenterPO.ManageRolePage import ManageRolePage
from time import sleep


class ManageRoleLogic(BasePage):

    def __init__(self, driver):
        super(ManageRoleLogic, self).__init__(driver)
        self.loginPage = LoginPage(driver)
        self.manageRolePage = ManageRolePage(driver)
        self.menuManager = MenuManager(driver)

    def into_manageRole_page(self):
        self.menuManager.choiceMenu("营销业务中心", "营销业务中心-角色功能管理")

    def switch_to_tab(self, tab_name):
        """

        :param tab_name: 置业顾问/行销人员/全民营销/访客
        :return:
        """
        self.manageRolePage.switch_to_tab(tab_name)

    def editor_sales_info(self, params, throw_except=True):
        """
        编辑置业顾问信息
        :param params:
        :return:
        """
        self.manageRolePage.editor_sales_info(params, throw_except)

    def editor_marketing_info(self, params, throw_except=True):
        """
        编辑行销人员信息
        :param params:
        :return:
        """
        self.manageRolePage.editor_marketing_info(params, throw_except)

    def editor_broker_info(self, params, throw_except=True):
        """
        编辑全民营销信息
        :param params:
        :param throw_except:
        :return:
        """
        self.manageRolePage.editor_broker_info(params, throw_except)

    def editor_guest_info(self, params, throw_except=True):
        """
        编辑访客信息
        :param params:
        :param throw_except:
        :return:
        """
        self.manageRolePage.editor_guest_info(params, throw_except)

    def setUp_sales_info(self):
        """
        初始化置业顾问页面信息，将所有开关关闭
        :return:
        """
        # 进入置业顾问页面
        self.switch_to_tab("置业顾问")
        # 将开关都关掉
        params = {
            'customer_protection_switch': False
        }
        self.editor_sales_info(params=params, throw_except=False)

    def setUp_marketing_info(self):
        """
        初始化行销人员页面信息，将所有开关关闭
        :return:
        """
        # 进入行销人员页面
        self.switch_to_tab("行销人员")
        # 将开关都关掉
        params = {
            'customer_protection_switch': False
        }
        self.editor_marketing_info(params=params, throw_except=False)

    def setUp_broker_info(self):
        """
        初始化全民营销页面信息，将所有开关关闭
        :return:
        """
        self.switch_to_tab("全民营销")
        params = {
            'marketing': {
                'switch': False
            }
        }
        self.editor_broker_info(params=params, throw_except=False)

    def setUp_guest_info(self):
        """
        初始化访客页面信息，将所有开关关闭
        :return:
        """
        self.switch_to_tab("访客")
        params = {
            'protection': {
                    'switch': False
                    },
            'house_buying_process': False
        }
        self.editor_guest_info(params=params, throw_except=False)
