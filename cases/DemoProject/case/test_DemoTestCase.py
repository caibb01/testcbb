# -*- encoding=utf8 -*-
from myweb.core.runner import TestCase
import time


class DemoTestCase(TestCase):
    __author__ = "zero"

    def test_case_01(self):
        """
        第一个用例 成功
        """
        if not self._check_case(["C00001"]): return
        time.sleep(0.2)
        print("另一种方式执行")
        pass


def test_case_02(self):
    if self._check_case(["C0000X"]): return
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
