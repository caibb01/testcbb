# -*- encoding=utf8 -*-
from myweb.core.runner import TestCase
import time
from myweb.tools.support_atmp.is_skip_case import is_skip


class DemoTestCase(TestCase):
    __author__ = "zero"

    def test_case_01(self):
        self.test_code = ["C00001", ]
        """
        第一个用例 成功
        """
        if is_skip(self.test_code):
            time.sleep(0.2)
            print("另一种方式执行")
            pass

    def test_case_02(self):
        self.test_code = ["C00002"]
        """
        第二个用例 失败
        """
        # print("test_case_01 fail")
        time.sleep(0.2)
        # print(time.time())
        # self.assertEqual(1, 2)

    # def test_case_03(self):
    #     self.test_code = "C12001"
    #     """
    #     第三个用例 失败
    #     """
    #     time.sleep(0.2)
    #     # raise Exception


if __name__ == '__main__':
    import unittest

    unittest.main()
