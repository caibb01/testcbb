from myweb.core.runner import TestCase
import unittest


class DemoTestCase(TestCase):
    __author__ = "zero"

    def test_case_01(self):
        """
        第一个用例 成功
        """
        if not self._check_case(["C00001"]): return
        print("用例执行：test_case_01")
        pass

    def test_case_02(self):
        if not self._check_case(["C00002"]): return
        print("用例执行：test_case_02")
        raise Exception("实际结果不一致")

    def test_case_03(self):
        print("用例执行：test_case_03")
        pass

    def test_case_04_01(self):
        if not self._check_case(["C00004"], "pass_part"): return
        print("用例执行：test_case_04")
        pass

    def test_case_04_02(self):
        if not self._check_case(["C00004"], "pass_all"): return
        print("用例执行：test_case_04")
        pass

    def test_case_05(self):
        if not self._check_case(["C00005"]): return
        print("用例执行：test_case_05")
        pass


if __name__ == '__main__':
    unittest.main()
