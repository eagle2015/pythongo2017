#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2,urllib
import os
import cookielib
from bs4 import BeautifulSoup
cookie = cookielib.CookieJar()
cookie_handler = urllib2.HTTPCookieProcessor(cookie)

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36'
}

path = os.getcwd()
new_path = os.path.join(path, u'豆瓣妹子')
if not os.path.isdir(new_path):
    os.makedirs(new_path, 7777)

page_number = 1


def get_image():
    global page_number
    url = 'http://www.dbmeizi.com/?p=%s' % page_number
    site_url = 'http://www.dbmeizi.com'
    request = urllib2.Request(url=url, headers=header)
    opener = urllib2.build_opener(cookie_handler)
    response = opener.open(request)
    page = response.read()

    soup = BeautifulSoup(page)
    for image in soup.findAll('img'):
        if not image:
            exit()
        file_handler = urllib2.urlopen(site_url+image['data-bigimg']).read()
        with open(u'豆瓣妹子/'+image['data-bigimg'][-11:], 'wb') as empty_file:
            empty_file.write(file_handler)
            print image['data-bigimg']

    page_number += 1
    print '第%s页下载完毕，现在开始下载第%s页' % (page_number,page_number+1)
    get_image()

get_image()