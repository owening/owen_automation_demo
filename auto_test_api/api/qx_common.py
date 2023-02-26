#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：qx_common.py
@IDE  ：PyCharm
@Author ：Owen
@Date ：2021/12/6 20:37
'''
import os
import sys

sys.path.append(os.path.realpath(__file__))

import requests
from auto_test_api.api.base_api import BaseApi
from auto_test_api.common.conn_DB import ConnDB
from auto_test_api.common.get_log import log


class QxCommon(BaseApi):
    db = ConnDB()
    # 获取成员登录态fmpUid
    def get_member_fmpUid(self, mobile, password):
        req_data = {
            "mobile": mobile,
            "password": password
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "memberLogin")
        if res.status_code == 200 and res.json()["success"] is True:
            cookie = res.cookies.get_dict()
            fmp_uid = cookie['fmpUid']
        log.info(f"获取的到cookie为{cookie}")
        log.info(f"获取的到fmpUid为{fmp_uid}")
        return fmp_uid

    # 渠道登录
    def get_partner_fmpUid(self, member_fmpUid, partner_id):
        '''
            :param member_fmpUid:成员登录后获取的fmpuid
            :param partner_id: 要登录的渠道id
        '''
        req_data = {
            "partner_id": str(partner_id),
            "member_fmpUid": str(member_fmpUid),
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "partnerLogin")
        if res.status_code == 200 and res.json()["success"] is True:
            partner_fmp_uid = res.cookies.get_dict()['fmpUid']
        return partner_fmp_uid

    def get_fmp_smsCode(self, mobile, smsCodeType):
        '''
        新会员体系账户获取验证码
        :param mobile:
        :param sms_code_type:
        :return:
        '''
        req_data = {
            "mobile": mobile,
            "sms_code_type": smsCodeType
        }
        res = self.send_api_data("data/qx_common_api.yaml", req_data, "fmpSms")
        return res


    def get_huntian_token(self, username, password):
        req_data = {'data': {'jcaptcha': 1, 'password': password, 'redirectUrl': None, 'username': username},
                    'headers': {'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8', 'User-Agent': 'Mozilla/5.0'},
                    'method': 'post', 'url': 'https://xxxx.xxx.com/login'}
        session = requests.session()

        res = session.request(**req_data)
        if res.status_code == 200:
            huntian_token = requests.utils.dict_from_cookiejar(session.cookies).get("token")
        log.info(f"获取token为：{h_token}")
        return h_token

    def venus_review_back(self, commission_withdraw_id,huntian_token):
        """
        审核-打回
        :return:
        """
        req_data = {
            "commissionWithdrawId": commission_withdraw_id,
            "token": huntian_token
        }
        res = self.send_api_data("data/qx_common_api.yaml", req_data, "venusReviewBack")
        return res



if __name__=="__main__":
    pass