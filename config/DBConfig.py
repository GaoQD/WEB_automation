# -*- coding: utf-8 -*-
# @Time    : 2018/9/10/010 10:01
# @Author  : Administor
# @File    : DBConfig.py
# @Software: PyCharm

import pymysql
'''
    数据库连接
    关闭数据库
'''
def getMysqlConnect(host,port,user,passwd,db):
    connect = pymysql.Connect(host=host,port=port,user=user,passwd=passwd,db=db,charset='utf8')
    cursors = connect.cursor()
    return cursors

def closeMysqlConnect(host,port,user,passwd,db):
    connect = getMysqlConnect(host,port,user,passwd,db,charset='utf-8')
    connect.close()

# if __name__ == '__main__':
#     cursors = getMysqlConnect('192.168.1.11',3306,'test','test@2018','financial_huanqiu')
#     sql = "SELECT product_name FROM main_product WHERE `status`='SALES'"
#     cursors.execute(sql)
#     data = cursors.fetchall()
#     productList = []
#     for i in data:
#         productList.append(i[0])
#     print(productList)
#     print("玖富履保120天-禁止删改" in productList)