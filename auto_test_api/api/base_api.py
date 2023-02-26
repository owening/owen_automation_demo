#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：base_api.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/4 9:47 
'''
import os
import re
from string import Template
from urllib.parse import urlparse

import requests
import yaml
from jsonpath import jsonpath
from auto_test_api.common.config import cf
from auto_test_api.common.get_log import log
import traceback
from datetime import datetime


class BaseApi:

    Base_Path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    def send_api(self, req: dict):
        session = requests.session()
        return session.request(**req)

    @classmethod
    def template(cls, path, data, sub=None):
        with open(path, encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(Template(f.read()).substitute(data))
            else:
                return yaml.safe_load(Template(yaml.dump(yaml.safe_load(f)[sub])).substitute(data))


    def replace_host(self, data):
        host_name = urlparse(str(data["url"])).hostname
        ip = cf.get_key("pre-env", host_name)
        data["url"] = str(data["url"]).replace(host_name, ip)
        return data

    def send_api_data(self, path, req_data, sub):
        api_name = traceback.extract_stack()[-2][2]  # [-3][3]
        log.info(f"------------接口{api_name}开始执行--------------")
        # 链接根路径和yml文件的相对路径，简化文件路径
        path = os.path.join(self.Base_Path, path)
        # 获取请求数据
        data: dict = self.template(path, req_data, sub)
        log.info(f"api模板改变的参数为：{req_data}")
        # 由于Template转化的数据都是字符串，None也会变成'None'，通过下面的方法解决这个问题
        # 防止有些请求没有请求体的，不然就报错了
        try:
            for i in data['json'].keys():
                if data['json'][i] == 'None':
                    data['json'][i] = None
                elif data['json'][i] in ('True', 'true'):
                    data['json'][i] = True
                elif data['json'][i] in ('False', 'false'):
                    data['json'][i] = False
        except:
            pass
        # 使用template方法返回的数据会将时间字符串转化为datetime格式，导致json无法解析，需要重新转化为字符串格式
        if "json" in data:
            for key, value in data["json"].items():
                if isinstance(value, datetime):
                    data["json"][key] = datetime.strftime(value, "%Y-%m-%d %H:%M:%S")
        log.info(f"修改后的请求为：{data}")
        # 将请求url中的域名替换成配置环境中域名对应的IP
        # self.replace_host(data)
        # log.info(f"替换域名后的请求为：{data}")
        res = self.send_api(data)
        if res.status_code == 200:
            log.info((f"响应为：{res.json()}"))
        else:
            log.info((f"响应为：{res}"))
        log.info(f"------------接口{api_name}执行结束--------------")
        return res



    @classmethod
    def read_yaml(cls, path, sub=None):
        """
        读取yaml文件转成python数据类型
        """
        path = os.path.join(cls.Base_Path, path)
        with open(path, encoding="utf-8") as f:
            if sub is None:
                return yaml.safe_load(f)
            else:
                return yaml.safe_load(f)[sub]

    @classmethod
    def save_yaml(cls, path, data):
        """
        python数据写入yaml文件中
        """
        path = os.path.join(cls.Base_Path, path)
        with open(path, "a+", encoding="utf-8") as f:
            yaml.safe_dump(data, f, allow_unicode=True)

    @classmethod
    def json_path(cls, json, expr):
        return jsonpath(json, expr)

    @classmethod
    def extractData(cls,regex, content, index):
        r = '0'
        pattern = re.compile(regex)
        m = pattern.search(content)
        if m:
            r = m.group(index)
        return r
