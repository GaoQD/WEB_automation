# -*- coding: utf-8 -*-
# @Time    : 2018/9/6/006 16:48
# @Author  : Administor
# @File    : LoginPage.py
# @Software: PyCharm
from page import page

def input_username(username,dr):
    dr.find_element(page.loc)
    dr.highlight(dr.find_element(page.loc))
    dr.send_key(page.loc,username)
    dr.wait(3)

def input_password(password,dr):
    dr.find_element(page.loc1)
    dr.highlight(dr.find_element(page.loc1))
    dr.send_key(page.loc1,password)
    dr.wait(3)

def click_submit(dr):
    dr.find_element(page.login_button)
    dr.click(page.login_button)
    dr.wait(10)
