from myweb.core.runner import TestCase
import unittest


class DemoTestCase02(TestCase):
    def test_case_01(self):
        print("用例执行：test_case_01")
        pass


if __name__ == '__main__':
    unittest.main()
