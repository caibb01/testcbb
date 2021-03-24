# coding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from myweb.core.BasePage import BasePage
import time


class ManagerBlankPagePage(BasePage):
    controls = {
        "新建页面-按钮": (By.XPATH, "//span[contains(text(), '新建页面')]/parent::button"),
        "新建页面-页面名称-输入框": (By.XPATH, "//div[contains(text(), '页面名称')]/following-sibling::div[1]/input"),
        "新建页面-描述-输入框": (By.XPATH, "//div[contains(text(), '描述')]/following-sibling::div[1]/textarea"),
        "新建页面-关联项目-输入框": (By.XPATH, "//div[contains(text(), '新增页面')]/parent::div/following-sibling::div[@class='ant-modal-body']//div[contains(text(), '关联项目')]/following-sibling::div[1]"),
        "新建页面-关联项目-下拉搜索框": (By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-bottomLeft']//input[contains(@placeholder, '请选择项目')]"),
        "新建页面-关联项目-下拉选择框": (By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-bottomLeft']/div/div[2]/div[text()='{content}']"),
        "新建页面-页面背景-上传图片": (By.XPATH, "//div[contains(text(), '页面背景:')]/following-sibling::div[1]/div/div/span/div/span/input"),
        "新建页面-分享背景-上传图片": (By.XPATH, "//div[contains(text(), '分享背景:')]/following-sibling::div[1]/div/div/span/div/span/input"),
        "新建页面-业务关系-一级选择框": (By.XPATH, "//div[contains(text(), '业务关系:')]//following-sibling::div/div[1]"),
        "新建页面-业务关系-一级下拉框": (By.XPATH, "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[text()='{content}']"),
        "新建页面-业务关系-二级选择框": (By.XPATH, "//div[contains(text(), '业务关系:')]//following-sibling::div/div[2]"),
        "新建页面-业务关系-项目-二级下拉框": (By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-topLeft']/div/div[2]/div[text()='{content}']"),
        "新建页面-业务关系-区域-二级下拉框": (By.XPATH, "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-topLeft']/div/div/ul/li/ul/li[text()='{content}']"),
        "上传图片-确定": (By.XPATH, "//div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        "新建页面-保存按钮": (By.XPATH, "//div[contains(text(), '新增页面')]/parent::div/following-sibling::div[@class='ant-modal-footer']/div/button/span[contains(text(), '保 存')]/parent::button"),
        "新建页面-取消按钮": (By.XPATH, "//div[contains(text(), '新增页面')]/parent::div/following-sibling::div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        "上传图片等待": (By.CLASS_NAME, "upload-progress"),
        "主页面-关联项目-输入框": (By.XPATH, "//div[contains(text(), '关联项目：')]/div"),
        "主页面-关联项目-下拉框": (By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-bottomLeft']/div/div[2]/div[text()='{content}']"),
        "主页面-页面名称-搜索框": (By.XPATH, "//div[contains(text(), '关联项目：')]/parent::div/div[2]/input"),
        "主页面-页面名称-搜索按钮": (By.XPATH, "//div[contains(text(), '关联项目：')]/parent::div/div[2]/button"),
        "主页面-操作-删除按钮": (By.XPATH, "//tbody[@class='ant-table-tbody']/tr/td[2 and text()='{content}']/parent::tr/td[5]/span/button/span[text()='删除']/parent::button"),
        "主页面-操作-编辑按钮": (By.XPATH,
                        "//tbody[@class='ant-table-tbody']/tr/td[2 and text()='{content}']/parent::tr/td[5]/span/button/span[text()='编辑']/parent::button"),
        "主页面-删除-确认删除按钮": (By.XPATH, "//span[text()='确认删除页面？']/parent::div/following-sibling::div/button/span[text()='确 认']/parent::button"),
        # 编辑空白页相关
        "编辑页面-按钮": (By.XPATH, "//tbody[@class='ant-table-tbody']/tr/td[2 and text()='{content}']/parent::tr/td[5]/span/button/span[text()='编辑']/parent::button"),
        "更新页面-页面基础配置-按钮": (By.XPATH, "//div[@class='pages-page_decorate-content-index-module_1tH4J flex-column']//span[contains(text(), '基础信息配置')]/parent::button"),
        "更新页面-页面名称-输入框": (By.XPATH, "//div[contains(text(), '页面名称')]/following-sibling::div[1]/input"),
        "更新页面-描述-输入框": (By.XPATH, "//div[contains(text(), '描述')]/following-sibling::div[1]/textarea"),
        "更新页面-关联项目-输入框": (By.XPATH,
                          "//div[contains(text(), '更新页面')]/parent::div/following-sibling::div[@class='ant-modal-body']//div[contains(text(), '关联项目')]/following-sibling::div[1]"),
        "更新页面-关联项目-下拉搜索框": (By.XPATH,
                            "//div[@class='ant-dropdown ant-dropdown-placement-bottomLeft']//input[contains(@placeholder, '请选择项目')]"),
        "更新页面-关联项目-下拉选择框": (
        By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-bottomLeft']/div/div[2]/div[text()='{content}']"),
        "更新页面-页面背景-上传图片": (
        By.XPATH, "//div[contains(text(), '页面背景:')]/following-sibling::div[1]/div/div/span/div/span/input"),
        "更新页面-分享背景-上传图片": (
        By.XPATH, "//div[contains(text(), '分享背景:')]/following-sibling::div[1]/div/div/span/div/span/input"),
        "更新页面-业务关系-一级选择框": (By.XPATH, "//div[contains(text(), '业务关系:')]//following-sibling::div/div[1]"),
        "更新页面-业务关系-一级下拉框": (By.XPATH,
                            "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-bottomLeft']/div/ul/li[text()='{content}']"),
        "更新页面-业务关系-二级选择框": (By.XPATH, "//div[contains(text(), '业务关系:')]//following-sibling::div/div[2]"),
        "更新页面-业务关系-项目-二级下拉框": (
        By.XPATH, "//div[@class='ant-dropdown ant-dropdown-placement-topLeft']/div/div[2]/div[text()='{content}']"),
        "更新页面-业务关系-区域-二级下拉框": (By.XPATH,
                               "//div[@class='ant-select-dropdown ant-select-dropdown--single ant-select-dropdown-placement-topLeft']/div/div/ul/li/ul/li[text()='{content}']"),
        "更新-上传图片-确定": (
        By.XPATH, "//div[@class='ant-modal-footer']/div/button/span[contains(text(), '确 定')]/parent::button"),
        "更新页面-保存按钮": (By.XPATH,
                      "//div[contains(text(), '更新页面')]/parent::div/following-sibling::div[@class='ant-modal-footer']/div/button/span[contains(text(), '保 存')]/parent::button"),
        "更新页面-取消按钮": (By.XPATH,
                      "//div[contains(text(), '更新页面')]/parent::div/following-sibling::div[@class='ant-modal-footer']/div/button/span[contains(text(), '取 消')]/parent::button"),
        "页面配置-按钮": (By.XPATH, "//div[@class='pages-page_decorate-content-index-module_1tH4J flex-column']//button[contains(@class, 'components-page_decorate-pannel_relation-common-page-config-index-module_1UPff')]"),
        "页面配置-头部样式-选择": (By.XPATH, "//label[contains(text(), '头部样式')]/parent::div/following-sibling::div[1]//div[contains(text(), '{content}')]"),
        "页面配置-模块颜色-选择": (By.XPATH, "//label[contains(text(), '模块颜色')]/parent::div/following-sibling::div[1]//span[contains(text(), '{content}')]/parent::label"),
        "页面配置-保存按钮": (By.XPATH, "//div[contains(text(), '页面配置')]/parent::div/following-sibling::div[@class='ant-modal-footer']//span[contains(text(), '保 存')]/parent::button"),
        "页面配置-取消按钮": (By.XPATH, "//div[contains(text(), '页面配置')]/parent::div/following-sibling::div[@class='ant-modal-footer']//span[contains(text(), '取 消')]/parent::button"),
        "空白页编辑-发布": (By.XPATH, "//div[@class='components-page_decorate-pannel_config-index-module_3Htpd']//span[contains(text(), '发 布')]/parent::button"),
        "空白页编辑-保存": (By.XPATH, "//div[@class='components-page_decorate-pannel_config-index-module_3Htpd']//span[contains(text(), '保 存')]/parent::button")
    }

    def __init__(self, driver):
        super(ManagerBlankPagePage, self).__init__(driver)
        self.module_operate = {
                "大图": self._insert_module_big_picture
        }

    def insert_blankPage(self, params):
        """
        新增新页面
        :param params:
        {
            'page_name': '新页面名称',
            'desc': '描述'
            'relation_project': '全局',
            'background_img': '../src/image/img01.jpg',
            'share_img': '../src/image/img02.jpg',
            'business_relation': ['项目', '哥伦布多项目三'],
            'button': '保存'
        }
        :return:
        """
        if self.is_exist_element(self.controls['新建页面-按钮']):
            self.find_element(self.controls['新建页面-按钮']).click()
            # 输入弹窗名称
            if 'page_name' in params.keys():
                if self.is_exist_element(self.controls["新建页面-页面名称-输入框"]):
                    page_name_el = self.find_element(self.controls["新建页面-页面名称-输入框"])
                    page_name_el.click()
                    if page_name_el.get_attribute('value'):
                        page_name_el.send_keys(Keys.CONTROL, 'a')
                        page_name_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    page_name_el.send_keys(params['page_name'])
            # 输入描述
            if 'desc' in params.keys():
                if self.is_exist_element(self.controls["新建页面-描述-输入框"]):
                    page_desc_el = self.find_element(self.controls["新建页面-描述-输入框"])
                    page_desc_el.click()
                    if page_desc_el.get_attribute('value'):
                        page_desc_el.send_keys(Keys.CONTROL, 'a')
                        page_desc_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    page_desc_el.send_keys(params['desc'])
            # 设置关联项目
            if 'relation_project' in params.keys():
                self.find_element(self.controls['新建页面-关联项目-输入框']).click()
                relation_project_el = (
                    self.controls["新建页面-关联项目-下拉选择框"][0], self.controls["新建页面-关联项目-下拉选择框"][1].format(content=params['relation_project']))
                if self.is_exist_element(relation_project_el):
                    self.find_element(relation_project_el).click()
            # 设置页面背景
            if 'background_img' in params.keys():
                self._upload_image(image_path= params['background_img'],
                                   el= self.controls['新建页面-页面背景-上传图片'],
                                   loading_el= self.controls['上传图片等待'])
                # 裁剪图片（todo）
                # 点击确定
                if self.is_exist_element(self.controls['上传图片-确定']):
                    self.find_element(self.controls['上传图片-确定']).click()
            # 设置分享图片
            if 'share_img' in params.keys():
                self._upload_image(image_path=params['share_img'],
                                   el=self.controls['新建页面-分享背景-上传图片'],
                                   loading_el=self.controls['上传图片等待'])
                # 裁剪图片（todo）
                # 点击确定
                if self.is_exist_element(self.controls['上传图片-确定']):
                    self.find_element(self.controls['上传图片-确定']).click()
            # 设置业务关系
            if 'business_relation' in params.keys():
                self.find_element(self.controls["新建页面-业务关系-一级选择框"]).click()
                business_relation_element_one = (
                    self.controls["新建页面-业务关系-一级下拉框"][0], self.controls["新建页面-业务关系-一级下拉框"][1].format(content=params['business_relation'][0]))
                if self.is_exist_element(business_relation_element_one):
                    self.find_element(business_relation_element_one).click()
                self.find_element(self.controls["新建页面-业务关系-二级选择框"]).click()
                # 暂时只有区域/项目区分，所以这里用三元表达式，如果一级选择器是项目时，二级选择器使用项目的，如果不是项目时（是区域），二级选择器使用区域的
                business_relation_element_selector = self.controls["新建页面-业务关系-项目-二级下拉框"] if params['business_relation'][0] == "项目" else self.controls[
                    "新建页面-业务关系-区域-二级下拉框"]
                business_relation_element_second = (
                    business_relation_element_selector[0], business_relation_element_selector[1].format(content=params['business_relation'][1]))
                if self.is_exist_element(business_relation_element_second):
                    self.find_element(business_relation_element_second).click()
            # 点击保存 or 取消按钮
            if 'button' in params.keys():
                if params['button'] == '保存':
                    self.find_element(self.controls['新建页面-保存按钮']).click()
                elif params['button'] == '取消':
                    self.find_element(self.controls['新建页面-取消按钮']).click()
        else:
            raise Exception("can not find element ['新建页面-按钮']")

    def delete_blankPage(self, params):
        """
        删除空白页
        :param params:
        {
            'page_name': 'xxx',
            'relation_project': '全局'
        }
        :return:
        """
        # 根据名称、关联项目查询空白页
        self._select_blankPage(**params)
        # 删除名称相同的空白页
        page_delete_el = (self.controls['主页面-操作-删除按钮'][0], self.controls['主页面-操作-删除按钮'][1].format(content=params['relation_project']))
        if self.is_exist_element(page_delete_el):
            self.find_element(page_delete_el).click()
        if self.is_exist_element(self.controls['主页面-删除-确认删除按钮']):
            self.find_element(self.controls['主页面-删除-确认删除按钮']).click()

    def edit_blankPage(self, params):
        """
        编辑空白页页面基础配置（背景图等）、页面配置（头部样式、模块颜色）
        :param params:
        {
            'blank_page': {
                'page_name': 'xxx',
                'relation_project': '全局'
            }
            'page_base_config': {
                'page_name': '页面名称',
                'desc': '描述'
                'relation_project': '全局',
                'background_img': '../src/image/img01.jpg',
                'share_img': '../src/image/img02.jpg',
                'business_relation': ['项目', '哥伦布多项目三'],
                'button': '保存'
            }
            'page_config': {
                # 默认/透明/隐藏/渐现/浮动渐现
                'header_style': '默认',
                # 白色/藏青色
                'module_color': '白色',
                'button': '保存'
            }
        }
        :return:
        """
        # 更新空白页页面基础配置
        if 'page_base_config' in params.keys():
            # 打开 更新空白页 页面基础配置按钮
            if self.is_exist_element(self.controls['更新页面-页面基础配置-按钮']):
                self.find_element(self.controls['更新页面-页面基础配置-按钮']).click()
            # 编辑空白页 页面名称
            if 'page_name' in params['page_base_config'].keys():
                if self.is_exist_element(self.controls["更新页面-页面名称-输入框"]):
                    page_name_el = self.find_element(self.controls["更新页面-页面名称-输入框"])
                    page_name_el.click()
                    if page_name_el.get_attribute('value'):
                        page_name_el.send_keys(Keys.CONTROL, 'a')
                        page_name_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    page_name_el.send_keys(params['page_base_config']['page_name'])
            # 编辑空白页 描述
            if 'desc' in params['page_base_config'].keys():
                if self.is_exist_element(self.controls["更新页面-描述-输入框"]):
                    page_desc_el = self.find_element(self.controls["更新页面-描述-输入框"])
                    page_desc_el.click()
                    if page_desc_el.get_attribute('value'):
                        page_desc_el.send_keys(Keys.CONTROL, 'a')
                        page_desc_el.send_keys(Keys.BACKSPACE)
                        time.sleep(2)
                    page_desc_el.send_keys(params['page_base_config']['desc'])
            # 编辑空白页 关联项目
            if 'relation_project' in params['page_base_config'].keys():
                self.find_element(self.controls['更新页面-关联项目-输入框']).click()
                relation_project_el = (
                    self.controls["更新页面-关联项目-下拉选择框"][0],
                    self.controls["更新页面-关联项目-下拉选择框"][1].format(content=params['page_base_config']['relation_project']))
                if self.is_exist_element(relation_project_el):
                    self.find_element(relation_project_el).click()
            # 编辑空白页 背景图
            if 'background_img' in params['page_base_config'].keys():
                self._upload_image(image_path=params['page_base_config']['background_img'],
                                   el=self.controls['更新页面-页面背景-上传图片'],
                                   loading_el=self.controls['上传图片等待'])
                # 裁剪图片（todo）
                # 点击确定
                if self.is_exist_element(self.controls['上传图片-确定']):
                    self.find_element(self.controls['上传图片-确定']).click()
            # 编辑空白页 分享图
            if 'share_img' in params['page_base_config'].keys():
                self._upload_image(image_path=params['page_base_config']['share_img'],
                                   el=self.controls['更新页面-分享背景-上传图片'],
                                   loading_el=self.controls['上传图片等待'])
                # 裁剪图片（todo）
                # 点击确定
                if self.is_exist_element(self.controls['上传图片-确定']):
                    self.find_element(self.controls['上传图片-确定']).click()
            # 编辑空白页描述
            if 'business_relation' in params['page_base_config'].keys():
                self.find_element(self.controls["更新页面-业务关系-一级选择框"]).click()
                business_relation_element_one = (
                    self.controls["更新页面-业务关系-一级下拉框"][0],
                    self.controls["更新页面-业务关系-一级下拉框"][1].format(content=params['page_base_config']['business_relation'][0]))
                if self.is_exist_element(business_relation_element_one):
                    self.find_element(business_relation_element_one).click()
                self.find_element(self.controls["更新页面-业务关系-二级选择框"]).click()
                # 暂时只有区域/项目区分，所以这里用三元表达式，如果一级选择器是项目时，二级选择器使用项目的，如果不是项目时（是区域），二级选择器使用区域的
                business_relation_element_selector = self.controls["更新页面-业务关系-项目-二级下拉框"] if params['page_base_config']['business_relation'][
                                                                                                0] == "项目" else \
                self.controls[
                    "更新页面-业务关系-区域-二级下拉框"]
                business_relation_element_second = (
                    business_relation_element_selector[0],
                    business_relation_element_selector[1].format(content=params['page_base_config']['business_relation'][1]))
                if self.is_exist_element(business_relation_element_second):
                    self.find_element(business_relation_element_second).click()
            # 点击保存/取消 按钮
            if 'button' in params['page_base_config'].keys():
                if params['page_base_config']['button'] == '保存':
                    self.find_element(self.controls['更新页面-保存按钮']).click()
                elif params['page_base_config']['button'] == '取消':
                    self.find_element(self.controls['更新页面-取消按钮']).click()
        # 更新空白页 页面配置（头部配置等）
        if 'page_config' in params.keys():
            # 打开更新空白页-页面配置（右边小齿轮） 弹窗
            if self.is_exist_element(self.controls['页面配置-按钮']):
                self.find_element(self.controls['页面配置-按钮']).click()
            # 编辑空白页 头部样式
            if 'header_style' in params['page_config'].keys():
                header_style_el = (self.controls["页面配置-头部样式-选择"][0],
                                   self.controls["页面配置-头部样式-选择"][1].format(content=params['page_config']['header_style']))
                self.find_element(header_style_el).click()
                time.sleep(2)
            # 编辑空白页 模块颜色
            if 'module_color' in params['page_config'].keys():
                module_color_el = (self.controls["页面配置-模块颜色-选择"][0],
                                   self.controls["页面配置-模块颜色-选择"][1].format(
                                       content=params['page_config']['module_color']))
                self.find_element(module_color_el).click()
                time.sleep(2)
            # 点击保存/取消 按钮
            if 'button' in params['page_config'].keys():
                if params['page_config']['button'] == '保存':
                    self.find_element(self.controls['页面配置-保存按钮']).click()
                elif params['page_config']['button'] == '取消':
                    self.find_element(self.controls['页面配置-取消按钮']).click()
                time.sleep(2)
        # 点击保存
        self.find_element(self.controls['空白页编辑-发布']).click()
        # 返回空白页列表页
        self.back()

    def module_blankPage(self, params):
        """
        添加
        :param params:
        :return:
        """
        for module in params:
            module["module"]["name"]

    def into_blankPage_edit_page(self, page_name, relation_project, **kwags):
        # 进入空白页编辑页面
        # 根据名称+关联区域搜索空白页
        self._select_blankPage(page_name, relation_project, **kwags)
        edit_black_el = (
        self.controls['编辑页面-按钮'][0], self.controls['编辑页面-按钮'][1].format(content=page_name))
        self.find_element(edit_black_el).click()

    def _insert_module_big_picture(self, params):
        """
        新增大图模块
        :return:
        """


    def _select_blankPage(self, page_name, relation_project, **kwargs):
        self.find_element(self.controls['主页面-关联项目-输入框']).click()
        relation_project_el = (self.controls['主页面-关联项目-下拉框'][0], self.controls['主页面-关联项目-下拉框'][1].format(content=relation_project))
        if self.is_exist_element(relation_project_el):
            self.find_element(relation_project_el).click()
        # 输入页面名称，搜索，进行删除
        if self.is_exist_element(self.controls["主页面-页面名称-搜索框"]):
            page_name_el = self.find_element(self.controls["主页面-页面名称-搜索框"])
            page_name_el.click()
            if page_name_el.get_attribute('value'):
                page_name_el.send_keys(Keys.CONTROL, 'a')
                page_name_el.send_keys(Keys.BACKSPACE)
                time.sleep(2)
            page_name_el.send_keys(page_name)
        if self.is_exist_element(self.controls['主页面-页面名称-搜索按钮']):
            self.find_element(self.controls['主页面-页面名称-搜索按钮']).click()

    def _upload_image(self, image_path, el, loading_el, timeout=10):
        """

        :param image_path: 图片地址
        :param el: 图片上传元素
        :param loading_el: 可以表明元素正在loading的元素（例如upload-progress）
        :param timeout:
        :return:
        """
        start_time = time.time()
        if self.is_exist_element(el):
            self.find_element(el).send_keys(image_path)
        while time.time() - start_time <= timeout:
            if not self.is_exist_element(loading_el):
                break
        else:
            raise Exception("upload image timeout!")