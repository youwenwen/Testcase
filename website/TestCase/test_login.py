import unittest
from time import sleep
from website.TestCase.model import function, myunit
from website.TestCase.page_object.LoginPage import *


class LoginTest(myunit.MyTest):
    def test_login01(self):
        print("test_login01 is start running...")
        po = LoginPage(self.driver)
        po.login_action("test", "123456")
        sleep(3)
        self.assertEqual(po.type_loginPass_hint(), "修改密码00")
        function.insert_img(self.driver, "login01.png")
        print("test_login01's test is end")

    def test_login02(self):
        print("test_login02 is start running...")
        po = LoginPage(self.driver)
        po.login_action("wyou", "12345678")
        sleep(3)
        self.assertEqual(po.type_loginFail_hint(), "")
        function.insert_img(self.driver, "login02.png")
        print("test_login02's test is end")

    def test_login03(self):
        print("test_login03 is start running...")
        po = LoginPage(self.driver)
        po.login_action("", "")
        sleep(3)
        self.assertEqual(po.type_loginFail_hint(), "")
        function.insert_img(self.driver, "login03.png")
        print("test_login03's test is end")


if __name__ == '__main__':
    unittest.main()
