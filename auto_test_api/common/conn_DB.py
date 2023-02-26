#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：conn_DB.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/17 14:57 
'''
import os
import sys

sys.path.append(os.path.realpath(__file__))

import pymysql
from auto_test_api.common.config import cf
from auto_test_api.common.get_log import log



class ConnDB():

    def __init__(self):
        host = cf.get_key("qx_mysql", "host")
        port = int(cf.get_key("qx_mysql", "port"))
        user = cf.get_key("qx_mysql", "user")
        password = cf.get_key("qx_mysql", "password")
        charset = cf.get_key("qx_mysql", "charset")

        sms_host = cf.get_key("sms_mysql", "host")
        sms_port = int(cf.get_key("sms_mysql", "port"))
        sms_user = cf.get_key("sms_mysql", "user")
        sms_password = cf.get_key("sms_mysql", "password")
        sms_charset = cf.get_key("sms_mysql", "charset")
        try:
            self.conn = pymysql.connect(host=host, port=port, user=user, password=password, charset=charset)
            self.sms_conn = pymysql.connect(host=sms_host, port=sms_port, user=sms_user, password=sms_password, charset=sms_charset)
        except Exception as e:

            log.error(f"无法连接数据库，错误原因:{e}")


    def select(self, query):
        try:
            #创建游标对象
            cur = self.conn.cursor()
            #使用游标的execute()方法执行sql语句
            cur.execute(query)
            #获取所有结果数据
            select_data = cur.fetchall()
            log.info("数据查询成功")
            # 关闭游标连接
            cur.close()
            # 关闭数据库连接
            # self.conn.close()
            return select_data

        except Exception as e:
            log.error(f"select查询语句错误，错误原因：{e}")

    def sms_select(self, query):
        try:
            #创建游标对象
            cur = self.sms_conn.cursor()
            #使用游标的execute()方法执行sql语句
            cur.execute(query)
            #获取所有结果数据
            select_data = cur.fetchall()
            log.info("数据查询成功")
            # 关闭游标连接
            cur.close()
            # # 关闭数据库连接
            # self.sms_conn.close()
            return select_data

        except Exception as e:
            log.error(f"select查询语句错误，错误原因：{e}")





if __name__ == "__main__":
    #db = ConnDB()
    # # sql_result = sql.sms_select()
    # sql_result = db.select()
    # # # str_sql = sql_result[0][0]
    # # # # customerId = fmp.extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
    # # #
    # # #     # extractData(r"(\d+(\.\d+)?)", str(sql_result), 0)
    # # #
    # print(f"第一打印{sql_result[0][0]}")
    # # print(f"打印{str_sql}")
    pass


