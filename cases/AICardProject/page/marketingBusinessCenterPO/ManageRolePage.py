# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from myweb.core.BasePage import BasePage
import time


class ManageRolePage(BasePage):
    controls = {
        "TAB切换-置业顾问": (
            By.XPATH, "//div[contains(@class, 'ant-tabs-nav-scroll')]/div/div/div[contains(text(), '置业顾问')]"),
        "TAB切换-行销人员": (
            By.XPATH, "//div[contains(@class, 'ant-tabs-nav-scroll')]/div/div/div[contains(text(), '行销人员')]"),
        "TAB切换-全民营销": (
            By.XPATH, "//div[contains(@class, 'ant-tabs-nav-scroll')]/div/div/div[contains(text(), '全民营销')]"),
        "TAB切换-访客": (By.XPATH, "//div[contains(@class, 'ant-tabs-nav-scroll')]/div/div/div[contains(text(), '访')]"),
        # 置业顾问tab页
        "置业顾问-拓客保护期开关": (By.XPATH,
                         "//div[@aria-hidden='false']/div[contains(@class, 'pages-manager_role-index-module_-qttQ')]/div/div/div/div/div[2]/button"),
        "置业顾问-拓客保护期-编辑按钮": (By.XPATH,
                            "//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']//div/button[@aria-checked='true']/following-sibling::span/button/span[contains(text(), '编辑')]"),
        "置业顾问-拓客保护期设置-输入框": (By.XPATH,
                             "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-body']/div/div/span/span/input"),
        "置业顾问-拓客保护期设置-确定按钮": (By.XPATH,
                              "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        "置业顾问-拓客保护期设置-取消按钮": (By.XPATH,
                              "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        # 行销人员tab页-与置业顾问页面完全一致，所以暂时复用置业顾问
        # 全民营销
        '全民营销-总开关': (By.XPATH, "//div[text()='全民营销']/parent::div/following-sibling::div/button"),
        '全民营销-总开关-编辑按钮': (By.XPATH,
                          "//div[text()='全民营销']/parent::div/following-sibling::div/button[@aria-checked='true']/following-sibling::span/button/span[contains(text(), '编辑')]"),
        '全民营销-总开关-编辑弹窗': (
        By.XPATH, "//div[@class='ant-modal-mask']/parent::div//div['全民营销']/parent::div[@class='ant-modal-header']"),
        '全民营销-总开关-编辑设置-统一身份展示': (By.XPATH, "//div[contains(text(), '统一身份展示：')]/following-sibling::div/input"),
        '全民营销-总开关-编辑设置-拓客保护期': (By.XPATH, "//div[contains(text(), '拓客保护期：')]/following-sibling::div/span/span/input"),
        '全民营销-总开关-编辑设置-确认按钮': (By.XPATH,
                               "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        '全民营销-总开关-编辑设置-取消按钮': (By.XPATH,
                               "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        '全民营销-项目楼盘报备入口-开关': (By.XPATH, "//div[text()='项目楼盘报备入口']/parent::div/following-sibling::div/button"),
        '全民营销-项目楼盘报备入口-编辑按钮': (By.XPATH,
                               "//div[text()='项目楼盘报备入口']/parent::div/following-sibling::div/button[@aria-checked='true']/following-sibling::span/button/span[contains(text(), '编辑')]"),
        '全民营销-项目楼盘报备入口-编辑弹窗': (
            By.XPATH,
            "//div[@class='ant-modal-mask']/parent::div//div['项目楼盘报备入口']/parent::div[@class='ant-modal-header']"),
        '全民营销-项目楼盘报备入口-编辑设置-入口名称': (By.XPATH, "//div[contains(text(), '入口名称：')]/following-sibling::div/input"),
        '全民营销-项目楼盘报备入口-编辑设置-跳转方式': (By.XPATH, "//div[contains(text(), '跳转方式：')]/following-sibling::div/div"),
        '全民营销-项目楼盘报备入口-编辑设置-跳转方式-次级选择框': (By.XPATH,
                                          "//ul[@class='ant-select-dropdown-menu  ant-select-dropdown-menu-root ant-select-dropdown-menu-vertical']/li[contains(text(), '{content}')]"),
        '全民营销-项目楼盘报备入口-编辑设置-确认按钮': (By.XPATH,
                                    "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        '全民营销-项目楼盘报备入口-编辑设置-取消按钮': (By.XPATH,
                                    "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        '全民营销-名片-开关': (By.XPATH, "//div[text()='名片']/parent::div/following-sibling::div/button"),
        '全民营销-名片-编辑按钮': (By.XPATH,
                       "//div[text()='名片']/parent::div/following-sibling::div/button[@aria-checked='true']/following-sibling::span/button/span[contains(text(), '编辑')]"),
        '全民营销-名片-编辑弹窗': (
            By.XPATH,
            "//div[@class='ant-modal-mask']/parent::div//div['名片']/parent::div[@class='ant-modal-header']"),
        '全民营销-名片-编辑设置-全选选项': (
            By.XPATH,
            "//div[@class='ant-modal-title' and text()='名片']/parent::div/following-sibling::div[@class='ant-modal-body']/div/div/label/span[2 and text()='全选']/parent::label"),
        '全民营销-名片-编辑设置-选项': (By.XPATH,
                            "//div[@class='ant-modal-title' and text()='名片']/parent::div/following-sibling::div[@class='ant-modal-body']/div/div/label/span[2 and text()='{content}']"),
        '全民营销-名片-编辑设置-确认按钮': (By.XPATH,
                              "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        '全民营销-名片-编辑设置-取消按钮': (By.XPATH,
                              "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        '全民营销-留电转经纪人-开关': (By.XPATH, "//div[text()='留电转经纪人']/parent::div/following-sibling::div/button"),
        # 访客tab
        '访客-拓客保护期-开关': (By.XPATH, "//div[@aria-hidden='false']//div[text()='拓客保护期']/parent::div/following-sibling::div/button"),
        '访客-拓客保护期-编辑按钮': (By.XPATH,
                          "//div[text()='拓客保护期']/parent::div/following-sibling::div/button[@aria-checked='true']/following-sibling::span/button/span[contains(text(), '编辑')]"),
        '访客-拓客保护期-编辑弹窗': (By.XPATH, "//div[@class='ant-modal-mask']/parent::div//div['拓客保护期']/parent::div[@class='ant-modal-header']"),
        '访客-拓客保护期-编辑设置-拓客保护期': (By.XPATH, "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-body']/div/div/span/span/input"),
        '访客-拓客保护期-编辑设置-确认按钮': (By.XPATH,
                               "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        '访客-拓客保护期-编辑设置-取消按钮': (By.XPATH,
                               "//div[@class='ant-modal-mask']/following-sibling::div/div/div/div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        '访客-购房进程状态信息呈现-开关': (By.XPATH, "//div[@aria-hidden='false']//div[text()='购房进程状态信息呈现']/parent::div/following-sibling::div/button")
    }

    def switch_to_tab(self, tab_name):
        if tab_name == '置业顾问':
            if self.is_exist_element(self.controls['TAB切换-置业顾问']):
                self.find_element(self.controls['TAB切换-置业顾问']).click()
        if tab_name == '行销人员':
            if self.is_exist_element(self.controls['TAB切换-行销人员']):
                self.find_element(self.controls['TAB切换-行销人员']).click()
        if tab_name == '全民营销':
            if self.is_exist_element(self.controls['TAB切换-全民营销']):
                self.find_element(self.controls['TAB切换-全民营销']).click()
        if tab_name == '访客':
            if self.is_exist_element(self.controls['TAB切换-访客']):
                self.find_element(self.controls['TAB切换-访客']).click()

    def editor_sales_info(self, params, throw_except=True):
        """
        编辑置业顾问信息
        :param params: dict.
        :param throw_except: Boolean.
        :return:
        """
        # 打开或者关闭拓客保护期开关
        if 'customer_protection_switch' in params.keys():
            switch_result, err = self._update_switch(
                commandSwitchState=params['customer_protection_switch'], el=self
                    .controls['置业顾问-拓客保护期开关'])
            # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
            if (not switch_result) and throw_except:
                raise Exception(err)
        # 输入拓客保护期
        if 'customer_protection_time' in params.keys():
            update_protection_time_result, err = self._update_sales_customer_protection_time(
                customer_protection_time=params['customer_protection_time'])
            # 如果修改时间后的状态不符合预期，且需要抛出异常，则抛出异常
            if (not update_protection_time_result) and throw_except:
                raise Exception(err)
        # 选择确定或者取消
        if 'button' in params.keys():
            print('点击保存')
            self._update_sales_click_the_button(button=params['button'])

    def editor_marketing_info(self, params, throw_except=True):
        """
        编辑行销人员信息-因为行销人员与置业顾问编辑页面完全一致，所以暂时套用
        :param params: dict.
        :param throw_except: Boolean.
        :return:
        """
        self.editor_sales_info(params, throw_except)

    def editor_broker_info(self, params, throw_except=True):
        """
        编辑行销人员信息
        :param params:
            {
                'marketing': {
                    'switch': True,
                    'show_identity': '全民营销',
                    'protection_time': '1',
                    'button': '确定'
                    },
                'recommend_entry': {
                    'switch': True,
                    'entry_name': '立享佣金',
                    'jump_way': 'Pass全民营销',
                    'button': '确定'
                    },
                'card': {
                    'switch': True,
                    'options': ['自由经纪人', '老业主'],
                    'button': '确定'
                    },
                'get_phone_number_become_broker': True
            }
        :param throw_except: Boolean.
        :return:
        """
        # 编辑全民营销信息
        if 'marketing' in params.keys():
            if 'switch' in params['marketing'].keys():
                switch_result, err = self._update_switch(
                    commandSwitchState=params['marketing']['switch'],
                    el=self.controls['全民营销-总开关'])
                # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
                if (not switch_result) and throw_except:
                    raise Exception(err)
            if 'show_identity' in params['marketing'].keys() or 'protection_time' in params['marketing'].keys():
                # 如果没有编辑弹窗则点击编辑按钮，如果有啥都不干
                if not self.is_exist_element(self.controls['全民营销-总开关-编辑弹窗']):
                    self.find_element(self.controls['全民营销-总开关-编辑按钮']).click()
            if 'show_identity' in params['marketing'].keys():
                # 输入 全民营销-统一身份展示 信息
                if self.is_exist_element(self.controls['全民营销-总开关-编辑设置-统一身份展示']):
                    show_identity_el = self.find_element(self.controls['全民营销-总开关-编辑设置-统一身份展示'])
                    show_identity_el.click()
                    # 如果输入框有值，则全选删除之后再输入内容
                    if show_identity_el.get_attribute('value'):
                        show_identity_el.send_keys(Keys.CONTROL, 'a')
                        show_identity_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    show_identity_el.send_keys(params['marketing']['show_identity'])
            if 'protection_time' in params['marketing'].keys():
                # 输入 全民营销-拓客保护期 信息
                if self.is_exist_element(self.controls['全民营销-总开关-编辑设置-拓客保护期']):
                    protection_time_el = self.find_element(self.controls['全民营销-总开关-编辑设置-拓客保护期'])
                    protection_time_el.click()
                    # 如果输入框有值，则全选删除之后再输入内容
                    if protection_time_el.get_attribute('value'):
                        protection_time_el.send_keys(Keys.CONTROL, 'a')
                        protection_time_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    protection_time_el.send_keys(params['marketing']['protection_time'])
            if 'show_identity' in params['marketing'].keys() or 'protection_time' in params['marketing'].keys():
                # 如果需要保存则点击保存
                if 'button' in params['marketing'].keys():
                    self._update_sales_click_the_button(button=params['marketing']['button'])

        # 编辑项目楼盘报备信息
        if 'recommend_entry' in params.keys():
            if 'switch' in params['recommend_entry'].keys():
                switch_result, err = self._update_switch(
                    commandSwitchState=params['recommend_entry']['switch'],
                    el=self.controls['全民营销-项目楼盘报备入口-开关'])
                # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
                if (not switch_result) and throw_except:
                    raise Exception(err)
            if 'entry_name' in params['recommend_entry'].keys() or 'jump_way' in params['recommend_entry'].keys():
                # 如果没有编辑弹窗则点击编辑按钮，如果有啥都不干
                if not self.is_exist_element(self.controls['全民营销-项目楼盘报备入口-编辑弹窗']):
                    self.find_element(self.controls['全民营销-项目楼盘报备入口-编辑按钮']).click()
            if 'entry_name' in params['recommend_entry'].keys():
                # 输入 项目楼盘报备入口-入口名称 信息
                if self.is_exist_element(self.controls['全民营销-项目楼盘报备入口-编辑设置-入口名称']):
                    show_identity_el = self.find_element(self.controls['全民营销-项目楼盘报备入口-编辑设置-入口名称'])
                    show_identity_el.click()
                    # 如果输入框有值，则全选删除之后再输入内容
                    if show_identity_el.get_attribute('value'):
                        show_identity_el.send_keys(Keys.CONTROL, 'a')
                        show_identity_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    show_identity_el.send_keys(params['recommend_entry']['entry_name'])
            if 'jump_way' in params['recommend_entry'].keys():
                # 选择 跳转方式
                if self.is_exist_element(self.controls['全民营销-项目楼盘报备入口-编辑设置-跳转方式']):
                    self.find_element(self.controls['全民营销-项目楼盘报备入口-编辑设置-跳转方式']).click()
                    jump_way_el = (self.controls['全民营销-项目楼盘报备入口-编辑设置-跳转方式-次级选择框'][0],
                                   self.controls['全民营销-项目楼盘报备入口-编辑设置-跳转方式-次级选择框'][1].format(
                                       content=params['recommend_entry']['jump_way']))
                    self.find_element(jump_way_el).click()
            if 'entry_name' in params['recommend_entry'].keys() or 'jump_way' in params['recommend_entry'].keys():
                # 如果需要保存则点击保存
                if 'button' in params['recommend_entry'].keys():
                    self._update_sales_click_the_button(button=params['recommend_entry']['button'])

        # 编辑名片信息
        if 'card' in params.keys():
            if 'switch' in params['card'].keys():
                switch_result, err = self._update_switch(
                    commandSwitchState=params['card']['switch'],
                    el=self.controls['全民营销-名片-开关'])
                # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
                if (not switch_result) and throw_except:
                    raise Exception(err)
            if 'options' in params['card'].keys():
                # 如果没有编辑弹窗的话，点一下编辑按钮，如果没有啥都不干
                if not self.is_exist_element(self.controls['全民营销-名片-编辑弹窗']):
                    self.find_element(self.controls['全民营销-名片-编辑按钮']).click()
                # 选择 经纪人身份（这里是列表，可以循环选择）
                if self.is_exist_element(self.controls['全民营销-名片-编辑设置-全选选项']):
                    # 判断一下全选选择框有没有选中，选中的话点一下，没选中点两下（用于清除之前的选项）
                    time.sleep(3)
                    full_option_el = self.find_element(self.controls['全民营销-名片-编辑设置-全选选项'])
                    full_option_class = self.getAttribute(full_option_el, 'class')
                    full_option_el.click()
                    if 'ant-checkbox-wrapper-checked' not in full_option_class:
                        time.sleep(1)
                        full_option_el.click()
                        time.sleep(1)
                    for op in params['card']['options']:
                        option_el = (self.controls['全民营销-名片-编辑设置-选项'][0], self.controls['全民营销-名片-编辑设置-选项'][1].format(content=op))
                        if self.is_exist_element(option_el):
                            self.find_element(option_el).click()
                        else:
                            print("can not find element %s, %s" % option_el)
                            if throw_except:
                                raise ("can not find element %s, %s" % option_el)
                if 'button' in params['card'].keys():
                    self._update_sales_click_the_button(button=params['card']['button'])

        # 编辑留电转经纪人信息
        if 'get_phone_number_become_broker' in params.keys():
            switch_result, err = self._update_switch(
                commandSwitchState=params['get_phone_number_become_broker'],
                el=self.controls['全民营销-留电转经纪人-开关'])
            # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
            if (not switch_result) and throw_except:
                raise Exception(err)

    def editor_guest_info(self, params, throw_except=True):
        """
        编辑普通访客信息
        :param params:
            {
                'protection': {
                    'switch': True,
                    'protection_time': '1',
                    'button': '确定'
                    },
                'house_buying_process': True
            }
        :param throw_except: Boolean.
        :return:
        """
        # 编辑访客拓客保护期信息
        if 'protection' in params.keys():
            if 'switch' in params['protection'].keys():
                switch_result, err = self._update_switch(
                    commandSwitchState=params['protection']['switch'],
                    el=self.controls['访客-拓客保护期-开关'])
                # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
                if (not switch_result) and throw_except:
                    raise Exception(err)
            if 'protection_time' in params['protection'].keys():
                # 如果没有编辑弹窗的话，点一下编辑按钮，如果没有啥都不干
                if not self.is_exist_element(self.controls['访客-拓客保护期-编辑弹窗']):
                    self.find_element(self.controls['访客-拓客保护期-编辑按钮']).click()
                # 输入 全民营销-拓客保护期 信息
                if self.is_exist_element(self.controls['访客-拓客保护期-编辑设置-拓客保护期']):
                    protection_time_el = self.find_element(self.controls['访客-拓客保护期-编辑设置-拓客保护期'])
                    protection_time_el.click()
                    # 如果输入框有值，则全选删除之后再输入内容
                    if protection_time_el.get_attribute('value'):
                        protection_time_el.send_keys(Keys.CONTROL, 'a')
                        protection_time_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    protection_time_el.send_keys(params['protection']['protection_time'])
                    # 如果需要保存则点击保存
            if 'button' in params['protection'].keys():
                self._update_sales_click_the_button(button=params['protection']['button'])

        # 编辑购房进程状态信息
        if 'house_buying_process' in params.keys():
            switch_result, err = self._update_switch(
                commandSwitchState=params['house_buying_process'],
                el=self.controls['访客-购房进程状态信息呈现-开关'])
            # 如果点击开关的状态不符合预期，且需要抛出异常，则抛出异常
            if (not switch_result) and throw_except:
                raise Exception(err)

    def _update_switch(self, commandSwitchState, el):
        """
        修改开关状态-打开 or 关闭开关
        :param is_open: Boolean. True or False
        :param el: Element.  (By.Xpath, '//div')
        :return: tuple. (Boolean, "error info")
        """
        result = (True, "")
        if self.is_exist_element(el):
            customer_protection_switch = self.find_element(el)
            currentSwitchState = self._is_switch_open(customer_protection_switch)
            commandSwitchState = commandSwitchState
            if isinstance(commandSwitchState, bool):
                if commandSwitchState == currentSwitchState:
                    # 当前开关状态与指令状态相等时，结果写入
                    result = (False,
                              "current switch state matches the command switch state! currentSwitchState: %s, commandSwitchState: %s" % (
                                  currentSwitchState, commandSwitchState))
                elif commandSwitchState == True:
                    customer_protection_switch.click()

                elif commandSwitchState == False:
                    customer_protection_switch.click()
            else:
                result = (False, "commandSwitchState need boolean!  customer_protection_switch:%s" % commandSwitchState)
        else:
            result = (False, "cannot find element %s" % el[1])
        return result

    def _update_sales_customer_protection_time(self, customer_protection_time):
        """
        修改置业顾问-拓客保护期时间
        :param: customer_protection_time: int.
        :return: tuple. (Boolean, "error info")
        """
        result = (True, "")
        # 判断是否有编辑按钮，有没有都继续输入拓客保护期时间
        if self.is_exist_element(self.controls['置业顾问-拓客保护期-编辑按钮']):
            self.find_element(self.controls['置业顾问-拓客保护期-编辑按钮']).click()
        if self.is_exist_element(self.controls['置业顾问-拓客保护期设置-输入框']):
            # 如果界面上已经存在输入框弹窗，则直接进行输入
            seller_customer_protection_time_input_el = self.find_element(self.controls['置业顾问-拓客保护期设置-输入框'])
            seller_customer_protection_time_input_el.click()
            if seller_customer_protection_time_input_el.get_attribute('value'):
                seller_customer_protection_time_input_el.send_keys(Keys.CONTROL, 'a')
                seller_customer_protection_time_input_el.send_keys(Keys.BACKSPACE)
                time.sleep(2)
            seller_customer_protection_time_input_el.send_keys(customer_protection_time)
        else:
            result = (False, "can not find ['置业顾问-拓客保护期设置-输入框']")
        return result

    def _update_sales_click_the_button(self, button):
        """

        :param button: string. 确定 or 取消
        :return:
        """
        if button == '确定':
            self.find_element(self.controls['置业顾问-拓客保护期设置-确定按钮']).click()
        elif button == '取消':
            self.find_element(self.controls['置业顾问-拓客保护期设置-取消按钮']).click()

    def _is_switch_open(self, el):
        flag = False
        switch_flag = self.getAttribute(el, 'aria-checked')
        if switch_flag == 'true':
            flag = True
            print("当前开关状态: %s" % switch_flag)
        print("------------")
        return flag
