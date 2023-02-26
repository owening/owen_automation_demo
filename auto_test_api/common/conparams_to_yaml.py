#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：owen_automation_demo_copy
@File ：conparams_to_yaml.py
@IDE  ：PyCharm 
@Author ：Owen
@Date ：2021/11/16 16:02 
'''
import datetime
import os
import random

from auto_test_api.api.base_api import BaseApi
BASE_DIR = os.path.dirname(os.path.dirname(__file__))



class ConYaml:
    baseapi = BaseApi()



    def add_yaml(self, path, data):
        self.baseapi.save_yaml(path, data)

    def red_yaml(self, path):
        return self.baseapi.read_yaml(path)

    def get_test_data(self):
        custName = "自动测试客户" + str(random.randint(0, 9999999)) + "号"
        contact = "自动测试联系人" + str(random.randint(0, 9999999)) + "号"
        mobile = str(random.randint(13720000001, 13799999999))
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
            "trafficName": trafficName
        }
        return test_data


if __name__ == "__main__":

    path = "data/test_para_data.yaml"

    data = {
    "contact":"玩啊啊啊",
    "email":"98416516@qq.com",
    "mobile":"13751421021",
    "roleKey":"offline_ordering_staff",
    "relationMerchantIds":[
        "1028446"
    ],
    "registrationRegionCode":"110000",
    "registrationRegion":"北京市",
    "merchantIdBrokerConfig":1028446,
    "waitOpenCompanyList":[
        {
            "companyId":20029
        },
        {
            "companyId":1103
        }
    ]
}

    # conyaml = ConYaml()
    # conyaml.add_yaml(path, data)


#     str = conyaml.get_test_data().get('mobile')
#     str2 = conyaml.get_test_data().get('mobile')
# #     res = conyaml.red_yaml(path)
#     print(res)
    # print(type(res))
    #   rep_file_name = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
    #   print(rep_file_name)
    # conyaml.get_test_data()

    # # print(conyaml.get_test_data().get('mobile'))
    # print(str)
    # print(str2)




if __name__=="__main__":
    ConYaml()