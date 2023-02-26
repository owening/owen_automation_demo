#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：test_fmp_member.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/14 15:15 
'''
import pytest
import allure

from auto_test_api.api.account import FmpMember
from auto_test_api.test_case.test_base import BaseTest


@allure.feature("齐欣会员体系接口测试")
class TestFmpMember(BaseTest):
    fmp_member = FmpMember()
    para_data = fmp_member.read_yaml("data/account/fmp_member_data.yaml")

    @allure.story("登录测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize("mobile,password,expected", para_data["login"]["data"])
    def test_login(self, mobile, password, expected):
        res = self.fmp_member.fmp_login(mobile, password)
        assert res["success"] == True
        assert expected == res["data"]["true"]

    @allure.story("获取登录账户信息测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("getfmpUid", para_data["accountInfo"]["data"], indirect=True)
    def test_account_info(self, getfmpUid):
        res = self.fmp_member.get_account_info(getfmpUid)
        assert res["data"]["memberInfo"]["memberSessionVO"]["email"] == "testxxxx@xxxx.com"
        assert res["success"] == True

    @allure.story("注册会员测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=3)
    def test_register_member(self, register_data):
        sms_code, fmpSmsToken = self.get_sms_code(register_data.get("mobile"), register_data.get("sms_code_type"))
        res = self.fmp_member.register_member(register_data.get("custName"), register_data.get("contact"),
                                              register_data.get("mobile"), sms_code, fmpSmsToken)
        assert res["code"] == 0

    @allure.story("创建客户/合作测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize("create_account_data", para_data["createAccount"]["data"], indirect=True)
    def test_create_account(self, create_account_data):
        res = self.fmp_member.create_account(create_account_data, self.huntian_token)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("新增业务线测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=5)
    @pytest.mark.parametrize("add_business_line", para_data["createBusinessLine"]["data"], indirect=True)
    def test_add_business_line(self, add_business_line):
        res = self.fmp_member.create_business_line(add_business_line, self.huntian_token)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("成员激活测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=6)
    def test_active_member(self, active_member_data):
        sms_code, fmpSmsToken = self.get_sms_code(active_member_data.get("mobile"),active_member_data.get("sms_code_type"))
        active_member_data.pop("sms_code_type")
        active_member_data.update(sms_code=sms_code, fmpSmsToken=fmpSmsToken)
        res = self.fmp_member.active_member(active_member_data)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("主体暂存接口测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=7)
    def test_subject_temp_save(self, subject_temp):
        fmp_uid = self.get_member_fmpUid(subject_temp.get("mobile"), subject_temp.get("password"))
        subject_temp.pop("mobile"), subject_temp.pop("password"), subject_temp.update(fmpUid=fmp_uid)
        res = self.fmp_member.subject_temp_save(subject_temp)
        assert res["data"]["subjectInfo"] == True
        assert res["data"]["subjectFinanceInfo"] == True

    @allure.story("提测主体认证测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=8)
    def test_submit_subject_auth(self, submit_subject):
        fmp_uid = self.get_member_fmpUid(submit_subject.get("mobile"), submit_subject.get("password"))
        submit_subject.pop("mobile"), submit_subject.pop("password"), submit_subject.update(fmpUid=fmp_uid)
        res = self.fmp_member.submit_subject_auth(submit_subject)
        assert res["success"] == True

    @allure.story("主体认证审核测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=9)
    def test_subject_audit(self, subject_audit):
        subject_audit.update(token=self.huntian_token)
        res = self.fmp_member.subject_audit(subject_audit)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("添加成员测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=10)
    def test_add_member(self, add_member_data):
        fmp_uid = self.get_member_fmpUid(add_member_data.get("mobile"), add_member_data.get("password"))
        add_member_data.pop("password"), add_member_data.update(fmpUid=fmp_uid)
        res = self.fmp_member.add_member(add_member_data)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("修改成员信息测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=11)
    def test_edit_member(self, edit_member_data):
        fmp_uid = self.get_member_fmpUid(edit_member_data.get("mobile"), edit_member_data.get("password"))
        edit_member_data.pop("password"), edit_member_data.update(fmpUid=fmp_uid)
        res = self.fmp_member.edit_member(edit_member_data)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("查询成员列表测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=12)
    @pytest.mark.parametrize("mobile,password,page_index,page_size", para_data["queryMemberList"]["data"])
    def test_query_member_list(self, mobile, password, page_index, page_size):
        fmp_uid = self.get_member_fmpUid(mobile, password)
        res = self.fmp_member.query_member_list(fmp_uid, page_index, page_size)
        assert res["code"] == 0
        assert res["success"] == True
        assert res["data"]["total"] > 0

    @allure.story("获取成员数据权限测试")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=13)
    @pytest.mark.parametrize("mobile,password", para_data["accountInfo"]["data"])
    def test_query_member_permission_data(self, mobile, password):
        fmp_uid = self.get_member_fmpUid(mobile, password)
        res = self.fmp_member.query_member_permission_data(fmp_uid)
        assert res["code"] == 0
        assert "income_data" in res["data"]["permissionKeyList"]

    @allure.story("获取成员所有权限")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=14)
    @pytest.mark.parametrize("mobile, password", para_data["accountInfo"]["data"])
    def test_query_member_permission_all(self, mobile, password):
        fmp_uid = self.get_member_fmpUid(mobile, password)
        res = self.fmp_member.query_member_permission_all(fmp_uid)
        assert res["code"] == 0
        assert res["success"] == True
        assert "use_new_member" in res["data"]["permissionKeyList"]

    @allure.story("获取渠道业务线权限")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=15)
    @pytest.mark.parametrize("mobile, password, partner_id", para_data["partnerInfo"]["data"])
    def test_query_partner_permission(self, mobile, password, partner_id):
        partner_fmp_uid = self.get_partner_fmpUid(self.get_member_fmpUid(mobile, password), partner_id)
        res = self.fmp_member.query_partner_permission(partner_fmp_uid, partner_id)
        assert res["code"] == 0
        assert res["success"] == True

    @allure.story("成员退出登录")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.run(order=16)
    @pytest.mark.parametrize("mobile, password", para_data["accountInfo"]["data"])
    def test_fmp_logout(self, mobile, password):
        res = self.fmp_member.fmp_logout(self.get_member_fmpUid(mobile, password))
        assert res["code"] == 0
        assert res["success"] == True


if __name__ == "__main__":
    pytest.main()
