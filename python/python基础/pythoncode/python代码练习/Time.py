# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

Now = time.time()
print "当前时间戳为:", Now

import time

localtime = time.localtime(time.time())
print "本地时间为 :", localtime
'''
time.struct_time(tm_year=2017, tm_mon=2, tm_mday=19, tm_hour=23, tm_min=11, tm_sec=51, tm_wday=6, tm_yday=50,
                 tm_isdst=0)
'''


localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime


# 格式化成2017-02-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2017形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))



import calendar

cal = calendar.month(2017, 2)
print "以下输出2017年1月份的日历:"
print cal;



# ! /usr/bin/python
# coding=utf-8

from datetime import datetime, tzinfo, timedelta

"""
tzinfo是关于时区信息的类
tzinfo是一个抽象类，所以不能直接被实例化
"""


class UTC(tzinfo):
    """UTC"""

    def __init__(self, offset=0):
        self._offset = offset

    def utcoffset(self, dt):
        return timedelta(hours=self._offset)

    def tzname(self, dt):
        return "UTC +%s" % self._offset

    def dst(self, dt):
        return timedelta(hours=self._offset)


# 北京时间
beijing = datetime(2017, 2, 11, 0, 0, 0, tzinfo=UTC(8))
print "beijing time:", beijing
# 曼谷时间
bangkok = datetime(2017, 2, 11, 0, 0, 0, tzinfo=UTC(7))
print "bangkok time", bangkok
# 北京时间转成曼谷时间
print "beijing-time to bangkok-time:", beijing.astimezone(UTC(7))

'''
beijing time: 2017-02-11 00:00:00+08:00
bangkok time 2017-02-11 00:00:00+07:00
beijing-time to bangkok-time: 2017-02-10 23:00:00+07:00
'''

# 计算时间差时也会考虑时区的问题
timespan = beijing - bangkok
print "#时差:", timespan


#时差: -1 day, 23:00:00

print time.time()
#1487518230.33
#struct_time to timestamp
print time.mktime(time.localtime())
#生成struct_time
# timestamp to struct_time 本地时间
print time.localtime()
print time.localtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=16, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

# timestamp to struct_time 格林威治时间
print time.gmtime()
print time.gmtime(time.time())
# time.struct_time(tm_year=2016, tm_mon=10, tm_mday=26, tm_hour=8, tm_min=45, tm_sec=8, tm_wday=2, tm_yday=300, tm_isdst=0)

#format_time to struct_time
print time.strptime('2017-05-05 16:37:06', '%Y-%m-%d %X')
# time.struct_time(tm_year=2011, tm_mon=5, tm_mday=5, tm_hour=16, tm_min=37, tm_sec=6, tm_wday=3, tm_yday=125, tm_isdst=-1)

#生成format_time
#struct_time to format_time
print time.strftime("%Y-%m-%d %X")
print time.strftime("%Y-%m-%d %X",time.localtime())
# 2017-02-19 23:32:18


#生成固定格式的时间表示格式
print time.asctime(time.localtime())
print time.ctime(time.time())
# Sun Feb 19 23:32:40 2017

import pytz
pytz.country_timezones('cn')

'''
#from dateutil.parserimport parse
parse("Wed, Nov12")
#datetime.datetime(2017, 11, 12, 0, 0)
parse("2017-08-20")
#datetime.datetime(2017, 8, 20, 0, 0)
parse("20170820")
#datetime.datetime(2017, 8, 20, 0, 0)
parse("2017,08,20")
#datetime.datetime(2017, 8, 20, 0, 0)
#parse("08,20")
datetime.datetime(2017, 8, 20, 0, 0)
#parse("12:00:00")
datetime.datetime(2017, 2, 15, 12, 0)
#parse("thisis the wonderful moment 12:00:00,I feel good",fuzzy=True)#fuzzy开启模糊匹配，过滤掉无法识别的时间日期字符
datetime.datetime(2017,2, 15, 12, 0)

'''
