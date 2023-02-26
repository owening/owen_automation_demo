from auto_test_api.common.get_log import log
from auto_test_api.api.account import FmpMember
from datetime import datetime


class CommonFunc():
    def __init__(self):
        self.log = log


    def test_running_log(self, func):
        log = self.log
        def inner(*args):
            log.info(f"-----------用例{func.__name__}开始执行--------------------")
            func(*args)
            log.info(f"-----------用例{func.__name__}执行结束--------------------")

        return inner

    def get_member_fmpUid(self, mobile, password):
        return FmpMember().get_member_fmpUid(mobile, password)


    def get_partner_fmpUid(self, member_fmpUid, partner_id):
        return FmpMember().get_partner_fmpUid(member_fmpUid, partner_id)


    def transform_response_dict(self, response_data, return_type, *key):
        '''
        用于将接口查询接口转化为数组格式，与数据库查询结果作对比 ((1, 2), (1, 2))
        :param response_data: 接口返回的结果数据 [{}, {}]、{}
        :param return_type: 希望返回数据的类型，tuple or list
        :param *key：要取的结果各字段key
        '''
        return_data = []
        if type(response_data) == dict:
            for k in key:
                return_data.append(response_data[k])
        elif type(response_data) in (list, tuple):
            for dic in response_data:
                item = []
                for k in key:
                    item.append(dic[k])
                return_data.append(return_type(item))

        return return_type(return_data)

    def transform_between_list_and_tuple(self, data, return_type):
        '''
        将数据格式转化为列表或者元组，源数据：[(),()]、[[],[]]、([],[])、((),())
        :param data:
        :param return_type:
        :return:
        '''
        if type(data) not in (list, tuple):
            raise data + "is not list or tuple, can't be transformed"

        data = list(data)
        for item in data:
            index = data.index(item)
            item = return_type(item)
            data[index] = item
        return return_type(data)


    def transform_datetime_into_str(self, data, time_str="%Y-%m-%d %H:%M:%S"):
        '''
        将数据中的datetime格式转化为字符串，源数据：datetime、{"a":1,"b":2,"time":datetime}、[(1,2,datetime)]等
        :param data:
        :param time_str:
        :return:
        '''
        if type(data) == datetime:
            return data.strftime(time_str)
        elif type(data) == dict:
            for key, value in data.items():
                if type(value) == datetime:
                    data[key] = value.strftime(time_str)
        elif type(data) in (list, tuple):
            data_type = type(data)
            data = list(data)
            for item in data:
                item_index = data.index(item)
                item_type = type(item)
                if item_type == dict:
                    for key, value in item.items():
                        if type(value) == datetime:
                            item[key] = value.strftime(time_str)
                elif item_type in (list, tuple):
                    item = list(item)
                    for sub in item:
                        if type(sub) == datetime:
                            #print("11111")
                            sub_index = item.index(sub)
                            #print("index", sub_index)
                            item[sub_index] = sub.strftime(time_str)
                    item = item_type(item)
                data[item_index] = item
                #print(data)
            data = data_type(data)
        else:
            raise data+"格式不正确"

        return data


    def has_same_items(self, p1, p2):
        different_item_p1 = [x for x in p1 if x not in p2]
        different_item_p2 = [x for x in p2 if x not in p1]
        return False if different_item_p1 or different_item_p2 else True

if __name__=="__main__":
    member_fmpUid = CommonFunc().get_member_fmp_uid("mobile", "123456")
    partner_fmpUid = CommonFunc().get_partner_fmp_uid(member_fmpUid, "2027118")