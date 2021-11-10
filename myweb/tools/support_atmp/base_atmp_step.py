# -*- coding:utf-8 -*-
from myweb.core.BasePage import *


class BaseAtmp(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)

    # 等待某个元素出现
    def waitfor_not_exist_short(self, element, by=By.XPATH):
        # try:
            BasePage.wait_eleVisible(self, (by, element))
        # except:
        #     print(u"找不到元素：%s" % element[0])

    # 判断某个元素是否存在
    def is_waitfor_exist_short(self, element, by=By.XPATH):
        try:
            BasePage.wait_eleVisible(self, (by, element[0]))
            return True
        except:
            print(u"找不到元素：%s" % element[0])
            return False

    # 点击某个元素
    def click(self, element, by=By.XPATH):
        self.waitfor_not_exist_short(element[0], by=By.XPATH)
        els = self.find_element((by, element[0]))
        BasePage.click(self, els)

    # 输入文本
    def input_text(self, element, by=By.XPATH):
        self.waitfor_not_exist_short(element[0])
        els = self.find_element((by, element[0]))
        els.send_keys(element[1])

    # 输入文本
    def set_text(self, element, by=By.XPATH):
        print("###")
        print(element[0])
        self.waitfor_not_exist_short(element[0])
        els = self.find_element((by, element[0]))
        els.send_keys(element[1])

    # 获取属性
    def get_attri(self,element,by=By.XPATH):
        self.waitfor_not_exist_short(element[0])
        els = self.find_element((by, element[0]))
        return els.get_attribute(element[1])

    # 关闭窗口
    def close_window(self):
        self.driver.close()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 执行js脚本
    def eventjs(self,js):
        self.driver.execute_script(js)

    # 访问页面
    def visit(self,url):
        self.driver.get(url)


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("https://www.baidu.com")
    b = BaseAtmp(driver)
    print(b.waitfor_not_exist_short([".//input[@id='kw']"],by=By.XPATH))
    # time.sleep(1)
    # b.eventjs("document.getElementById('su').click()")
    # print(result)
    # driver.close()
