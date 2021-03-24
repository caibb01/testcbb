from myweb.core.runner import My4wTestCase
import unittest
import time

class DemoTestCase02(My4wTestCase):
    def test_case_01(self):
        """
        test_case_01 success
        """
        # print("test_case_01 success")
        # print("另2种方式执行")
        pass

    def test_case_02(self):
        """
        test_case_02 fail
        """
        # print("test_case_01 fail")
        time.sleep(2)
        print(time.time())
        self.assertEqual(1, 2)

    def test_case_03(self):
        # print("test_case_03 error")
        time.sleep(0.2)
        # raise Exception

if __name__ == '__main__':
    unittest.main()