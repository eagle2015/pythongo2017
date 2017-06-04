#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode


# ----------------------------------
# 苹果序列号调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/37
# ----------------------------------

def main():
    # 配置您申请的APPKey
    appkey = "CCPK66YDDTD2"

    # 1.苹果序列号/IMEI号查询
    request1(appkey, "GET")


# 苹果序列号/IMEI号查询
def request1(appkey, m="GET"):
    url = "http://apis.juhe.cn/appleinfo/index"
    params = {
        "sn": "",  # 苹果产品的序列号或IMEI号
        "dtype": "",  # 返回数据格式：json或xml,默认json
        "key": appkey,  # 你申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"], res["reason"])
    else:
        print "request api error"


if __name__ == '__main__':
    main()