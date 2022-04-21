import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class bookingManagementPO(BasePage):
    control = {
        # 进入预约管理
        "营销业务中心": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[1]/div/div[2]/ul/li[4]/div[1]/span/span'),
        "预约管理": (By.XPATH, '//*[@id="sub3$Menu"]/li[5]/span'),
        # 【预约须知设置】模块
        "项目名称": (By.XPATH, "//*[@id='project_id']/div/div"),
        "输入项目名称": (By.XPATH, "//*[@id='project_id']/div/div[2]/div/div/div/div[1]/input"),
        "选择项目": (By.XPATH, "//*[@id='project_id']/div/div[2]/div/div/div/div[2]/div[1]"),
        "用户是否可线上预约看房": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/form[2]/div/div[2]/div/span/button'),
        "确认启用": (By.XPATH, '//*[contains(text(), "我已知晓风险，确认继续")]'),
        "取消取用": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[3]/div/button[1]'),
        "项目预约二维码": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[1]/div[1]/button'),
        "复制跳转链接": (By.XPATH, '//*[contains(text(), "复制跳转链接")]'),
        "复制图片链接": (By.XPATH, '//*[contains(text(), "复制图片链接")]'),
        "下载图片": (By.XPATH, '//*[contains(text(), "下载图片")]'),
        "关闭项目预约二维码弹窗": (By.XPATH, '//i[@class = "anticon anticon-close ant-modal-close-icon"]'),
        "编辑": (By.XPATH, '//span[contains(text(), "编 辑")]'),
        "预约通知": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div/div[1]/textarea'),
        "保存预约通知": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div/div[2]/button[1]'),
        "取消保存预约通知": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/div/div/div[2]/button[2]'),
        "复制当前设置到其他项目1": (By.XPATH, '//*[contains(text(), "复制当前设置到其他项目")]'),
        "输入需要复制的项目名称1": (By.XPATH, '//input[@class = "ant-input"]'),
        "全选项目": (By.XPATH, '//input[@class = "ant-checkbox-input"]'),
        "确认复制按钮": (By.XPATH, "//*[contains(text(), '确 定')]"),
        # 【页面设置】模块
        "页面设置": (By.XPATH, '//span[contains(text(), "页面设置")]'),
        "默认背景": (By.XPATH, '//span[contains(text(), "默认背景")]'),
        "自定义背景颜色": (By.XPATH, '//span[contains(text(), "自定义背景颜色")]'),
        "自定义背景图片": (By.XPATH, '//span[contains(text(), "自定义背景图片")]'),
        "上传图片-文案": (By.XPATH, '//p[contains(text(), "上传图片")]'),
        "上传图片": (By.XPATH, '//i[@class = "anticon anticon-plus components-common-Uploader-ui-rc-normal-module_-KHUq"]'),
        "上传图片+按钮": (By.XPATH, '//div[@class = "components-common-Uploader-ui-rc-normal-module_1XPht"]/i'),
        "裁剪框确定": (By.XPATH, "//span[text()='确 定']/parent::button"),
        "保存页面设置": (By.XPATH, '//*[contains(text(), "保 存")]'),
        # 【填写字段设置】模块
        "填写字段设置": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[2]/div[2]'),
        "固定位置": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/div[1]/div/div/div/div[6]'),
        "删除添加字段": (By.XPATH, '//i[@class = "anticon anticon-close pages-setting_appointment-look-tabs-tab-fields-index-module_37sIb"]'),
        "添加字段": (By.XPATH, '//i[@class = "anticon anticon-plus pages-setting_appointment-look-tabs-tab-fields-index-module_37sIb"]'),
        "身份证号": (By.XPATH, '//*[contains(text(), "身份证号")]'),
        "户籍": (By.XPATH, '//*[contains(text(), "户籍")]'),
        "确定": (By.XPATH, '//*[contains(text(), "确 定")]'),
        "取消": (By.XPATH, '//button[@class = "ant-btn"]'),
        "提示": (By.XPATH, '//div[contains(text(), "您还没有选择项目哦~")]'),
        "知道了": (By.XPATH, '//span[contains(text(), "知道了")]'),
        # 【自定义字段】模块
        "自定义字段": (By.XPATH, '//i[@class = "anticon anticon-plus pages-setting_appointment-look-tabs-tab-fields-index-module_37sIb"]'),
        "字段名称": (By.XPATH, '//*[@class = "ant-input"]'),
        "填充类型": (By.XPATH, '//*[@class = "anticon anticon-down ant-select-arrow-icon"]'),
        "下拉框": (By.XPATH, '//div[@id="112e6707-65d3-4339-f252-75c57b285ae8"]/ul/li[2]'),
        # 校验类型
        "校验类型": (By.XPATH, '//input[@class = "ant-radio-input"]'),
        "确定按钮": (By.XPATH, '//*[contains(text(), "确 定")]'),
        "取消按钮": (By.XPATH, '//*[contains(text(), "取 消")]'),
        # 【陪同人员设置】
        "开启陪同人员设置": (By.XPATH, '//span[@class = "ant-switch-inner"]'),
        "开启陪同人员设置-文本": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[3]/div/form/div[1]/div[2]/div/span/button/span'),
        "陪同人数限制": (By.XPATH, '//div[@class = "ant-select-sm ant-select ant-select-enabled"]'),
        # 【接待量设置】模块
        "接待量设置": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div[1]/div[2]/div[2]/div[3]'),
        "编辑按钮": (By.XPATH, '//span[contains(text(), "编 辑")]'),
        "预约可选时间粒度": (By.XPATH, '//*[@id="time_granularity"]/div/div'),
        "是否启用": (By.XPATH, '//*input[@class = "ant-checkbox-input"]'),
        "时间粒度": (By.XPATH, '//span[@class = "ant-checkbox ant-checkbox-checked"]'),
        "保存": (By.XPATH, '//*[contains(text(), "保 存")]'),
        # 【可预约日期设置】
        "可预约日期设置": (By.XPATH, '//*[contains(text(), "可预约日期设置")]'),
        "预约时间跨度": (By.ID, 'appoint_day'),
        "选择日期": (By.XPATH, "//div[@class = 'DayPicker-Day DayPicker-Day--highlighted DayPicker-Day--today']"),
        # 【资格验证设置】
        "资格验证设置":  (By.XPATH, '//*[contains(text(), "资格验证设置")]'),
        "到访人员核验配置": (By.XPATH, '//input[@class = "ant-input"]'),
        "添加-到访人员配置": (By.XPATH, '//i[@class = "anticon components-common-plusAndMinus-index-module_3bzjQ cursor"]'),
        "删除-到访人员配置": (By.XPATH, '//i[@class = "anticon components-common-plusAndMinus-index-module_3bzjQ cursor"]')
    }

    def __init__(self, driver):
        super(bookingManagementPO, self).__init__(driver)

    # 强制点击
    def force_click(self, element):
        self.driver.execute_script('arguments[0].click()', element)

    # 下拉框操作
    def select_by_index(self, locator, index=1):
        # 下拉列表选择 公共方法
        time.sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    # 删除内容
    def empty_content(self, location):
        _element = self.find_element(location).click()
        ActionChains(self.driver).send_keys(Keys.BACKSPACE).perform()

    # 进入预约管理
    def into_booking_management(self):
        # 进入预约管理
        self.wait_eleVisible(self.control['营销业务中心'])
        self.find_element(self.control['营销业务中心']).click()
        time.sleep(2)
        self.find_element(self.control['预约管理']).click()
        time.sleep(3)
        # 点击【项目名称】
        time.sleep(2)
        self.find_element(self.control['项目名称']).click()
        time.sleep(3)
        # 输入项目名称
        # self.find_element(self.control['输入项目名称']).send_keys(pro_name)
        time.sleep(1)
        # 选择项目
        self.find_element(self.control['选择项目']).click()
        time.sleep(1)

    # 页面设置
    def page_setup(self, path):
        self.force_click(self.find_element(self.control['页面设置']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['自定义背景颜色']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['自定义背景图片']))
        time.sleep(2)
        if self.find_element(self.control['上传图片-文案']).text == "上传图片":
            upload_location = self.find_element(self.control['上传图片'])
            ActionChains(self.driver).click(upload_location).perform()
            time.sleep(4)
            self.upload(path)
            time.sleep(3)
            self.find_element(self.control['裁剪框确定']).click()
            time.sleep(2)
            self.force_click(self.find_element(self.control['保存页面设置']))

        else:
            upload_location = self.find_elements(self.control['上传图片+按钮'], 1)
            ActionChains(self.driver).click(upload_location).perform()
            time.sleep(4)
            self.upload(path)
            time.sleep(3)
            self.find_element(self.control['裁剪框确定']).click()
            time.sleep(2)
            self.force_click(self.find_element(self.control['保存页面设置']))

    # 预约须知设置
    def booking_instructions(self, description, p_ame):
        # 获取“用户是否可线上预约看房”按钮文本，判断开启/禁用
        if self.find_element(self.control['用户是否可线上预约看房']).text == '禁用':
            time.sleep(1)
            self.find_element(self.control['用户是否可线上预约看房']).click()
            self.wait_eleVisible(self.control['确认启用'])
            self.force_click(self.find_element(self.control['确认启用']))
            time.sleep(1)
            self.find_element(self.control['项目预约二维码']).click()
            time.sleep(2)
            self.force_click(self.find_element(self.control['复制跳转链接']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['复制图片链接']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['下载图片']))
            time.sleep(1)
            self.force_click(self.find_element(self.control['关闭项目预约二维码弹窗']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['编辑']))
            time.sleep(2)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.empty_content(self.control['预约通知'])
            time.sleep(1)
            self.find_element(self.control['预约通知']).send_keys(description)
            time.sleep(2)
            self.find_element(self.control['保存预约通知']).click()
            time.sleep(1)
            self.force_click(self.find_element(self.control['复制当前设置到其他项目1']))
            time.sleep(2)
            self.find_element(self.control['输入需要复制的项目名称1']).click()
            time.sleep(1)
            self.find_element(self.control['输入需要复制的项目名称1']).send_keys(p_ame)
            time.sleep(2)
            self.force_click(self.find_element(self.control['全选项目']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['确认复制按钮']))

        else:
            self.find_element(self.control['用户是否可线上预约看房']).click()
            time.sleep(1)
            self.force_click(self.find_element(self.control['复制当前设置到其他项目1']))
            time.sleep(2)
            self.find_element(self.control['输入需要复制的项目名称1']).click()
            time.sleep(1)
            self.find_element(self.control['输入需要复制的项目名称1']).send_keys(p_ame)
            time.sleep(2)
            self.force_click(self.find_element(self.control['全选项目']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['确认复制按钮']))

    # 填写字段设置-添加字段
    def add_filed(self):
        self.find_element(self.control['填写字段设置']).click()
        time.sleep(3)
        if self.find_element(self.control['固定位置']).text == '身份证号':
            time.sleep(2)
            self.force_click(self.find_element(self.control['删除添加字段']))
            time.sleep(2)
            if self.find_element(self.control['固定位置']).text == '户籍':
                time.sleep(2)
                self.force_click(self.find_element(self.control['删除添加字段']))
                time.sleep(3)
                self.force_click(self.find_elements(self.control['添加字段'], 0))
                time.sleep(1)
                self.find_element(self.control['身份证号']).click()
                time.sleep(1)
                self.find_element(self.control['户籍']).click()
                time.sleep(1)
                self.force_click(self.find_element(self.control['确定']))

            else:
                time.sleep(2)
                self.find_elements(self.control['添加字段'], 0).click()
                time.sleep(3)
                self.find_element(self.control['身份证号']).click()
                time.sleep(1)
                self.find_element(self.control['户籍']).click()
                time.sleep(1)
                self.force_click(self.find_element(self.control['确定']))

        elif self.find_element(self.control['固定位置']).text == '户籍':
            time.sleep(2)
            self.force_click(self.find_element(self.control['删除添加字段']))
            time.sleep(3)
            self.force_click(self.find_elements(self.control['添加字段'], 0))
            time.sleep(1)
            self.find_element(self.control['身份证号']).click()
            time.sleep(1)
            self.find_element(self.control['户籍']).click()
            time.sleep(1)
            self.force_click(self.find_element(self.control['确定']))

        else:
            time.sleep(2)
            self.force_click(self.find_elements(self.control['添加字段'], 0))
            time.sleep(1)
            self.find_element(self.control['身份证号']).click()
            time.sleep(1)
            self.find_element(self.control['户籍']).click()
            time.sleep(1)
            self.force_click(self.find_element(self.control['确定']))

    # 填写字段设置-自定义字段
    def add_custom_filed(self, enter_name, p_name2):
        self.find_element(self.control['填写字段设置']).click()
        time.sleep(3)
        self.force_click(self.find_elements(self.control['自定义字段'], 1))
        time.sleep(3)
        self.find_element(self.control['字段名称']).click()
        time.sleep(1)
        self.find_element(self.control['字段名称']).send_keys(enter_name)
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 0).click()
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 1).click()
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 2).click()
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 3).click()
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 4).click()
        time.sleep(2)
        self.find_elements(self.control['校验类型'], 5).click()
        time.sleep(2)
        self.force_click(self.find_element(self.control['确定按钮']))
        time.sleep(3)
        self.force_click(self.find_elements(self.control['删除添加字段'], 2))
        # 陪同人员设置
        if self.find_element(self.control['开启陪同人员设置-文本']).text == '关闭':
            time.sleep(2)
            self.force_click(self.find_elements(self.control['开启陪同人员设置'], 1))
            time.sleep(2)
            self.select_by_index(self.control['陪同人数限制'])
            time.sleep(2)
            self.force_click(self.find_element(self.control['复制当前设置到其他项目2']))
            self.force_click(self.find_element(self.control['复制当前设置到其他项目1']))
            time.sleep(2)
            self.find_element(self.control['输入需要复制的项目名称1']).click()
            time.sleep(1)
            self.find_element(self.control['输入需要复制的项目名称1']).send_keys(p_name2)
            time.sleep(2)
            self.force_click(self.find_element(self.control['全选项目']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['确认复制按钮']))

        else:
            time.sleep(2)
            self.force_click(self.find_element(self.control['复制当前设置到其他项目1']))
            time.sleep(2)
            self.find_element(self.control['输入需要复制的项目名称1']).click()
            time.sleep(1)
            self.find_element(self.control['输入需要复制的项目名称1']).send_keys(p_name2)
            time.sleep(2)
            self.force_click(self.find_element(self.control['全选项目']))
            time.sleep(2)
            self.force_click(self.find_element(self.control['确认复制按钮']))

    # 接待量设置
    def reception_setting(self):
        time.sleep(3)
        self.find_element(self.control['接待量设置']).click()
        time.sleep(2)
        self.force_click(self.find_element(self.control['编辑按钮']))
        time.sleep(2)
        self.select_by_index(self.control['预约可选时间粒度'])
        time.sleep(2)
        self.force_click(self.find_elements(self.control['时间粒度'], 0))
        time.sleep(2)
        self.force_click(self.find_element(self.control['保存']))

    # 可预约日期设置
    def appointment_date(self, days):
        time.sleep(2)
        self.find_element(self.control['可预约日期设置']).click()
        time.sleep(2)
        self.empty_content(self.control['预约时间跨度'])
        time.sleep(2)
        self.empty_content(self.control['预约时间跨度'])
        time.sleep(2)
        self.find_element(self.control['预约时间跨度']).send_keys(days)
        time.sleep(2)
        self.force_click(self.find_element(self.control['选择日期']))
        time.sleep(2)
        self.force_click(self.find_element(self.control['保存']))

    # 资格验证设置
    def qualification_setting(self, phone01, phone02):
        time.sleep(2)
        self.find_element(self.control['资格验证设置']).click()
        time.sleep(2)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.empty_content(self.control['到访人员核验配置'])
        time.sleep(1)
        self.find_element(self.control['到访人员核验配置']).send_keys(phone01)
        time.sleep(2)
        self.force_click(self.find_elements(self.control['添加-到访人员配置'], 0))
        time.sleep(2)
        self.find_elements(self.control['到访人员核验配置'], 1).send_keys(phone02)
        time.sleep(2)
        self.force_click(self.find_elements(self.control['删除-到访人员配置'], 3))
        time.sleep(2)
        self.force_click(self.find_element(self.control['保存']))















