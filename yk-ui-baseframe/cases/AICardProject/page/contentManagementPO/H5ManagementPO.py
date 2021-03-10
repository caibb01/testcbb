#-*- coding:utf-8 -*-
from selenium.webdriver.common.by import By
from util.BasePage import BasePage
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from pymouse import PyMouse
from pykeyboard import PyKeyboard

class H5ManagementPO(BasePage):
    controls = {
        "添加": (By.XPATH, "//*[text()='添 加']"),
        "标题": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[2]/input'),
        "描述": (By.XPATH, "//*[@class='ant-input fs-12']"),
        "链接": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/input'),
        "类型": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div/div/div/div'),
        "类型-选择": (By.XPATH, '/html/body/div[2]/div/div[2]/div/div[2]/div[2]/div/div[4]/div[2]/div/div/div/div'),

        "关联项目": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "关联地区": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "关联地区": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),
        "输入查询条件": (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/span/input'),

    }