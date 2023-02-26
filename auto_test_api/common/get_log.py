#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：get_log.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/7 18:49 
'''
import datetime
import logging
import os


from auto_test_api.common.config import cf


class Log():
    formatter = logging.Formatter("%(asctime)s|%(levelname)-6s|%(filename)s-%(funcName)s:%(lineno)-3s|%(message)s", "%Y-%m-%d-%H:%M")
    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def __init__(self, name="logs"):
        """
             初始化生成器
             :param name: 生成器的名称
        """
        self.log_name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

    #初始化流处理器
    def set_stream(self):
        consle_handle = logging.StreamHandler()
        consle_handle.setLevel(logging.DEBUG)
        consle_handle.setFormatter(self.formatter)
        self.logger.addHandler(consle_handle)

    #初始化文件处理器
    def set_file(self):
        a = self.log_name + "_" + str(datetime.date.today()) + ".log"
        b= os.path.join(self.BASE_PATH,"logs",a)
        file_mode = cf.get_key("logs", "file_mode")
        file_handle = logging.FileHandler(filename=b,mode=file_mode)
        file_handle.setLevel(logging.INFO)
        file_handle.setFormatter(self.formatter)
        self.logger.addHandler(file_handle)

    #获取运行日志
    def get_log(self):
        self.set_stream()
        self.set_file()
        return self.logger

log = Log().get_log()

