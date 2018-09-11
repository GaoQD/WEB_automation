# -*- coding: utf-8 -*-
# @Time    : 2018/9/4/004 17:07
# @Author  : Administor
# @File    : test_BannerManagement.py
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
from common.browser_driver import browser_driver
import page.page as page
from common.base_common import base_common
from page.LoginPage import input_password,input_username,click_submit
from page.BannerPage import banner_channel,banner_manage,h5_page,pc_page,query,app_page,reset_search,get_page_total
from interfaces.all_interface import banner

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='test_case').getlog()


class test_BannerManagement(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)
        logger.info('test_BannerManagement start')

    def test_banner_management(self):
        dr = base_common(self.driver)
        input_username(page.user_name, dr)
        input_password(page.passwd, dr)
        click_submit(dr)
        banner_manage(dr,page.banner_management)
        banner_channel(dr,page.banner_channel)
        h5_page(dr,page.h5_page)
        query(dr,page.query_button)
        base_common.js_scroll_end(self)
        banner_limit = get_page_total(dr,page.banner_limit)
        self.assertEqual(banner_limit,str(banner(page.h5_url,page.login)),logger.info("h5端对比结果：成功"))
        pc_page(dr,page.pc_page)
        query(dr,page.query_button)
        self.assertEqual(banner_limit,str(banner(page.pc_url,page.login)),logger.info("pc端对比结果：成功"))
        app_page(dr,page.app_page)
        query(dr,page.query_button)
        base_common.js_scroll_end(self)
        self.assertEqual(banner_limit,str(banner(page.app_url,page.login)),logger.info("app端对比结果：成功"))

    def tearDown(self):
        browser_driver.quit_browser(self)
        logger.info('test_BannerManagement end \r\n')


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')