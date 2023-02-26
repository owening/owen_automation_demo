#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：fmp_member.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/5 19:08 
'''
import os
import sys

sys.path.append(os.path.realpath(__file__))

from auto_test_api.api.base_api import BaseApi
from auto_test_api.common.get_log import log


class FmpMember(BaseApi):

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
        else:
            raise res.json()

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
        else:
            raise Exception(res.json())

    # 新体系账户登录
    def fmp_login(self, mobile, password):
        req_data = {
            "mobile": mobile,
            "password": password
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "memberLogin")
        return res.json()

    def fmp_logout(self, fmpUid):
        """
        退出登录
        :param fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": fmpUid
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "memberLogout")
        return res.json()

    # 获取登录账户信息
    def get_account_info(self, fmpUid):
        """
        获取登录账户信息
        :param fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": fmpUid
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "accountInfo")
        return res.json()

    def register_member(self, custName, contact, mobile, sms_code, fmpSmsToken):
        """
        申请会员/注册
        :param custName:
        :param contact:
        :param mobile:
        :param sms_code:
        :param fmpSmsToken:
        :return:
        """
        req_data = {
            "custName": custName,
            "contact": contact,
            "mobile": mobile,
            "sms_code": sms_code,
            "fmpSmsToken": fmpSmsToken
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "memberRegister")
        return res.json()

    def create_account(self, req_data, huntian_token):
        """
        创建客户/创建合作
        :param req_data:
        :param huntian_token:
        :return:
        """
        req_data.update(token=huntian_token)
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "createAccount")
        return res.json()

    def create_business_line(self, req_data, huntian_token):
        """
        新增业务线
        :param req_data:
        :param huntian_token:
        :return:
        """
        req_data.update(token=huntian_token)
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "createBusinessLine")
        return res.json()

    def active_member(self, req_data):
        """
        激活成员
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "activeMember")
        return res.json()

    def subject_temp_save(self, req_data):
        """
        主体信息暂存
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "subjectTempSave")
        return res.json()

    def submit_subject_auth(self, req_data):
        """
        提交主体认证
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "submitSubjectAuth")
        return res.json()

    def subject_audit(self, req_data):
        """
        主体认证审核
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "subjectAudit")
        return res.json()

    def add_member(self, req_data):
        """
        添加成员
        :param req_data:
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "addMember")
        return res.json()

    def edit_member(self, req_data):
        """
        修改成员信息
        :return:
        """
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "editMember")
        return res.json()

    def query_member_list(self, fmp_uid, page_index, page_size):
        """
        成员列表查询
        :param fmp_uid:
        :param page_index:
        :param page_size:
        :return:
        """
        req_data = {
            "fmpUid": fmp_uid,
            "pageIndex": page_index,
            "pageSize": page_size
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "queryMemberList")
        return res.json()

    def query_member_permission_data(self, member_fmpUid):
        """
        查询成员数据权限
        :param member_fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": member_fmpUid
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml",req_data, "queryMemberPermissionData")
        return res.json()

    def query_member_permission_all(self, member_fmpUid):
        """
        获取成员所有权限
        :param member_fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": member_fmpUid
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml",req_data, "queryMemberPermissionAll")
        return res.json()

    def query_partner_permission(self, partner_fmpUid,partner_Id):
        """
        获取渠道权限
        :param partner_fmpUid:
        :return:
        """
        req_data = {
            "fmpUid": partner_fmpUid,
            "partner_id": partner_Id
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "queryPartnerPermission")
        return res.json()

    def get_member_info(self, member_fmpUid):
        """
        获取成员详情
        :param member_fmpUid:
        :return:
        """
        req_data = {
            "member_FmpUid": member_fmpUid
        }
        res = self.send_api_data("data/account/fmp_member_api.yaml", req_data, "memberInfo")
        return res.json()


    def query_member_index(self, fmpUid):
        """
        会员首页详情
        :param fmpUid:
        :return:
        """
        pass
