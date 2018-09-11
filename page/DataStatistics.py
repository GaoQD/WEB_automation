# -*- coding: utf-8 -*-
# @Time    : 2018/9/11/011 14:23
# @Author  : Administor
# @File    : DataStatistics.py
# @Software: PyCharm

def click_regist_statistics(dr,data_statistics,regist_statistics,start_time,
                            start_time_value,end_time,end_time_value,channel,all_channel,regist_query):
    dr.find_element(data_statistics)
    dr.click(data_statistics)
    dr.wait(3)
    dr.find_element(regist_statistics)
    dr.click(regist_statistics)
    dr.wait(3)
    dr.find_element(start_time)
    dr.click(start_time)
    dr.wait(3)
    dr.find_element(start_time_value)
    dr.click(start_time_value)
    dr.wait(3)
    dr.find_element(end_time)
    dr.click(end_time)
    dr.wait(3)
    dr.find_element(end_time_value)
    dr.click(end_time_value)
    dr.wait(3)
    dr.find_element(channel)
    dr.click(channel)
    dr.wait(3)
    dr.find_element(all_channel)
    dr.click(all_channel)
    dr.wait(3)
    dr.find_element(regist_query)
    dr.click(regist_query)
    dr.wait(3)

def get_text(dr,obtain_succ_regist):
    content = dr.get_text(obtain_succ_regist)
    return content

def reset(dr,reset_search):
    dr.find_element(reset_search)
    dr.click(reset_search)
    dr.wait(3)