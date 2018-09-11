# -*- coding: utf-8 -*-
# @Time    : 2018/9/5/005 10:54
# @Author  : Administor
# @File    : browser_driver.py
# @Software: PyCharm

import os
from Log.logger import Logger
from selenium import webdriver
from config.readConfig import ReadConfig

logger = Logger(logger='browser_driver').getlog()

class browser_driver(object):
    path = os.path.dirname(os.path.abspath('.'))
    firefox_driver_path = path + '\\driver\\geckodriver.exe'
    chrome_driver_path = path + '\\driver\\chromedriver.exe'
    ie_driver_path = path + '\\driver\\IEDriverServer.exe'

    def __init__(self,driver):
        self.driver = driver


    def openbrowser(self,driver):
        browser = ReadConfig().get_string('browser_type','browserName')
        logger.info("选择的浏览器为: %s 浏览器" % browser)


        if browser == 'Firefox':
            driver = webdriver.Firefox()
            logger.info("启动火狐浏览器")
        elif browser == 'Chrome':
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("启动谷歌浏览器")
        elif browser == 'IE':
            driver = webdriver.Ie(self.ie_driver_path)
            logger.info("启动IE浏览器")

        url = ReadConfig().get_string('url','login_url')
        driver.get(url)
        logger.info("打开URL： %s" % url)
        driver.maximize_window()
        logger.info("全屏当前窗口")
        driver.implicitly_wait(5)
        logger.info("设置5秒隐式等待时间")
        return driver

    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()

    def clearLog(file_name):
        with open(file_name, 'r+') as f:
            f.seek(0)
            f.truncate()

if __name__ == '__main__':
    browser_driver.clearLog('..\\Log\\test.log')