
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from myweb.core.BasePage import BasePage




class OperationStrategyPO(BasePage):
    control = {
        # 进入营销业务中心
        "营销业务中心": (By.XPATH, '//span[contains(text(), "营销业务中心")]'),
        "类型": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[2]/div'),
        "状态": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div'),
        "搜索输入框": (By.XPATH, '//input[@placeholder="输入标题进行筛选"]'),
        # 进入运营策略
        "运营策略": (By.XPATH, '//span[contains(text(), "运营策略")]'),
        # 新建到访转化策略
        "到访转化策略": (By.XPATH, '//button[@class="ant-btn pages-operation_strategy-index-module_2dYHb ant-btn-primary"]'),
        "到访转化策略名称输入框": (By.XPATH, '//input[@class="ant-input pages-operation_strategy-pages-index-module_3z5am"]'),
        "到访转化策略选择人群下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div'),
        "到访转化策略执行策略下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div'),
        "到访转化策略选择动作": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[1]/div/div'),
        "到访转化策略选择页面": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div[1]/div'),
        "到访转化策略引导设置": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[3]/div/div'),
        "到访转化策略上传图片": (By.XPATH, '//*[@class="ant-upload ant-upload-select ant-upload-select-text"]'),
        "到访转化策略裁剪框-确定": (By.XPATH, '//span[contains(text(), "确 定")]'),
        "到访转化策略图片透明度": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[5]/div/div[4]'),
        "关闭按钮-开启": (By.XPATH, '//span[contains(text(), " 开启 ")]'),
        "显示设置-到时消失输入框": (By.XPATH, '//*[@class="ant-input-number-input-wrap"]/input'),
        "到访转化策略触发设置下拉框": (
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[7]/div[2]/div[1]/div/div[1]/div'),

        "到访转化策略跳转设置一级下拉框": (By.XPATH, '//*[@class="ant-select ant-select-enabled ant-select-allow-clear"]'),
        "到访转化策略跳转设置二级下拉框": (By.XPATH, '//*[@class="ant-select ant-select-enabled ant-select-allow-clear"]'),
        "到访转化策略跳转设置关联资源下拉框": (
            By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[7]/div[2]/div[2]/div/div[1]/div[3]'),
        "到访转化策略跳转设置关联资源标签": (By.XPATH, '//*[@class="ant-btn fs-12 blue ant-btn-link ant-btn-sm"]'),
        "到访转化策略保存": (By.XPATH, '//span[contains(text(), "保 存")]'),
        "发布到访转化策略": (By.XPATH, '//span[contains(text(), "发布策略")]'),
        "暂停到访转化策略": (By.XPATH, '//span[contains(text(), "暂停")]'),
        "确定到访转化策略暂停": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        "开启到访转化策略": (By.XPATH, '//span[contains(text(), "开启")]'),
        "确定到访转化策略开启": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        "删除到访转化策略": (By.XPATH, '//span[contains(text(), "删除")]'),
        "确定到访转化策略删除": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        "编辑到访转化策略": (By.XPATH, '//span[contains(text(), "编辑")]'),
        "到访转化策略详情": (By.XPATH, '//span[contains(text(), "详情")]'),
        "到访转化策略数据": (By.XPATH, '//span[contains(text(), "数据")]'),


        # 新建成交转化策略
        "成交转化策略": (By.XPATH, '//*[@class="ant-btn pages-operation_strategy-index-module_2dYHb ant-btn-primary"]'),
        "成交转化策略名称输入框": (By.XPATH, '//input[@class="ant-input pages-operation_strategy-pages-index-module_3z5am"]'),
        "成交转化策略选择人群下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div'),
        "成交转化策略执行策略下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div'),
        "成交转化策略选择动作": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[1]/div/div'),
        "成交转化策略选择页面": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div[1]/div'),
        "成交转化策略选择页面二级下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div[2]/div'),
        "成交转化策略引导设置": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[3]/div/div'),
        "成交转化策略引导设置二级下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[3]/div[3]/div'),
        #"成交转化策略引导设置三级下拉框": (By.XPATH, '//*[@class="pages-operation_strategy-pages-index-module_2NibQ"]/div[3]/div[4]/div'),
        "成交转化策略引导设置三级下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[3]/div[5]/div'),
        "成交转化策略显示设置-保持显示": (By.XPATH, '//span[contains(text(), "保持显示")]'),
        "成交转化策略关闭按钮-开启": (By.XPATH, '//span[contains(text(), " 开启 ")]'),
        "发布成交转化策略": (By.XPATH, '//span[contains(text(), "发布策略")]'),
        "暂停成交转化策略": (By.XPATH, '//span[contains(text(), "暂停")]'),
        "确定成交转化策略暂停": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        "删除成交转化策略": (By.XPATH, '//span[contains(text(), "删除")]'),
        "确定成交转化策略删除": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        # 新建顾问转化策略
        "顾问转化策略": (By.XPATH, '//*[@class="ant-btn pages-operation_strategy-index-module_2dYHb ant-btn-primary"]'),
        "顾问转化策略名称输入框": (By.XPATH, '//input[@class="ant-input pages-operation_strategy-pages-index-module_3z5am"]'),
        "顾问转化策略选择人群下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[2]/div/div'),
        "顾问转化策略执行策略下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[3]/div/div'),
        "顾问转化策略选择动作": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[1]/div/div'),
        "顾问转化策略选择页面": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div[1]/div'),
        "顾问转化策略选择页面二级下拉框": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div[6]/div[2]/div[2]/div'),
        "顾问转化策略上传图片": (By.XPATH, '//*[@class="ant-upload ant-upload-select ant-upload-select-text"]'),
        "顾问转化策略显示设置-到时消失": (By.XPATH, '//span[contains(text(), "到时消失")]'),
        "到时消失下拉框": (By.XPATH, '//*[@class="ant-input-number-input-wrap"]'),
        "到时消失-2秒消失": (By.XPATH, '//*[@class="ant-input-number inp w-88"]/div[1]/span[1]'),
        "顾问转化策略裁剪框-确定": (By.XPATH, '//span[contains(text(), "确 定")]'),
        "发布顾问转化策略": (By.XPATH, '//span[contains(text(), "发布策略")]'),
        "暂停顾问转化策略": (By.XPATH, '//span[contains(text(), "暂停")]'),
        "确定顾问转化策略暂停": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),
        "删除顾问转化策略": (By.XPATH, '//span[contains(text(), "删除")]'),
        "确定顾问转化策略删除": (By.XPATH, '//*[@class="ant-btn ant-btn-primary"]'),

    }

    def __init__(self, driver):
        super(OperationStrategyPO, self).__init__(driver)

    def select_by_index_down(self, locator, index):
        # 下拉列表选择 公共方法
        time.sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.DOWN).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def select_by_index_up(self, locator, index):
        # 下拉列表选择 公共方法
        time.sleep(2)
        _element = self.find_element(locator).click()
        for _i in range(index):
            ActionChains(self.driver).send_keys(Keys.UP).perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def clear_contents_inputbox(self, locator):
        # 清除输入框内容
        time.sleep(2)
        _element = self.find_element(locator).clear()


    def force_click(self, element):
        # 强制点击
        self.driver.execute_script('arguments[0].click()', element)

    def enter_operation_strategy(self):
        # 进入运营策略
        self.wait_eleVisible(self.control['营销业务中心'])
        self.force_click(self.find_element(self.control['营销业务中心']))
        time.sleep(1)
        self.wait_eleVisible(self.control['运营策略'])
        self.force_click(self.find_element(self.control['运营策略']))

    def new_visit_transformation_strategy(self, params):
        # 新增到访转化策略
        self.wait_eleVisible(self.control['到访转化策略'])
        self.find_elements(self.control['到访转化策略'], 0).click()
        # 清除到访转化策略名称
        self.wait_eleVisible(self.control['到访转化策略名称输入框'])
        self.find_element(self.control['到访转化策略名称输入框']).click()
        self.clear_contents_inputbox(self.control['到访转化策略名称输入框'])
        # 输入到访转化策略名称
        if params['visit_conversion_policy_name'] != '':
            self.find_element(self.control['到访转化策略名称输入框']).send_keys(params['visit_conversion_policy_name'])
        # 选择人群
        self.wait_eleVisible(self.control['到访转化策略选择人群下拉框'])
        self.select_by_index_up(self.control['到访转化策略选择人群下拉框'], index=1)

        # 选择执行策略
        self.wait_eleVisible(self.control['到访转化策略执行策略下拉框'])
        self.select_by_index_down(self.control['到访转化策略执行策略下拉框'], index=0)
        # 策略配置--选择动作
        self.wait_eleVisible(self.control['到访转化策略选择动作'])
        self.select_by_index_up(self.control['到访转化策略选择动作'], index=1)
        #  策略配置--选择页面
        self.wait_eleVisible(self.control['到访转化策略选择页面'])
        self.select_by_index_up(self.control['到访转化策略选择页面'], index=4)
        #  策略配置--引导设置
        self.wait_eleVisible(self.control['到访转化策略引导设置'])
        self.select_by_index_down(self.control['到访转化策略引导设置'], index=0)
        # 策略配置--引导图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['到访转化策略上传图片'])
            choose = self.find_element(self.control['到访转化策略上传图片'])
            ActionChains(self.driver).click(choose).perform()
            time.sleep(2)
            self.upload(params['path'])
            self.wait_eleVisible(self.control['到访转化策略裁剪框-确定'])
            self.force_click(self.find_element(self.control['到访转化策略裁剪框-确定']))
            time.sleep(2)

        # 关闭按钮-开启
        self.wait_eleVisible(self.control['关闭按钮-开启'])
        self.force_click(self.find_element(self.control['关闭按钮-开启']))
        # 触发设置
        self.wait_eleVisible(self.control['到访转化策略触发设置下拉框'])
        self.select_by_index_down(self.control['到访转化策略触发设置下拉框'], index=0)
        # 跳转设置-按标签
        self.wait_eleVisible(self.control['到访转化策略跳转设置一级下拉框'])
        self.select_by_index_up(self.control['到访转化策略跳转设置一级下拉框'], index=1)
        # 跳转设置-项目楼盘
        self.wait_eleVisible(self.control['到访转化策略跳转设置二级下拉框'])
        self.select_by_index_down(self.control['到访转化策略跳转设置二级下拉框'], index=0)
        # 选择关联资源
        self.wait_eleVisible(self.control['到访转化策略跳转设置关联资源下拉框'])
        self.find_element(self.control['到访转化策略跳转设置关联资源下拉框']).click()
        time.sleep(2)
        self.wait_eleVisible(self.control['到访转化策略跳转设置关联资源标签'])
        self.find_element(self.control['到访转化策略跳转设置关联资源标签']).click()
        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.driver.execute_script(js)
        # 点击保存
        self.wait_eleVisible(self.control['到访转化策略保存'])
        self.force_click(self.find_element(self.control['到访转化策略保存']))

    def new_transaction_conversion_strategy(self, params):
        # 新建成交转化策略
        self.wait_eleVisible(self.control['成交转化策略'])
        self.find_elements(self.control['成交转化策略'], 1).click()
        # 清除成交转化策略名称
        self.wait_eleVisible(self.control['成交转化策略名称输入框'])
        self.find_element(self.control['成交转化策略名称输入框']).click()
        self.clear_contents_inputbox(self.control['成交转化策略名称输入框'])
        # 输入成交转化策略名称
        if params['name_of_transaction_conversion_strategy'] != '':
            self.find_element(self.control['成交转化策略名称输入框']).send_keys(params['name_of_transaction_conversion_strategy'])
        # 成交转化策略选择人群
        self.wait_eleVisible(self.control['成交转化策略选择人群下拉框'])
        self.select_by_index_up(self.control['成交转化策略选择人群下拉框'], index=3)
        # 成交转化策略选择执行策略
        self.wait_eleVisible(self.control['成交转化策略执行策略下拉框'])
        self.select_by_index_down(self.control['成交转化策略执行策略下拉框'], index=0)
        # 成交转化策略策略配置--选择动作
        self.wait_eleVisible(self.control['成交转化策略选择动作'])
        self.select_by_index_down(self.control['成交转化策略选择动作'], index=2)
        # 成交转化策略策略配置--选择页面
        self.wait_eleVisible(self.control['到访转化策略选择页面'])
        self.select_by_index_up(self.control['到访转化策略选择页面'], index=3)
        time.sleep(2)
        # 成交转化策略--选择页面二级选择
        self.wait_eleVisible(self.control['成交转化策略选择页面二级下拉框'])
        self.select_by_index_down(self.control['成交转化策略选择页面二级下拉框'], index=4)
        # 成交转化策略引导设置
        self.wait_eleVisible(self.control['到访转化策略引导设置'])
        self.select_by_index_down(self.control['到访转化策略引导设置'], index=2)
        time.sleep(1)
        # 成交转化策略--引导设置二级选择
        self.wait_eleVisible(self.control['成交转化策略引导设置二级下拉框'])
        self.select_by_index_down(self.control['成交转化策略引导设置二级下拉框'], index=2)
        time.sleep(1)
        # 成交转化策略--引导设置三级选择
        self.wait_eleVisible(self.control['成交转化策略引导设置三级下拉框'])
        self.select_by_index_down(self.control['成交转化策略引导设置三级下拉框'], index=0)
        time.sleep(1)
        # 显示设置-保持显示
        self.wait_eleVisible(self.control['成交转化策略显示设置-保持显示'])
        self.force_click(self.find_element(self.control['成交转化策略显示设置-保持显示']))
        time.sleep(1)
        # 发布策略
        self.wait_eleVisible(self.control['发布成交转化策略'])
        self.force_click(self.find_element(self.control['发布成交转化策略']))

    def new_consultant_transformation_strategy(self, params):
        # 新建顾问转化策略
        self.wait_eleVisible(self.control['顾问转化策略'])
        self.find_elements(self.control['顾问转化策略'], 2).click()
        # 清除顾问转化策略名称
        self.wait_eleVisible(self.control['顾问转化策略名称输入框'])
        self.find_element(self.control['顾问转化策略名称输入框']).click()
        self.clear_contents_inputbox(self.control['顾问转化策略名称输入框'])
        # 输入顾问转化策略名称
        if params['consultant_conversion_strategy_name'] != '':
            self.find_element(self.control['顾问转化策略名称输入框']).send_keys(params['consultant_conversion_strategy_name'])
        # 顾问转化策略选择人群
        self.wait_eleVisible(self.control['顾问转化策略选择人群下拉框'])
        self.select_by_index_down(self.control['顾问转化策略选择人群下拉框'], index=3)
        # 顾问转化策略选择执行策略
        self.wait_eleVisible(self.control['顾问转化策略执行策略下拉框'])
        self.select_by_index_down(self.control['顾问转化策略执行策略下拉框'], index=0)
        # 顾问转化策略策略配置--选择动作
        self.wait_eleVisible(self.control['顾问转化策略选择动作'])
        self.select_by_index_down(self.control['顾问转化策略选择动作'], index=0)
        # 顾问转化策略策略配置--选择页面
        self.wait_eleVisible(self.control['顾问转化策略选择页面'])
        self.select_by_index_down(self.control['顾问转化策略选择页面'], index=4)
        time.sleep(2)
        # 顾问转化策略--选择页面二级选择
        self.wait_eleVisible(self.control['顾问转化策略选择页面二级下拉框'])
        self.select_by_index_down(self.control['顾问转化策略选择页面二级下拉框'], index=0)
        # 成交转化策略引导图片
        if params['path'] != '':
            self.wait_eleVisible(self.control['顾问转化策略上传图片'])
            choose = self.find_element(self.control['顾问转化策略上传图片'])
            ActionChains(self.driver).click(choose).perform()
            time.sleep(2)
            self.upload(params['path'])
            self.wait_eleVisible(self.control['顾问转化策略裁剪框-确定'])
            self.force_click(self.find_element(self.control['顾问转化策略裁剪框-确定']))
            time.sleep(2)
        # 显示设置-到时消失
        self.wait_eleVisible(self.control['顾问转化策略显示设置-到时消失'])
        self.force_click(self.find_element(self.control['顾问转化策略显示设置-到时消失']))
        ActionChains(self.driver).move_to_element(self.find_element(self.control['到时消失下拉框'])).perform()
        time.sleep(1)
        # 到时消失设置成2秒
        ActionChains(self.driver).move_to_element(self.find_element(self.control['到时消失-2秒消失'])).perform()
        time.sleep(2)
        self.find_element(self.control['到时消失-2秒消失']).click()
        time.sleep(2)
        # 发布顾问转化策略
        self.wait_eleVisible(self.control['发布顾问转化策略'])
        self.force_click(self.find_element(self.control['发布顾问转化策略']))


    def pause_visit_conversion_strategy(self):
        # 暂停到访转化策略
        # 点击暂停
        self.wait_eleVisible(self.control['暂停到访转化策略'])
        self.force_click(self.find_elements(self.control['暂停到访转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定到访转化策略暂停'])
        self.force_click(self.find_element(self.control['确定到访转化策略暂停']))

    def pause_transaction_conversion_strategy(self):
        # 暂停成交转化策略
        # 点击暂停
        self.wait_eleVisible(self.control['暂停到访转化策略'])
        self.force_click(self.find_elements(self.control['暂停到访转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定到访转化策略暂停'])
        self.force_click(self.find_element(self.control['确定到访转化策略暂停']))

    def pause_consultant_transformation_strategy(self):
        # 暂停顾问转化策略
        # 点击暂停
        self.wait_eleVisible(self.control['暂停顾问转化策略'])
        self.force_click(self.find_elements(self.control['暂停顾问转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定顾问转化策略暂停'])
        self.force_click(self.find_element(self.control['确定顾问转化策略暂停']))


    def cannot_delete_directly(self):
        # 策略开启状态下点击删除
        self.wait_eleVisible(self.control['删除到访转化策略'])
        self.force_click(self.find_elements(self.control['删除到访转化策略'], 0))
        time.sleep(2)

    def delete_visit_conversion_policy(self):
        # 删除到访转化策略
        # 策略暂停状态下点击删除
        self.wait_eleVisible(self.control['删除到访转化策略'])
        self.force_click(self.find_elements(self.control['删除到访转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定到访转化策略删除'])
        self.force_click(self.find_element(self.control['确定到访转化策略删除']))

    def delete_transaction_conversion_policy(self):
        # 删除成交转化策略
        # 策略暂停状态下点击删除
        self.wait_eleVisible(self.control['删除成交转化策略'])
        self.force_click(self.find_elements(self.control['删除成交转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定成交转化策略删除'])
        self.force_click(self.find_element(self.control['确定成交转化策略删除']))

    def delete_consultant_conversion_policy(self):
        # 删除顾问转化策略
        # 策略暂停状态下点击删除
        self.wait_eleVisible(self.control['删除顾问转化策略'])
        self.force_click(self.find_elements(self.control['删除顾问转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定顾问转化策略删除'])
        self.force_click(self.find_element(self.control['确定顾问转化策略删除']))


    def open_visit_conversion_strategy(self):
        # 点击开启
        self.wait_eleVisible(self.control['开启到访转化策略'])
        self.force_click(self.find_elements(self.control['开启到访转化策略'], 0))
        time.sleep(2)
        # 点击确定
        self.wait_eleVisible(self.control['确定到访转化策略开启'])
        self.find_element(self.control['确定到访转化策略开启']).click()

    def view_visit_forwarding_policy_details(self):
        # 点击详情
        self.wait_eleVisible(self.control['到访转化策略详情'])
        self.force_click(self.find_elements(self.control['到访转化策略详情'], 0))
        # 返回上一页
        time.sleep(5)
        self.driver.back()

    def view_visit_forwarding_policy_data(self):
        # 点击数据
        self.wait_eleVisible(self.control['到访转化策略数据'])
        self.force_click(self.find_elements(self.control['到访转化策略数据'], 0))
        # 返回上一页
        time.sleep(2)
        self.driver.back()

    def type_search(self):
        # 类型筛选
        self.wait_eleVisible(self.control['类型'])
        self.select_by_index_down(self.control['类型'], index=1)

    def status_search(self):
        # 状态筛选
        self.wait_eleVisible(self.control['状态'])
        self.select_by_index_down(self.control['状态'], index=0)

    def title_search(self, params):
        # 标题筛选
        self.wait_eleVisible(self.control['搜索输入框'])
        self.find_element(self.control['搜索输入框']).click()
        if params['title_name'] != '':
            self.find_element(self.control['搜索输入框']).send_keys(params['title_name'])
            time.sleep(1)
            ActionChains(self.driver).send_keys(Keys.ENTER).perform()
            time.sleep(2)

    def edit_visit_transformation_operation_strategy(self):
        # 编辑策略
        self.wait_eleVisible(self.control['编辑到访转化策略'])
        self.force_click(self.find_elements(self.control['编辑到访转化策略'], 0))
        time.sleep(2)
        self.wait_eleVisible(self.control['到访转化策略选择人群下拉框'])
        self.select_by_index_down(self.control['到访转化策略选择人群下拉框'], index=1)
        time.sleep(2)
        self.wait_eleVisible(self.control['到访转化策略执行策略下拉框'])
        self.select_by_index_down(self.control['到访转化策略执行策略下拉框'], index=1)
        time.sleep(1)
        self.wait_eleVisible(self.control['发布到访转化策略'])
        self.force_click(self.find_element(self.control['发布到访转化策略']))
        time.sleep(2)
