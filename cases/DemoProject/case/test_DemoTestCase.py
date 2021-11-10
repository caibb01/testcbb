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
        time.sleep(0.1)
        pass

    def test_case_02(self):
        """
        第二个用例 失败
        """
        if not self._check_case(["C00002x"]): return
        self.assertEqual(1, 2)
        time.sleep(0.2)


if __name__ == '__main__':
    import unittest

    unittest.main()
