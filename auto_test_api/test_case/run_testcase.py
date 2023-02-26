#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：run_testcase.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/12/15 18:07 
'''
import datetime
import os
import sys


for root, dirs, files in os.walk(
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))))):
    sys.path.append(root)
    for dir in dirs:
        dir_path = os.path.join(root, dir)
        sys.path.append(dir_path)

rep_file_name = datetime.datetime.now().strftime("%Y-%m-%d")
rep_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__)))) + "/report"
print(f"测试报告结果路径{rep_path}")
case_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
print(f"测试用例路径{case_path}")

import pytest

if __name__ == "__main__":
    pytest.main(["-vs", f"{case_path}", f"--alluredir={rep_path}/result", "--clean-alluredir", ])
    os.system(f"allure generate {rep_path}/result -o {rep_path}/allure_html/{rep_file_name} --clean")
