# -*- coding: utf-8 -*-
# @Time    : 2018/9/10/010 17:55
# @Author  : Administor
# @File    : test_ChannelManagement.py
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
from page.LoginPage import *
from common.base_common import *
from common.browser_driver import *
from page.ChannelManagement import *
from config.DBConfig import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='test_case').getlog()


class test_ChannelManagement(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)
        logger.info('test_ChannelManagement start')

    def test_channel_management(self):
        dr = base_common(self.driver)
        input_username(page.user_name, dr)
        input_password(page.passwd, dr)
        click_submit(dr)
        click_channel_management(dr,page.market_promotion,page.channel_management)
        channel_name_query(dr,page.channel_name,page.channel_value,page.query_button,page.reset_search)
        sql = "SELECT COUNT(id) FROM channel WHERE channel_name='天天爱看' AND is_delete=0"
        self.assertIn(get_page_text(dr, page.limit), str(select_mysql(sql)[0]), logger.info("比对结果正确"))
        channel_parameter_query(dr,page.reset_search,page.channel_parameter,page.channel_parameter_value,page.query_button)
        sql1 = "SELECT channel_name FROM channel WHERE channel_parameter='pc-channel-ttak'"
        self.assertIn(get_text(dr,page.select_result),select_mysql(sql1),logger.info("比对结果正确"))
        add_channel(dr,page.add_channel,page.add_channel_name,page.add_channel_param,page.next_step,page.add_channel_commit,page.add_commit_next,page.pane_succ_commit,page.pane_fail_commit,page.pane_old_commit)
        channel_name_query(dr,page.channel_name,page.add_channel_value,page.query_button,page.reset_search)
        sql2 = "SELECT channel_name FROM channel WHERE channel_name='" + page.add_channel_value + "' AND is_delete=0"
        self.assertIn(get_text(dr,page.select_result),select_mysql(sql2)[0],logger.info("比对结果正确"))
        delete_channel(dr,page.delete_channel,page.delete_confirm)


    def tearDown(self):
        # browser_driver.quit_browser(self)
        logger.info('test_ChannelManagement end \r\n')


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')