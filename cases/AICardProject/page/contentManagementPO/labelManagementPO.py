#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

class LabelManagementPO(BasePage):
    control = {
        # 切换tab
        "项目楼盘": (By.XPATH, '//div[text()="项目楼盘"]'),
        "报名活动": (By.XPATH, '//div[text()="报名活动"]'),
        "优惠券": (By.XPATH, '//div[text()="优惠券"]'),
        "原创文章": (By.XPATH, '//div[text()="原创文章"]'),
        "公众号文章": (By.XPATH, '//div[text()="公众号文章"]'),
        "活动中心": (By.XPATH, '//div[text()="活动中心"]'),

        # 新增标签
        "新增标签": (By.XPATH, '//span[text()="新增标签"]/parent::button'),
        "报名活动-新增标签": (By.XPATH, '//div[2]/div[3][@class="tr"]/button[@class="ant-btn ant-btn-primary"]'),
        "标签名": (By.XPATH, '//input[@placeholder="请输入名称（1-4个字符）"]'),
        "关联项目选择框": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "关联项目下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "项目输入框": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "确定": (By.XPATH, '//div/button[2][@class="ant-btn ant-btn-primary"]'),

        # 添加关联关系
        "添加按钮": (By.XPATH, '//div[3][@class="tr"]/button[@class="ant-btn ant-btn-primary"]'),
        "勾选框1": (By.XPATH, '//tr[2]/td[1]/span/label/span'),
        "勾选框2": (By.XPATH, '//tr[3]/td[1]/span/label/span'),
        "城市筛选框": (By.XPATH, '//span[text()="请选择地区"]'),
        "城市输入框": (By.XPATH, '//input[@placeholder="输入城市名进行搜索"]'),
        "搜索按钮": (By.XPATH, '//button[@class="ant-btn ant-input-search-button ant-btn-primary"]'),
        "选择全局": (By.XPATH, '//span[text()="全 局"]/parent::button'),
        "取消按钮": (By.XPATH, '//span[text()="取 消"]/parent::button'),
        "确定添加": (By.XPATH, '//span[text()="确 定"]/parent::button'),
        # "确定添加": (By.XPATH,'/html/body/div[3]/div/div[2]/div/div[2]/div[3]/div/button[2]'),
        # '//div[3]/div/button[2]'

        # 删除关联
        "删除按钮": (By.XPATH, '//tr[1]/td[4]/button'),
        "确定按钮": (By.XPATH, '//div/div[2][@class="ant-modal-confirm-btns"]/button[2]'),

        # 删除标签
        "标签": (By.XPATH, '//span[text()="JK标签"]'),
        "删除": (By.XPATH, '//span[text()="JK标签"]/following-sibling::i[text()="x"]'),
        "确定删除": (By.XPATH, '//div[2][@class="ant-modal-confirm-btns"]/button[2]'),

        # 排序
        "上移": (By.XPATH, '//tr[2]/td[3]/button[1]'),
        "下移": (By.XPATH, '//tr[1]/td[3]/button[2]'),
        "置顶": (By.XPATH, '//tr[2]/td[3]/button[3]'),

        # 添加关联关系-翻页
        "每页条数": (By.XPATH, '//div[2]/div/div/div/div[@class="ant-select-selection__rendered"]'),
        "共计总记录": (By.XPATH, '//div[2]/div/span[@class="primary"]'),
        "上一页": (By.XPATH, '//div[2]/ul/li[@title="上一页"]'),
        "下一页": (By.XPATH, '//div[2]/ul/li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "关闭按钮": (By.XPATH, '//button[@class="ant-modal-close"]'),
    }

    def __init__(self, driver):
        super(LabelManagementPO, self).__init__(driver)
        self.driver = driver

    def switch_to_tab(self, tab_name):
        # 切换tab 公共方法
        if tab_name == '项目楼盘':
            self.wait_eleVisible(self.control['项目楼盘'])
            self.find_element(self.control['项目楼盘']).click()
        if tab_name == '报名活动':
            self.wait_eleVisible(self.control['报名活动'])
            self.find_element(self.control['报名活动']).click()
        if tab_name == '优惠券':
            self.wait_eleVisible(self.control['优惠券'])
            self.find_element(self.control['优惠券']).click()
        if tab_name == '原创文章':
            self.wait_eleVisible(self.control['原创文章'])
            self.find_element(self.control['原创文章']).click()
        if tab_name == '公众号文章':
            self.wait_eleVisible(self.control['公众号文章'])
            self.find_element(self.control['公众号文章']).click()
        if tab_name == '活动中心':
            self.wait_eleVisible(self.control['活动中心'])
            self.find_element(self.control['活动中心']).click()
        sleep(2)

    def new_label(self, params=None):
        # 新增标签
        self.refresh()
        sleep(2)
        # 点击新增标签按钮
        self.wait_eleVisible(self.control['新增标签'])
        self.find_element(self.control['新增标签']).click()
        sleep(2)
        # 输入标签名
        if params['label_name'] != '':
            self.wait_eleVisible(self.control['标签名'])
            self.find_element(self.control['标签名']).click()
            self.find_element(self.control['标签名']).send_keys(params['label_name'])
            sleep(1)
        # 选择关联项目
        self.wait_eleVisible(self.control['关联项目选择框'])
        self.find_element(self.control['关联项目选择框']).click()
        sleep(1)
        if params['project_name'] != '':
            self.wait_eleVisible(self.control['项目输入框'])
            self.find_element(self.control['项目输入框']).click()
            self.find_element(self.control['项目输入框']).send_keys(params['project_name'])
            sleep(2)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['关联项目下拉列表'])
        self.find_elements(self.control['关联项目下拉列表'], i).click()
        sleep(1)
        self.wait_eleVisible(self.control['确定'])
        self.find_element(self.control['确定']).click()

    def add_association(self, params=None):
        # 添加关联关系
        # # 选择刚添加的标签
        # self.find_element(self.control['标签']).click()
        # 点击添加按钮
        self.wait_eleVisible(self.control['添加按钮'])
        self.find_element(self.control['添加按钮']).click()
        sleep(2)
        # 选择城市
        self.wait_eleVisible(self.control['城市筛选框'])
        self.find_element(self.control['城市筛选框']).click()
        sleep(1)
        if params['city_name'] != '':
            self.wait_eleVisible(self.control['城市输入框'])
            self.find_element(self.control['城市输入框']).click()
            self.find_element(self.control['城市输入框']).send_keys(params['city_name'])
            sleep(1)
            self.wait_eleVisible(self.control['搜索按钮'])
            self.find_element(self.control['搜索按钮']).click()
            sleep(1)
        self.wait_eleVisible(self.control['选择全局'])
        self.find_element(self.control['选择全局']).click()
        sleep(1)
        # 点击勾选框
        self.wait_eleVisible(self.control['勾选框1'])
        self.find_element(self.control['勾选框1']).click()
        sleep(2)
        self.wait_eleVisible(self.control['勾选框2'])
        self.find_element(self.control['勾选框2']).click()
        sleep(3)
        # 点击确定
        # for i in range(2, 10):  # 也可以设置一个较大的数，一下到底
        #     js = "var q=document.documentElement.scrollTop={}".format(i * 100)  # javascript语句
        #     self.driver.execute_script(js)
        # sleep(3)
        # if self.is_exist_element(self.control['确定添加']):
        #     self.find_element(self.control['确定添加']).click()
        # if self.is_exist_element(self.control['确定']):
        #     self.find_element(self.control['确定']).click()

    def del_association(self):
        # 删除关联关系
        # 点击删除按钮
        if self.is_exist_element(self.control['删除按钮']):
            self.wait_eleVisible(self.control['删除按钮'])
            self.find_element(self.control['删除按钮']).click()
            sleep(1)
            self.wait_eleVisible(self.control['确定按钮'])
            self.find_element(self.control['确定按钮']).click()

    def del_label(self):
        # 删除标签
        # 鼠标悬浮在标签上
        self.wait_eleVisible(self.control['标签'])
        self.move_mouse_to_element(self.control['标签'])
        # 点击删除按钮
        self.wait_eleVisible(self.control['删除'])
        self.find_element(self.control['删除']).click()
        sleep(1)
        self.wait_eleVisible(self.control['确定删除'])
        self.find_element(self.control['确定删除']).click()

    def label_sort(self):
        # 关联数据排序
        # 点击上移按钮
        if self.is_exist_element(self.control['上移']):
            self.find_element(self.control['上移']).click()
            sleep(2)
        # 点击下移按钮
        if self.is_exist_element(self.control['下移']):
             self.find_element(self.control['下移']).click()
             sleep(2)
        # 点击置顶按钮
        if self.is_exist_element(self.control['置顶']):
            self.find_element(self.control['置顶']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # sleep(2)
        # self.find_element(self.control['添加按钮']).click()
        # sleep(2)
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
            # sleep(2)
            # self.find_element(self.control['确定添加']).click()
            # sleep(2)


