#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：broker.py
@IDE  ：PyCharm
@Author ：Owen
@Date ：2022/7/4 10:30 
'''
import os
import sys

sys.path.append(os.path.realpath(__file__))

from auto_test_api.api.base_api import BaseApi





class Broker(BaseApi):

    def add_broker(self, req_data):
        """
        添加经纪人员
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/broker_api.yaml", req_data, "addBroker")
        return res.json()

    def get_main_merchant_list(self, fmpUid):
        """
        获取成员对应客户下主账户
        :param fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": fmpUid
        }
        res = self.send_api_data("data/account/broker_api.yaml", req_data, "getMainMerchantList")
        return res.json()

    def get_region_list(self, fmpUid):
        """
        获取展业区域
        :param fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": fmpUid
        }
        res = self.send_api_data("data/account/broker_api.yaml", req_data, "getRegionList")
        return res.json()

    def broker_basic_edit(self, req_data):
        """
        经纪人员个人信息编辑
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/broker_api.yaml", req_data, "brokerBasicEdit")
        return res.json()