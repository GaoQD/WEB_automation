# -*- coding: utf-8 -*-
# @Time    : 2018/9/5/005 10:20
# @Author  : Administor
# @File    : base_common.py
# @Software: PyCharm
from selenium.common.exceptions import *
import time
from Log.logger import Logger
import os


logger = Logger(logger='base_common').getlog()

class base_common(object):

    def __init__(self,driver):
        self.driver = driver


    def get_page_title(self):
        logger.info("当前页面的title为: %s" % self.driver.title)
        return self.driver.title


    def find_element(self,loc):
        by = loc[0]
        value = loc[1]
        element = None
        if by == 'id' or by =='name' or by =='class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    logger.error("没有找到元素")
                logger.info('元素定位成功。定位方式：%s，使用的值%s：' % (by,value))
                return element
            except NoSuchElementException:
                logger.error("报错信息：",exc_info = 1)
                self.get_screenshots()
        else:
            logger.error('输入的元素定位方式错误')

    def send_key(self,loc,text):
        logger.info('清空文本框内容: %s...' % loc[1])
        self.find_element(loc).clear()
        time.sleep(1)
        logger.info('输入内容方式 by %s: %s...' % (loc[0], loc[1]))
        logger.info('输入内容: %s' % text)
        try:
            self.find_element(loc).send_keys(text)
            time.sleep(2)
        except Exception as e:
            logger.info('输入内容失败: %s' % e)
            self.get_screenshots()

    def click(self,loc):
        logger.info('点击元素 by %s: %s...' % (loc[0], loc[1]))
        try:
            self.find_element(loc).click()
            time.sleep(2)
        except AttributeError as e:
            logger.error('无法点击元素：%s' % e)
            raise

    def back(self):
        self.driver.back()
        logger.info('返回上一个页面')

    def forward(self):
        self.driver.forward()
        logger.info('前进到下一个页面')


    def wait(self,seconds):
        self.driver.implicitly_wait(seconds)
        logger.info("等待 %d 秒" % seconds)

    def clear(self,loc):
        element = self.find_element(*loc)
        try:
            element.clear()
            logger.info('清空文本框内容')
        except NameError as ne:
            logger.error('清空文本框内容失败：%s' % ne)
            self.get_screenshots()


    def get_screenshots(self):
        path = os.path.dirname(os.path.abspath('.')) + '.\\screentshots\\'
        now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        screen_name = path + now_time + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("页面已截图，截图的路径在项目: /screenshots路径下")
        except NameError as ne:
            logger.error("失败截图 %s" % ne)


    def js_scroll_end(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        logger.info("滑动到页面底部")

    def get_title(self):
        return self.driver.title

    def get_text(self,loc):
        element = self.find_element(loc)
        return element.text

    def highlight(self,element):
        self.driver.execute_script('arguments[0].setAttribute("style",arguments[1]);',element,'background:white;border:2px solid red;')
        logger.info("高亮显示：%s" % element)