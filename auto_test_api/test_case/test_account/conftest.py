#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：qowen_automation_demo
@File ：conftest.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/15 14:10 
'''

import os
import sys



sys.path.append(os.path.realpath(__file__))

import random
import pytest
from auto_test_api.api.qx_common import QxCommon
from auto_test_api.common.conn_DB import ConnDB
from auto_test_api.common.get_log import log

qx_common = QxCommon()
db = ConnDB()



class TestData:

    def get_test_data(self):
        custName = "自动测试客户" + str(random.randint(0, 9999999)) + "号"
        contact = "自动测试联系人" + str(random.randint(0, 9999999)) + "号"
        broker = "自动测试经纪人员" + str(random.randint(0, 9999999)) + "号"
        prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153",
                   "155", "156", "157", "158", "159", "186", "187", "188"]
        mobile = random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))
        subjectName = "自动测试主体" + str(random.randint(0, 9999999)) + "号"
        email = "test" + str(random.randint(0, 9999999)) + "@test.com"
        telephone = "0755-" + str(random.randint(10000000, 99999999))
        trafficName = "自动测试平台名" + str(random.randint(0, 9999999)) + "号"

        test_data = {
            "custName": custName,
            "contact": contact,
            "mobile": mobile,
            "subjectName": subjectName,
            "email": email,
            "telephone": telephone,
            "trafficName": trafficName,
            "broker": broker
        }
        return test_data


testdata = TestData()


@pytest.fixture(scope="session")
def getfmpUid(request):
    mobile = request.param[0]
    password = request.param[1]
    fmpUid = qx_common.get_member_fmpUid(mobile, password)
    log.info(f"登录态所属账户为{mobile, password}")
    return fmpUid


@pytest.fixture(scope="session")
def register_data():
    reg_data = {
        "custName": testdata.get_test_data().get("custName"),
        "contact": testdata.get_test_data().get("contact"),
        "mobile": testdata.get_test_data().get("mobile"),
        "sms_code_type": 0
    }
    return reg_data


@pytest.fixture(scope="session")
def active_member_data():
    sql_result = db.select()
    mobile = qx_common.extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
    active_data = {
        "mobile": mobile,
        "password": 123456,
        "sms_code_type": 1
    }
    return active_data


@pytest.fixture(scope="session")
def create_account_data(request):
    sql_result = db.select()
    customerId = qx_common.extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
    account_data = {
        "memberName": testdata.get_test_data().get("contact"),
        "mobile": testdata.get_test_data().get("mobile"),
        "customerId": customerId,
        "subjectName": testdata.get_test_data().get("subjectName"),
        "trafficName": testdata.get_test_data().get("trafficName"),
        "feeTemplateId": request.param[0],
        "solutionType": request.param[1]
    }
    return account_data


@pytest.fixture(scope="session")
def add_business_line(request):
    sql_result = db.select()
    business_data = {
        "trafficName": testdata.get_test_data().get("trafficName"),
        "feeTemplateId": request.param[0],
        "solutionType": request.param[1],
        "customerId": sql_result[0][0],
        "subjectId": sql_result[0][1]
    }
    return business_data


@pytest.fixture(scope="session")
def subject_temp():
    sql_result = db.select()
    subject_temp_data = {
        "mobile": sql_result[0][0],
        "password": "123456",
        "subjectId": sql_result[0][1],
        "bankAccountName": testdata.get_test_data().get("subjectName"),
        "companyName": testdata.get_test_data().get("subjectName"),
        "email": testdata.get_test_data().get("email"),
        "telephone": testdata.get_test_data().get("telephone")

    }
    return subject_temp_data


@pytest.fixture(scope="session")
def submit_subject():
    sql_result = db.select()
    submit_subject_data = {
        "mobile": sql_result[0][2],
        "password": "123456",
        "customerId": sql_result[0][0],
        "customerName": testdata.get_test_data().get("custName"),
        "memberId": sql_result[0][1],
        "subjectId": sql_result[0][3],
        "bankAccountName": testdata.get_test_data().get("subjectName"),
        "companyName": testdata.get_test_data().get("subjectName"),
        "email": testdata.get_test_data().get("email"),
        "telephone": testdata.get_test_data().get("telephone")
    }
    return submit_subject_data


@pytest.fixture(scope="session")
def subject_audit():
    sql_result = db.select()
    subjectHistory_id = qx_common.extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
    subject_audit_data = {
        "subjectHistoryId": subjectHistory_id,
        "authState": 2  # 已认证
    }
    return subject_audit_data


@pytest.fixture(scope="session")
def add_member_data():
    sql_result = db.select()   add_member_data = {
        "mobile": sql_result[0][0],
        "password": "123456",
        "contact": testdata.get_test_data().get("contact"),
        "subjectId": sql_result[0][2],
        "lineId": sql_result[0][1],
        "email": testdata.get_test_data().get("email"),
        "newmobile": testdata.get_test_data().get("mobile")
    }
    return add_member_data


@pytest.fixture(scope="session")
def edit_member_data():
    sql_result = db.select()
    edit_member_data = {
        "mobile": sql_result[0][0],
        "password": "123456",
        "contact": testdata.get_test_data().get("contact"),
        "subjectId": sql_result[0][2],
        "lineId": sql_result[0][1],
        "email": testdata.get_test_data().get("email"),
        "newmobile": testdata.get_test_data().get("mobile"),
        "memberId": sql_result[0][3]
    }
    return edit_member_data


@pytest.fixture(scope="session")
def add_broker_data():
    sql_result = db.select()
    broker_data = {
        "mobile": sql_result[0][0],
        "password": "123456",
        "contact": testdata.get_test_data().get("broker"),
        "email": testdata.get_test_data().get("email"),
        "newmobile": testdata.get_test_data().get("mobile"),
        "merchantId": sql_result[0][1],
        "registrationRegion": "北京市"
    }
    return broker_data


@pytest.fixture(scope="session")
def edit_broker_basic_data():
    sql_result = db.select()

    active_broker = {
        "mobile": sql_result[0][0],
        "password": 123456,
        "sms_code_type": 1
    }

    broker_basic_data = {
        "mobile": sql_result[0][0],
        "password": "123456",
        "brokerName": sql_result[0][1]
    }
    return active_broker,broker_basic_data


def teardown_module():
    db.conn.close()
