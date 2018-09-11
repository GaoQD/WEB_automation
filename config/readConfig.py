# -*- coding: utf-8 -*-
# @Time    : 2018/9/4/004 15:16
# @Author  : Administor
# @File    : readConfig.py
# @Software: PyCharm
import os
import configparser


proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir,"cfg.ini")

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='utf-8')

    def get_sections(self):
        if self.cf:
            return self.cf.sections()

    def get_sections_items(self,section):
        if self.cf:
            return self.cf.items(section)

    def get_string(self,section,option):
        if self.cf:
            return self.cf.get(section,option)

    def get_int(self,section,option):
        if self.cf:
            return self.cf.get(section,option)

    def get_float(self,section,option):
        if self.cf:
            return self.cf.get(section,option)

    def get_boolean(self,section,option):
        if self.cf:
            return self.cf.get(section,option)

if __name__ == '__main__':
    print(ReadConfig().get_string('email','testuser'))