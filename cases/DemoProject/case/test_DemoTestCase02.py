import time

from myweb.core.runner import TestCase
import unittest


class DemoTestCase02(TestCase):
    @classmethod
    def setUpClass(cls):
        super(DemoTestCase02, cls).setUpClass()

    def test_case_01(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.maximize_window()
        time.sleep(5)

if __name__ == '__main__':
    unittest.main()
