# coding=utf-8
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from myweb.core.BasePage import BasePage
import time


class popupManagementPO(BasePage):
    control = {
        # 进入弹窗管理
        "营销业务中心": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/ul/li[4]/div[1]/span/span'),
        "弹窗管理": (By.XPATH, '//*[@id="sub3$Menu"]/li[2]'),
        # 搜索项目
        "关联项目下拉框": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "关联项目下拉列表": (By.XPATH, '//*[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "关联项目输入框": (By.XPATH, '//input[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "搜索输入框": (By.XPATH, '//*[@class="ant-input-wrapper ant-input-group"]/input'),
        "搜索按钮": (By.XPATH, '//*[@class="ant-btn ant-input-search-button ant-btn-primary"]'),
        # 新增营销弹窗
        "新增营销弹窗": (By.XPATH, '//div[@class="right"]/button'),
        "营销弹窗名称输入框": (By.XPATH, '//*[@class="ant-input inp w-400"]'),
        "营销弹窗关联项目下拉框": (By.XPATH, '//*[@class="ant-col ant-col-21 right"]/div'),
        "营销弹窗关联项目输入框": (By.XPATH, '//input[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "营销弹窗关联项目下拉列表": (By.XPATH, '//*[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "营销弹窗生效页面一级下拉框": (By.XPATH, '//div[@class="ant-select ant-select-enabled"]/div'),
        "营销弹窗生效页面二级下拉框": (By.XPATH, '//div[@class="w-120 ant-select ant-select-enabled"]/div'),
        "营销弹窗跳转页面一级下拉框": (By.XPATH, '//*[@class="ant-select ant-select-enabled ant-select-allow-clear"]'),
        "营销弹窗跳转页面二级下拉框": (By.XPATH, '//*[@class="ant-select ant-select-enabled ant-select-allow-clear"]'),
        "营销弹窗跳转页面三级下拉框": (By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div[1]/div[3]'),
        "营销弹窗跳转页面关联资源选择": (By.XPATH, '//span[contains(text(), "选择")]'),
        "营销弹窗触发条件": (By.XPATH, '//*[@class="inp w-400 ant-select ant-select-enabled"]/div'),
        "营销弹窗开始日期选择框": (By.XPATH, '//span/div/input[@placeholder="开始日期"]'),
        "营销弹窗开始日期输入框": (By.XPATH, '//div/div/input[@placeholder="开始日期"]'),
        "营销弹窗结束日期选择框": (By.XPATH, '//span/div/input[@placeholder="结束日期"]'),
        "营销弹窗结束日期输入框": (By.XPATH, '//div/div/input[@placeholder="结束日期"]'),
        "确定按钮": (By.XPATH, '//*[@class="ant-calendar-ok-btn"]'),
        "营销弹窗上传图片": (By.XPATH, '//div[@class = "ant-upload ant-upload-select ant-upload-select-text"]'),
        "保存按钮": (By.XPATH, '//span[contains(text(), "保 存")]'),
        # 编辑营销弹窗
        "编辑营销弹窗": (By.XPATH, '//span[contains(text(), "编辑")]'),
        "删除营销弹窗": (By.XPATH, '//span[contains(text(), "删除")]'),
        "删除营销弹窗-确定按钮": (By.XPATH, '//*[@class="ant-btn ant-btn-danger"]'),
        # 授权弹窗
        "授权弹窗": (By.XPATH, '//*[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]'),
        "授权弹窗-搜索输入框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div[1]/div/span/span/input'),
        "新增授权弹窗": (By.XPATH, '//span[contains(text(), "新增授权弹窗")]'),
        "授权弹窗-弹窗名称": (By.XPATH, '//input[@placeholder="请输入标题，最多20个汉字"]'),
        "授权弹窗-触发条件": (By.XPATH, '//div[@class="w-400 ant-select ant-select-enabled"]'),
        "引用协议": (By.XPATH, '//div[@class="w-400 ant-select ant-select-enabled"]'),
        "授权弹窗生效页面": (By.XPATH, '//div[@class="w-400 ant-select ant-select-enabled"]/div/div'),
        "授权类型": (By.XPATH, '//input[@class="ant-input ant-cascader-input "]'),
        "业务授权": (By.XPATH, '//li[contains(text(), "业务授权")]'),
        "微信授权": (By.XPATH, '//li[contains(text(), "微信授权")]'),
        "用户昵称头像授权": (By.XPATH, '//li[contains(text(), "用户昵称头像授权")]'),
        "用户手机号授权": (By.XPATH, '//li[contains(text(), "用户手机号授权")]'),
        "按钮图片": (By.XPATH, '//span[@class="ant-uploader-customer"]'),
        "图片": (By.XPATH, '//span[@class="ant-uploader-customer"]'),
        "空白处": (By.XPATH, '//div[contains(text(), "新增授权弹窗")]'),
        "保存": (By.XPATH, '//span[contains(text(), "保 存")]'),
        "裁剪框-确定": (By.XPATH, '//span[contains(text(), "确 定")]'),
        "编辑授权弹窗": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/span/button[1]'),
        "删除授权弹窗": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[3]/div[2]/div[2]/div[2]/div/div/div/div/div/table/tbody/tr[1]/td[4]/span/button[2]'),
        "删除确定": (By.XPATH, '//button[@class="ant-btn ant-btn-danger"]'),

    }

    def __init__(self, driver):
        super(popupManagementPO, self).__init__(driver)

    def select_by_index(self, locator, index=0):
        # 下拉列表选择 公共方法
        time.sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def clear_contents_inputbox(self, locator):
        # 清除输入框内容
        time.sleep(2)
        _element = self.find_element(locator).clear()


    def force_click(self, element):
        # 强制点击
        self.driver.execute_script('arguments[0].click()', element)

    def into_popup_management(self):
        # 进入弹窗管理
        self.wait_eleVisible(self.control['营销业务中心'])
        self.find_element(self.control['营销业务中心']).click()
        time.sleep(2)
        self.find_element(self.control['弹窗管理']).click()

    def select_item(self, params):
        # 关联项目搜索营销弹窗
        self.wait_eleVisible(self.control['关联项目下拉框'])
        self.find_element(self.control['关联项目下拉框']).click()
        time.sleep(1)
        if params['project_name'] != '':
            ele = self.control['关联项目输入框']
            self.wait_eleVisible(ele)
            self.find_element(ele).click()
            self.find_element(ele).send_keys(params['project_name'])
            time.sleep(1)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['关联项目下拉列表'])
        self.find_element(self.control['关联项目下拉列表'], i).click()
        time.sleep(1)

    def search_marketing_popup(self, params):
        # 输入关键字
        if params['key_word'] != '':
            self.wait_eleVisible(self.control['搜索输入框'])
            self.find_element(self.control['搜索输入框']).click()
            self.find_element(self.control['搜索输入框']).send_keys(params['key_word'])
            time.sleep(1)
            # 点击搜索
            self.wait_eleVisible(self.control['搜索按钮'])
            self.find_element(self.control['搜索按钮']).click()

    def new_marketing_popup(self, params):
        # 新增营销弹窗
        self.wait_eleVisible(self.control['新增营销弹窗'])
        self.find_element(self.control['新增营销弹窗']).click()
        # 输入弹窗名称
        self.wait_eleVisible(self.control['营销弹窗名称输入框'])
        self.find_element(self.control['营销弹窗名称输入框']).click()
        time.sleep(1)
        if params['associated_items'] != '':
            ele = self.control['营销弹窗名称输入框']
            self.wait_eleVisible(ele)
            self.find_element(ele).click()
            self.find_element(ele).send_keys(params['associated_items'])
            time.sleep(1)
        # 关联项目
        self.wait_eleVisible(self.control['营销弹窗关联项目下拉框'])
        self.find_element(self.control['营销弹窗关联项目下拉框']).click()
        time.sleep(1)
        if params['entry_name'] != '':
            self.wait_eleVisible(self.control['营销弹窗关联项目输入框'])
            self.find_element(self.control['营销弹窗关联项目输入框']).click()
            self.find_element(self.control['营销弹窗关联项目输入框']).send_keys(params['entry_name'])
            time.sleep(2)
        i = -1
        i += 1
        self.wait_eleVisible(self.control['营销弹窗关联项目下拉列表'])
        self.find_elements(self.control['营销弹窗关联项目下拉列表'], i).click()
        # 生效页面区域
        self.wait_eleVisible(self.control['营销弹窗生效页面一级下拉框'], 0)
        self.select_by_index((self.control['营销弹窗生效页面一级下拉框']), 0)
        # 选择关联区域
        self.wait_eleVisible(self.control['营销弹窗生效页面二级下拉框'])
        self.select_by_index(self.control['营销弹窗生效页面二级下拉框'])
        # 选择跳转类型
        self.wait_eleVisible(self.control['营销弹窗跳转页面一级下拉框'], 0)
        self.select_by_index(self.control['营销弹窗跳转页面一级下拉框'], 0)
        # 选择关联类型
        self.wait_eleVisible(self.control['营销弹窗跳转页面一级下拉框'], 1)
        self.select_by_index(self.control['营销弹窗跳转页面一级下拉框'], 1)
        # 选择关联资源
        self.wait_eleVisible(self.control['营销弹窗跳转页面三级下拉框'])
        self.select_by_index(self.control['营销弹窗跳转页面三级下拉框'])
        # 选择具体的关联资源
        time.sleep(2)
        self.force_click(self.find_elements(self.control['营销弹窗跳转页面关联资源选择'], 2))
        # 触发条件
        self.wait_eleVisible(self.control['营销弹窗触发条件'], 1)
        self.select_by_index(self.control['营销弹窗触发条件'], 1)
        # 起止时间
        # 选择开始时间
        self.wait_eleVisible(self.control['营销弹窗开始日期选择框'])
        self.find_element(self.control['营销弹窗开始日期选择框']).click()
        time.sleep(1)
        if params['start_date'] != '':
            self.wait_eleVisible(self.control['营销弹窗开始日期输入框'])
            self.find_element(self.control['营销弹窗开始日期输入框']).click()
            self.find_element(self.control['营销弹窗开始日期输入框']).send_keys(params['start_date'])
            time.sleep(1)
            self.wait_eleVisible(self.control['确定按钮'])
            self.find_element(self.control['确定按钮']).click()
            time.sleep(1)
        # 选择结束时间
        self.wait_eleVisible(self.control['营销弹窗结束日期选择框'])
        self.find_element(self.control['营销弹窗结束日期选择框']).click()
        time.sleep(1)
        if params['end_date'] != '':
            self.wait_eleVisible(self.control['营销弹窗结束日期输入框'])
            self.find_element(self.control['营销弹窗结束日期输入框']).click()
            self.find_element(self.control['营销弹窗结束日期输入框']).send_keys(params['end_date'])
            time.sleep(1)
            self.wait_eleVisible(self.control['确定按钮'])
            self.find_element(self.control['确定按钮']).click()
            time.sleep(1)
        # 上传图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['营销弹窗上传图片'])
            choose = self.find_element(self.control['营销弹窗上传图片'])
            ActionChains(self.driver).click(choose).perform()
            time.sleep(2)
            self.upload(params['path'])
            time.sleep(2)
            self.force_click(self.find_element(self.control['保存按钮']))

        # 编辑营销弹窗

    def edit_marketing_popup(self, params):
        # 点击编辑
        self.wait_eleVisible(self.control['编辑营销弹窗'])
        self.force_click(self.find_element(self.control['编辑营销弹窗']))
        # 清除输入框内容
        time.sleep(2)
        self.wait_eleVisible(self.control['营销弹窗名称输入框'])
        self.find_element(self.control['营销弹窗名称输入框']).click()
        self.clear_contents_inputbox(self.control['营销弹窗名称输入框'])
        # 修改营销名称弹窗名称
        if params['modify marketing pop-up name'] != '':
            self.find_element(self.control['营销弹窗名称输入框']).send_keys(params['modify marketing pop-up name'])
            # 点击保存
            self.force_click(self.find_element(self.control['保存按钮']))

    def delete_marketing_popup(self):
        # 点击删除
        self.wait_eleVisible(self.control['删除营销弹窗'])
        self.force_click(self.find_element(self.control['删除营销弹窗']))
        time.sleep(2)
        # 点击确定
        self.force_click(self.find_element(self.control['删除营销弹窗-确定按钮']))

    def access_authorization_popup(self):
        # 进入授权弹窗
        time.sleep(2)
        self.wait_eleVisible(self.control['授权弹窗'])
        self.force_click(self.find_element(self.control['授权弹窗']))


    def keyword_search(self, params):
        # 关键字搜索授权弹窗
        if params['authorization_pop-up_keyword'] != '':
            self.wait_eleVisible(self.control['授权弹窗-搜索输入框'])
            self.force_click(self.find_element(self.control['授权弹窗-搜索输入框']))
            time.sleep(1)
            # 输入关键字
            self.find_element(self.control['授权弹窗-搜索输入框']).send_keys(params['authorization_pop-up_keyword'])
            time.sleep(2)
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def add_authorization_popup(self, params):
        # 新增授权弹窗
        time.sleep(2)
        self.wait_eleVisible(self.control['新增授权弹窗'])
        self.force_click(self.find_element(self.control['新增授权弹窗']))
        # 点击弹窗名称
        if params['authorization_popup_name'] != '':
            time.sleep(2)
            self.wait_eleVisible(self.control['授权弹窗-弹窗名称'])
            self.find_element(self.control['授权弹窗-弹窗名称']).click()
            self.find_element(self.control['授权弹窗-弹窗名称']).send_keys(params['authorization_popup_name'])
        # 选择触发条件
        self.wait_eleVisible(self.control['授权弹窗-触发条件'])
        self.select_by_index(self.control['授权弹窗-触发条件'], 0)
        # 选择引用协议
        self.wait_eleVisible(self.control['引用协议'])
        self.select_by_index(self.control['引用协议'], 1)
        # 生效页面
        # time.sleep(2)
        # self.wait_eleVisible(self.control['授权弹窗生效页面'], 2)
        # self.find_elements(self.control['授权弹窗生效页面'], 2).click()
        # self.clear_contents_inputbox(self.control['授权弹窗生效页面'])
        # time.sleep(1)
        # if params['effective page'] != '':
        #     self.find_element(self.control['授权弹窗生效页面']).send_keys(params['effective page'])
        # 授权类型
        self.wait_eleVisible(self.control['授权类型'])
        self.force_click(self.find_element(self.control['授权类型']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['微信授权']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['用户手机号授权']))
        # 上传按钮图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['按钮图片'])
            choose = self.find_elements(self.control['按钮图片'], 0)
            ActionChains(self.driver).click(choose).perform()
            time.sleep(2)
            self.upload(params['path'])
            time.sleep(2)
            self.wait_eleVisible(self.control['裁剪框-确定'])
            self.force_click(self.find_element(self.control['裁剪框-确定']))
            time.sleep(2)
        # 上传图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['按钮图片'])
            choose = self.find_elements(self.control['按钮图片'], 1)
            ActionChains(self.driver).click(choose).perform()
            time.sleep(2)
            self.upload(params['path'])
            self.wait_eleVisible(self.control['裁剪框-确定'])
            self.force_click(self.find_element(self.control['裁剪框-确定']))
            time.sleep(2)
        # 点击保存
        self.wait_eleVisible(self.control['保存'])
        self.force_click(self.find_elements(self.control['保存'], 0))

    def edit_authorization_popup(self):
        # 编辑授权弹窗
        self.wait_eleVisible(self.control['编辑授权弹窗'])
        self.force_click(self.find_element(self.control['编辑授权弹窗']))
        time.sleep(2)
        self.wait_eleVisible(self.control['授权类型'])
        self.force_click(self.find_element(self.control['授权类型']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['微信授权']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['用户昵称头像授权']))
        time.sleep(1)
        self.force_click(self.find_elements(self.control['保存'], 0))

    def delete_authorization_popup(self):
        self.wait_eleVisible(self.control['删除授权弹窗'])
        self.force_click(self.find_element(self.control['删除授权弹窗']))
        time.sleep(2)
        self.find_element(self.control['删除确定']).click()










