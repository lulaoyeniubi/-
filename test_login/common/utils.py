import time
import csv
import os
import re
import requests

base_path = os.path.dirname(os.path.dirname(__file__))
case_path = os.path.join(base_path, "case")
data_path = os.path.join(base_path, "data")
report_path = os.path.join(base_path, "report")


def request(url, method, data=None, header=None):
    rq = requests.session()  # 创建session对象
    if method in ("get", "Get", "GET"):
        r = rq.get(url=url, params=data, headers=header)
    elif method in ("POST", "post", "Post"):
        r = rq.post(url=url, data=data, headers=header)
    return r


def get_time():
    t = time.strftime("%Y-%m-%d %X")
    print(t)
    return t


def read_csv(file):
    if os.path.exists(file):
        with open(file=file, mode='r') as f:
            d = csv.reader(f)
            return list(d)
    else:
        print(f'文件{file}不存在')
        return False


def get_test_data(s):
    '''
    把 'account=张三，\npassword=123456'  转换为 {‘account’:‘张三’，’password‘:’123456'}
    :return:
    '''
    #########
    # data = dict()
    # ss = s.split(",")
    # for v in ss:
    #     sv = v.split("=")
    #     # print(sv[0])
    #     svv = sv[0].split("\n")
    #     # print(len(svv))
    #     idx = sv[0]
    #     if len(svv) > 1:
    #         idx = svv[1]
    #     data[idx] = sv[1]
    # data = json.dumps(data)
    # return data
    ###########

    data = {}
    r = re.split(',\n', s)
    for i, j in enumerate(r):
        tmp = j.split("=")
        data[tmp[0]] = tmp[1]
        print(type(data), data)
    return data


if __name__ == '__main__':
    r = read_csv(data_path + '/test_logins.csv')
    s = 'account=aaa,\npassword=123456'
    g = get_test_data(s)
    print("g", g)
