#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：test_base.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/17 18:08 
'''
from time import sleep


from auto_test_api.common.conn_DB import ConnDB
from auto_test_api.common.get_log import log

db = ConnDB()
qx_comm = QxCommon()
para_data = qx_comm.read_yaml("data/qx_common_data.yaml")
ht_data = qx_comm.read_yaml("data/qx_common_data.yaml")["hLogin"]


class BaseTest():



    def get_sms_code(self, mobile, sms_code_type):
        """
        会员体系获取验证码
        :param mobile:
        :param sms_code_type:
        :return:
        """
        res = qx_comm.get_fmp_smsCode(mobile, sms_code_type)
        if res.json()["data"] != None:
            log.info(f"等待5s,等待验证码入库")
            sleep(5)
            sql_result = db.sms_select()
        sms_code = qx_comm.extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
        sms_token = res.json()["data"]
        log.info(f"获取到的短信数据为{sms_code, sms_token}")
        return sms_code,sms_token



    def get_member_fmpUid(self, mobile, password):
        return qx_comm.get_member_fmpUid(mobile, password)


    def get_partner_fmpUid(self, member_fmpUid, partner_id):
        return qx_comm.get_partner_fmpUid(member_fmpUid, partner_id)


def teardown_module():
    db.sms_conn.close()

