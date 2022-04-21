# -*- coding:utf-8 -*-
from myweb.core.BasePage import BasePage
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class OfficialAccountsManagementPO(BasePage):
    controls = {
        "添加公众号文章": (By.XPATH, '//span[text()="添 加"]/parent::button'),
        "添加公众号文章标识": (By.XPATH, ".//*[text()='添加公众号文章']"),
        "标题": (By.XPATH, '//input[@class="ant-input inp"]'),
        "描述": (By.XPATH, '//textarea[@class="ant-input fs-12"]'),
        "链接": (By.XPATH, '//input[@class="ant-input"]'),

        "关联项目": (By.XPATH, '//div[@class="ant-col ant-col-21 right"]/div[@class="components-common-SelectTree-index-module_2aYRl  ant-dropdown-trigger"]'),
        "关联项目-搜索项目": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "关联项目-选择项目": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),

        "关联地区": (By.XPATH, '//div[@class="common-component-select-styles undefined"]'),
        "关联地区-搜索区域": (By.XPATH, '//input[@placeholder="输入城市名进行搜索"]'),
        "关联地区-搜索": (By.XPATH, '//span[text()="搜 索"]/parent::button'),
        "关联地区-全局": (By.XPATH, '//span[text()="全 局"]/parent::button'),

        "上传图片": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_35VD_"]'),
        "上传图片-确定": (By.XPATH, '//span[text()="确 定"]/parent::button'),
        "图片区域": (By.XPATH, '//span[@class="ant-upload"]/div/div'),
        "重新上传图片": (By.XPATH, '//div/div[2]/i[1][@class="anticon anticon-upload components-common-Uploader-ui-rc-normal-module_V-8Ba"]'),

        "保存": (By.XPATH, '//span[text()="保 存"]/parent::button'),
        "编辑": (By.XPATH, '//span[text()="编辑"]/parent::button'),
        "删除": (By.XPATH, '//span[text()="删除"]/parent::button'),
        "删除-确认": (By.XPATH, '//button[@class="ant-btn ant-btn-danger"]'),

        # 列表搜索
        "请选择项目": (By.XPATH, '//span[text()="请选择"]/parent::div'),
        "项目查询条件": (By.XPATH, '//input[@placeholder="请选择项目"]'),
        "项目选择列表": (By.XPATH, '//div[@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
    }

    def relationProject(self, pro_name):
        """
        选择项目
        pro_name:只支持项目全名称的情况
        :return:
        """
        self.find_element(self.controls["关联项目"]).click()
        sleep(2)
        self.find_element(self.controls["关联项目-搜索项目"]).clear()
        self.find_element(self.controls["关联项目-搜索项目"]).send_keys(pro_name)
        sleep(1)
        i = -1
        i += 1
        self.find_elements(self.controls["关联项目-选择项目"], i).click()
        sleep(2)

    def relationRegion(self, city_name):
        """
        选择关联地区
        :return:
        """
        sleep(2)
        self.find_element(self.controls["关联地区"]).click()
        sleep(2)
        self.find_element(self.controls["关联地区-搜索区域"]).clear()
        self.find_element(self.controls["关联地区-搜索区域"]).send_keys(city_name)
        self.find_element(self.controls["关联地区-搜索"]).click()
        sleep(2)
        self.find_element(self.controls["关联地区-全局"]).click()
        sleep(2)

    def addImage(self, path):
        """
        上传图片
        :return:
        """
        self.find_element(self.controls["上传图片"]).click()
        sleep(2)
        self.upload(path)
        sleep(2)
        # 保存图片
        self.find_element(self.controls["上传图片-确定"]).click()
        sleep(3)

    def newOfficialAccounts(self, params=None):
        '''
        新增公众号文章
        '''
        self.find_element(self.controls["添加公众号文章"]).click()
        sleep(2)
        self.find_element(self.controls["标题"]).send_keys(params['title'])
        sleep(1)
        self.find_element(self.controls["描述"]).send_keys(params['content'])
        sleep(1)
        self.find_element(self.controls["链接"]).send_keys(params['url'])
        sleep(2)
        self.relationProject(params['project_name'])
        self.relationRegion(params['city_name'])
        self.addImage(params['path'])
        self.find_element(self.controls["保存"]).click()

    def updateOfficialAccounts(self, params=None):
        '''
        更新公众号文章
        '''
        self.find_element(self.controls["编辑"]).click()
        sleep(2)
        self.find_element(self.controls["标题"]).clear()
        self.find_element(self.controls["标题"]).send_keys(params['title'])
        sleep(1)
        self.find_element(self.controls["描述"]).clear()
        self.find_element(self.controls["描述"]).send_keys(params['content'])
        sleep(1)
        self.find_element(self.controls["链接"]).clear()
        self.find_element(self.controls["链接"]).send_keys(params['url'])
        sleep(1)
        self.relationProject(params['project_name'])
        self.relationRegion(params['city_name'])
        # 重新上传图片
        self.move_mouse_to_element(self.controls['图片区域'])
        sleep(1)
        self.find_element(self.controls['重新上传图片']).click()
        sleep(2)
        self.upload(params['path'])
        sleep(2)
        self.find_element(self.controls["上传图片-确定"]).click()
        sleep(3)
        self.find_element(self.controls["保存"]).click()

    def delOfficialAccounts(self):
        '''
        删除公众号文章
        '''
        self.find_element(self.controls["删除"]).click()
        sleep(1)
        self.find_element(self.controls["删除-确认"]).click()

    def queryOfficialAccounts(self, proName):
        '''
        搜索公众号文章
        '''
        self.find_element(self.controls["请选择项目"]).click()
        sleep(1)
        self.find_element(self.controls["项目查询条件"]).send_keys(proName)
        sleep(2)
        i = -1
        i += 1
        self.find_elements(self.controls["项目选择列表"], i).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['下一页'])
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        self.refresh()
        while (self.check_button_clickable()):
            nextNum = len(self.find_elements_list(self.controls['下一页']))
            if nextNum > 1:
                self.find_elements(self.controls['下一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的下一页']).click()

    def check_button_previous_page(self):
        # 检查上一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['上一页'])
        for i in range(int(len(nextNum)-1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        while(self.check_button_previous_page()):
            nextNum = len(self.find_elements_list(self.controls['上一页']))
            if nextNum > 1:
                self.find_elements(self.controls['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data/number_page)
        if page > 1:
            self.wait_eleVisible(self.controls['跳转至第几页'])
            self.find_element(self.controls['跳转至第几页']).send_keys(page+1)
            sleep(2)
            self.find_element(self.controls['跳转至第几页']).send_keys(Keys.ENTER)
            sleep(2)

    def total_data(self):
        '''获取当前查询共计总记录'''
        if self.is_exist_element(self.controls['共计总记录']):
            return self.find_element(self.controls['共计总记录']).text
        return 1

    def number_page(self):
        '''获取每页的条数'''
        if self.is_exist_element(self.controls['每页条数']):
            return self.find_element(self.controls['每页条数']).text
        return 1

