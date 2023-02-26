#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：test_broker.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2022/7/5 11:14 
'''

import allure
import pytest

from auto_test_api.api.account import Broker
from auto_test_api.api.account import FmpMember
from auto_test_api.test_case.test_base import BaseTest


class TestBroker(BaseTest):

    broker = Broker()
    fmp_member = FmpMember()
    para_data = broker.read_yaml("data/account/broker_data.yaml")

    @allure.story("添加经纪人员测试")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_add_broker(self, add_broker_data):
        fmp_uid = self.get_member_fmpUid(add_broker_data.get("mobile"),add_broker_data.get("password"))
        add_broker_data.pop("password")
        add_broker_data.update(fmpUid=fmp_uid)
        res = self.broker.add_broker(add_broker_data)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("获取成员对应客户下所有主账户测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("mobile, password",para_data["accountInfo"]["data"])
    def test_get_main_merchant_list(self,mobile, password):
        fmpUid = self.get_member_fmpUid(mobile, password)
        res = self.broker.get_main_merchant_list(fmpUid)
        assert res["code"] == 0
        assert res["data"][0]["merchantId"] > 0

    @allure.story("获取展业区域测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("mobile, password",para_data["accountInfo"]["data"])
    def test_get_region_list(self, mobile, password):
        fmpUid = self.get_member_fmpUid(mobile, password)
        res = self.broker.get_region_list(fmpUid)
        assert res["code"] == 0
        assert int(res["data"][0]["value"]) > 0


    def test_broker_basic_edit(self, edit_broker_basic_data):
        sms_code, fmpSmsToken = self.get_sms_code(edit_broker_basic_data[0].get("mobile"),edit_broker_basic_data[0].get("sms_code_type"))
        edit_broker_basic_data[0].pop("sms_code_type")
        edit_broker_basic_data[0].update(sms_code=sms_code, fmpSmsToken=fmpSmsToken)
        self.fmp_member.active_member(edit_broker_basic_data[0])
        fmp_uid = self.get_member_fmpUid(edit_broker_basic_data[1].get("mobile"),edit_broker_basic_data[1].get("password"))
        edit_broker_basic_data[1].pop("password")
        edit_broker_basic_data[1].update(fmpUid=fmp_uid)

        res = self.broker.broker_basic_edit(edit_broker_basic_data[1])
        assert res["code"] == 0
        pass

