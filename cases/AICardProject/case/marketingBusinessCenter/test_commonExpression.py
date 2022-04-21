import unittest
import os
import time
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.commonExpressionLg import CommonExpressionLg
from myweb.core.runner import TestCase
from myweb.tools.env_params import get_env_params
from myweb.utils.config import JsonConfig


class test_commonExpression(TestCase):
    __author__ = "yeting"
    # 登录配置数据
    __data_path = os.path.join(os.path.abspath(os.path.join(os.path.abspath(__file__), "../../..")), 'data',
                               'loginInfo.json')
    # 获取登录数据
    __login_data = JsonConfig(__data_path).get()

    @classmethod
    def setUpClass(cls):
        super(test_commonExpression, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.env_param = get_env_params()
        cls.commonExpression = CommonExpressionLg(cls.driver)
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])
        cls.commonExpression.into_common_expression_page()

    def test_01_add_buyer_expression(self):
        if not self._check_case(["C00315"]): return
        self.commonExpression.add_buyer_expression()

    def test_02_add_seller_expression(self):
        if not self._check_case(["C00318"]): return
        self.commonExpression.add_seller_expression()

    def test_03_edit_expression(self):
        if not self._check_case(["C00324"]): return
        self.commonExpression.edit_expression()

    def test_04_delete_expression(self):
        if not self._check_case(["C00325"]): return
        self.commonExpression.delete_expression()

    def tearDown(self):
        super(test_commonExpression, self).tearDown()

    @classmethod
    def tearDownClass(cls):
        super(test_commonExpression, cls).tearDownClass()


if __name__ == '__main__':
    unittest.main()
