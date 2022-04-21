import os
import time
import unittest
from ddt import data, ddt
from cases.AICardProject.logic.LoginLogic import LoginLogic
from cases.AICardProject.logic.marketingBusinessCenterLG.OperationStrategyLg import OperationStrategyLg
from myweb.core.runner import TestCase
from myweb.tools.env_params import get_env_params
from myweb.utils.config import JsonConfig


@ddt
class test_operation_Strategy(TestCase):
    __author__ = "mabb01"
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
        super(test_operation_Strategy, cls).setUpClass()
        cls.loginLogic = LoginLogic(cls.driver)
        cls.OperationStrategyLg = OperationStrategyLg(cls.driver)
        cls.env_param = get_env_params()
        cls.loginLogic.login(url=cls.env_param['url'],
                             username=cls.env_param['username'],
                             password=cls.env_param['password'],
                             orgname=cls.env_param['orgname'])
        cls.loginLogic.logincheck(cls.env_param['loginuser'])
        cls.loginLogic.openAI(cls.env_param['ai_xpath'])

    @data(
        {
            "path": IMAGE_PATH,

        }
    )
    def test_case_01_new_visit_transformation_strategy(self, data):
        if not self._check_case(["C00261"]): return
        params = {
            "path": data['path'],
            "visit_conversion_policy_name": "mbb创建的到访转化策略",

        }
        # 进入营销业务中心--运营策略
        self.OperationStrategyLg.enter_operation_strategy_lg()
        # 新增到访转化策略
        self.OperationStrategyLg.new_visit_transformation_strategy_lg(params)
        time.sleep(2)

    def test_case_02_edit_visit_transformation_operation_strategy(self):
        if not self._check_case(["C00265"]): return
        # 编辑策略
        self.OperationStrategyLg.edit_visit_transformation_operation_strategy_lg()
        time.sleep(3)

    def test_case_03_search_operation_strategy(self):
        if not self._check_case(["C00262"]): return
        params = {
            "title_name": "mbb创建的到访转化策略",

        }
        # 选择类型筛选运营策略
        self.OperationStrategyLg.status_search_lg()
        time.sleep(2)
        # 选择状态筛选运营策略
        self.OperationStrategyLg.type_search_lg()
        time.sleep(2)
        # 通过标题筛选运营策略
        self.OperationStrategyLg.title_search_lg(params)
        time.sleep(2)

    def test_case_04_cannot_delete_directly(self):
        if not self._check_case(["C00742"]): return
        # 策略开启状态下无法直接删除策略
        self.OperationStrategyLg.cannot_delete_directly_lg()
        time.sleep(3)

    def test_case_05_pause_visit_conversion_strategy(self):
        if not self._check_case(["C00263"]): return
        # 暂停到访转化策略
        # 暂停策略
        self.OperationStrategyLg.pause_visit_conversion_strategy_lg()
        time.sleep(3)

    def test_case_06_open_visit_conversion_strategy(self):
        if not self._check_case(["C00264"]): return
        # 暂停到访转化策略
        # 开启策略
        self.OperationStrategyLg.open_visit_conversion_strategy_lg()
        time.sleep(3)

    def test_case_07_view_visit_forwarding_policy_details(self):
        if not self._check_case(["C00266"]): return
        # 进入到访转化策略详情
        self.OperationStrategyLg.view_visit_forwarding_policy_details_lg()
        time.sleep(6)

    def test_case_08_view_visit_forwarding_policy_data(self):
        if not self._check_case(["C00741"]): return
        # 进入到访转化策略数据详情
        self.OperationStrategyLg.view_visit_forwarding_policy_data_lg()
        time.sleep(2)

    def test_case_09_delete_visit_conversion_policy(self):
        if not self._check_case(["C00740"]): return
        # 暂停到访转化策略
        self.OperationStrategyLg.pause_visit_conversion_strategy_lg()
        time.sleep(2)
        # 删除到访转化策略
        self.OperationStrategyLg.delete_visit_conversion_policy_lg()
        time.sleep(3)

    def test_case_10_new_transaction_conversion_strategy(self):
        if not self._check_case(["C00261"]): return
        params = {
            "name_of_transaction_conversion_strategy": "mbb创建的成交转化策略",

        }
        # 新建成交转化策略
        self.OperationStrategyLg.new_transaction_conversion_strategy_lg(params)
        time.sleep(2)

    def test_case_11_delete_transaction_conversion_policy(self):
        if not self._check_case(["C00740"]): return
        # 暂停成交转化策略
        self.OperationStrategyLg.pause_transaction_conversion_strategy_lg()
        time.sleep(2)
        # 删除成交转化策略
        self.OperationStrategyLg.delete_transaction_conversion_policy_lg()
        time.sleep(2)

    @data(
        {
            "path": IMAGE_PATH,

        }
    )
    def test_case_12_new_consultant_transformation_strategy(self, data):
        if not self._check_case(["C00261"]): return
        params = {
            "consultant_conversion_strategy_name": "mbb创建的顾问转化策略",
            "path": data['path'],

        }
        # 新建成交转化策略
        self.OperationStrategyLg.new_consultant_transformation_strategy_lg(params)
        time.sleep(2)

    def test_case_13_delete_consultant_conversion_policy(self):
        if not self._check_case(["C00740"]): return
        # 暂停顾问转化策略
        self.OperationStrategyLg.pause_consultant_conversion_strategy_lg()
        time.sleep(2)
        # 删除顾问转化策略
        self.OperationStrategyLg.delete_consultant_conversion_policy_lg()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        time.sleep(2)
        super(test_operation_Strategy, cls).tearDownClass()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
