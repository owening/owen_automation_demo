#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：config.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/7 11:36 
'''
import configparser
import os


class ConfigIni():

   BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
   config_file_path = os.path.join(BASE_PATH, "config.ini")

   def __init__(self, file_path=config_file_path):

       self.config_file_path = file_path
       self.cf = configparser.ConfigParser()
       self.cf.read(file_path)

   def get_key(self,section, option):
        value = self.cf.get(section,option)
        return value

   def set_value(self, section, option, value):
       self.cf.set(section, option, value)

       with open(self.config_file_path, "w+") as f:
           self.cf.write(f)



cf = ConfigIni()

