from myweb.core.runner import TestCase
import unittest


class DemoTestCase(TestCase):
    __author__ = "zero"

    def test_case_01(self):
        if not self._check_case(["C11001"]): return
        print("用例执行：test_case_01")
        pass

    def test_case_02(self):
        if not self._check_case(["C11002"]): return
        print("用例执行：test_case_02")
        raise Exception("实际结果不一致")


if __name__ == '__main__':
    unittest.main()
