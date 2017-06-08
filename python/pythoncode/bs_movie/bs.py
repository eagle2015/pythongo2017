#!/usr/bin/env python
# -*- conding=utf-8 -*-

import urllib
import re
import request

def get_url(page):
    return  'http://www.budejie.com/video' +str(page)

#获取html 源代码
def get_html(url):
    return  urllib.urlopen(url).read() #读取

def download(mp4_url,path):
    print path #标题
    path = "".join(path.split())
    urllib.urlretrieve(mp4_url,TV\%(path.decode('utf-8').encode(gbk)))
    print "ok!!!"


#匹配视频
def get_mp4_url(request):
    reg = r'data-mp4="(.*?)"'
    return   re.findall(reg,request)  #列表返回

#匹配标题

def get_name(request)
    reg =  re.complie(r'<a href="/detail-.{8}?.html">(.*?)</a>',re.S) # re.S  匹配换行
    return  re.findall(reg,request)

for i in range(1,2): #调用网址，视频地址，视频名字
    html = get_html(get_url(i))
    mp4_url = get_mp4_url(html)
    mp4_name = get_name(html)


for x,y in zip(mp4_url,mp4_name):
    download(x,y)