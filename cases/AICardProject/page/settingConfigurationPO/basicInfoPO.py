#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class BasicInfoPO(BasePage):
    controls = {
        "企业形象图-重新上传": (By.XPATH, '//div[@style="width: 150px; height: 120px;"]//i[@aria-label="图标: upload"]'),
        "企业形象图-删除": (By.XPATH, '//div[@style="width: 150px; height: 120px;"]//i[@aria-label="图标: delete"]'),
        "企业形象图-上传": (By.XPATH, '//div[@style="width: 150px; height: 120px;"]//p[text()="上传图片"]'),
        "企业LOGO-重新上传": (By.XPATH, '//div[@style="width: 100px; height: 100px;"]//i[@aria-label="图标: upload"]'),
        "企业LOGO-删除": (By.XPATH, '//div[@style="width: 100px; height: 100px;"]//i[@aria-label="图标: delete"]'),
        "企业LOGO-上传": (By.XPATH, '//div[@style="width: 100px; height: 100px;"]//p[text()="上传图片"]'),
        "授权背景图-重新上传": (By.XPATH, '//div[@style="width: 100px; height: 172.8px;"]//i[@aria-label="图标: upload"]'),
        "授权背景图-删除": (By.XPATH, '//div[@style="width: 100px; height: 172.8px;"]//i[@aria-label="图标: delete"]'),
        "授权背景图-上传": (By.XPATH, '//div[@style="width: 100px; height: 172.8px;"]//p[text()="上传图片"]'),
        "裁剪框-确定": (By.XPATH, '//span[text()="确 定"]//parent::button'),
        "保存": (By.XPATH, '//span[text()="保 存"]//parent::button')
    }


    # 企业形象图的上传、重新上传、删除
    def portrait_upload(self):
        sleep(2)
        print(self.find_elements_list(self.controls["企业形象图-上传"]))
        if self.find_elements_list(self.controls["企业形象图-上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\1.png'
            self.find_element(self.controls["企业形象图-上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("已有图片，无需上传,接下来分别执行以下操作：重新上传、删除")
            self.portrait_reUpload()
            self.portrait_delete()

    def portrait_reUpload(self):
        sleep(2)
        if self.find_elements_list(self.controls["企业形象图-重新上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\2.png'
            self.find_element(self.controls["企业形象图-重新上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.portrait_upload()
            self.portrait_reUpload()
            self.portrait_delete()

    def portrait_delete(self):
        sleep(2)
        if self.find_elements_list(self.controls["企业形象图-删除"]) != []:
            self.find_element(self.controls["企业形象图-删除"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.portrait_upload()
            self.portrait_reUpload()
            self.portrait_delete()

    # 企业LOGO的上传、重新上传、删除
    def logo_upload(self):
        sleep(2)
        print(self.find_elements_list(self.controls["企业LOGO-上传"]))
        if self.find_elements_list(self.controls["企业LOGO-上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\1.png'
            self.find_element(self.controls["企业LOGO-上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("已有图片，无需上传,接下来分别执行以下操作：重新上传、删除")
            self.logo_reUpload()
            self.logo_delete()

    def logo_reUpload(self):
        sleep(2)
        if self.find_elements_list(self.controls["企业LOGO-重新上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\2.png'
            self.find_element(self.controls["企业LOGO-重新上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.logo_upload()
            self.logo_reUpload()
            self.logo_delete()

    def logo_delete(self):
        sleep(2)
        if self.find_elements_list(self.controls["企业LOGO-删除"]) != []:
            self.find_element(self.controls["企业LOGO-删除"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.logo_upload()
            self.logo_reUpload()
            self.logo_delete()

    # 授权背景图的上传、重新上传、删除
    def bgPic_upload(self):
        sleep(2)
        print(self.find_elements_list(self.controls["授权背景图-上传"]))
        if self.find_elements_list(self.controls["授权背景图-上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\1.png'
            self.find_element(self.controls["授权背景图-上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("已有图片，无需上传,接下来分别执行以下操作：重新上传、删除")
            self.bgPic_reUpload()
            self.bgPic_delete()

    def bgPic_reUpload(self):
        sleep(2)
        if self.find_elements_list(self.controls["授权背景图-重新上传"]) != []:
            path = r'C:\Users\Yet03\Desktop\2.png'
            self.find_element(self.controls["授权背景图-重新上传"]).click()
            sleep(2)
            self.upload(filepath=path)
            sleep(3)
            self.find_element(self.controls["裁剪框-确定"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.bgPic_upload()
            self.bgPic_reUpload()
            self.bgPic_delete()

    def bgPic_delete(self):
        sleep(2)
        if self.find_elements_list(self.controls["授权背景图-删除"]) != []:
            self.find_element(self.controls["授权背景图-删除"]).click()
        else:
            print("还未上传图片，接下来执行上传图片、重新上传、删除操作")
            self.bgPic_upload()
            self.bgPic_reUpload()
            self.bgPic_delete()

    # 保存配置
    def save_info(self):
        self.find_element(self.controls["保存"]).click()