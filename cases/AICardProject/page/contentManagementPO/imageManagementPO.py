#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

class imageManagementPO(BasePage):
    control = {
        # 上传图片
        "上传图片按钮": (By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'),
        "标题": (By.XPATH, '//input[@id="title"]'),
        "关联类型-全局": (By.XPATH, '//div[@class="ant-radio-group ant-radio-group-outline"]/label[1]/span[1]'),
        "关联类型-项目": (By.XPATH, '//div[@class="ant-radio-group ant-radio-group-outline"]/label[2]/span[1]'),
        "点击关联项目": (By.XPATH, '//div[text()="请选择关联项目"]'),
        "点击上传图片": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_35VD_"]'),
        "确认保存": (By.XPATH, '//div/button[2][@class="ant-btn ant-btn-primary"]'),

        # 图片详情
        "详情按钮": (By.XPATH, '//div[1]/div[2]/div[2]/button[1][@class="ant-btn pages-manager_image-content-component-item-image-index-module_1ppYW mr10 ant-btn-primary"]'),
        "图片区域": (By.XPATH, '//span[@class="ant-upload"]/div/div'),
        # '//div[@class="components-common-Uploader-ui-rc-normal-module_1XPht"]'
        "查看大图": (By.XPATH, '//button[@class="ant-btn ant-btn-default"]'),
        "关闭大图": (By.XPATH, '//div/div[2]/i[@class="react-viewer-icon react-viewer-icon-close"]'),
        "删除图片": (By.XPATH, '//div/div[2]/i[2][@class="anticon anticon-delete components-common-Uploader-ui-rc-normal-module_V-8Ba"]'),
        "重新上传图片": (By.XPATH, '//div/div[2]/i[1][@class="anticon anticon-upload components-common-Uploader-ui-rc-normal-module_V-8Ba"]'),
        "弹框空白处": (By.XPATH, '//form[@class="ant-form ant-form-horizontal"]'),

        # 删除图片
        "删除按钮": (By.XPATH, '//div[1]/div[2]/div[2]/button[2][@class="ant-btn pages-manager_image-content-component-item-image-index-module_1ppYW ant-btn-default"]'),
        "确定按钮": (By.XPATH, '//div/div[2]/button[2][@class="ant-btn ant-btn-primary"]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
    }

    def __init__(self, driver):
        super(imageManagementPO, self).__init__(driver)
        self.driver = driver

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def upload_image(self, params=None):
        # 上传图片
        # 点击上传图片按钮
        self.wait_eleVisible(self.control['上传图片按钮'])
        self.find_element(self.control['上传图片按钮']).click()
        sleep(2)
        # 输入标题
        if params['title'] != '':
            self.wait_eleVisible(self.control['标题'])
            self.find_element(self.control['标题']).click()
            self.find_element(self.control['标题']).send_keys(params['title'])
            sleep(1)
        # 选择关联类型
        self.wait_eleVisible(self.control['关联类型-全局'])
        self.find_element(self.control['关联类型-全局']).click()
        sleep(1)
        # 上传图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['点击上传图片'])
            choose = self.find_element(self.control['点击上传图片'])
            ActionChains(self.driver).click(choose).perform()
            sleep(2)
            self.upload(params['path'])
            sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确认保存'])
        self.find_element(self.control['确认保存']).click()

    def image_detail(self, params=None):
        # 查看图片详情
        # 点击详情按钮
        self.wait_eleVisible(self.control['详情按钮'])
        self.find_element(self.control['详情按钮']).click()
        sleep(2)
        # 修改标题
        if params['title'] != '':
            self.wait_eleVisible(self.control['标题'])
            self.find_element(self.control['标题']).click()
            self.find_element(self.control['标题']).clear()
            self.find_element(self.control['标题']).send_keys(params['title'])
            sleep(1)
        # # 选择关联类型
        # self.wait_eleVisible(self.control['关联类型-项目'])
        # self.find_element(self.control['关联类型-项目']).click()
        # sleep(1)
        # # 选择关联项目
        # self.wait_eleVisible(self.control['点击关联项目'])
        # self.select_by_index(self.control['点击关联项目'])
        # sleep(1)
        # # 点击弹框空白处
        # self.wait_eleVisible(self.control['弹框空白处'])
        # self.find_element(self.control['弹框空白处']).click()
        # sleep(1)
        # 查看大图再关闭
        self.wait_eleVisible(self.control['查看大图'])
        self.find_element(self.control['查看大图']).click()
        sleep(2)
        self.wait_eleVisible(self.control['关闭大图'])
        self.find_element(self.control['关闭大图']).click()
        sleep(1)
        # 鼠标移动到图片区域
        self.wait_eleVisible(self.control['图片区域'])
        self.move_mouse_to_element(self.control['图片区域'])
        # 删除原有图片再上传图片
        if params['path'] != '':
            # self.wait_eleVisible(self.control['删除图片'])
            # self.find_element(self.control['删除图片']).click()
            # sleep(1)
            self.wait_eleVisible(self.control['重新上传图片'])
            choose = self.find_element(self.control['重新上传图片'])
            ActionChains(self.driver).click(choose).perform()
            sleep(2)
            self.upload(params['path'])
            sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确认保存'])
        self.find_element(self.control['确认保存']).click()

    def delete_image(self):
        # 删除图片
        # 点击删除按钮
        self.wait_eleVisible(self.control['删除按钮'])
        self.find_element(self.control['删除按钮']).click()
        # 点击确定
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        while (self.check_button_clickable()):
            nextNum = len(self.find_elements_list(self.control['下一页']))
            if nextNum > 1:
                self.find_elements(self.control['下一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.control['获取可点击的下一页']).click()

    def check_button_previous_page(self):
        # 检查上一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['上一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        while (self.check_button_previous_page()):
            nextNum = len(self.find_elements_list(self.control['上一页']))
            if nextNum > 1:
                self.find_elements(self.control['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.control['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data / number_page)
        if page > 1:
            self.wait_eleVisible(self.control['跳转至第几页'])
            self.find_element(self.control['跳转至第几页']).send_keys(page + 1)
            sleep(2)
            self.find_element(self.control['跳转至第几页']).send_keys(Keys.ENTER)
            sleep(2)

    def total_data(self):
        # 获取当前查询共计总记录
        if self.is_exist_element(self.control['共计总记录']):
            return self.find_element(self.control['共计总记录']).text
        return 1

    def number_page(self):
        # 获取每页的条数
        if self.is_exist_element(self.control['每页条数']):
            return self.find_element(self.control['每页条数']).text
        return 1
