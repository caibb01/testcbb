# -*- coding:utf-8 -*-
from fuzzywuzzy import fuzz
from selenium.webdriver.common.by import By
from time import sleep
from myweb.core.runner import TestCase
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from myweb.core.BasePage import BasePage


class customersManagement(BasePage,TestCase):
    control = {
       "客群管理":(By.XPATH,'//header[@class="pages-manager_user_group-index-module_3m0qv"]/h3')
    }

    def __init__(self, driver):
        super(customersManagement, self).__init__(driver)

    def check_title(self,checkData):
        '''检查客群管理页面的标题'''
        sleep(2)
        actualResult = self.find_element(self.control['客群管理']).text
        # print('actualResult:'+actualResult)
        # print("checkData['expectData']:"+checkData['expectData'])
        self.assertIn(actualResult,checkData['expectData'],msg=checkData['msg'])