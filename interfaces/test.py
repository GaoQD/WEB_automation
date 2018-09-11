# -*- coding: utf-8 -*-
# @Time    : 2018/9/7/007 15:41
# @Author  : Administor
# @File    : test.py
# @Software: PyCharm
from Log.logger import Logger
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import warnings
import requests
import ssl
import json
import page.page as page


requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
ssl._create_default_https_context = ssl._create_unverified_context()
warnings.simplefilter('ignore', ResourceWarning)

logger = Logger(logger='interfaces').getlog()


def login(login_url):
    r = requests.session().post(login_url,json={"mobile": "18399917685", "password": "zh0514"})
    status_code = r.status_code
    if status_code == 200 :
        json_dict = json.loads(r.text)
        if type(json_dict).__name__ == 'dict':
            session = json_dict['data']['token']
            return session,r.cookies
        else:
            logger.error("登录失败：%s" % status_code)
    else:
        logger.error("登录失败：%s" % status_code)

def product_name(login_url,url):
    r = requests.session().get(url,cookies = login(login_url)[1])
    status_code = r.status_code
    if status_code == 200 :
        json_dict = json.loads(r.text)
        if type(json_dict).__name__ == 'dict':
            for i in json_dict['data']['list']:
                return i['product_name']
        else:
            logger.error("接口返回：%s" % status_code)
    else:
        logger.error("接口返回：%s" % status_code)

def product_status(login_url,url):
    r = requests.session().get(url,cookies = login(login_url))
    status_code = r.status_code
    if status_code == 200 :
        json_dict = json.loads(r.text)
        if type(json_dict).__name__ == 'dict':
            print(json_dict)
        else:
            logger.error("接口返回：%s" % status_code)
    else:
        logger.error("接口返回：%s" % status_code)


if __name__ == '__main__':
    login_url = 'http://huanqiu-v2.test.congred.com/api/financial/manager/login'
    url1 = 'http://huanqiu-v2.test.congred.com/api/financial/manager/product_cunguan?sort=create_at&pagesize=10&page=0&status=SALES'
    url = 'http://huanqiu-v2.test.congred.com/api/financial/manager/product_cunguan?sort=create_at&pagesize=10&page=0&product_name=三只松鼠'
    print(product_status(login_url,url1))