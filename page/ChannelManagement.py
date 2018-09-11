# -*- coding: utf-8 -*-
# @Time    : 2018/9/10/010 18:00
# @Author  : Administor
# @File    : ChannelManagement.py
# @Software: PyCharm

import page.page as page
import re
from config.DBConfig import *
def click_channel_management(dr,market_promotion,channel_management):
    dr.find_element(market_promotion)
    dr.click(market_promotion)
    dr.wait(3)
    dr.find_element(channel_management)
    dr.click(channel_management)
    dr.wait(3)

#跟据渠道名称查询
def channel_name_query(dr,channel_name,text,query,reset_search):
    dr.find_element(channel_name)
    dr.send_key(channel_name,text)
    dr.wait(3)
    dr.find_element(query)
    dr.click(query)
    dr.wait(3)
    dr.find_element(reset_search)
    dr.click(reset_search)
    dr.wait(3)

def get_page_text(dr,select_result):
    content = dr.get_text(select_result)
    total = re.findall('\d+',content)[0]
    return total

def select_mysql(sql):
    cursors = getMysqlConnect('192.168.1.11',3306,'test','test@2018','financial_huanqiu')
    cursors.execute(sql)
    results = cursors.fetchall()
    productList = []
    for i in results:
        productList.append(i[0])
    return productList

#跟据渠道参数进行查询
def channel_parameter_query(dr,reset_search,channel_parameter,text,query):
    #重置搜索
    dr.find_element(reset_search)
    dr.click(reset_search)
    dr.wait(3)
    #输入渠道参数进行查询
    dr.find_element(channel_parameter)
    dr.send_key(channel_parameter,text)
    dr.wait(3)
    dr.find_element(query)
    dr.click(query)
    dr.wait(3)

def get_text(dr,channel_parameter_value):
    content = dr.get_text(channel_parameter_value)
    return content
#新增渠道
def add_channel(dr,add_channel,add_channel_name,add_channel_param,next_step,
                add_channel_commit,add_commit_next,pane_succ_commit,pane_fail_commit,pane_old_commit):
    dr.find_element(add_channel)
    dr.click(add_channel)
    dr.wait(3)
    dr.find_element(add_channel_name)
    dr.send_key(add_channel_name,page.add_channel_value)
    dr.wait(3)
    dr.find_element(add_channel_param)
    dr.send_key(add_channel_param,page.add_param_value)
    dr.wait(3)
    dr.find_element(next_step)
    dr.click(next_step)
    dr.wait(3)
    dr.find_element(add_channel_commit)
    dr.click(add_channel_commit)
    dr.wait(3)
    dr.find_element(add_commit_next)
    dr.click(add_commit_next)
    dr.wait(3)
    dr.find_element(pane_succ_commit)
    dr.click(pane_succ_commit)
    dr.wait(3)
    dr.find_element(add_commit_next)
    dr.click(add_commit_next)
    dr.wait(3)
    dr.find_element(pane_fail_commit)
    dr.click(pane_fail_commit)
    dr.wait(3)
    dr.find_element(add_commit_next)
    dr.click(add_commit_next)
    dr.wait(3)
    dr.find_element(pane_old_commit)
    dr.click(pane_old_commit)
    dr.wait(3)
    dr.find_element(add_commit_next)
    dr.click(add_commit_next)
    dr.wait(3)


def delete_channel(dr,delete_channel,delete_confirm):
    dr.find_element(delete_channel)
    dr.click(delete_channel)
    dr.wait(3)
    dr.find_element(delete_confirm)
    dr.click(delete_confirm)
    dr.wait(3)