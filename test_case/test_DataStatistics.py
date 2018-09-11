# -*- coding: utf-8 -*-
# @Time    : 2018/9/11/011 14:17
# @Author  : Administor
# @File    : test_DataStatistics.py
# @Software: PyCharm
import unittest
from Log.logger import Logger
from config.readConfig import ReadConfig
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import requests
import ssl
from common.browser_driver import *
from common.base_common import *
from page.LoginPage import *
from page.DataStatistics import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='test_case').getlog()


class test_DataStatistics(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)
        logger.info('test_DataStatistics start')

    def test_data_statistics(self):
        dr = base_common(self.driver)
        input_username(page.user_name, dr)
        input_password(page.passwd, dr)
        click_submit(dr)
        click_regist_statistics(dr,page.data_statistics,page.regist_statistics,page.start_time,page.start_time_value,page.end_time,page.end_time_value,page.channel,page.all_channel,page.regist_query)
        logger.info("注册成功人数：%s" % get_text(dr,page.obtain_succ_regist))

    def tearDown(self):
        # browser_driver.quit_browser(self)
        logger.info('test_DataStatistics end \r\n')


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')