import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class CommonExpressionPO(BasePage):
    controls = {
        "营销业务中心": (By.XPATH, '//span[text()="营销业务中心"]'),
        "常用语设置": (By.XPATH, '//span[text()="常用语设置"]'),

        # 添加常用语
        "添加常用语": (By.XPATH, '//span[text()="添加常用语"]/parent::button'),
        "角色": (By.XPATH, '//div[text()="请选择"]/parent::div'),
        "项目": (By.XPATH, '//div[text()="请选择项目"]'),
        "快捷设置-是": (By.XPATH, '//input[@value=1]'),
        "快捷设置-否": (By.XPATH, '//input[@value=0]'),
        "快捷设置-是-快捷按钮": (By.XPATH, '//input[@placeholder="请输入快捷按钮内容（上限10字）"]'),
        "填写话术": (By.XPATH, '//textarea[@placeholder="请输入填写话术（上限30字）"]'),
        "手机号": (By.XPATH, '//span[text()="手机号"]'),
        "楼盘": (By.XPATH, '//span[text()="楼盘"]'),
        "户型": (By.XPATH, '//span[text()="户型"]'),
        "确定": (By.XPATH, '//span[text()="确 定"]/parent::button'),

        # 编辑常用语
        "编辑": (By.XPATH, '//tr[@data-row-key="1"]//span[contains(text(), "编辑")]/parent::button'),
        "编辑常用语": (By.XPATH, '//div[text()="编辑常用语"]'),

        # 删除常用语
        "删除": (By.XPATH, '//tr[@data-row-key="1"]//span[contains(text(), "删除")]/parent::button'),
        "删除提示": (By.XPATH, '//div[text()="是否确定删除该常用语？"]'),
        "确认": (By.XPATH, '//span[text()="确 认"]/parent::button')
    }

    def __init__(self, driver):
        super(CommonExpressionPO, self).__init__(driver)
        self.driver = driver

    def add_buyer_expression(self):
        """
            角色:购房者
            快捷设置：是
            添加手机号、楼盘、户型
        """
        self.wait_eleVisible(self.controls["添加常用语"])
        self.find_element(self.controls["添加常用语"]).click()
        time.sleep(2)
        self.find_element(self.controls["角色"]).click()
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element(self.controls["快捷设置-是"]))
        time.sleep(2)
        self.driver.execute_script("arguments[0].value='10个字符呢'", self.find_element(self.controls["快捷设置-是-快捷按钮"]))
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element(self.controls["快捷设置-否"]))
        time.sleep(2)
        self.find_element(self.controls["手机号"]).click()
        time.sleep(1)
        self.find_element(self.controls["楼盘"]).click()
        time.sleep(1)
        self.find_element(self.controls["户型"]).click()
        time.sleep(1)
        self.find_element(self.controls["填写话术"]).click()
        self.find_element(self.controls["填写话术"]).send_keys("填写话术")
        time.sleep(2)
        self.find_element(self.controls["确定"]).click()
        time.sleep(2)

    def add_seller_expression(self):
        """
            角色:顾问、行销、经纪人
            快捷设置：是
            添加手机号
        """
        self.wait_eleVisible(self.controls["添加常用语"])
        self.find_element(self.controls["添加常用语"]).click()
        time.sleep(2)
        self.find_element(self.controls["角色"]).click()
        for i in range(3):
            self.driver.switch_to.active_element.send_keys(Keys.DOWN)
            self.driver.switch_to.active_element.send_keys(Keys.ENTER)
            time.sleep(2)

        self.driver.execute_script("arguments[0].click();", self.find_element(self.controls["项目"]))
        self.driver.switch_to.active_element.send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.execute_script("arguments[0].click();", self.find_element(self.controls["快捷设置-是"]))
        time.sleep(2)
        self.find_element(self.controls["快捷设置-是-快捷按钮"]).send_keys("10个字符呢")
        time.sleep(2)
        self.find_element(self.controls["填写话术"]).click()
        time.sleep(2)
        self.find_element(self.controls["填写话术"]).send_keys("填写话术")
        time.sleep(2)
        self.find_element(self.controls["手机号"]).click()
        time.sleep(1)
        self.find_element(self.controls["确定"]).click()

    def edit_expression(self):
        """
            编辑常用语
        """
        self.wait_eleVisible(self.controls["编辑"])
        self.find_element(self.controls["编辑"]).click()
        self.wait_eleVisible(self.controls["编辑常用语"])
        self.find_element(self.controls["确定"]).click()

    def delete_expression(self):
        """
            删除常用语
        """
        self.wait_eleVisible(self.controls["删除"])
        self.find_element(self.controls["删除"]).click()
        self.wait_eleVisible(self.controls["删除提示"])
        self.find_element(self.controls["确认"]).click()
