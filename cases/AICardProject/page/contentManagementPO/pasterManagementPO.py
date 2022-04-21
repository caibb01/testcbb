# -*- encoding=utf8 -*-
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class pasterManagementPO(BasePage):
    control = {
        # 海报管理-海报列表
        # tab
        "海报列表": (By.XPATH, '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[1]'),
        "海报分类": (By.XPATH, '//div[@class="ant-tabs-nav ant-tabs-nav-animated"]/div/div[2]'),

        # 查询
        "项目下拉框": (By.XPATH, '//div[@class="pages-manager_poster-content-poster_list-index-module_2N8FF"]/div[1]/div[2]/div'),
        "项目下拉框列表": (By.XPATH, '//div/div[2][@class="select-tree-ids components-common-SelectTree-index-module_3B_Wp"]'),
        "海报分类下拉框": (By.XPATH, '//div[@class="pages-manager_poster-content-poster_list-index-module_2N8FF"]/div[2]/div[2]/div'),
        "海报分类列表": (By.XPATH, '//*[@id="20a6bb44-f657-4b0b-91ce-bf4666761304"]/ul'),
        "海报列表搜索框": (By.XPATH, '//span[@class="ant-input-wrapper ant-input-group"]/input'),
        "海报搜索按钮": (By.XPATH, '//span[@class="ant-input-wrapper ant-input-group"]/span/button'),

        "首条海报序号": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[1]/span'),
        "首条海报名称": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[2]'),
        "首条海报分类": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[3]'),
        "首条海报类型": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[4]'),
        "首条海报推广次数": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[5]'),
        "首条海报创建日期": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr/td[6]'),

        # 操作按钮
        "创建海报": (By.XPATH, '//div[@class="pages-manager_poster-content-poster_list-index-module_1YtJk"][4]/button'),
        "首条海报预览": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]/div/span[1]'),
        "首条海报推广": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]/div/span[2]'),
        "首条海报编辑": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]/div/span[3]'),
        "首条海报删除": (By.XPATH, '//tbody[@class="ant-table-tbody"]/tr[1]/td[7]/div/span[4]'),

        # 删除确认弹窗
        "删除弹窗确定": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[2]'),
        "删除弹窗取消": (By.XPATH, '//div[@class="ant-modal-confirm-btns"]/button[1]'),

        # 创建/编辑海报
        "窗口标题": (By.XPATH, '//span[@class="ant-form-item-children"]/input'),
        "海报标题框": (By.XPATH, '//*[@id="title"]'),
        "海报分类框": (By.XPATH, '//form[@class="ant-form ant-form-horizontal"]/div[2]//div[@class="ant-select-selection__placeholder"]'),
        "海报分类框2": (By.XPATH,
                  '//form[@class="ant-form ant-form-horizontal"]/div[2]//div[@class="ant-select-selection__rendered"]'),
        "海报分类框列表": (By.XPATH, '//ul[@role="listbox"]/li'),
        "海报分类框列表第一个": (By.XPATH, '//ul[@role="listbox"]/li[1]'),
        "海报分类框列表第二个": (By.XPATH, '//ul[@role="listbox"]/li[2]'),
        "关联全局": (By.XPATH, '//*[@id="publish_range"]/label[1]/span[2]'),
        "关联项目": (By.XPATH, '//*[@id="publish_range"]/label[2]/span[2]'),
        "关联项目选择框": (By.XPATH, '//*[@id="project_relation_ids"]/div/div/div'),
        "关联项目列表": (By.XPATH, '/html/body/div[4]/div/div/div/ul/li'),
        "图片区域": (By.XPATH, '//span[@class="ant-upload"]/div/div'),
        "上传图片": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_35VD_"]'),
        "重新上传图片": (By.XPATH, '//div[@class="components-common-Uploader-ui-rc-normal-module_1XPht"]/i[1]'),
        "海报确定": (By.XPATH, '//div[3][@class="ant-modal-footer"]/div/button[2]'),
        # '/html/body/div[7]/div/div[2]/div/div[2]/div[3]/div/button[2]'
        "编辑海报确定": (By.XPATH, '//span[text()="确 定"]/parent::button'),
        "海报取消": (By.XPATH, '/html/body/div[5]//div[@class="ant-modal-footer"]/div/button[1]'),
        "取消": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[1]'),
        "确定": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[2]'),

        # 海报管理-海报分类
        # 搜索
        "分类搜索按钮": (By.XPATH, '//span[@class="ant-input-wrapper ant-input-group"]/span/button'),
        "分类搜索框": (By.XPATH, '//input[@placeholder="请输入关键字搜索"]'),

        # 新增
        "创建分类": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[3]/div[2]/div[2]/div[1]/div[2]/button'),
        "创建分类输入框": (By.XPATH, '//div[@class="ant-form-item-control"]/span/input'),
        "创建分类取消按钮": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[1]'),
        "创建分类确定按钮": (By.XPATH, '//div[@class="ant-modal-footer"]/div/button[2]'),
        "编辑分类输入框": (By.XPATH, '//div[@class="ant-form-item-control has-success"]/span/input'),

        "首条分类序号": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr[1]/td[1]/span'),
        "首条分类名称": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr[1]/td[2]'),
        "首条分类关联海报数": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr[1]/td[3]'),

        # 操作按钮
        "首条分类编辑": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr[1]/td[4]/span/a[1]'),
        "首条分类删除": (By.XPATH, '//div[@class="ant-table-body"]/table/tbody/tr[1]/td[4]/span/a[2]'),
        "确定删除": (By.XPATH, '//div[@class="ant-modal-confirm-body-wrapper"]/div[2]/button[2]'),

        # 翻页
        "每页条数": (By.XPATH, '//div[@class="ant-select-sm ant-select ant-select-enabled"]'),
        "共计总记录": (By.XPATH, '//span[@class="primary"]'),
        "上一页": (By.XPATH, '//li[@title="上一页"]'),
        "下一页": (By.XPATH, '//li[@title="下一页"]'),
        "获取可点击的下一页": (By.XPATH, '//li[@title="下一页"][@aria-disabled="false"]'),
        "获取可点击的上一页": (By.XPATH, '//li[@title="上一页"][@aria-disabled="false"]'),
        "跳转至第几页": (By.XPATH, '//div[@class="ant-pagination-options-quick-jumper"]/input'),
    }
    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def uploadImg(self, path):
        """
        上传一张图片
        :return:
        """
        sleep(2)
        self.find_element(self.control["上传图片"]).click()
        # self.find_element(self.control["重新上传图片"]).click()
        sleep(2)
        self.send_keys(path)  # 发送文件地址
        sleep(2)
        self.send_keys("{ENTER}")
        sleep(2)
        self.send_keys("{ENTER}")
        sleep(2)

    def addPaster(self, title, imagePath):
        """
        新增一个海报
        """
        sleep(3)
        self.find_element(self.control['创建海报']).click()
        sleep(1)
        self.find_element(self.control['海报标题框']).clear()
        self.find_element(self.control['海报标题框']).send_keys(title)
        sleep(1)
        self.find_element(self.control['海报分类框']).click()
        self.find_element(self.control['海报分类框列表第一个']).click()
        sleep(1)
        self.find_element(self.control['关联全局']).click()
        sleep(2)
        self.find_element(self.control["上传图片"]).click()
        # self.uploadImg(imagePath)
        sleep(2)
        self.upload(imagePath)
        sleep(1)
        self.find_elements(self.control['海报确定'], 1).click()
        sleep(2)
        self.find_elements(self.control['确定'], 0).click()

    def searchPaster(self, pasterTitle):
        """
        搜索一个海报
        """
        self.find_element(self.control['海报列表搜索框']).clear()
        self.find_element(self.control['海报列表搜索框']).send_keys(pasterTitle)
        sleep(2)
        self.find_element(self.control['海报搜索按钮']).click()
        sleep(2)
        # title = self.find_element(self.control['首条海报名称']).text
        # if pasterTitle != title:
        #     return title, "未找到搜索结果"
        # else:
        #     return "已找到名为：", pasterTitle, "的海报。"

    def editPaster(self, newtitle, imagePath):
        """
        修改海报
        """
        # self.searchPaster(pasterTitle)
        # sleep(5)
        self.find_element(self.control['首条海报编辑']).click()
        sleep(3)
        self.find_element(self.control['海报标题框']).clear()
        self.find_element(self.control['海报标题框']).send_keys(newtitle)
        sleep(1)
        self.find_element(self.control['海报分类框2']).click()
        sleep(1)
        self.find_elements(self.control['海报分类框列表'], 0).click()
        sleep(1)
        # self.find_element(self.control['关联项目']).click()
        # sleep(1)
        # self.find_element(self.control['关联项目选择框']).click()
        # sleep(1)
        # self.select_by_index(self.control['关联项目选择框'])
        # sleep(3)
        # self.find_element(self.control['窗口标题']).click()
        self.move_mouse_to_element(self.control['图片区域'])
        sleep(2)
        # self.find_element(self.control["上传图片"]).click()
        self.find_element(self.control["重新上传图片"]).click()
        sleep(2)
        self.upload(imagePath)
        sleep(2)
        self.find_elements(self.control['编辑海报确定'], 1).click()
        sleep(2)
        self.find_elements(self.control['确定'], 0).click()
    def delPaster(self):
        """
        删除一个海报
        """
        # sleep(2)
        # self.searchPaster(saerchTitle)
        # sleep(6)
        if self.is_exist_element(self.control['首条海报删除']):
            self.find_element(self.control['首条海报删除']).click()
            sleep(1)
            self.find_element(self.control['删除弹窗确定']).click()

    def addSort(self, sortTitle):
        """
        添加一个分类
        """
        sleep(2)
        self.find_element(self.control['海报分类']).click()
        sleep(2)
        self.find_element(self.control['创建分类']).click()
        sleep(1)
        self.find_element(self.control['创建分类输入框']).clear()
        self.find_element(self.control['创建分类输入框']).send_keys(sortTitle)
        sleep(1)
        self.find_element(self.control['创建分类确定按钮']).click()

    def search_poster(self, poster_title):
        """
        搜索海报
        """
        # self.refresh()
        # sleep(2)
        self.find_element(self.control['项目下拉框']).click()
        self.find_elements(self.control['项目下拉框列表'], 0).click()
        sleep(2)
        self.find_element(self.control['海报分类下拉框']).click()
        self.select_by_index(self.control['海报分类下拉框'])
        sleep(2)
        self.find_element(self.control['海报列表搜索框']).clear()
        self.find_element(self.control['海报列表搜索框']).send_keys(poster_title)
        sleep(2)
        self.find_element(self.control['海报搜索按钮']).click()

    def check_button_clickable(self):
        # 判断下一页按钮是否可点击
        nextNum = self.find_elements_list(self.control['下一页'])
        for i in range(int(len(nextNum) - 1)):
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
        for i in range(int(len(nextNum) - 1)):
            self.driver.execute_script("arguments[0].removeAttribute(arguments[1]);", nextNum[i], 'title')
        button_clickable = self.is_exist_element(self.control['获取可点击的上一页'])
        return button_clickable

    def click_previous(self):
        # 点击上一页
        while (self.check_button_previous_page()):
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
        '''获取当前查询共计总记录'''
        if self.is_exist_element(self.control['共计总记录']):
            return self.find_element(self.control['共计总记录']).text
        return 1

    def number_page(self):
        '''获取每页的条数'''
        if self.is_exist_element(self.control['每页条数']):
            return self.find_element(self.control['每页条数']).text
        return 1

    def edit_sort(self, sort_title):
        # 编辑海报分类
        self.find_element(self.control['首条分类编辑']).click()
        sleep(1)
        self.find_element(self.control['编辑分类输入框']).clear()
        self.find_element(self.control['编辑分类输入框']).send_keys(sort_title)
        sleep(1)
        self.find_element(self.control['创建分类确定按钮']).click()

    def del_sort(self):
        # 删除海报分类
        self.find_element(self.control['首条分类删除']).click()
        sleep(1)
        self.find_element(self.control['确定删除']).click()

    def search_sort(self, keywords):
        # 查询海报分类
        self.find_element(self.control['分类搜索框']).clear()
        self.find_element(self.control['分类搜索框']).send_keys(keywords)
        sleep(1)
        self.find_element(self.control['分类搜索按钮']).click()