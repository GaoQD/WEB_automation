# -*- coding: utf-8 -*-
# @Time    : 2018/9/5/005 9:57
# @Author  : Administor
# @File    : test_ProductCommonProblem.py
# @Software: PyCharm
import unittest
from Log.logger import Logger
from config.readConfig import ReadConfig
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import requests
import ssl
from selenium import webdriver
import time
import page.page as page
from common.browser_driver import browser_driver
from page.LoginPage import *
from common.base_common import base_common

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='test_case').getlog()


class test_ProductCommonProblem(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)
        logger.info('test_ProductCommonProblem start')

    def test_product_common_problem(self):
        dr = base_common(self.driver)
        input_username(page.user_name, dr)
        input_password(page.passwd, dr)
        click_submit(dr)

    def tearDown(self):
        browser_driver.quit_browser(self)
        logger.info('test_ProductCommonProblem end \r\n')


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')