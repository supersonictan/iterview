#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json
from Logger import *
import copy
import re
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import lxml
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='diff.log', logger="asiaSp").getlog()



#http://4444av.co/list/1.html------http://4444av.co/list/1-469.html
url = 'http://4444av.co/vod/11.html'
#url = 'http://4444av.co/vod/11814.html'

def get_url_result(list_url, encoding):
    #headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    #r = requests.get(list_url,headers=headers)
    r = requests.get(list_url)
    r.encoding = encoding
    return r.text


def parse_vdo_html(html):

    soup = BeautifulSoup(html, 'lxml')
    print html

    p = str(soup)

    #title
    title = soup.find('h1').string
    print title

    #download
    download_link = re.search('"ed2k:.*?/"',p).group().replace('"', '')
    print download_link

    #area
    area_tmp = re.search('<li><span>影片类型：.*?</a>', p).group()
    area = re.search('title=".+?"', area_tmp).group().replace('title="', '').replace('"', '')
    print area

    #time 案例：更新日期：</span>2017-04-18</div>
    time = re.search('更新日期：.*?</div>', p).group().replace('更新日期：</span>', '').replace('</div>', '')


    #main-pic
    reg_main_pic_reg = '<div class="pic">.*?jpg'
    main_pic = re.search(reg_main_pic_reg, p).group().replace('<div class="pic"><img src="//', '')

    #vdo_pic
    vdo_pic_reg = 'endtext vodimg.*?</p><br />'
    vdo_pic_reg_old = '<img.*?font-family:Simsun;font-size:medium;line-height:normal;"'
    vdo_pic_div = re.search(vdo_pic_reg, p)
    if vdo_pic_div:
        print vdo_pic_div.group()
    else:
        vdo_pic_div = re.findall(vdo_pic_reg_old, p)
        print vdo_pic_div
    print vdo_pic_div
    #vdo_pid_reg_2 = 'src=.*?.jpg'
    #print re.findall(vdo_pid_reg_2, vdo_pic_div)



if __name__ == '__main__':
    html = get_url_result(url, 'utf-8')
    #print html
    parse_vdo_html(html)