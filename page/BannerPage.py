# -*- coding: utf-8 -*-
# @Time    : 2018/9/7/007 9:04
# @Author  : Administor
# @File    : BannerPage.py
# @Software: PyCharm

import page.page as page
import re

def banner_manage(dr,banner_manage):
    dr.find_element(banner_manage)
    dr.click(banner_manage)
    # dr.highlight(page.banner_management)
    dr.wait(3)

def banner_channel(dr,banner_channel):
    dr.find_element(banner_channel)
    dr.click(banner_channel)
    # dr.highlight(page.banner_channel)
    dr.wait(3)

def h5_page(dr,h5_page):
    dr.find_element(h5_page)
    dr.click(h5_page)
    # dr.highlight(page.h5_page)
    dr.wait(3)

def query(dr,query_button):
    dr.find_element(query_button)
    dr.click(query_button)
    dr.wait(3)

def pc_page(dr,pc_page):
    banner_channel(dr,banner_channel)
    dr.find_element(pc_page)
    dr.click(pc_page)
    dr.wait(3)

def app_page(dr,app_page):
    banner_channel(dr,banner_channel)
    dr.find_element(app_page)
    dr.click(app_page)
    # dr.highlight(page.app_page)
    dr.wait(3)

def reset_search(dr,reset_search):
    dr.find_element(reset_search)
    dr.click(reset_search)
    dr.wait(3)

def get_page_total(dr,banner_limit):
    content = dr.get_text(banner_limit)
    total = re.findall('\d+',content)[0]
    return total