Python 日期和时间

Python程序能用很多方式处理日期和时间，转换日期格式是一个常见的功能。
Python提供了一个time和 calendar 模块可以用于格式化日期和时间。
时间间隔是以秒为单位的浮点小数。
每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
Python的time模块下有很多函数可以转换常见日期格式。如函数time.time()用于获取当前时间戳, 如下实例:
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time;  # 引入time模块

Now = time.time()
print "当前时间戳为:", Now

以上实例输出结果：
当前时间戳为: 1487516921.98
时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。

什么是时间元组？
很多Python函数用一个元组装起来的9组数字处理时间:

也就是struct_time元组。这种结构具有如下属性：

序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜


获取当前时间
从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time

localtime = time.localtime(time.time())
print "本地时间为 :", localtime
以上实例输出结果：
本地时间为:time.struct_time(tm_year=2017, tm_mon=2, tm_mday=19, tm_hour=23, tm_min=11, tm_sec=51, tm_wday=6, tm_yday=50,
                 tm_isdst=0)

获取格式化的时间
你可以根据需求选取各种格式，但是最简单的获取可读的时间模式的函数是asctime():
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time

localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime
以上实例输出结果：
本地时间为 : Sun Feb 19 23:12:54 2017

格式化日期
我们可以使用time 模块的strftime
方法来格式化日期，：
time.strftime(format[, t])
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import time

# 格式化成2017-02-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2017形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2017"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

以上实例输出结果：

2017-02-19 23:14:38
Sun Feb 19 23:14:38 2017
1490711064.0


python中时间日期格式化符号：
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身



Calendar模块有很广泛的方法用来处理年历和月历，例如打印某月的月历：
# !/usr/bin/python
# -*- coding: UTF-8 -*-

import calendar

cal = calendar.month(2017, 2)
print "2017年2月份的日历:"
print cal;
以上实例输出结果：
2017年2月份的日历:

   February 2017
Mo Tu We Th Fr Sa Su
       1  2  3  4  5
 6  7  8  9 10 11 12
13 14 15 16 17 18 19
20 21 22 23 24 25 26
27 28

Time 模块
Time 模块包含了以下内置函数，既有时间处理相的，也有转换时间格式的：
序号	函数及描述
1	time.altzone 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
2	time.asctime([tupletime]) 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
3	time.clock( ) 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
4	time.ctime([secs]) 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
5	time.gmtime([secs]) 接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0
6	time.localtime([secs]) 接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。
7	time.mktime(tupletime) 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。
8	time.sleep(secs) 推迟调用线程的运行，secs指秒数。
9	time.strftime(fmt[,tupletime]) 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
10	time.strptime(str,fmt='%a %b %d %H:%M:%S %Y') 根据fmt的格式把一个时间字符串解析为时间元组。
11	time.time( ) 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。
12	time.tzset() 根据环境变量TZ重新初始化时间相关设置。

Time模块包含了以下2个非常重要的属性：
序号	属性及描述
1	time.timezone 属性time.timezone是当地时区（未启动夏令时）距离格林威治的偏移秒数（>0，美洲;<=0大部分欧洲，亚洲，非洲）。
2	time.tzname  属性time.tzname包含一对根据情况的不同而不同的字符串，分别是带夏令时的本地时区名称，和不带的。

日历（Calendar）模块
此模块的函数都是日历相关的，例如打印某月的字符月历。
星期一是默认的每周第一天，星期天是默认的最后一天。更改设置需调用calendar.setfirstweekday()函数。模块包含了以下内置函数：
序号	函数及描述
1	calendar.calendar(year,w=2,l=1,c=6) 返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
2	calendar.firstweekday( ) 返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
3	calendar.isleap(year) 是闰年返回True，否则为false。
4	calendar.leapdays(y1,y2) 返回在Y1，Y2两年之间的闰年总数。
5	calendar.month(year,month,w=2,l=1) 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
6	calendar.monthcalendar(year,month) 返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
7	calendar.monthrange(year,month) 返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
8	calendar.prcal(year,w=2,l=1,c=6) 相当于 print calendar.calendar(year,w,l,c).
9	calendar.prmonth(year,month,w=2,l=1) 相当于 print calendar.calendar（year，w，l，c）。
10	calendar.setfirstweekday(weekday) 设置每周的起始日期码。0（星期一）到6（星期日）。
11	calendar.timegm(tupletime) 和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
12	calendar.weekday(year,month,day) 返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。


在Python中，其他处理日期和时间的模块还有：
datetime模块
pytz模块
dateutil模块


datetime模块

datatime模块重新封装了time模块，提供更多接口，提供的类有：date,time,datetime,timedelta,tzinfo。

1、date类

datetime.date(year, month, day)

静态方法和字段
date.max、date.min：date对象所能表示的最大、最小日期；
date.resolution：date对象表示日期的最小单位。这里是天。
date.today()：返回一个表示当前本地日期的date对象；
date.fromtimestamp(timestamp)：根据给定的时间戮，返回一个date对象；


方法和属性
d1 = date(2011, 06, 03)  # date对象
d1.year、date.month、date.day：年、月、日；
d1.replace(year, month, day)：生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
d1.timetuple()：返回日期对应的time.struct_time对象；
d1.weekday()：返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
d1.isoweekday()：返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
d1.isocalendar()：返回格式如(year，month，day)的元组；
d1.isoformat()：返回格式如
'YYYY-MM-DD’的字符串；
d1.strftime(fmt)：和time模块format相同。

2、time类
datetime.time(hour[, minute[, second[, microsecond[, tzinfo]]]] )

静态方法和字段

time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
time.resolution：时间的最小单位，这里是1微秒；


方法和属性
t1 = datetime.time(10, 23, 15)  # time对象
t1.hour、t1.minute、t1.second、t1.microsecond：时、分、秒、微秒；
t1.tzinfo：时区信息；
t1.replace([hour[, minute[, second[, microsecond[, tzinfo]]]]] )：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
t1.isoformat()：返回型如
"HH:MM:SS"
格式的字符串表示；
t1.strftime(fmt)：同time模块中的format；

3、datetime类
datetime相当于date和time结合起来。
datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]] )

静态方法和字段
datetime.today()：返回一个表示当前本地时间的datetime对象；
datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
datetime.utcnow()：返回一个当前utc时间的datetime对象；  # 格林威治时间
datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
datetime.combine(date, time)：根据date和time，创建一个datetime对象；
datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；


方法和属性
dt = datetime.now()  # datetime对象
dt.year、month、day、hour、minute、second、microsecond、tzinfo：
dt.date()：获取date对象；
dt.time()：获取time对象；
dt.replace([year[, month[, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]]]]])：
dt.timetuple()
dt.utctimetuple()
dt.toordinal()
dt.weekday()
dt.isocalendar()
dt.isoformat([sep])
dt.ctime()：返回一个日期时间的C格式字符串，等效于time.ctime(time.mktime(dt.timetuple()))；
dt.strftime(format)

4.timedelta类，时间加减

使用timedelta可以很方便的在日期上做天days，小时hour，分钟，秒，毫秒，微妙的时间计算，如果要计算月份则需要另外的办法。
# coding:utf-8
from  datetime import *

dt = datetime.now()
# 日期减一天
dt1 = dt + timedelta(days=-1)  # 昨天
dt2 = dt - timedelta(days=1)  # 昨天
dt3 = dt + timedelta(days=1)  # 明天
delta_obj = dt3 - dt
print type(delta_obj), delta_obj  # <type 'datetime.timedelta'> 1 day, 0:00:00
print delta_obj.days, delta_obj.total_seconds()  # 1 86400.0

5、tzinfo时区类
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
beijing = datetime(2011, 11, 11, 0, 0, 0, tzinfo=UTC(8))
print "beijing time:", beijing
# 曼谷时间
bangkok = datetime(2011, 11, 11, 0, 0, 0, tzinfo=UTC(7))
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
print "时差:", timespan


# 时差: -1 day, 23:00:00

pytz查询某个的时区

可以根据国家代码查找这个国家的所有时区。

>>> import pytz
>>> pytz.country_timezones('cn')
['Asia/Shanghai', 'Asia/Harbin', 'Asia/Chongqing', 'Asia/Urumqi', 'Asia/Kashgar']
pytz创建时区对象

根据上面得到的时区信息，就可以创建指定的时区对象。比如创建上海时区对象：

tz = pytz.timezone('Asia/Shanghai')
得到某个时区的时间

然后在创建时间对象时进行指定上面时区，就可以得到指定时区的日期时间：

>>> import datetime
>>> datetime.datetime.now(tz)
datetime.datetime(2009, 2, 21, 15, 12, 33, 906000, tzinfo=<DstTzInfo 'Asia/Shanghai' CST+8:00:00 STD>)


dateutil模块主要有两个函数:
parser和rrule。parser是根据字符串解析成datetime，而rrule是则是根据定义的规则来生成datetime。

parser
parser是根据字符串解析成datetime,字符串可以很随意，可以用时间日期的英文单词，可以用横线、逗号、空格等做分隔符。
没指定时间默认是0点，没指定日期默认是今天，没指定年份默认是今年。

'''
from dateutil.parserimport parse
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


rrule
rrule(self, freq, dtstart=None, interval=1, wkst=None,count=None, until=None, bysetpos=None,
       bymonth=None, bymonthday=None, byyearday=None, byeaster=None,byweekno=None, byweekday=None, byhour=None, byminute=None, bysecond=None,cache=False)
参数理解
freq:可以理解为单位。可以是 YEARLY, MONTHLY, WEEKLY,DAILY, HOURLY, MINUTELY, SECONDLY。即年月日周时分秒。
dtstart,until:是开始和结束时间。
wkst:周开始时间。
interval:间隔。
count:指定生成多少个。
byxxx:指定匹配的周期。比如byweekday=(MO,TU)则只有周一周二的匹配。byweekday可以指定MO,TU,WE,TH,FR,SA,SU。即周一到周日。


'''
from dateutil.rruleimport *
list(rrule(DAILY,dtstart=parse('2017-08-01'),until=parse('2017-08-07')))
#2017-08-01到2017-08-07每日
#[datetime.datetime(2017, 8, 1, 0, 0),
datetime.datetime(2017,8, 2, 0, 0),
datetime.datetime(2017,8, 3, 0, 0),
datetime.datetime(2017,8, 4, 0, 0),
datetime.datetime(2017,8, 5, 0, 0),
datetime.datetime(2017,8, 6, 0, 0),
datetime.datetime(2017,8, 7, 0, 0)]

list(rrule(DAILY,interval=3,dtstart=parse('2017-08-01'),until=parse('2017-08-07')))#间隔为3
#[datetime.datetime(2017, 8, 1, 0, 0),
datetime.datetime(2017,8, 4, 0, 0),
datetime.datetime(2017,8, 7, 0, 0)]

list(rrule(DAILY,count=3,dtstart=parse('2017-08-01'),until=parse('2017-08-07')))#只生成3个
#[datetime.datetime(2017, 8, 1, 0, 0),
datetime.datetime(2017,8, 2, 0, 0),
datetime.datetime(2017,8, 3, 0, 0)]

list(rrule(DAILY,byweekday=(MO,TU),dtstart=parse('2017-08-01'),until=parse('2017-08-07')))#只匹配周一周二的
#[datetime.datetime(2017, 8, 5, 0, 0), datetime.datetime(2017, 8, 6,0, 0)]

list(rrule(MONTHLY,dtstart=parse('2017-05-19'),until=parse('2017-08-20')))#按月为单位
#[datetime.datetime(2017, 5, 19, 0, 0),
datetime.datetime(2017,6, 19, 0, 0),
datetime.datetime(2017,7, 19, 0, 0),
datetime.datetime(2017,8, 19, 0, 0)]

'''