#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AreaSettingPO(BasePage):
    controls = {
        "新增区域": (By.XPATH, '//span[text()="新增区域"]//parent::button[@type="button"]'),
        "新增区域-区域名称": (By.XPATH, '//input[@id="regionName"]'),
        "新增区域-区域首字母": (By.XPATH, '//div[text()="请选择区域首字母"]'),
        "新增区域-关联项目": (By.XPATH, '//div[text()="请选择"]'),
        "新增区域-确定": (By.XPATH, '//span[text()="确 定"]//parent::button[@type="button"]'), # 编辑弹框时，也是用的该定位
        "编辑": (By.XPATH, '//tbody[@class="ant-table-tbody"]//tr[1]//td[1]//span[text()="编辑"]//parent::button[@type="button"]'),
        "编辑-区域首字母": (By.XPATH, '//div[@id="initials"]//div[@role="combobox"]'),
        "编辑-区域首字母-删除": (By.XPATH, '//i[@aria-label="图标: close-circle"]'),
        "编辑-关联项目-删除": (By.XPATH, '//li//i[@aria-label="图标: close"]'),  # 返回1个或多个删除项目按钮
        "删除": (By.XPATH, '//tbody[@class="ant-table-tbody"]//tr[1]//td[1]//span[text()="删除"]//parent::button[@type="button"]'),
        "删除-确认": (By.XPATH, '//span[text()="确 认"]//parent::button[@type="button"]'),
        "定位匹配设置": (By.XPATH, '//span[text()="定位匹配设置"]//parent::button[@type="button"]'),
        "定位匹配设置-定位重定向": (By.XPATH, '//span[@class="ant-switch-inner"]//parent::button[@type="button"]'),
        "定位匹配设置-冲突区域": (By.XPATH, '//div[@class="ant-select ant-select-enabled"]'),
        "定位匹配设置-关闭窗口": (By.XPATH, '//span[@class="ant-modal-close-x"]//parent::button[@type="button"]')
    }

    def add_area(self):
        self.wait_eleVisible(controls=self.controls["新增区域"])
        self.find_element(self.controls["新增区域"]).click()
        self.wait_eleVisible(controls=self.controls["新增区域-区域名称"])
        self.find_element(self.controls["新增区域-区域名称"]).send_keys("豆子")

        self.wait_eleVisible(controls=self.controls["新增区域-区域首字母"])
        self.find_element(self.controls["新增区域-区域首字母"]).click()
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)

        self.wait_eleVisible(controls=self.controls["新增区域-关联项目"])
        self.find_element(self.controls["新增区域-关联项目"]).click()
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)

        self.wait_eleVisible(controls=self.controls["新增区域-确定"])
        self.find_element(self.controls["新增区域-确定"]).click()
        sleep(2)

    def edit_area(self):
        self.wait_eleVisible(controls=self.controls["编辑"])
        self.find_element(self.controls["编辑"]).click()
        sleep(2)
        self.wait_eleVisible(controls=self.controls["编辑-区域首字母"])
        self.move_mouse_to_element(self.controls["编辑-区域首字母"])
        sleep(2)
        self.wait_eleVisible(controls=self.controls["编辑-区域首字母-删除"])
        self.find_element(self.controls["编辑-区域首字母-删除"]).click()
        sleep(2)
        self.wait_eleVisible(controls=self.controls["编辑-关联项目-删除"])
        self.find_element(self.controls["编辑-关联项目-删除"]).click()
        self.wait_eleVisible(controls=self.controls["新增区域-确定"])
        self.find_element(self.controls["新增区域-确定"]).click()

    def delete_area(self):
        self.wait_eleVisible(controls=self.controls["删除"])
        self.find_element(self.controls["删除"]).click()
        self.wait_eleVisible(controls=self.controls["删除-确认"])
        self.find_element(self.controls["删除-确认"]).click()

    def location_matching_settings(self):
        self.wait_eleVisible(controls=self.controls["定位匹配设置"])
        self.find_element(self.controls["定位匹配设置"]).click()

        self.wait_eleVisible(controls=self.controls["定位匹配设置-定位重定向"])
        self.find_element(self.controls["定位匹配设置-定位重定向"]).click()
        sleep(2)
        self.find_element(self.controls["定位匹配设置-定位重定向"]).click()
        sleep(2)

        self.wait_eleVisible(controls=self.controls["定位匹配设置-冲突区域"])
        # 点击第三个冲突区域
        self.find_elements(self.controls["定位匹配设置-冲突区域"], 2).click()
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)

        # 点击第二个冲突区域
        self.find_elements(self.controls["定位匹配设置-冲突区域"], 1).click()
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)

        # 点击第一个冲突区域
        self.find_elements(self.controls["定位匹配设置-冲突区域"], 0).click()
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ARROW_DOWN)
        sleep(2)
        self.switch_to_active_element().send_keys(Keys.ENTER)
        sleep(2)

        self.find_elements(self.controls["定位匹配设置-关闭窗口"], 1).click()



