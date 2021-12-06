#-*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class TaskCenterPO(BasePage):
    control = {
        "营销业务中心": (By.XPATH, '//*[text()="营销业务中心"]'),
        # 新建/编辑任务
        "新建任务按钮": (By.XPATH, "//div/div[2]/div[2]/button[@class='ant-btn ant-btn-primary']"),
        "任务名称": (By.XPATH, "//input[@placeholder='请输入标题，最多32个汉字']"),
        "任务内容下拉框-一级": (By.XPATH, "//div[@class='w-120 ant-select ant-select-enabled ant-select-allow-clear']"),
        "任务内容下拉框-二级": (By.XPATH, "//div[@class='w-150 ant-select ant-select-enabled']"),
        "执行范围下拉框": (By.XPATH, "//div[@class='pages-manager_task-index-module_3txtw mb10']/div[1]"),
        "执行对象下拉框": (By.XPATH, "//div[@class='flex-default mb10']/div"),
        "执行周期": (By.XPATH, "//div/div[5]/div[2]/div/div[2]/input"),
        "任务动作下拉框": (By.XPATH, "//div[@class='common-documents-modal-content']/div[6]/div[2]/div"),
        "执行指标": (By.XPATH, "//div/div[7]/div[2]/div/div[2]/input"),
        "开始时间选择框": (By.XPATH, "//input[@placeholder='请选择日期']"),
        "开始时间输入框": (By.XPATH, "//input[@class='ant-calendar-input ']"),
        "确定按钮": (By.XPATH, "//a[text()='确 定']"),
        "上传海报": (By.XPATH, "//div[@class='components-common-Uploader-ui-rc-normal-module_35VD_']"),
        "裁剪框": (By.XPATH, "/html/body/div[5]/div/div[2]/div/div[2]"),
        "裁剪框-确定": (By.XPATH, "//span[text()='确 定']/parent::button"),
        "保存": (By.XPATH, "//div[@class='ant-modal-footer']/div/button[2]"),
        "编辑按钮": (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']/td[8]/span/button[1]"),

        # 删除任务
        "删除按钮": (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']/td[8]/span/button[4]"),
        "确定删除": (By.XPATH, "//button[@class='ant-btn ant-btn-danger']"),

        # 查看进展
        "进展按钮": (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']/td[8]/span/button[2]"),
        "关闭窗口": (By.XPATH, "//button[@class='ant-modal-close']"),

        # 查看排行榜
        "排行榜按钮": (By.XPATH, "//tr[@class='ant-table-row ant-table-row-level-0']/td[8]/span/button[3]"),
        "关闭按钮": (By.XPATH, "//div[4]/div/div[2]/div/div[2]/button/span/i"),
        # '/html/body/div[4]/div/div[2]/div/div[2]/button/span/i'

        # 列表查询
        "范围下拉框-一级": (By.XPATH, "//div[@class='flex-default fs-14 mr20']/div/div/div/div/div"),
        "范围下拉框-二级": (By.XPATH, "//div[@class='pages-manager_task-index-module_3FtJm mb10']/div[2]/div/div/div"),
        "状态下拉框": (By.XPATH, "//div[2][@class='flex-default fs-14 mr20']/div/div/div"),
        "关键词搜索框": (By.XPATH, "//input[@placeholder='请输入搜索关键词']"),
        "搜索按钮": (By.XPATH, "//button[@class='ant-btn ant-input-search-button ant-btn-primary']"),

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
        super(TaskCenterPO, self).__init__(driver)
        self.driver = driver

    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def save_task(self, params=None):
        # 新建任务
        # 点击新建任务按钮
        self.click_add_button()
        sleep(2)
        # 输入任务名称
        if params['title'] != '':
            self.input_title(params['title'])
        sleep(1)
        # 选择任务内容
        self.input_content()
        sleep(1)
        # 选择执行范围
        self.input_perform_range()
        sleep(1)
        # # 选择执行对象
        # self.input_perform_object()
        sleep(1)
        # 输入执行周期
        if params['perform_cycle'] != '':
            self.input_perform_cycle(params['perform_cycle'])
        sleep(1)
        # 选择任务动作
        self.input_task_action()
        sleep(1)
        # 输入执行指标
        if params['perform_index'] != '':
            self.input_perform_index(params['perform_index'])
        sleep(1)
        # 选择开始时间
        if params['start_time'] != '':
            self.input_start_time(params['start_time'])
        sleep(1)
        # 上传海报
        if params['path'] != '':
            self.upload_poster(params['path'])
        sleep(3)
        # 点击保存按钮
        self.click_save_button()

    def edit_task(self, params=None):
        # 编辑任务
        # 点击编辑按钮
        self.wait_eleVisible(self.control['编辑按钮'])
        self.find_element(self.control['编辑按钮']).click()
        sleep(2)
        # 输入任务名称
        if params['title'] != '':
            self.input_title(params['title'])
        sleep(1)
        # 点击保存按钮
        self.click_save_button()

    def check_progress(self):
        # 查看进展
        # 点击进展按钮
        self.wait_eleVisible(self.control['进展按钮'])
        self.find_element(self.control['进展按钮']).click()
        sleep(3)
        # 关闭窗口
        # self.wait_eleVisible(self.control['关闭窗口'])
        self.find_element(self.control['关闭窗口']).click()

    def view_ranking_list(self):
        # 查看排行榜
        # 点击排行榜按钮
        self.wait_eleVisible(self.control['排行榜按钮'])
        self.find_element(self.control['排行榜按钮']).click()
        sleep(6)
        # # 关闭窗口
        # self.wait_eleVisible(self.control['关闭按钮'])
        # self.find_element(self.control['关闭按钮']).click()

    def search_task(self, params):
        # 列表搜索
        # 选择范围
        self.wait_eleVisible(self.control['范围下拉框-一级'])
        self.select_by_index(self.control['范围下拉框-一级'])
        sleep(1)
        # self.wait_eleVisible(self.control['范围下拉框-二级'])
        # self.select_by_index(self.control['范围下拉框-二级'])
        # sleep(3)
        # 选择状态
        self.wait_eleVisible(self.control['状态下拉框'])
        self.select_by_index(self.control['状态下拉框'])
        sleep(2)
        # 输入关键词
        if params['keywords'] != '':
            self.wait_eleVisible(self.control['关键词搜索框'])
            self.find_element(self.control['关键词搜索框']).click()
            self.find_element(self.control['关键词搜索框']).send_keys(params['keywords'])
            sleep(1)
        # 点击搜索按钮
        self.wait_eleVisible(self.control['搜索按钮'])
        self.find_element(self.control['搜索按钮']).click()

    def delete_task(self):
        # 删除任务
        # 点击删除按钮
        self.wait_eleVisible(self.control['删除按钮'])
        self.find_element(self.control['删除按钮']).click()
        sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定删除'])
        self.find_element(self.control['确定删除']).click()

    def click_add_button(self):
        # 点击新建任务按钮
        self.wait_eleVisible(self.control['新建任务按钮'])
        self.find_element(self.control['新建任务按钮']).click()

    def click_save_button(self):
        # 点击保存按钮
        self.wait_eleVisible(self.control['保存'])
        self.find_element(self.control['保存']).click()

    def input_title(self, title=None):
        # 输入任务名称
        self.wait_eleVisible(self.control['任务名称'])
        ele = self.find_element(self.control['任务名称'])
        ele.click()
        ele.clear()
        ele.send_keys(title)

    def input_content(self):
        # 选择任务内容
        self.wait_eleVisible(self.control['任务内容下拉框-一级'])
        self.select_by_index(self.control['任务内容下拉框-一级'])
        sleep(1)
        self.wait_eleVisible(self.control['任务内容下拉框-二级'])
        self.select_by_index(self.control['任务内容下拉框-二级'])

    def input_perform_range(self):
        # 选择执行范围
        self.wait_eleVisible(self.control['执行范围下拉框'])
        self.select_by_index(self.control['执行范围下拉框'])

    def input_perform_object(self):
        # 选择执行对象
        self.wait_eleVisible(self.control['执行对象下拉框'])
        self.select_by_index(self.control['执行对象下拉框'])
        sleep(1)
        self.find_element(self.control['营销业务中心']).click()

    def input_perform_cycle(self, perform_cycle=None):
        # 输入执行周期
        self.wait_eleVisible(self.control['执行周期'])
        ele = self.find_element(self.control['执行周期'])
        ele.click()
        ele.clear()
        ele.send_keys(perform_cycle)

    def input_task_action(self):
        # 选择任务动作
        self.wait_eleVisible(self.control['任务动作下拉框'])
        self.select_by_index(self.control['任务动作下拉框'])

    def input_perform_index(self, perform_index=None):
        # 输入执行指标
        self.wait_eleVisible(self.control['执行指标'])
        ele = self.find_element(self.control['执行指标'])
        ele.click()
        ele.clear()
        ele.send_keys(perform_index)

    def input_start_time(self, start_time=None):
        # 选择开始时间
        # 点击选择框
        self.wait_eleVisible(self.control['开始时间选择框'])
        self.find_element(self.control['开始时间选择框']).click()
        sleep(2)
        # 输入开始时间
        self.wait_eleVisible(self.control['开始时间输入框'])
        time_inputbox = self.find_element(self.control['开始时间输入框'])
        time_inputbox.click()
        time_inputbox.clear()
        time_inputbox.send_keys(start_time)
        sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定按钮'])
        self.find_element(self.control['确定按钮']).click()

    def upload_poster(self, path):
        # 上传海报
        self.wait_eleVisible(self.control['上传海报'])
        choose = self.find_element(self.control['上传海报'])
        ActionChains(self.driver).click(choose).perform()
        sleep(2)
        self.upload(path)
        sleep(2)
        self.wait_eleVisible(self.control['裁剪框-确定'])
        self.find_element(self.control['裁剪框-确定']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        self.refresh()
        sleep(3)
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