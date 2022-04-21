# coding=utf-8
import unittest

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep


class LoginPage(BasePage):
    controls = {
        "更新说明弹窗的关闭按钮": (By.XPATH, "//button[@title='取消']"),
        "弹出框提示点击以后再说":(By.XPATH,"//button[text() = '以后再说']"),
        "企业号输入框": (By.CSS_SELECTOR, "#org_name"),
        "用户名输入框": (By.CSS_SELECTOR, "#user_name"),
        "密码输入框": (By.CSS_SELECTOR, "#password"),
        "登录按钮": (By.CSS_SELECTOR, "#login_btn"),
        "关闭登录广告弹窗": (By.XPATH, "//button[@class='update-dialog-close js_pop_close']"),
        "登录蒙层": (By.XPATH, "/html/body/div[6]/div/a"),
        # "获取登录用户名": (By.XPATH, '//*[@id="js_user_name"]'),
        "获取登录用户名": (By.XPATH, '//*[@id="yk_header"]/header/div/div[3]/div[2]/div[2]/div[1]/span[2]'),
        "更新说明":(By.XPATH, '//button[@title="取消"]'),
        "点击智慧名片测试版": (
            By.XPATH, './/*[text()="智慧名片测试版"]/../../div/div[@class="yzh-caro-box"]/div/ul/li/a/div[text()="AI云店"]'),
        "检查是否打开AI云店": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[1]/div[2]/p[2]')
    }

    def login(self, username, password, orgname):
        if self.is_exist_element(self.controls["企业号输入框"], 5):
            self.find_element(self.controls["企业号输入框"]).send_keys(orgname)
            self.find_element(self.controls["用户名输入框"]).send_keys(username)
            self.find_element(self.controls["密码输入框"]).send_keys(password)
            self.find_element(self.controls["登录按钮"]).click()

    def login_check(self, loginuser='400'):
        sleep(2)
        if self.is_exist_element(self.controls["更新说明"]):
            self.find_element(self.controls["更新说明"]).click()
        sleep(2)
        # qs = self.find_element(self.controls["关闭登录广告弹窗"]).text
        # if len(qs) == "":
        #     print(u"没有找到元素")
        #     self.driver.refresh()
        # else:
        #     # 关闭弹窗，弹窗有时候不是唯一的,这里对元素进行判断
        #     self.find_element(self.controls["关闭登录广告弹窗"]).click()
        #     sleep(2)
        #     if self.is_exist_element(self.controls["登录蒙层"]):
        #         self.find_element(self.controls["登录蒙层"]).click()
        # 检查是否登录成功
        # self.wait_eleVisible(self.controls["获取登录用户名"])
        # logintext = self.find_element(self.controls["获取登录用户名"]).text
        # print("logintext=", logintext)
        # print("loginuser=", loginuser)
        # if logintext == loginuser:
        #     print(u"登录成功！")
        # else:
        #     print(u"登录账号和预期不一致！")

    def openAI(self,ai_xpath = None):
        sleep(2)
        if (self.is_exist_element(self.controls["弹出框提示点击以后再说"])):
            self.find_element(self.controls['弹出框提示点击以后再说']).click()
        sleep(3)
        for i in range(2, 10):  # 也可以设置一个较大的数，一下到底
            js = "var q=document.documentElement.scrollTop={}".format(i * 50)  # javascript语句
            self.driver.execute_script(js)
        # 选择云店入口打开智慧名片测试版，存在的问题是，如果运营主体取消置顶会出现定位不到的现象---用xpath 解决了这个问题
        if self.is_exist_element(self.controls["更新说明弹窗的关闭按钮"]):
            self.find_element(self.controls["更新说明弹窗的关闭按钮"]).click()
        self.driver.find_element_by_xpath(ai_xpath).click()
        #self.find_element(self.controls["点击智慧名片测试版"]).click()
        sleep(6)
        bz = self.find_element(self.controls["检查是否打开AI云店"]).text
        if bz == u"智慧名片测试版":
            print(u"成功打开AI云店")
        else:
            print(u"打开失败")
        sleep(2)
