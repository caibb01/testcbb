from myweb.core.runner import TestCase
import unittest


class DemoTestCase(TestCase):
    __author__ = "zero"

    def test_case_01(self):
        print("用例执行：2.01.001")
        pass

    def test_case_02(self):
        print("用例执行：2.01.002")
        pass


if __name__ == '__main__':
    unittest.main()
