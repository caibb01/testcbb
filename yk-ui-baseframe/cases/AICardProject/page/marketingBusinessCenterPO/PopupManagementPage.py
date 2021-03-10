# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from util.BasePage import BasePage
import time

class PopupManagementPage(BasePage):
    controls = {
        "新增弹窗": (By.CSS_SELECTOR, "div.components-common-PageBlockHeader-index-module_2tJ-g > div.right > button"),
        "弹窗名称输入框": (By.XPATH, "//div[contains(text(), '弹窗名称')]/following-sibling::div[1]/input"),
        "关联项目输入框": (By.XPATH, "//div[contains(text(), '关联项目')]/following-sibling::div[1]"),
        "关联项目下拉框": (By.XPATH, "//div[contains(@class, 'select-tree-ids')]/div[text()='{content}']"),
        "生效页面一级输入框": (By.XPATH, "//div[contains(text(), '生效页面')]/following-sibling::div[1]/div/div[1]"),
        "生效页面一级下拉框": (By.XPATH, "//ul[contains(@class, 'ant-select-dropdown-menu')]/li[text()='{content}']"),
        "生效页面二级输入框": (By.XPATH, "//div[contains(text(), '生效页面')]/following-sibling::div[1]/div/div[2]"),
        "生效页面二级下拉框": (By.XPATH, "//ul[contains(@class, 'ant-select-dropdown-menu')]/li[text()='{content}']"),
        "跳转页面一级输入框": (By.XPATH, "//div[contains(text(), '跳转页面')]/following-sibling::div[1]/div/div/div[1]"),
        "跳转页面一级下拉框": (By.XPATH, "//ul[contains(@class, 'ant-select-dropdown-menu')]/li[text()='{content}']"),
        "跳转页面二级输入框": (By.XPATH, "//div[contains(text(), '跳转页面')]/following-sibling::div[1]/div/div/div[2]"),
        "跳转页面二级下拉框": (By.XPATH, "//ul[contains(@class, 'ant-select-dropdown-menu')]/li[text()='{content}']"),
        "跳转页面三级输入框": (By.XPATH, "//div[contains(text(), '跳转页面')]/following-sibling::div[1]/div/div/div[3]"),
        "跳转页面三级下拉框": (By.XPATH, "//tr[contains(@class, 'ant-table-row ant-table-row-level-0')]/td[text()='{content}']/following-sibling::td[1]/span/button"),
        "触发条件输入框": (By.XPATH, "//div[contains(text(), '触发条件')]/following-sibling::div[1]"),
        "触发条件下拉框": (By.XPATH, "//ul[contains(@class, 'ant-select-dropdown-menu')]/li[text()='{content}']"),
        "开始时间选择框": (By.XPATH, "//div[contains(text(), '起止时间')]/following-sibling::div[1]/span/span[1]/div/input[@placeholder='开始日期']"),
        "开始时间输入框": (By.XPATH, "//input[contains(@class, 'ant-calendar-input') and @placeholder='开始日期']"),
        "结束时间选择框": (By.XPATH, "//div[contains(text(), '起止时间')]/following-sibling::div[1]/span/span[2]/div/input[@placeholder='结束日期']"),
        "结束时间输入框": (By.XPATH, "//input[contains(@class, 'ant-calendar-input') and @placeholder='结束日期']"),
        "上传图片": (By.XPATH, "//div[contains(text(), '图片:')]/following-sibling::div[1]/div/div/span"),
        "上传图片输入框": (By.XPATH, "//div[contains(text(), '图片:')]/following-sibling::div[1]/div/div/span/div/span/input"),
        "上传图片等待": (By.CLASS_NAME, "upload-progress"),
        "保存": (By.XPATH, "//div[@class='ant-modal-footer']/div/button/span[contains(text(), '保 存')]/parent::button"),
        "取消": (By.XPATH, "//div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        "编辑按钮": (By.XPATH, "//tbody[@class='ant-table-tbody']/tr/td/div[contains(text(), '{content}')]/parent::td/following-sibling::td[5]/span/button/span[contains(text(), '编辑')]/parent::button"),
        "删除按钮": (By.XPATH, "//tbody[@class='ant-table-tbody']/tr/td/div[contains(text(), '{content}')]/parent::td/following-sibling::td[5]/span/button/span[contains(text(), '删除')]/parent::button"),
        "确认删除按钮": (By.XPATH, "//div[@class='ant-modal-confirm-btns']/button/span[contains(.,'确 定')]/parent::button"),
        "搜索输入框": (By.XPATH, "//input[contains(@class, 'ant-input') and @placeholder='请输入搜索关键词']"),
        "搜索按钮": (By.XPATH, "//input[contains(@class, 'ant-input') and @placeholder='请输入搜索关键词']/following-sibling::span[1]/button"),
    }

    def insert_popup(self, params):
        '''
        :param params: {

        }
        :return:
        '''
        # 点击新增弹窗
        if self.is_exist_element(self.controls["新增弹窗"]):
            self.find_element(self.controls["新增弹窗"]).click()
        # 输入弹窗名称
        self._update_popup_name(popup_name=params['popup_name'])
        # 点击关联项目，进行选择
        self._update_popup_project_relation_name(project_relation_name=params['project_relation_name'])
        # 点击生效页面，进行选择
        self._update_popup_control_page(control_page=params['control_page'])
        # 点击跳转页面，进行选择
        self._update_popup_jump_page(jump_page=params['jump_page'])
        # 点击触发条件，进行选择
        self._update_popup_trigger_condition(condition=params['condition'])
        # 点击起止时间，进行输入
        self._update_popup_start_and_end_time(start_time=params['start_and_end_time'][0], end_time=params['start_and_end_time'][1])
        # 点击上传图片
        self._update_popup_image(image_path=params['image_path'])
        # 点击保存
        self.find_element(self.controls["保存"]).click()


    def delete_popup(self, params):
        if self.is_exist_element(self.controls["搜索输入框"]):
            search_input_el = self.find_element(self.controls["搜索输入框"])
            search_input_el.click()
            search_input_el.send_keys(Keys.CONTROL,'a')
            search_input_el.send_keys(Keys.BACKSPACE)
            time.sleep(2)
            self.find_element(self.controls["搜索输入框"]).send_keys(params['popup_name'])
            self.find_element(self.controls["搜索按钮"]).click()
        delete_button_el = (self.controls["删除按钮"][0], self.controls["删除按钮"][1].format(content=params['popup_name']))
        if self.is_exist_element(delete_button_el):
            self.find_element(delete_button_el).click()
        if self.is_exist_element(self.controls["确认删除按钮"]):
            self.find_element(self.controls["确认删除按钮"]).click()
        search_input_el.click()
        search_input_el.send_keys(Keys.CONTROL, 'a')
        search_input_el.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        self.find_element(self.controls["搜索按钮"]).click()


    def editor_popup(self, params):
        if self.is_exist_element(self.controls["搜索输入框"]):

            self.find_element(self.controls["搜索输入框"]).click()
            self.find_element(self.controls["搜索输入框"]).send_keys(params['popup_name_old'])
            self.find_element(self.controls["搜索按钮"]).click()
        editor_button_el = (self.controls["编辑按钮"][0], self.controls["编辑按钮"][1].format(content=params['popup_name_old']))
        if self.is_exist_element(editor_button_el):
            self.find_element(editor_button_el).click()

        if "popup_name" in params.keys():
            self._update_popup_name(params["popup_name"])
        if "project_relation_name" in params.keys():
            self._update_popup_project_relation_name(params["project_relation_name"])
        if "control_page" in params.keys():
            self._update_popup_control_page(params["control_page"])
        if "jump_page" in params.keys():
            self._update_popup_jump_page(params["jump_page"])
        if "condition" in params.keys():
            self._update_popup_trigger_condition(params["condition"])
        if "start_and_end_time" in params.keys():
            self._update_popup_start_and_end_time(start_time=params["start_and_end_time"][0], end_time=params["start_and_end_time"][2])
        # 点击保存
        self.find_element(self.controls["保存"]).click()


    def _update_popup_name(self, popup_name):
        # 输入弹窗名称
        if self.is_exist_element(self.controls["弹窗名称输入框"]):
            popup_name_el = self.find_element(self.controls["弹窗名称输入框"])
            popup_name_el.click()
            if popup_name_el.get_attribute('value'):
                popup_name_el.send_keys(Keys.CONTROL, 'a')
                popup_name_el.send_keys(Keys.BACKSPACE)
                time.sleep(2)
            popup_name_el.send_keys(popup_name)


    def _update_popup_project_relation_name(self, project_relation_name):
        self.find_element(self.controls["关联项目输入框"]).click()
        project_relation_element = (
        self.controls["关联项目下拉框"][0], self.controls["关联项目下拉框"][1].format(content=project_relation_name))
        if self.is_exist_element(project_relation_element):
            self.find_element(project_relation_element).click()


    def _update_popup_control_page(self, control_page):
        self.find_element(self.controls["生效页面一级输入框"]).click()
        control_page_element_one = (
        self.controls["生效页面一级下拉框"][0], self.controls["生效页面一级下拉框"][1].format(content=control_page[0]))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()
        self.find_element(self.controls["生效页面二级输入框"]).click()
        control_page_element_one = (
            self.controls["生效页面二级下拉框"][0], self.controls["生效页面二级下拉框"][1].format(content=control_page[1]))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()


    def _update_popup_jump_page(self, jump_page):
        self.find_element(self.controls["跳转页面一级输入框"]).click()
        control_page_element_one = (
            self.controls["跳转页面一级下拉框"][0], self.controls["跳转页面一级下拉框"][1].format(content=jump_page[0]))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()
        self.find_element(self.controls["跳转页面二级输入框"]).click()
        control_page_element_one = (
            self.controls["跳转页面二级下拉框"][0], self.controls["跳转页面二级下拉框"][1].format(content=jump_page[1]))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()
        self.find_element(self.controls["跳转页面三级输入框"]).click()
        control_page_element_one = (
            self.controls["跳转页面三级下拉框"][0], self.controls["跳转页面三级下拉框"][1].format(content=jump_page[2]))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()


    def _update_popup_trigger_condition(self, condition):
        self.find_element(self.controls["触发条件输入框"]).click()
        control_page_element_one = (
            self.controls["触发条件下拉框"][0], self.controls["触发条件下拉框"][1].format(content=condition))
        if self.is_exist_element(control_page_element_one):
            self.find_element(control_page_element_one).click()


    def _update_popup_start_and_end_time(self, start_time, end_time):
        if self.is_exist_element(self.controls["开始时间选择框"]):
            start_time_el = self.find_element(self.controls["开始时间选择框"])
            self.driver.execute_script("arguments[0].removeAttribute('readonly');", start_time_el)
            start_time_el.click()
            self.find_element(self.controls["开始时间输入框"]).send_keys(start_time)
            time.sleep(0.5)
            self.find_element(self.controls["开始时间输入框"]).send_keys(Keys.ENTER)

        if self.is_exist_element(self.controls["结束时间选择框"]):
            end_time_el = self.find_element(self.controls["结束时间选择框"])
            self.driver.execute_script("arguments[0].removeAttribute('readonly');", end_time_el)
            end_time_el.click()
            self.find_element(self.controls["结束时间输入框"]).send_keys(end_time)
            time.sleep(0.5)
            self.find_element(self.controls["结束时间输入框"]).send_keys(Keys.ENTER)


    def _update_popup_image(self, image_path, timeout=10):
        start_time = time.time()
        if self.is_exist_element(self.controls["上传图片输入框"]):
            self.find_element(self.controls["上传图片输入框"]).send_keys(image_path)
        while time.time() - start_time <= timeout:
            if not self.is_exist_element(self.controls["上传图片等待"]):
                break
        else:
            raise Exception("upload image timeout!")

