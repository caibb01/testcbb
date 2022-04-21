# -*- coding:utf-8 -*-

# from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, logging
from pykeyboard import PyKeyboard
import myweb.core.runner as cf
import datetime, os
import platform

if (platform.system() == 'Windows'):
    import win32gui
    import win32con


class BasePage(object):
    """description of class"""

    # webdriver instance
    def __init__(self, driver):
        '''
        initialize selenium webdriver, use chrome as default webdriver
        '''
        self.driver = driver
        self.storage = None

    def move_mouse_to_element(self, element):
        '''
        :param element:
        :return: 移动鼠标到指定的元素上
        '''
        try:
            type = element[0]
            value = element[1]
            if type.lower() == "id" or type.lower() == By.ID:
                el = self.driver.find_element_by_id(value)
            elif type.lower() == "name" or type.lower() == By.NAME:
                el = self.driver.find_element_by_name(value)
            elif "class" in type or type.lower() == "class" or type.lower() == By.CLASS_NAME:
                el = self.driver.find_element_by_class_name(value)
            elif type.lower() == "link_text" or type.lower() == By.LINK_TEXT:
                el = self.driver.find_element_by_link_text(value)
            elif type.lower() == "xpath" or type.lower() == By.XPATH:
                el = self.driver.find_element_by_xpath(value)
            elif "css" in type or type.lower() == "css" or type.lower() == By.CSS_SELECTOR:
                el = self.driver.find_element_by_css_selector(value)
            elif "tag" in type:
                el = self.driver.find_element_by_tag_name(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception as err:
            raise ValueError("No such element found" + str(element))
        ActionChains(self.driver).move_to_element(el).perform()

    def find_element(self, element, wait_times=10):
        '''
        :param element:
        :return: 找单个控件
        '''
        self.wait_eleVisible(element, wait_times=wait_times)
        element = self.driver.find_element(*element)
        self._mark(element)
        return element

    def find_elements(self, element, num):
        '''
        :param element: 找多个控件的第num个元素
        :param num:
        :return:
        '''
        try:
            type = element[0]
            value = element[1]
            global elem
            if type.lower() == "id" or type.lower() == By.ID:
                elem = self.driver.find_elements_by_id(value)

            elif type.lower() == "name" or type.lower() == By.NAME:
                elem = self.driver.find_elements_by_name(value)

            elif type.lower() == "class" or type.lower() == By.CLASS_NAME:
                elem = self.driver.find_elements_by_class_name(value)

            elif type.lower() == "link_text" or type.lower() == By.LINK_TEXT:
                elem = self.driver.find_elements_by_link_text(value)

            elif type.lower() == "xpath" or type.lower() == By.XPATH:
                elem = self.driver.find_elements_by_xpath(value)

            elif type.lower() == "css" or type.lower() == By.CSS_SELECTOR:
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception as err:
            logging.info('the len(elem) : %s' % str(len(elem)))
            raise ValueError("No such element found" + str(element))
        print(len(elem))
        return elem[num]

    def find_elements_list(self, element):
        try:
            type = element[0]
            value = element[1]
            global elem
            if type.lower() == "id" or type.lower() == By.ID:
                elem = self.driver.find_elements_by_id(value)

            elif type.lower() == "name" or type.lower() == By.NAME:
                elem = self.driver.find_elements_by_name(value)

            elif type.lower() == "class" or type.lower() == By.CLASS_NAME:
                elem = self.driver.find_elements_by_class_name(value)

            elif type.lower() == "link_text" or type.lower() == By.LINK_TEXT:
                elem = self.driver.find_elements_by_link_text(value)

            elif type.lower() == "xpath" or type.lower() == By.XPATH:
                elem = self.driver.find_elements_by_xpath(value)

            elif type.lower() == "css" or type.lower() == By.CSS_SELECTOR:
                elem = self.driver.find_elements_by_css_selector(value)
            else:
                raise NameError("Please correct the type in function parameter")
        except Exception as err:
            logging.info('the len(elem) : %s' % str(len(elem)))
            raise ValueError("No such element found" + str(element))
        return elem

    def is_elem_visible(self, element):
        '''
        :param element:
        :return: 判断元素是不是可以点击
        '''
        type = element[0]
        value = element[1]
        if type.lower() == "id" or type.lower() == By.ID:
            el = self.driver.find_element_by_id(value).is_displayed()
        elif type.lower() == "name" or type.lower() == By.NAME:
            el = self.driver.find_element_by_name(value).is_displayed()
        elif "class" in type or type.lower() == "class" or type.lower() == By.CLASS_NAME:
            el = self.driver.find_element_by_class_name(value).is_displayed()
        elif type.lower() == "link_text" or type.lower() == By.LINK_TEXT:
            el = self.driver.find_element_by_link_text(value).is_displayed()
        elif type.lower() == "xpath" or type.lower() == By.XPATH:
            el = self.driver.find_element_by_xpath(value).is_displayed()
        elif "css" in type or type.lower() == By.CSS_SELECTOR:
            el = self.driver.find_element_by_css_selector(value).is_displayed()
        else:
            el = self.driver.find_element_by_tag_name(value).is_displayed()
        return el

    def is_exist_element(self, element, timeout=3):
        '''
        :param element:
        :return: 检查是否存在唯一控件
        '''
        start_time = time.time()
        flag = False
        while time.time() - start_time <= timeout:
            elem = None
            try:
                type = element[0]
                value = element[1]
                if type == "id" or type == "ID" or type == "Id" or type == By.ID:
                    elem = self.driver.find_element_by_id(value)
                elif type == "name" or type == "NAME" or type == "Name" or type == By.NAME:
                    elem = self.driver.find_element_by_name(value)

                elif type == "class" or type == "CLASS" or type == "Class" or type == 'class name' or type == By.CLASS_NAME:
                    elem = self.driver.find_element_by_class_name(value)

                elif "link" in type or type == "link_text" or type == "LINK_TEXT" or type == "Link_text" or type == 'link text' or type == By.LINK_TEXT:
                    elem = self.driver.find_element_by_link_text(value)

                elif type == "xpath" or type == "XPATH" or type == "Xpath" or type == By.XPATH:
                    elem = self.driver.find_element_by_xpath(value)

                elif type == "css" or type == "CSS" or type == "Css" or type == "css selector" or type == By.CSS_SELECTOR:
                    elem = self.driver.find_element_by_css_selector(value)
                else:
                    raise NameError("Please correct the type in function parameter")
            except Exception as e:
                print(e)
            finally:
                if elem:
                    flag = True
                    break
        if not flag:
            print('未找到元素：', element)
        else:
            self._mark(elem)
        cf._step_screenshot(driver=self.driver, ty="is_exist", type_name="判断元素", msg=str(element) + str(flag))
        return flag

    def get_page_info(self):
        '''
        :return: 页面信息
        '''
        info = self.driver.page_source
        return info

    def switch_to_alert(self):
        '''
        :return: 关闭弹框
        '''
        alert = self.driver.switch_to_alert()
        time.sleep(3)
        alert.dismiss()

    def switch_to_windows(self):
        '''
        :return:跳转到新的页面
        '''
        return self.driver.switch_to_window(self.driver.window_handles[1])

    def switch_to_active_element(self):
        '''
        :return: 跳转到活跃的页面
        '''
        return self.driver.switch_to.active_element

    def refresh(self):
        '''
        :return: 刷新当前界面
        '''
        self.driver.refresh()

    def send_keys(self, keywords):
        '''
        :param keywords: 暂时支持TAB，回车，右建，ESC和输入字符串
        :return: 模拟键盘输入
        '''
        k = PyKeyboard()
        if "{" not in keywords:
            k.type_string(keywords)
        elif "TAB" in keywords:
            k.tap_key(k.tab_key)
        elif "ENTER" in keywords:
            # k.press_key(k.enter_key)
            # k.release_key(k.enter_key)
            k.tap_key(k.enter_key)
        elif "RIGHT" in keywords:
            # k.press_key(k.right_key)
            # k.release_key(k.right_key)
            k.tap_key(k.right_key)
        elif "ESC" in keywords:
            k.tap_key(k.escape_key)
        elif "BACKSPACE" in keywords:
            k.tap_key(k.backspace_key)
        else:
            logging.info("keywords : %s is not support " % keywords)

    def open(self, url):
        '''
        Open web url

        Usage:
        self.open(url)
        '''
        if url != "":
            self.driver.get(url)
        else:
            raise ValueError("please provide a base url")

    def type(self, element, text):
        '''
        Operation input box.

        Usage:
        self.type(element,text)
        '''
        element.send_keys(text)

    def enter(self, element):
        '''
        Keyboard: hit return

        Usage:
        self.enter(element)
        '''
        element.send_keys(Keys.RETURN)

    def click(self, element):
        '''
        Click page element, like button, image, link, etc.
        '''
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script('arguments[0].click()', element)
        except ElementNotInteractableException:
            self.driver.execute_script('arguments[0].click()', element)
        except:
            ActionChains(self.driver).move_to_element(element).click().perform()

    def quit(self):
        '''
        Quit webdriver
        '''
        self.driver.quit()

    def getAttribute(self, element, attribute):
        '''
        Get element attribute

        '''
        return element.get_attribute(attribute)

    def getText(self, element):
        '''
        Get text of a web element

        '''
        return element.text

    def getTitle(self):
        '''
        Get window title
        '''
        return self.driver.title

    def getCurrentUrl(self):
        '''
        Get current url
        '''
        return self.driver.current_url

    def getScreenshot(self, targetpath):
        '''
        Get current screenshot and save it to target path
        '''
        self.driver.get_screenshot_as_file(targetpath)

    def maximizeWindow(self):
        '''
        Maximize current browser window
        '''
        self.driver.maximize_window()

    def back(self):
        '''
        Goes one step backward in the browser history.
        '''
        self.driver.back()

    def forward(self):
        """
        Goes one step forward in the browser history.
        """
        self.driver.forward()

    def getWindowSize(self):
        """
        Gets the width and height of the current window.
        """
        return self.driver.get_window_size()

    def upload(self, filepath):
        """
        非input标签上传操作,与windows弹窗进行交互
        :param filepath: 文件绝对路径
        :return:
        """
        dialog = win32gui.FindWindow("#32770", "打开")  # 一级窗口
        comboBoxEx32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)  # 二级
        comboBox = win32gui.FindWindowEx(comboBoxEx32, 0, "ComboBox", None)  # 三级
        edit = win32gui.FindWindowEx(comboBox, 0, "Edit", None)  # 四级
        button = win32gui.FindWindowEx(dialog, 0, "Button", None)  # 四级

        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, filepath)  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

    def upload_new(self, image_path, el, loading_el=None, end_el=None, timeout=10):
        """

        :param image_path: 文件地址
        :param el: 上传文件元素
        :param loading_el: 可以表明元素正在loading的元素（例如upload-progress）
        :param end_el: 可以表明元素已经结束上传的元素（例如finish-load-progress）
        :param timeout: 上传文件的总时长，超出时间则会抛出异常
        :return:
        """
        start_time = time.time()
        if self.is_exist_element(el):
            self.find_element(el).send_keys(image_path)
        while time.time() - start_time <= timeout:
            if loading_el and (not self.is_exist_element(loading_el)):
                break
            if self.is_exist_element(end_el):
                break
        else:
            raise Exception("upload image timeout!")

    def wait_eleVisible(self, controls, wait_times=10, poll_frequencey=0.5):
        """
        显性等待元素可见
        :param controls: 元素定位
        :param wait_times: 等待时间
        :param poll_frequencey: 时间间隔查询一次
        :return:
        """
        result = WebDriverWait(self.driver, timeout=wait_times, poll_frequency=poll_frequencey).until(
            EC.visibility_of_all_elements_located(controls))
        return result

    def _mark(self, el):
        mark_flag, _ = cf._decide_config("mark")
        if mark_flag:
            self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", el,
                                       'border: 5px solid red;')

    def compare_image(self, original_image_path):
        """
        图片对比
        :param original_image: 原图路径,推荐png类型图片
        :return: 返回对比图片的匹配度
        """
        current_stamp = datetime.datetime.now().timestamp()
        file_time = datetime.datetime.fromtimestamp(current_stamp).strftime("%Y%m%d%H%M%S")
        file_dir = os.path.split(original_image_path)
        file_name = os.path.splitext(file_dir[1])
        print(file_dir)
        print(file_name)
        new_imge_path = os.path.join(file_dir[0], file_name[0] + file_time + ".png")
        print(new_imge_path)
        self.driver.save_screenshot(new_imge_path)
        from myweb.tools.image_compare import ImageCompare
        img_comp = ImageCompare()
        return img_comp.calc_similar_by_path(original_image_path, new_imge_path) * 100

    def assert_compare_image_mach(self, original_image_path, percentage=100):
        """
        断言图片匹配度
        :param original_image_path: 原图路径
        :param percentage: 匹配程度，默认100匹配,传小数或整数
        :return:
        """
        image_percentage = self.compare_image(original_image_path)
        if image_percentage >= percentage:
            return True
        else:
            return False
