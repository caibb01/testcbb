# -*- encoding=utf8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.keys import Keys

class videoManagementPO(BasePage):
    controls = {
        # 视频管理页面
        "搜索框": (By.XPATH, '//input[@placeholder="请输入搜索关键字"]'),
        "搜索按钮": (By.XPATH, '//span[text()="搜 索"]/parent::button'),
        "新增视频": (By.XPATH, '//span[text()="新增视频"]/parent::button'),
        "首个视频封面": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[1]/img'),
        "首个视频描述": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[2]'),
        "首个视频关联项目": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[3]'),
        "首个视频更新时间": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[4]'),
        "首个视频编辑": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]/span/button[1]'),
        "首个视频删除": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[5]/span/button[2]'),

        # 删除弹窗
        "删除标题": (By.XPATH, '//div[@class="ant-modal-confirm-body-wrapper"]/div/span'),
        "删除文案": (By.XPATH, '//div[@class="ant-modal-confirm-body-wrapper"]/div/div'),
        "删除取消按钮": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[1]'),
        "删除确认按钮": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),

        # 新增/编辑视频弹窗
        "弹窗页标题": (By.XPATH, '//div[@class="ant-modal-title"]'),
        "弹窗关闭按钮": (By.XPATH, '//div[@class="ant-modal-content"]/button'),
        "视频描述": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[1]/div[1]/label'),
        "视频描述输入框": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[1]/div[2]/div/span/input'),
        "上传视频": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[2]/div[1]/label'),
        "上传视频按钮": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[2]/div[2]//button'),
        "上传视频说明": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[2]/div[2]//div[@class="ant-form-extra"]'),
        "封面图": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[3]/div[1]/label'),
        "添加图片": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_35VD_"]'),
        "添加图片确认": (By.XPATH, '//button[@class="ant-btn ant-btn-primary"]'),
        "添加图片说明": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[3]/div[2]//div[@class="ant-form-extra"]'),
        "权限关联项目": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[4]/div[1]/label'),
        "选择权限关联项目": (By.XPATH, '//div[@class="ant-modal-body"]/form/div[4]/div[2]/div/span/div/div'),
        "选择权限关联项目-输入搜索": (By.XPATH, '//*[@class="ant-input components-common-SelectTree-index-module_3tdMI"]'),
        "选择权限关联项目-选择搜索": (By.XPATH, '//div[@class="components-common-SelectTree-index-module_21xSF"]/input'),
        "选择": (By.XPATH,'//div/div[2][@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "勾选-我已阅读并同意": (By.XPATH, '//div[@class="ant-modal-body"]/div[2]/label/span/input'),
        "确认": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[2]'),
        "取消": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[1]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
    }

    def getProInfo(self, proName):
        """
        下拉选择项目
        :param proName:
        :return:
        """
        sleep(2)
        self.find_element(self.controls["选择权限关联项目"]).click()
        sleep(1)
        self.find_element(self.controls["选择权限关联项目-输入搜索"]).click()
        sleep(1)
        self.find_element(self.controls["选择权限关联项目-输入搜索"]).clear()
        sleep(1)
        self.find_element(self.controls["选择权限关联项目-输入搜索"]).send_keys(proName)
        sleep(2)
        self.find_elements(self.controls['选择'], 0).click()
        #self.find_element(self.controls["选择权限关联项目-选择搜索"]).click()

    def uploadVideo(self, path):
        """
        上传一个视频
        :return:
        """
        sleep(2)
        self.find_element(self.controls["上传视频按钮"]).click()
        sleep(2)
        self.upload(path)
        # self.send_keys(path)  # 发送文件地址
        # sleep(2)
        # self.send_keys("{ENTER}")
        # self.send_keys("{ENTER}")

    def uploadImg(self, path):
        """
        上传一张图片
        :return:
        """
        sleep(2)
        self.find_element(self.controls["添加图片"]).click()
        sleep(2)
        self.upload(path)
        # self.send_keys(path)  # 发送文件地址
        # sleep(2)
        # self.send_keys("{ENTER}")
        # self.send_keys("{ENTER}")
        sleep(2)
        self.find_elements(self.controls['添加图片确认'], 2).click()


    def addVideo(self, titleName, voidPath, imgPath, proName):
        sleep(2)
        self.find_element(self.controls["新增视频"]).click()
        sleep(2)
        # 由于这里选择项目会出错，这里的所以将顺序修改到这里
        self.getProInfo(proName=proName)
        self.find_element(self.controls["视频描述输入框"]).clear()
        self.find_element(self.controls["视频描述输入框"]).send_keys(titleName)
        # 上传视频
        self.uploadVideo(voidPath)
        # 视频上传有进度情况，增加等待时间
        sleep(20)
        # 上传图片
        self.uploadImg(imgPath)
        self.find_element(self.controls["勾选-我已阅读并同意"]).click()
        sleep(2)
        self.find_element(self.controls["确认"]).click()

    # 修改和更新用的同一个
    def updateVideo(self, titleName, proName):
        sleep(2)
        self.find_element(self.controls["首个视频编辑"]).click()
        sleep(2)
        self.getProInfo(proName=proName)
        self.find_element(self.controls["视频描述输入框"]).clear()
        self.find_element(self.controls["视频描述输入框"]).send_keys(titleName)
        # 上传视频
        # self.uploadVideo(voidName)
        # # 视频上传有进度情况，增加等待时间
        # sleep(30)
        # 上传图片
        # self.uploadImg(imgName)
        self.find_element(self.controls["勾选-我已阅读并同意"]).click()
        sleep(2)
        self.find_element(self.controls["确认"]).click()
        sleep(3)

    def delVideo(self):
        sleep(2)
        self.refresh()
        sleep(10)
        self.find_element(self.controls["首个视频删除"]).click()
        sleep(2)
        self.find_element(self.controls["删除确认按钮"]).click()

    def queryVideo(self, videoName):
        sleep(3)
        self.find_element(self.controls["搜索框"]).clear()
        self.find_element(self.controls["搜索框"]).send_keys(videoName)
        self.find_element(self.controls["搜索按钮"]).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['下一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的下一页'])
        return button_clickable

    def click_next(self):
        # 点击下一页
        self.refresh()
        # while (self.check_button_clickable()):
        if self.check_button_clickable():
            nextNum = len(self.find_elements_list(self.controls['下一页']))
            if nextNum > 1:
                self.find_elements(self.controls['下一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的下一页']).click()

    def check_button_previous_page(self):
        # 检查上一页按钮是否可点击
        nextNum = self.find_elements_list(self.controls['上一页'])
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.controls['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        # while (self.check_button_previous_page()):
        if self.check_button_previous_page():
            nextNum = len(self.find_elements_list(self.controls['上一页']))
            if nextNum > 1:
                self.find_elements(self.controls['上一页'], int(nextNum - 1)).click()
            else:
                self.find_element(self.controls['获取可点击的上一页']).click()

    def jump_page(self):
        # 跳页
        total_data = int(self.total_data())
        number_page = int(self.number_page())
        page = int(total_data / number_page)
        if page > 1:
            self.wait_eleVisible(self.controls['跳转至第几页'])
            self.find_element(self.controls['跳转至第几页']).send_keys(page + 1)
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
