#!/usr/bin/env python
# -*- coding:utf-8 -*-
#   语言：Python 2.7
#   程序：抓取 豆瓣妹子 图片

from bs4 import BeautifulSoup
import  urllib,urllib2,os,cookielib


'''
#模块：urllib2 ,urllib ,bs4(beautifulsoup 4)  热lxml request
#安装bs4：wget http://www.crummy.com/software/BeautifulSoup/bs4/download/4.3/beautifulsoup4-4.3.2.tar.gz
1.详细了解bs4 网页爬取数据
2.字符格式化 %s 占位符   {}.format
3.如何获取网页源码？ urlopen ，read
4.反爬 ，网站禁止爬虫。获取不到想要的东西，请求失败的，需要模拟浏览器访问，加上头部信息
5.获取图片 find_all  get
6. 下载 urlretrieve（需要下载的，路径）
'''

url = 'http://www.dbmeinv.com/?pager_offset=1'
x = 0

cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)
#header 头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
}
#获取源码
def get_img(url):
    req = urllib2.Request(url,headers=headers) #创建对象
    page = urllib2.urlopen(req,timeout=30) #设置超时时间
    contents = page.read()#获取源码
    #print contents
    soup = BeautifulSoup(contents,'html.parser')
    girl_img = soup.find_all('img') #找到img标签
    for girl in girl_img:  #遍历
        link = girl.get('src') #获取src 图片
        print link
get_img(url)

