#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CommentsPO(BasePage):
    control = {
        "营销业务中心": (By.XPATH, '//span[text()="营销业务中心"]'),

        # 新建评论
        "新建评论": (By.XPATH, '//div[@class="components-common-PageBlockHeader-index-module_2tJ-g"]/div[2]/button'),
        "选择项目下拉框": (By.XPATH, '//div[@class="ant-col ant-col-21 right"]/div/div'),
        "选择项目下拉列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "项目输入框": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "昵称": (By.XPATH, '//input[@placeholder="默认昵称小程序用户 + (10000与100000随机取数)"]'),
        "上传头像": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_35VD_"]'),
        "裁剪框-确定": (By.XPATH, "//span[text()='确 定']/parent::button"),
        "选择标签": (By.XPATH, "//div/span[text()='五证齐全']"),
        "客户状态": (By.XPATH, "//div/span[text()='实在']"),
        "评价": (By.XPATH, "//textarea[@placeholder='请输入评价']"),
        "保存": (By.XPATH, '//div[2][@class="ant-modal-content"]/div[3]/div/button[2]'),

        # 回复评论
        "回复": (By.XPATH, "//tr[1]/td[5]/span/button[1]"),
        "选择职位": (By.XPATH, "//div[1]/div[2]/div[@class='flex-default mb10']/div/div/div"),
        "选择人员": (By.XPATH, '//ul[@class="ant-list-items"]/li[1]'),
        "选择人员输入框": (By.XPATH, '//input[@class="ant-input"]'),
        "选择人员搜索按钮": (By.XPATH, '//span[@class="ant-input-suffix"]/i'),
        "回复内容": (By.XPATH, '//textarea[@placeholder="请输入内容"]'),
        "保存按钮": (By.XPATH, '//span[text()="保 存"]/parent::button'),
        # '/html/body/div[5]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        # 删除
        "删除按钮": (By.XPATH, "//tr[1]/td[5]/span/button[2]"),
        "确定按钮": (By.XPATH, '//div/button[2][@class="ant-btn ant-btn-danger"]'),

        # 回复历史
        "回复历史": (By.XPATH, "//tr[1]/td[5]/span/button[3]"),
        "关闭窗口": (By.XPATH, "//span[@class='ant-modal-close-x']/parent::button"),
        # '/html/body/div[2]/div/div[2]/div/div[2]/button'

        # 列表查询
        "开始日期选择框": (By.XPATH, '//span/input[@placeholder="开始日期"]'),
        "开始日期输入框": (By.XPATH, '//div/div/input[@placeholder="开始日期"]'),
        "结束日期选择框": (By.XPATH, '//span/input[@placeholder="结束日期"]'),
        "结束日期输入框": (By.XPATH, '//div/div/input[@placeholder="结束日期"]'),
        "项目下拉框": (By.XPATH, '//div/div[1]/div[2]/div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "项目查询": (By.XPATH, '//div[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]/div/div[1]/input[@placeholder="请选择项目"]'),
        "项目选择列表": (By.XPATH, '//div[@class="ant-dropdown ant-dropdown-placement-bottomLeft"]/div/div[2][@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "查询按钮": (By.XPATH, '//div[3]/button[@class="ant-btn ant-btn-primary"]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
        "知道了":(By.XPATH,"//div[@class='ant-modal-confirm-btns']/button"),
        "回复关闭弹窗":(By.XPATH,'/html/body/div[6]/div/div[2]/div/div[2]/button/span/i'),

    }

    def __init__(self, driver):
        super(CommentsPO, self).__init__(driver)
        self.driver = driver

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def save_comments(self, params=None):
        # 新建评论
        # 点击新建评论按钮
        self.wait_eleVisible(self.control['新建评论'])
        self.find_element(self.control['新建评论']).click()
        # 选择项目
        self.wait_eleVisible(self.control['选择项目下拉框'])
        self.find_element(self.control['选择项目下拉框']).click()
        sleep(1)
        if params['project_name'] != '':
            ele = self.control['项目输入框']
            self.wait_eleVisible(ele)
            self.find_element(ele).click()
            self.find_element(ele).send_keys(params['project_name'])
            sleep(1)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['选择项目下拉列表'])
        self.find_elements(self.control['选择项目下拉列表'], i).click()
        sleep(1)
        # 输入昵称
        if params['nick_name'] != '':
            self.wait_eleVisible(self.control['昵称'])
            self.find_element(self.control['昵称']).click()
            self.find_element(self.control['昵称']).send_keys(params['nick_name'])
            sleep(1)
        # 上传头像
        if params['path'] != '':
            self.wait_eleVisible(self.control['上传头像'])
            choose = self.find_element(self.control['上传头像'])
            ActionChains(self.driver).click(choose).perform()
            sleep(2)
            self.upload(params['path'])
            sleep(2)
            self.wait_eleVisible(self.control['裁剪框-确定'])
            self.find_element(self.control['裁剪框-确定']).click()
            sleep(2)
        # 选择标签
        self.wait_eleVisible(self.control['选择标签'])
        self.find_element(self.control['选择标签']).click()
        sleep(1)
        # 选择客户状态
        self.wait_eleVisible(self.control['客户状态'])
        self.find_element(self.control['客户状态']).click()
        sleep(1)
        # 输入评价
        if params['comments'] != '':
            self.wait_eleVisible(self.control['评价'])
            self.find_element(self.control['评价']).click()
            self.find_element(self.control['评价']).send_keys(params['comments'])
            sleep(1)
        # 点击保存
        self.wait_eleVisible(self.control['保存'])
        self.find_element(self.control['保存']).click()

    def reply_comments(self, params=None):
        # 回复评论
        # 点击回复按钮
        self.wait_eleVisible(self.control['回复'])
        self.find_element(self.control['回复']).click()
        sleep(2)
        # # 选择职位
        # self.wait_eleVisible(self.control['选择职位'])
        # self.select_by_index(self.control['选择职位'])
        # 选择人员
        # if params['name'] != '':
        #     self.wait_eleVisible(self.control['选择人员输入框'])
        #     self.find_element(self.control['选择人员输入框']).click()
        #     self.find_element(self.control['选择人员输入框']).send_keys(params['name'])
        #     sleep(1)
        #     self.wait_eleVisible(self.control['选择人员搜索按钮'])
        #     self.find_element(self.control['选择人员搜索按钮']).click()
        #     sleep(2)
        if self.is_exist_element(self.control['选择人员']):
            self.wait_eleVisible(self.control['选择人员'])
            self.find_element(self.control['选择人员']).click()
            sleep(1)
            # 输入回复内容
            if params['reply_content'] != '':
                self.wait_eleVisible(self.control['回复内容'])
                self.find_element(self.control['回复内容']).click()
                self.find_element(self.control['回复内容']).send_keys(params['reply_content'])
                sleep(2)
        # 点击保存
        # self.wait_eleVisible(self.control['保存按钮'])
        self.find_elements(self.control['保存按钮'], 1).click()
        sleep(2)
        if self.is_exist_element(self.control['知道了']):
            self.find_element(self.control['知道了']).click()
            sleep(2)
            self.find_element(self.control['回复关闭弹窗']).click()

    def delete_comments(self):
        # 删除评论
        # 点击删除按钮
        sleep(2)
        self.wait_eleVisible(self.control['删除按钮'])
        self.find_element(self.control['删除按钮']).click()
        # 点击确定
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()

    def reply_histroy(self):
        # 查看回复历史
        # 点击回复历史
        self.wait_eleVisible(self.control['回复历史'])
        self.find_element(self.control['回复历史']).click()
        sleep(1)
        # 关闭窗口
        # self.wait_eleVisible(self.control['关闭窗口'])
        # self.find_element(self.control['关闭窗口']).click()

    def search_comments(self, params=None):
        # 列表查询
        # 选择开始日期
        self.wait_eleVisible(self.control['开始日期选择框'])
        self.find_element(self.control['开始日期选择框']).click()
        sleep(1)
        if params['start_date'] != '':
            self.wait_eleVisible(self.control['开始日期输入框'])
            self.find_element(self.control['开始日期输入框']).click()
            self.find_element(self.control['开始日期输入框']).send_keys(params['start_date'])
            sleep(1)
            self.wait_eleVisible(self.control['营销业务中心'])
            self.find_element(self.control['营销业务中心']).click()
            sleep(1)

        # 选择结束日期
        self.wait_eleVisible(self.control['结束日期选择框'])
        self.find_element(self.control['结束日期选择框']).click()
        sleep(1)
        if params['end_date'] != '':
            self.wait_eleVisible(self.control['结束日期输入框'])
            self.find_element(self.control['结束日期输入框']).click()
            self.find_element(self.control['结束日期输入框']).send_keys(params['end_date'])
            sleep(1)
            self.wait_eleVisible(self.control['营销业务中心'])
            self.find_element(self.control['营销业务中心']).click()
            sleep(1)
        # 选择项目
        self.wait_eleVisible(self.control['项目下拉框'])
        self.find_element(self.control['项目下拉框']).click()
        sleep(1)
        if params['project_name'] != '':
            self.wait_eleVisible(self.control['项目查询'])
            self.find_element(self.control['项目查询']).click()
            self.find_element(self.control['项目查询']).send_keys(params['project_name'])
            sleep(2)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['项目选择列表'])
        self.find_elements(self.control['项目选择列表'], i).click()
        # 点击查询
        self.wait_eleVisible(self.control['查询按钮'])
        self.find_element(self.control['查询按钮']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum)-1)):
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
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        while(self.check_button_previous_page()):
            nextNum = len(self.find_elements_list(self.control['上一页']))
            if nextNum > 1:
                self.find_elements(self.control['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.control['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data/number_page)
        if page > 1:
            self.wait_eleVisible(self.control['跳转至第几页'])
            self.find_element(self.control['跳转至第几页']).send_keys(page+1)
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