import os
import time
import unittest

from ddt import data, ddt

from cases.AICardProject.logic.marketingBusinessCenterLG.bookingManagementLg import bookingManagementLG
from cases.AICardProject.logic.LoginLogic import LoginLogic
from myweb.core.runner import TestCase

from myweb.utils.config import JsonConfig
from myweb.tools.env_params import get_env_params


@ddt
class test_bookingManagement(TestCase):
    __author__ = "guogy"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()
    # 获取图片路径
    IMAGE_PATH = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data', 'image',
                              'th.jpg')

    @classmethod
    def setUpClass(cls):
        super(test_bookingManagement, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.bookingManagementLg = bookingManagementLG(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        # cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
    @data({
        "path": IMAGE_PATH
    })
    def test_bookingManagement(self, data):
        if not self._check_case(["C00277", "C00278", "C00279", "C00280", "C00281", "C00282",
                                 "C00283", "C00284", "C00285", "C00286", "C00287", "C00288",
                                 "C00289"]): return
        params = {
            "path": data['path'],
            # "pro_name": "G0小郭专属项目",
            "description": "预约看房，请准时。",
            "p_name": "天地玄黄",
            "enter_name": "姓名",
            "p_name2": "天地玄黄",
            "days": "39",
            "phone01": "17152774953",
            "phone02": "13135681435"
        }
        # 进入【预约管理】
        self.bookingManagementLg.into_booking_management(params)
        # 项目【预约须知设置】操作
        self.bookingManagementLg.booking_instructions_option(params)
        # 【页面设置】操作
        self.bookingManagementLg.booking_page_setup(params)
        self.bookingManagementLg.into_booking_management(params)
        # 【填写字段设置-添加字段】操作
        self.bookingManagementLg.add_filed_option()
        # 【填写字段设置-自定义字段】操作
        self.bookingManagementLg.add_custom_filed(params)
        # 【接待量设置】操作
        self.bookingManagementLg.reception_setting_option()
        # 【可预约日期】操作
        self.bookingManagementLg.appointment_date_option(params)
        # 【资格验证设置】操作
        self.bookingManagementLg.qualification_setting_option(params)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        super(test_bookingManagement, cls).tearDownClass()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
