from myweb.core.runner import TestCase
import unittest
import time


class DemoTestCase02(TestCase):
    def test_case_03(self):
        """
        test_case_03 success
        """
        print("test_case_03 success")
        time.sleep(0.3)
        pass


if __name__ == '__main__':
    unittest.main()
