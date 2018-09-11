# -*- coding: utf-8 -*-
# @Time    : 2018/9/4/004 15:58
# @Author  : Administor
# @File    : run_All_Case.py
# @Software: PyCharm

import unittest
import time
import HTMLTestRunner
from common.sendEmail import send_email
from common.browser_driver import browser_driver


if __name__ == '__main__':
    browser_driver.clearLog("..\\Log\\test.log")
    now_time = time.strftime('%Y-%m-%d_%H_%M_%S',time.localtime(time.time()))
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('.','test*.py')
    for case in all_cases:
        suite.addTest(case)
    fp = open('..\\report\\' + now_time + '.html','wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='huanqiu admin test',
        description='Test Case Run Result',
        verbosity=2
    )
    runner.run(suite)
    send_email(now_time)
    fp.close()