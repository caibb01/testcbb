# -*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys

class articleContent(BasePage):
    controls = {
        "选择内容管理": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/ul/li[2]/div/span/span'),
        "选择原创文章": (By.XPATH, '//*[@id="sub1$Menu"]/li[3]/span'),
        # 新建
        "点击新建文章": (By.XPATH, '//span[text()="新 建"]/parent::button'),
        "获取页面名称": (By.XPATH, '//*[@id="rcDialogTitle0"]'),
        "输入标题": (By.XPATH, '//span[text()="标题："]/following-sibling::input'),
        "输入内容": (By.CLASS_NAME, "w-e-text"),
        "点击封面": (By.XPATH, '//*[text()="上传图片"]/../p'),
        "保存图片": (By.XPATH, '//div[3][@class="ant-modal-footer"]/div/button[2]'),
        "发布范围-全局": (By.XPATH, '//div[3]/div/div[@class="ant-radio-group ant-radio-group-outline"]/label[1]/span[2]'),
        "关联活动-开启": (By.XPATH, '//span[text()="开启"]/preceding-sibling::span'),
        "活动按钮名称": (By.XPATH, '//input[@placeholder="默认：点我报名"]'),
        "活动开始时间选择框": (By.XPATH, '//span/div/input[@placeholder="开始日期"]'),
        "活动结束时间选择框": (By.XPATH, '//span/div/input[@placeholder="结束日期"]'),
        "活动开始时间输入框": (By.XPATH, '//div[@class="ant-calendar-date-input-wrap"]/input[@placeholder="开始日期"]'),
        "活动结束时间输入框": (By.XPATH, '//div[@class="ant-calendar-date-input-wrap"]/input[@placeholder="结束日期"]'),
        "保存": (By.XPATH, '//span[text()="保 存"]/parent::button'),

        # 查询
        "选择发布状态": (By.XPATH, '//span[@class="components-common-SelectTree-index-module_14dB0"]/parent::div'),
        "发布状态输入框": (By.XPATH, '//input[@placeholder="请输入关键字"]'),
        "发布状态下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "选择全局": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]/div[1]'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/input'),
        "点击查询": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/button'),
        "编辑文章": (By.XPATH,
                 '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[8]/span/button[1]'),
        "发布文章": (By.XPATH,
                 '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[5]/button/span'),
        "确认发布": (By.XPATH, '//span[text()="确 定"]/parent::button'),

        # 操作文章
        "关闭文章": (By.XPATH, '//tr[1]/td[5]/button'),
        "确定按钮": (By.XPATH, '//span[text()="确 定"]/parent::button'),

        # 报名列表
        "报名列表": (By.XPATH, '//tr[1]/td[8]/span/button[3]'),
        "手机号输入框": (By.XPATH, '//input[@placeholder="请输入手机号搜索"]'),
        "搜索按钮": (By.XPATH, '//div[1]/span/button'),
        "导出": (By.XPATH, '//span[text()="导 出"]/parent::button'),
        "关闭弹窗": (By.XPATH, '//button[@class="ant-modal-close"]'),

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
        super(articleContent, self).__init__(driver)

    def select_Menu(self):
        # 打开应用菜单
        self.find_element(self.controls["选择内容管理"]).click()
        sleep(1)
        # 打开原创文章
        self.find_element(self.controls["选择原创文章"]).click()

    def operation_new_Function(self, titleName, content, imagePath):
        # 新建原创文章
        sleep(2)
        self.find_element(self.controls["点击新建文章"]).click()
        sleep(2)
        wzbt = self.find_element(self.controls["获取页面名称"]).text
        print("wzbt=",wzbt)
        if wzbt == u'新增文章':
            self.find_element(self.controls["输入标题"]).clear()
            self.find_element(self.controls["输入标题"]).send_keys(titleName)
            sleep(2)
            self.find_element(self.controls["输入内容"]).send_keys(content)
            self.find_element(self.controls["点击封面"]).click()
            sleep(2)
            self.upload(imagePath)
            # self.send_keys(imagePath)  # 发送文件地址
            # sleep(3)
            # self.send_keys("{ENTER}")
            # self.send_keys("{ENTER}")
            sleep(3)
            # 保存图片
            self.find_element(self.controls["保存图片"]).click()
            sleep(2)
            # 选择全局
            self.find_element(self.controls["发布范围-全局"]).click()
            self.find_element(self.controls["保存"]).click()
            sleep(2)

    def operation_query_Function(self, queryTitle):
        # 查询  先选择全局，再输入查询条件
        sleep(2)
        self.wait_eleVisible(self.controls['选择发布状态'])
        self.find_element(self.controls["选择发布状态"]).click()
        sleep(2)
        self.find_element(self.controls["选择全局"]).click()
        sleep(2)
        self.find_element(self.controls["输入查询条件"]).clear()
        self.find_element(self.controls["输入查询条件"]).send_keys(queryTitle)
        sleep(1)
        self.find_element(self.controls["点击查询"]).click()

    def operation_update_Function(self, newTitle, newContent):
        # 点击更新文章
        sleep(2)
        self.find_element(self.controls["编辑文章"]).click()
        sleep(2)
        self.find_element(self.controls["输入标题"]).clear()
        self.find_element(self.controls["输入标题"]).send_keys(newTitle)
        sleep(1)
        self.find_element(self.controls["输入内容"]).clear()
        self.find_element(self.controls["输入内容"]).send_keys(newContent)
        sleep(2)
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

    def save_article(self, params=None):
        # 新建原创文章-开启活动
        sleep(2)
        self.find_element(self.controls["点击新建文章"]).click()
        sleep(2)
        if params['title'] != '':
            self.find_element(self.controls["输入标题"]).clear()
            self.find_element(self.controls["输入标题"]).send_keys(params['title'])
            sleep(2)
        if params['content'] != '':
            self.find_element(self.controls["输入内容"]).send_keys(params['content'])
            self.find_element(self.controls["点击封面"]).click()
            sleep(1)
        if params['imagePath'] != '':
            sleep(2)
            self.upload(params['imagePath'])
            # self.send_keys(params['imagePath'])  # 发送文件地址
            # sleep(2)
            # self.send_keys("{ENTER}")
            # self.send_keys("{ENTER}")
            sleep(3)
            # 保存图片
            self.find_element(self.controls["保存图片"]).click()
            sleep(2)
        # 关联活动选择开启
        self.wait_eleVisible(self.controls["关联活动-开启"])
        self.find_element(self.controls["关联活动-开启"]).click()
        sleep(2)
        if params['button_name'] != '':
            # 输入活动按钮名称
            self.find_element(self.controls["活动按钮名称"]).send_keys(params['button_name'])
            sleep(1)
        if params['start_time'] != '':
            # 输入活动开始时间
            self.find_element(self.controls["活动开始时间选择框"]).click()
            self.find_element(self.controls["活动开始时间输入框"]).send_keys(params['start_time'])
            sleep(1)
        if params['end_time'] != '':
            # 输入活动结束时间
            self.find_element(self.controls["活动结束时间选择框"]).click()
            self.find_element(self.controls["活动结束时间输入框"]).send_keys(params['end_time'])
            sleep(1)
        # 点击保存
        self.find_element(self.controls["保存"]).click()

    def close_article(self, publish_status):
        # 关闭文章
        # 查询已发布的文章
        self.wait_eleVisible(self.controls["选择发布状态"])
        self.find_element(self.controls["选择发布状态"]).click()
        sleep(1)
        self.wait_eleVisible(self.controls["发布状态输入框"])
        self.find_element(self.controls["发布状态输入框"]).send_keys(publish_status)
        sleep(1)
        self.wait_eleVisible(self.controls["发布状态下拉列表"])
        i = -1
        i += 1
        self.find_elements(self.controls["发布状态下拉列表"], i).click()
        sleep(3)
        self.wait_eleVisible(self.controls["输入查询条件"])
        self.find_element(self.controls["输入查询条件"]).clear()
        sleep(1)
        self.find_element(self.controls["点击查询"]).click()
        sleep(3)
        self.wait_eleVisible(self.controls["关闭文章"])
        self.find_element(self.controls["关闭文章"]).click()
        sleep(2)
        self.wait_eleVisible(self.controls["确定按钮"])
        self.find_element(self.controls["确定按钮"]).click()

    def apply_list(self, params=None):
        # 报名列表
        # 查出已开启活动的文章
        self.wait_eleVisible(self.controls["选择发布状态"])
        self.find_element(self.controls["选择发布状态"]).click()
        sleep(1)
        self.wait_eleVisible(self.controls["发布状态输入框"])
        self.find_element(self.controls["发布状态输入框"]).clear()
        self.find_element(self.controls["发布状态输入框"]).send_keys(params['publish_status'])
        sleep(1)
        self.wait_eleVisible(self.controls["发布状态下拉列表"])
        i = -1
        i += 1
        self.find_elements(self.controls["发布状态下拉列表"], i).click()
        sleep(3)
        self.wait_eleVisible(self.controls["输入查询条件"])
        self.find_element(self.controls["输入查询条件"]).clear()
        self.find_element(self.controls["输入查询条件"]).send_keys(params['title'])
        sleep(1)
        self.find_element(self.controls["点击查询"]).click()
        sleep(2)
        # 打开报名列表
        self.wait_eleVisible(self.controls["报名列表"])
        self.find_element(self.controls["报名列表"]).click()
        sleep(2)
        # 通过手机号进行搜索
        self.wait_eleVisible(self.controls["手机号输入框"])
        self.find_element(self.controls["手机号输入框"]).send_keys(params['phone_number'])
        sleep(2)
        self.wait_eleVisible(self.controls["搜索按钮"])
        self.find_element(self.controls["搜索按钮"]).click()
        sleep(2)
        # 导出报名列表
        self.wait_eleVisible(self.controls["导出"])
        self.find_element(self.controls["导出"]).click()
        sleep(2)
        # 关闭弹窗
        self.wait_eleVisible(self.controls["关闭弹窗"])
        self.find_element(self.controls["关闭弹窗"]).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['下一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        self.refresh()
        sleep(2)
        # 点击下一页
        if self.check_button_clickable():
        # while (self.check_button_clickable()):
            nextNum = len(self.find_elements_list(self.controls['下一页']))
            if nextNum > 1:
                self.find_elements(self.controls['下一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的下一页']).click()

    def check_button_previous_page(self):
        # 检查上一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['上一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        if self.check_button_previous_page():
        # while (self.check_button_previous_page()):
            nextNum = len(self.find_elements_list(self.controls['上一页']))
            if nextNum > 1:
                self.find_elements(self.controls['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data / number_page)
        if page > 1:
            self.wait_eleVisible(self.controls['跳转至第几页'])
            self.find_element(self.controls['跳转至第几页']).send_keys(page + 1)
            sleep(2)
            self.find_element(self.controls['跳转至第几页']).send_keys(Keys.ENTER)
            sleep(2)

    def total_data(self):
        # 获取当前查询共计总记录
        if self.is_exist_element(self.controls['共计总记录']):
            return self.find_element(self.controls['共计总记录']).text
        return 1

    def number_page(self):
        # 获取每页的条数
        if self.is_exist_element(self.controls['每页条数']):
            return self.find_element(self.controls['每页条数']).text
        return 1
