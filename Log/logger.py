# -*- coding: utf-8 -*-
# @Time    : 2018/9/4/004 14:24
# @Author  : Administor
# @File    : logger.py
# @Software: PyCharm

import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        log_path = os.path.dirname(os.path.abspath('.')) + '\\Log\\'
        log_name = log_path + 'test.log'

        filehandle = logging.FileHandler(log_name,encoding="utf-8")
        filehandle.setLevel(logging.INFO)

        controlhandle = logging.StreamHandler()
        controlhandle.setLevel(logging.INFO)

        formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
        filehandle.setFormatter(formatter)
        controlhandle.setFormatter(formatter)

        self.logger.addHandler(filehandle)
        self.logger.addHandler(controlhandle)

    def getlog(self):
        return self.logger

if __name__ == '__main__':
    Logger(logger='Log').getlog().info('ssssssssssss')