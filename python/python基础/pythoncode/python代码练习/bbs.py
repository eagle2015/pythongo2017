#!/usr/bin/env python
# -*- conding=utf-8 -*-

import urllib
import re
import request

def get_url(page):
    return  'http://www.budejie.com/video' +str(page)


def get_html(url):
    return  urllib.urlopen(url).read() #

def download(mp4_url,path):
    print path #
    path = "".join(path.split())
    print urllib.urlretrieve(mp4_url,TV\%s(path.decode('utf-8').encode('gbk')))
    print "ok!!!"



def get_mp4_url(request):
    reg = r'data-mp4="(.*?)"'
    return   re.findall(reg,request)  #



def get_name(request)
    reg =  re.complie(r'<a href="/detail-.{8}?.html">(.*?)</a>',re.S) # re.S
    return  re.findall(reg,request)

for i in range(1,2): #
    html = get_html(get_url(i))
    mp4_url = get_mp4_url(html)
    mp4_name = get_name(html)


for x,y in zip(mp4_url,mp4_name):
    download(x,y)