import os
import jpype
from jpype import *
from selenium import webdriver


class SikuliOperate(object):
    def __init__(self):
        try:
            jvmPath = jpype.getDefaultJVMPath()
            jpype.startJVM(jvmPath, "-ea", "-Djava.class.path=%s" % 'sikulix.jar')
            Screen = JClass("org.sikuli.script.Screen")  # 调用sikuli
            self.screen = Screen()
        except Exception as e:
            print(str(e))

    def sikuli_click(self, image_path):
        """
        通过图片点击
        :param image_path:  图片路径
        :return:
        """
        try:
            self.screen.click(image_path)
        except Exception as e:
            print(str(e))

    def sikuli_send_keys(self, image_path, text):
        """
        获取指定组件并输入内容
        :param image_path: 图片路径
        :param text: 内容
        :return:
        """
        try:
            self.screen.type(image_path, text)
        except Exception as e:
            print(str(e))

    def sikuli_double_click(self, image_path):
        """
        双击组件
        :param image_path: 图片路径
        :return:
        """
        try:
            self.screen.doubleClick(image_path)
        except Exception as e:
            print(str(e))

    def sikuli_right_click(self, image_path):
        """
        右击
        :param image_path: 图片路径
        :return:
        """
        try:
            self.screen.rightClick(image_path)
        except Exception as e:
            print(str(e))

    def sikuli_drag_drop(self, image_path1, image_path2):
        """
        拖拽组件
        :param image_path1: 拖拽组件图片路径
        :param image_path2: 拖拽后移动位置
        :return:
        """
        try:
            self.screen.dragDrop(image_path1, image_path2)
        except Exception as e:
            print(str(e))

    def sikuli_shutdowm(self):
        """
        关闭sikuli
        :return:
        """
        try:
            jpype.shutdownJVM()
        except Exception as e:
            print(str(e))


if __name__ == "__main__":
    driver = webdriver.Chrome(executable_path="D:\\chromedriver.exe")
    driver.get("https://mars-test.myscrm.cn/")
    driver.maximize_window()
    current_path = os.getcwd()
    so = SikuliOperate()
    so.sikuli_drag_drop(os.path.join(current_path, "image_package", "1638787671424.png"),
                        os.path.join(current_path, "image_package", "1.png"))
    # # so.sikuli_click(r"D:\testgit\yk-ui-baseframe\myweb\tools\sikuli\sikuli.sikuli\1638787711741.png")
    # so.sikuli_send_keys(r"D:\testgit\yk-ui-baseframe\myweb\tools\sikuli\sikuli.sikuli\1638787711741.png","f-20211122-optimization")
    # so.sikuli_click(r"D:\testgit\yk-ui-baseframe\myweb\tools\sikuli\sikuli.sikuli\1638787812618.png")
    so.sikuli_shutdowm()
    driver.quit()
