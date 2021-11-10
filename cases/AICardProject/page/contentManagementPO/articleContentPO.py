#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.keys import Keys
from pymouse import PyMouse
from pykeyboard import PyKeyboard
import os

class articleContent(BasePage):
    controls = {
        "选择内容管理": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/ul/li[2]/div/span/span'),
        "选择原创文章": (By.XPATH, '//*[@id="sub1$Menu"]/li[3]/span'),
        "点击新建文章": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button'),
        "获取页面名称": (By.XPATH, '//*[@id="rcDialogTitle0"]'),
        "输入标题": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[1]/input'),
        "输入内容": (By.CLASS_NAME, "w-e-text"),
        "点击封面": (By.XPATH, '//*[text()="上传图片"]/../p'),
                           # '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]'),
        "保存图片": (By.XPATH, "/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]"),
        "发布范围-全局": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/div/div/label[1]/span[2]'),
        # "关联活动": (By.XPATH, "/html/body/div[6]/div/a"),
        "保存": (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[7]/div/button[1]"),
        # 查询
        "选择发布状态": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[1]/div'),
        "选择全局": (By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div[1]"),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/input'),
        "点击查询": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/button'),
        "编辑文章": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/button[1]'),
        "发布文章": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/button/span'),
        "确认发布": (By.XPATH, '/html/body/div[6]/div/div[2]/div/div[2]/div/div/div[2]/button[2]'),
        "保存": (By.XPATH, "/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[7]/div/button[1]")

    }
    # 图片文件路径
    __image_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                                'image')

    def __init__(self, driver):
        super(articleContent, self).__init__(driver)


    def select_Menu(self):
        # 打开应用菜单
        self.find_element(self.controls["选择内容管理"]).click()
        sleep(1)
        # 打开原创文章
        self.find_element(self.controls["选择原创文章"]).click()


    def operation_new_Function(self, titleName, content):
        # 新建原创文章
        sleep(2)
        self.find_element(self.controls["点击新建文章"]).click()
        sleep(2)
        wzbt = self.find_element(self.controls["获取页面名称"]).text
        print(wzbt)
        if wzbt == u'新增文章':
            self.find_element(self.controls["输入标题"]).clear()
            self.find_element(self.controls["输入标题"]).send_keys(
                titleName)
            sleep(2)
            self.find_element(self.controls["输入内容"]).send_keys(content)
            self.find_element(self.controls["点击封面"]).click()
            sleep(1)

            path =os.path.join(self.__image_path, '200-200.jpg')
            print(path)
            self.send_keys(path)  # 发送文件地址
            self.send_keys("{ENTER}")
            sleep(2)
            # 保存图片
            self.find_element(self.controls["保存图片"]).click()
            sleep(2)
            # 选择全局
            self.find_element(self.controls["发布范围-全局"]).click()
            self.find_element(self.controls["保存"]).click()
            sleep(2)

    def operation_query_Function(self, queryTitle):
        # 查询  先选择全局，再输入查询条件
        self.find_element(self.controls["选择发布状态"]).click()
        self.find_element(self.controls["选择全局"]).click()
        self.find_element(self.controls["输入查询条件"]).clear()
        self.find_element(self.controls["输入查询条件"]).send_keys(queryTitle)
        self.find_element(self.controls["点击查询"]).click()


    def operation_update_Function(self, titleName, content):
        # 点击更新文章
        sleep(2)
        self.find_element(self.controls["编辑文章"]).click()
        sleep(2)
        self.find_element(self.controls["输入标题"]).clear()
        self.find_element(self.controls["输入标题"]).send_keys(titleName)
        self.find_element(self.controls["输入内容"]).clear()
        self.find_element(self.controls["输入内容"]).send_keys(content)
        self.find_element(self.controls["保存"]).click()
        sleep(2)

    def operation_state_Function(self):
        # 发布文章,这里有个弊端，如果状态不对，依然可以进行点就修改状态
        sleep(2)
        self.find_element(self.controls["发布文章"]).click()
        sleep(2)
        self.find_element(self.controls["确认发布"]).click()

        sleep(2)
        return u"发布成功！"


