#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class ChannelManagementPO(BasePage):
    control = {
        # 切换tab
        "渠道码": (By.XPATH, '//button[@class="ant-btn ant-btn-primary ant-btn-lg"]'),
        "获取路径码": (By.XPATH, '//button[@class="ant-btn ml20 ant-btn-default ant-btn-lg"]'),
        "获取单个路径码": (By.XPATH, '//div[@class="ant-tabs-tab-active ant-tabs-tab"]'),
        "获取批量码": (By.XPATH, '//div/div[2][@class=" ant-tabs-tab"]'),

        # 新增
        "新增按钮": (By.XPATH, '//button[@class="ant-btn fs-12 ml10 ant-btn-primary"]'),
        "渠道名称": (By.XPATH, '//input[@placeholder="请输入渠道名称"]'),
        "落地页一级下拉框": (By.XPATH, '//form[@class="ant-form ant-form-horizontal manager-channel-list-form"]/div[2]/div[2]/div/div/div/span/div'),
        "落地页二级下拉框": (By.XPATH, '//form/div[2]/div[3]/div/div/div/span/div/div'),
        "推广主体-一级": (By.XPATH, '//form/div[3]/div[2]/div/div/div/span/div/div/div'),
        "推广主体-二级": (By.XPATH, '//form/div[3]/div[3]/div/div/div/span/div/div'),
        "选择访问授权": (By.XPATH, '//*[@id="authorization"]/label[1]/span[1]/input'),
        "渠道投入": (By.XPATH, '//input[@placeholder="请输入渠道投入金额"]'),
        "应用场景": (By.XPATH, '//div[@id="useScene"]'),
        "确定按钮": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[2]'),
        "知道了按钮": (By.XPATH, '//div[2][@class="ant-modal-confirm-btns"]/button'),

        # 编辑
        "编辑按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[1]'),

        # 获取码
        "获取码按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[2]'),
        "下载按钮": (By.XPATH, '//div[@class="pages-manager_channel-modules-table-index-module_10KLT"]/button'),

        # 复制链接
        "复制链接按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[3]'),

        # 新客明细
        "新客明细按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[4]'),
        "去看看按钮": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),
        #"下载导出内容": (By.XPATH, '//tbody/tr[1]/td[6]/a'),
        "下载导出内容":(By.XPATH,'//table/tbody[@class="ant-table-tbody"]/tr[1]/td[6]/button'),
        "关闭导出弹窗": (By.XPATH, '//button[@class="ant-drawer-close"]'),

        # 曝光明细
        "曝光明细按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[5]'),

        # 删除
        "删除按钮": (By.XPATH, '//div[3]/div/div/table/tbody/tr[1]/td/button[6]'),
        "确定删除": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),

        # 列表查询
        "推广主体一级下拉框": (By.XPATH, '//form/div/div[2]/div[1]/div/div/div/span/div/div/div/div[1]'),
        "推广主体二级下拉框": (By.XPATH, '//form/div/div[2]/div[2]/div/div/div/span/div/div'),
        "落定页-一级": (By.XPATH, '//form/div/div[4]/div[1]/div/div/div/span/div/div/div/div[1]'),
        "落定页-二级": (By.XPATH, '//form/div/div[4]/div[2]/div/div/div/span/div/div/div/div[1]'),
        "搜索渠道": (By.XPATH, '//input[@placeholder="请输入您想查看的渠道码名称"]'),
        "搜索按钮": (By.XPATH, '//button[@class="ant-btn fs-12 ml10 ant-btn-primary ant-btn-background-ghost"]'),

        # 获取单个路径码
        "落地页一级": (By.XPATH, '//form/div[1]/div[2]/div/div/div/span/div/div/div/div[1]'),
        "落地页二级": (By.XPATH, '//form/div[1]/div[3]/div/div/div/span/div/div'),
        "推广主体1": (By.XPATH, '//div[1]/form/div[2]/div[2]/div/div/div/span/div/div/div/div'),
        # '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/form/div[2]/div[2]/div/div/div/span/div/div/div/div'
        "推广主体2": (By.XPATH, '//form/div[2]/div[3]/div/div/div/span/div/div'),
        # '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div[1]/form/div[2]/div[3]/div/div/div/span/div/div'
        "生成": (By.XPATH, '//span/button[@class="ant-btn ant-btn-primary"]'),
        "下载": (By.XPATH, '//form/div[6]/div[2]/div/button[1]'),
        "复制路径": (By.XPATH, '//form/div[6]/div[2]/div/button[2]'),

        # 获取批量码
        "落地页1": (By.XPATH, '//div/div[2]/form/div[1]/div[2]/div/div/div/span/div/div/div'),
        "落地页2": (By.XPATH, '//div/div[3]/div[2]/form/div[1]/div[3]/div/div/div/span/div/div/div/div'),
        "生成按钮": (By.XPATH, '//div[2]/form/div[4]/div/div/span/button'),
        "下载码": (By.XPATH, '//form/div[5]/div[2]/button'),
        #"下载批量码": (By.XPATH, '//tr[2]/td[6]/a[@class="ant-btn fs-12 ant-btn-link"]'),
        "下载批量码":(By.XPATH,'//table/tbody/tr[1]/td[6]/button'),
        "关闭弹窗": (By.XPATH, '//i[@class="anticon anticon-close"]'),

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
        super(ChannelManagementPO, self).__init__(driver)

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def switch_to_tab(self, tab_name):
        # 切换tab 公共方法
        if tab_name == '渠道码':
            self.wait_eleVisible(self.control['渠道码'])
            self.find_element(self.control['渠道码']).click()
        if tab_name == '获取路径码':
            self.wait_eleVisible(self.control['获取路径码'])
            self.find_element(self.control['获取路径码']).click()
        if tab_name == '获取单个路径码':
            self.wait_eleVisible(self.control['获取单个路径码'])
            self.find_element(self.control['获取单个路径码']).click()
        if tab_name == '获取批量码':
            self.wait_eleVisible(self.control['获取批量码'])
            self.find_element(self.control['获取批量码']).click()
        sleep(2)

    def save_channel(self, params=None):
        # 新增渠道码
        # 点击新增按钮
        self.wait_eleVisible(self.control['新增按钮'])
        self.find_element(self.control['新增按钮']).click()
        sleep(2)
        # 输入渠道名称
        if params['channel_name'] != '':
            self.wait_eleVisible(self.control['渠道名称'])
            self.find_element(self.control['渠道名称']).click()
            self.find_element(self.control['渠道名称']).send_keys(params['channel_name'])
        sleep(1)
        # 选择落地页
        self.wait_eleVisible(self.control['落地页一级下拉框'])
        self.select_by_index(self.control['落地页一级下拉框'])
        sleep(1)
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['落地页二级下拉框']):
            sleep(1)
            self.select_by_index(self.control['落地页二级下拉框'])
        sleep(1)
        # 选择推广主体
        self.wait_eleVisible(self.control['推广主体-一级'])
        self.select_by_index(self.control['推广主体-一级'])
        sleep(1)
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['推广主体-二级']):
            sleep(1)
            self.select_by_index(self.control['推广主体-二级'])
        sleep(1)
        # 选择访问授权
        self.find_element(self.control['选择访问授权']).click()
        sleep(1)
        # 输入渠道投入
        if params['channel_input'] != '':
            self.wait_eleVisible(self.control['渠道投入'])
            self.find_element(self.control['渠道投入']).click()
            self.find_element(self.control['渠道投入']).send_keys(params['channel_input'])
        sleep(1)
        # 选择应用场景
        self.wait_eleVisible(self.control['应用场景'])
        self.select_by_index(self.control['应用场景'])
        # 点击确定
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()
        sleep(1)
        # 点击知道了
        self.wait_eleVisible(self.control['知道了按钮'])
        self.find_element(self.control['知道了按钮']).click()

    def edit_channel(self, params=None):
        # 编辑渠道码
        # 点击编辑按钮
        self.wait_eleVisible(self.control['编辑按钮'])
        self.find_element(self.control['编辑按钮']).click()
        sleep(2)
        # 修改渠道投入
        if params['channel_input'] != '':
            self.wait_eleVisible(self.control['渠道投入'])
            self.find_element(self.control['渠道投入']).click()
            self.find_element(self.control['渠道投入']).clear()
            self.find_element(self.control['渠道投入']).send_keys(params['channel_input'])
        sleep(1)
        # 点击确定
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()
        sleep(1)
        # 点击知道了
        self.wait_eleVisible(self.control['知道了按钮'])
        self.find_element(self.control['知道了按钮']).click()

    def get_channel_code(self):
        # 获取渠道码
        # 鼠标移动到获取码按钮
        self.wait_eleVisible(self.control['获取码按钮'])
        self.move_mouse_to_element(self.control['获取码按钮'])
        sleep(5)
        # 点击下载按钮
        self.wait_eleVisible(self.control['下载按钮'])
        self.find_element(self.control['下载按钮']).click()

    def copy_link(self):
        # 复制链接
        # 点击复制链接按钮
        self.wait_eleVisible(self.control['复制链接按钮'])
        self.find_element(self.control['复制链接按钮']).click()

    def guest_detail(self):
        # 下载新客明细
        # 点击新客明细按钮
        sleep(2)
        self.wait_eleVisible(self.control['新客明细按钮'])
        self.find_element(self.control['新客明细按钮']).click()
        sleep(2)
        # 点击去看看按钮
        self.wait_eleVisible(self.control['去看看按钮'])
        self.find_element(self.control['去看看按钮']).click()
        sleep(3)
        # 点击下载
        self.wait_eleVisible(self.control['下载导出内容'])
        #self.find_element(self.control['下载导出内容']).click()
        self.find_elements(self.control['下载导出内容'],0).click()
        sleep(3)
        # 点击关闭弹窗
        self.wait_eleVisible(self.control['关闭导出弹窗'])
        self.find_element(self.control['关闭导出弹窗']).click()
        sleep(2)

    def exposure_detail(self):
        # 下载曝光明细
        # 点击曝光明细按钮
        self.wait_eleVisible(self.control['曝光明细按钮'])
        self.find_element(self.control['曝光明细按钮']).click()
        sleep(2)
        # 点击去看看按钮
        self.wait_eleVisible(self.control['去看看按钮'])
        self.find_element(self.control['去看看按钮']).click()
        sleep(3)
        # 点击下载
        self.wait_eleVisible(self.control['下载导出内容'])
        #self.find_element(self.control['下载导出内容']).click()
        self.find_elements(self.control['下载导出内容'],0).click()
        sleep(3)
        # 点击关闭弹窗
        self.wait_eleVisible(self.control['关闭导出弹窗'])
        self.find_element(self.control['关闭导出弹窗']).click()

    def search_channel(self, params=None):
        # 列表查询
        # 选择推广主体
        self.wait_eleVisible(self.control['推广主体一级下拉框'])
        self.select_by_index(self.control['推广主体一级下拉框'])
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['推广主体二级下拉框']):
            sleep(1)
            self.select_by_index(self.control['推广主体二级下拉框'])
        sleep(1)
        # 选择落地页
        self.wait_eleVisible(self.control['落定页-一级'])
        self.select_by_index(self.control['落定页-一级'])
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['落定页-二级']):
            sleep(1)
            self.select_by_index(self.control['落定页-二级'])
        sleep(1)
        # 输入渠道码名称
        if params['channel_name'] != '':
            self.wait_eleVisible(self.control['搜索渠道'])
            self.find_element(self.control['搜索渠道']).click()
            self.find_element(self.control['搜索渠道']).send_keys(params['channel_name'])
        # 点击搜索按钮
        self.wait_eleVisible(self.control['搜索按钮'])
        self.find_element(self.control['搜索按钮']).click()

    def delete_channel(self):
        # 删除渠道码
        # 刷新页面
        self.refresh()
        sleep(6)
        # 点击删除按钮
        self.wait_eleVisible(self.control['删除按钮'])
        self.find_element(self.control['删除按钮']).click()
        sleep(1)
        # 点击确定
        self.wait_eleVisible(self.control['确定删除'])
        self.find_element(self.control['确定删除']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        # while (self.check_button_clickable()):
        if self.check_button_clickable():
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
        # while (self.check_button_previous_page()):
        if self.check_button_previous_page():
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

    def single_path_code(self):
        # 生成单个路径码
        # 选择落地页
        self.wait_eleVisible(self.control['落地页一级'])
        self.select_by_index(self.control['落地页一级'])
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['落地页二级']):
            sleep(1)
            self.select_by_index(self.control['落地页二级'])
        sleep(1)
        # 选择推广主体
        self.wait_eleVisible(self.control['推广主体1'])
        self.select_by_index(self.control['推广主体1'])
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['推广主体2']):
            sleep(1)
            self.select_by_index(self.control['推广主体2'])
        sleep(1)
        # 点击生成按钮
        self.wait_eleVisible(self.control['生成'])
        self.find_element(self.control['生成']).click()
        sleep(3)
        # 点击下载按钮
        self.wait_eleVisible(self.control['下载'])
        self.find_element(self.control['下载']).click()
        sleep(2)
        # 点击复制路径按钮
        self.wait_eleVisible(self.control['复制路径'])
        self.find_element(self.control['复制路径']).click()

    def batch_code(self):
        # 获取批量码
        # 选择落地页
        self.wait_eleVisible(self.control['落地页1'])
        self.select_by_index(self.control['落地页1'])
        # 判断是否有二级下拉框
        if self.is_exist_element(self.control['落地页2']):
            sleep(1)
            self.select_by_index(self.control['落地页2'])
        sleep(1)
        # 点击生成按钮
        self.wait_eleVisible(self.control['生成按钮'])
        self.find_element(self.control['生成按钮']).click()
        sleep(3)
        # 点击去看看按钮
        self.wait_eleVisible(self.control['去看看按钮'])
        self.find_element(self.control['去看看按钮']).click()
        sleep(2)
        # 点击关闭弹窗
        self.wait_eleVisible(self.control['关闭弹窗'])
        self.find_element(self.control['关闭弹窗']).click()
        sleep(2)
        # 点击下载码按钮
        self.wait_eleVisible(self.control['下载码'])
        self.find_element(self.control['下载码']).click()
        sleep(2)
        # 点击下载按钮
        self.wait_eleVisible(self.control['下载批量码'])
        self.find_element(self.control['下载批量码']).click()
        sleep(2)
        # 点击关闭弹窗
        self.wait_eleVisible(self.control['关闭弹窗'])
        self.find_element(self.control['关闭弹窗']).click()