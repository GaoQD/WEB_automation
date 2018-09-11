# -*- coding: utf-8 -*-
# @Time    : 2018/9/6/006 10:40
# @Author  : Administor
# @File    : test_ProductManagement.py
# @Software: PyCharm
import unittest
from Log.logger import Logger
from common.browser_driver import browser_driver
from config.readConfig import ReadConfig
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import requests
import ssl
import re
import page.page as page
from common.base_common import base_common
from page.ProductManagement import *
from page.LoginPage import input_username,input_password,click_submit
from config.DBConfig import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='test_case').getlog()


class test_ProductManagement(unittest.TestCase):
    @classmethod
    def setUp(self):
        browser = browser_driver(self)
        self.driver = browser.openbrowser(self)
        logger.info('test_ProductManagement start')

    def test_product_management(self):
        dr = base_common(self.driver)
        input_username(page.user_name, dr)
        input_password(page.passwd, dr)
        click_submit(dr)
        product_management(dr,page.product_management)
        rich_product(dr,page.rich_product)
        #输入产品名称进行查询
        enter_product_name(dr,page.enter_product_name)
        query(dr,page.query_button)
        self.assertIn(get_page_text(dr,page.select_result),page.enter_name,logger.info("对比结果：成功"))
        #重置搜索
        reset(dr,page.reset_search)
        #跟据状态进行查询
        product_status(dr,page.product_status)
        product_shelf(dr,page.shelf_button)
        query(dr,page.query_button)
        #通过查询数据库，不同状态的产品名称存入list，获取当前页面返回的产品名称，进行对比
        sql = "SELECT product_name FROM main_product WHERE `status`='SALES'"
        self.assertIn(get_page_text(dr,page.select_result),select_mysql(sql),logger.info("比对结果正确"))
        reset(dr,page.reset_search)
        product_status(dr,page.product_status)
        product_shelf(dr,page.lower_frame)
        query(dr,page.query_button)
        sql1 = "SELECT product_name FROM main_product WHERE `status`='OFF_LINE'"
        self.assertIn(get_page_text(dr,page.select_result),select_mysql(sql1),logger.info("比对结果正确"))
        #添加玖富产品
        # add_rich_product(dr,page.add_rich_product_button)




    def tearDown(self):
        browser_driver.quit_browser(self)
        logger.info('test_ProductManagement end \r\n')


if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')