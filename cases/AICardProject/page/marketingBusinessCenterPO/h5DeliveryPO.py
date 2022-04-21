#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.common.keys import Keys

class H5DeliveryPO(BasePage):
    control = {
        # 新增
        "新增按钮": (By.XPATH, '//span[text()="新 增"]/parent::button'),
        "H5单页名称": (By.XPATH, '//input[@placeholder="请输入H5单页名称"]'),
        "落地页-二级": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "搜索项目": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "项目下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "落地页-三级": (By.XPATH, '//div[text()="请选择页面"]'),
        "推广主体": (By.XPATH, '//div[3]/div[2]/div/div/div/span/div/div/div/div'),
        "推广主体-二级": (By.XPATH, '//form/div[3]/div[3]/div/div/div/span/div/div'),
        "选择访问授权": (By.XPATH, '//span[@class="ant-checkbox"]'),
        "投放渠道": (By.XPATH, '//span[text()="请选择投放渠道"]'),
        "投放渠道列表": (By.XPATH, '//ul[@class="ant-select-tree"]'),
        "渠道投入": (By.XPATH, '//input[@placeholder="请输入渠道投入金额"]'),
        "确定": (By.XPATH, '//div/button[2]'),
        "知道了": (By.XPATH, '//span[text()="知道了"]/parent::button'),

        # 编辑
        "编辑按钮": (By.XPATH, '//tr[1]/td[1]/button[1]'),

        # 复制链接
        "复制链接按钮": (By.XPATH, '//tr[1]/td[1]/button[2]'),

        # 客户明细
        "客户明细按钮": (By.XPATH, '//tr[1]/td[1]/button[3]'),
        "去看看": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),
        "下载": (By.XPATH, '//span[text()="下载"]/parent::button'),
        "关闭弹窗": (By.XPATH, '//button[@class="ant-drawer-close"]'),

        # 删除
        "删除按钮": (By.XPATH, '//tr[1]/td[1]/button[4]'),
        "确定删除": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),

        # 列表查询
        "推广主体一级下拉框": (By.XPATH, '//form/div/div[2]/div[1]/div/div/div/span/div/div/div/div[1]'),
        "推广主体二级下拉框": (By.XPATH, '//form/div/div[2]/div[2]/div/div/div/span/div/div'),
        "推广主体下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "搜索名称": (By.XPATH, '//input[@placeholder="请输入您想查看的H5单页名称"]'),
        "搜索按钮": (By.XPATH, '//button[@class="ant-btn fs-12 ml10 ant-btn-primary ant-btn-background-ghost"]'),

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
        super(H5DeliveryPO, self).__init__(driver)
        self.driver = driver

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def save_h5(self, params=None):
        # 新增h5
        # 点击新增按钮
        self.wait_eleVisible(self.control['新增按钮'])
        self.find_element(self.control['新增按钮']).click()
        sleep(2)
        # 输入标签名
        if params['name'] != '':
            self.wait_eleVisible(self.control['H5单页名称'])
            self.find_element(self.control['H5单页名称']).click()
            self.find_element(self.control['H5单页名称']).send_keys(params['name'])
            sleep(1)
        # 选择落地页
        self.wait_eleVisible(self.control['落地页-二级'])
        self.find_element(self.control['落地页-二级']).click()
        sleep(1)
        if params['project'] != '':
            self.find_elements(self.control['搜索项目'], 0).click()
            self.find_elements(self.control['搜索项目'], 0).send_keys(params['project'])
            sleep(1)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['项目下拉列表'])
        self.find_elements(self.control['项目下拉列表'], i).click()
        sleep(1)
        self.wait_eleVisible(self.control['落地页-三级'])
        self.select_by_index(self.control['落地页-三级'])
        # 选择推广主体
        self.wait_eleVisible(self.control['推广主体'])
        self.select_by_index(self.control['推广主体'])
        sleep(1)
        # i = -1
        # i += 1
        if self.is_exist_element(self.control['推广主体-二级']):
            self.find_element(self.control['推广主体-二级']).click()
            sleep(1)
            self.select_by_index(self.control['推广主体-二级'])
            # self.find_elements(self.control['推广主体下拉列表'], i).click()
            sleep(1)
        # 选择访问授权
        self.wait_eleVisible(self.control['选择访问授权'])
        self.find_elements(self.control['选择访问授权'], 0).click()
        sleep(1)
        # 选择投放渠道
        self.find_element(self.control['投放渠道']).click()
        i = -1
        i += 1
        self.find_elements(self.control['投放渠道列表'], i).click()
        sleep(1)
        if params['channel_into'] != '':
            self.wait_eleVisible(self.control['渠道投入'])
            self.find_element(self.control['渠道投入']).click()
            self.find_element(self.control['渠道投入']).send_keys(params['channel_into'])
            sleep(1)
        # 点击确定
        self.wait_eleVisible(self.control['确定'])
        self.find_element(self.control['确定']).click()

    def edit_h5(self, channel_into):
        # 编辑h5
        # 点击编辑按钮
        if self.is_exist_element(self.control['编辑按钮']):
            self.find_element(self.control['编辑按钮']).click()
            sleep(2)
            self.find_element(self.control['渠道投入']).click()
            self.find_element(self.control['渠道投入']).clear()
            self.find_element(self.control['渠道投入']).send_keys(channel_into)
            sleep(2)
            # 点击确定
            self.wait_eleVisible(self.control['确定'])
            self.find_element(self.control['确定']).click()
            sleep(2)
            self.wait_eleVisible(self.control['知道了'])
            self.find_element(self.control['知道了']).click()

    def copy_link(self):
        # 复制链接
        # 点击复制链接按钮
        if self.is_exist_element(self.control['复制链接按钮']):
            self.find_element(self.control['复制链接按钮']).click()

    def customer_detail(self):
        # 导出客户明细
        # 点击客户明细
        if self.is_exist_element(self.control['客户明细按钮']):
            self.find_element(self.control['客户明细按钮']).click()
            sleep(2)
            # 点击去看看按钮
            self.wait_eleVisible(self.control['去看看'])
            self.find_element(self.control['去看看']).click()
            sleep(6)
            # 点击下载
            self.wait_eleVisible(self.control['下载'])
            self.find_elements(self.control['下载'],0).click()
            sleep(3)
            # 点击关闭弹窗
            self.wait_eleVisible(self.control['关闭弹窗'])
            self.find_element(self.control['关闭弹窗']).click()

    def delete_h5(self):
        # 删除h5
        # 点击删除按钮
        if self.is_exist_element(self.control['删除按钮']):
            self.find_element(self.control['删除按钮']).click()
            sleep(2)
            # 点击确定按钮
            self.find_element(self.control['确定删除']).click()

    def search_h5(self, params=None):
        # 列表查询
        # 选择推广主体
        self.wait_eleVisible(self.control['推广主体一级下拉框'])
        self.select_by_index(self.control['推广主体一级下拉框'])
        sleep(1)
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['推广主体二级下拉框']):
            self.find_element(self.control['推广主体二级下拉框']).click()
            sleep(1)
            self.select_by_index(self.control['推广主体二级下拉框'])
            sleep(1)
        # 输入H5单页名称
        if params['name'] != '':
            self.wait_eleVisible(self.control['搜索名称'])
            self.find_element(self.control['搜索名称']).click()
            self.find_element(self.control['搜索名称']).send_keys(params['name'])
            sleep(1)
            # 点击搜索按钮
            self.wait_eleVisible(self.control['搜索按钮'])
            self.find_element(self.control['搜索按钮']).click()

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


