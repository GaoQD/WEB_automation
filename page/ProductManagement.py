# -*- coding: utf-8 -*-
# @Time    : 2018/9/7/007 14:43
# @Author  : Administor
# @File    : ProductManagement.py
# @Software: PyCharm
from config.DBConfig import *
import page.page as page

def product_management(dr,product_management):
    dr.find_element(product_management)
    dr.click(product_management)
    dr.wait(3)

def rich_product(dr,rich_product):
    dr.find_element(rich_product)
    dr.click(rich_product)
    dr.wait(3)

def enter_product_name(dr,enter_product_name):
    dr.find_element(enter_product_name)
    dr.click(enter_product_name)
    dr.send_key(enter_product_name,page.enter_name)
    dr.wait(3)

def query(dr,query_button):
    dr.find_element(query_button)
    dr.click(query_button)
    dr.wait(3)

def reset(dr,reset_search):
    dr.find_element(reset_search)
    dr.click(reset_search)
    dr.wait(3)

def get_page_text(dr,select_result):
    content = dr.get_text(select_result)
    return content

def select_mysql(sql):
    cursors = getMysqlConnect('192.168.1.11',3306,'test','test@2018','financial_huanqiu')
    cursors.execute(sql)
    results = cursors.fetchall()
    productList = []
    for i in results:
        productList.append(i[0])
    return productList

def product_status(dr,product_status):
    dr.find_element(product_status)
    dr.click(product_status)
    dr.wait(3)

def product_shelf(dr,shelf_button):
    dr.find_element(shelf_button)
    dr.click(shelf_button)
    dr.wait(3)

def add_rich_product(dr,add_rich_product_button):
    dr.find_element(add_rich_product_button)
    dr.click(add_rich_product_button)
    dr.wait(3)
    add_product_id(dr,page.product_id,page.id_name)
    add_product_name(dr,page.product_name,page.pro_name)
    choose_risk_level(dr,page.risk_level,page.low_risk_level)
    add_priority(dr,page.priority)
    add_placement(dr,page.placement,page.home_selection)
    add_floating_rate(dr,page.floating_rate,page.floating_rate_value)
    add_rate(dr,page.rate,page.rate_value)
    add_release_time(dr,page.release_time,page.cur_time,page.confirm)

def add_product_id(dr,product_id,id_name):
    dr.find_element(product_id)
    dr.send_key(product_id,id_name)
    dr.wait(3)

def add_product_name(dr,product_name,pro_name):
    dr.find_element(product_name)
    dr.send_key(product_name,pro_name)
    dr.wait(3)

def choose_risk_level(dr,risk_level,levels):
    dr.find_element(risk_level)
    dr.click(risk_level)
    dr.wait(3)
    dr.find_element(levels)
    dr.click(levels)
    dr.wait(3)

def add_priority(dr,priority):
    dr.find_element(priority)
    dr.send_key(priority,text=page.priority_value)
    dr.wait(3)

def add_placement(dr,placement,position):
    dr.find_element(placement)
    dr.click(placement)
    dr.wait(3)
    dr.find_element(position)
    dr.click(position)
    dr.wait(3)

def add_floating_rate(dr,floating_rate,text):
    dr.find_element(floating_rate)
    dr.send_key(floating_rate,text)
    dr.wait(3)

def add_rate(dr,rate,text):
    dr.find_element(rate)
    dr.send_key(rate,text)
    dr.wait(3)

def add_release_time(dr,release_time,cur_time,confirm):
    dr.find_element(release_time)
    dr.click(release_time)
    dr.find_element(cur_time)
    dr.click(confirm)
    dr.wait(3)