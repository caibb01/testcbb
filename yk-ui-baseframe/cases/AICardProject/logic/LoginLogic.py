# coding=utf-8
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
import sys
from cases.AICardProject.page.LoginPage import LoginPage
from time import sleep


class LoginLogic(BasePage):

    def __init__(self, driver):
        super(LoginLogic, self).__init__(driver)
        self.loginPage = LoginPage(driver)

    def login(self, username, password, orgname):
        self.driver.get('https://test-qmyxcg.myscrm.com.cn/login.shtml')
        self.driver.maximize_window()
        self.loginPage.login(username=username, password=password, orgname=orgname)

    def logincheck(self, loginuser='400'):
        self.loginPage.login_check(loginuser)

    def openAI(self):
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