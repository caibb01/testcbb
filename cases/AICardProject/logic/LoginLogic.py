# coding=utf-8
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
import sys
import os
from cases.AICardProject.page.LoginPage import LoginPage
from time import sleep
from myweb.utils.config import JsonConfig
from myweb.tools.getpath import getFilePath


class LoginLogic(BasePage):

    def __init__(self, driver):
        super(LoginLogic, self).__init__(driver)
        self.loginPage = LoginPage(driver)

    def login(self,url, username, password, orgname):
        self.driver.get(url)
        self.driver.maximize_window()
        self.loginPage.login(username=username, password=password, orgname=orgname)

    def logincheck(self, loginuser='yktest'):
        self.loginPage.login_check(loginuser)

    def openAI(self,ai_xpath = None):
        self.loginPage.openAI(ai_xpath)

    def enterAIAction(self):
        # 登录配置数据
        __data_path = os.path.join(os.path.abspath(os.path.join
                                                   (os.path.abspath(__file__), "../../../..")), 'data', 'loginInfo.json')

        data_path = os.path.join(getFilePath('loginInfo.json'))
        # 获取登录数据
        # __login_data = JsonConfig(__data_path).get()
        __login_data = JsonConfig(data_path).get()
        """
        登录并打开AI云店
        """
        self.login(username=__login_data['username'],
                   password=__login_data['password'],
                   orgname=__login_data['orgname'])
        self.loginPage.openAI()

    def enterAIAction(self):
        # 登录配置数据
        __data_path = os.path.join(os.path.abspath(os.path.join
                                                   (os.path.abspath(__file__), "../../../..")), 'data', 'loginInfo.json')

        data_path = os.path.join(getFilePath('loginInfo.json'))
        # 获取登录数据
        # __login_data = JsonConfig(__data_path).get()
        __login_data = JsonConfig(data_path).get()
        """
        登录并打开AI云店
        """
        self.login(username=__login_data['username'],
                   password=__login_data['password'],
                   orgname=__login_data['orgname'])
        self.loginPage.openAI()

    # def getpath(self):
    #     # 取上上级目录
    #     current_dir = os.path.abspath(os.path.dirname(__file__))
    #     parent_path = os.path.dirname(current_dir)
    #     return parent_path


if __name__ == '__main__':
    l = LoginLogic("test")
    # l =LoginLogic()
    # print(l.getpath())
