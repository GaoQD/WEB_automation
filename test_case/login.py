# -*- coding: utf-8 -*-
# @Time    : 2018/9/6/006 16:57
# @Author  : Administor
# @File    : login.py
# @Software: PyCharm
import unittest
from common.browser_driver import browser_driver
from page.LoginPage import input_username,input_password,click_submit
import page.page as page
from common.base_common import base_common

class test_Login(unittest.TestCase):
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)

    def test_login(self):
        dr = base_common(self.driver)
        input_username(page.user_name,dr)
        input_password(page.passwd,dr)
        click_submit(dr)

    def tearDown(self):
        # self.driver.quit()
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore')