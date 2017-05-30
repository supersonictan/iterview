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

logger = Logger(logFileName='asia.log', logger="asia").getlog()



#http://4444av.co/list/1.html------http://4444av.co/list/1-469.html
#url = 'http://5555av.co/vod/11.html'
url = 'http://5555av.co/vod/20.html'

def get_url_result(list_url, encoding):
    #headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    #r = requests.get(list_url,headers=headers)
    r = requests.get(list_url)
    r.encoding = encoding
    return r.text


def parse_vdo_html(html):
    log_str = ''
    soup = BeautifulSoup(html, 'lxml')
    #print html

    p = str(soup)

    #title
    title = soup.find('h1').string
    log_str += title + '\t'
    #print title

    #download
    download_link = re.search('"ed2k:.*?/"',p).group().replace('"', '')
    log_str += download_link + '\t'
    #print download_link

    #area
    area_tmp = re.search('<li><span>影片类型：.*?</a>', p).group()
    area = re.search('title=".+?"', area_tmp).group().replace('title="', '').replace('"', '')
    log_str += area + '\t'
    #print area

    #time 案例：更新日期：</span>2017-04-18</div>
    time = re.search('更新日期：.*?</div>', p).group().replace('更新日期：</span>', '').replace('</div>', '')
    log_str += time + '\t'
    #print time


    #main-pic
    reg_main_pic_reg = '<div class="pic">.*?jpg'
    reg_main_pic_2 = '//.*?.jpg'
    #main_pic = re.search(reg_main_pic_reg, p).group().replace('<div class="pic"><img src="//', '')
    main_pic_tmp = re.search(reg_main_pic_reg, p).group()
    main_pic = 'http:' + re.search(reg_main_pic_2, main_pic_tmp).group()
    log_str += main_pic + '\t'
    #print 'mian pic:' + main_pic

    #vdo_pic
    vdo_pic_reg = 'endtext vodimg.*'
    vdo_pic_reg_old = '<img.*'
    vdo_reg_tmp = 'img.*?Simsun;'
    vdo_pic_div = re.search(vdo_pic_reg, p)
    vdo_pic_list = []
    if vdo_pic_div:
        res_list = re.findall('//.*?.jpg', vdo_pic_div.group())
        if res_list:
            for pic in res_list:
                #vdo_pic_list.append(pic.replace('src="', '').replace('http://', '').replace('//', ''))
                vdo_pic_list.append(pic.replace('src="', ''))
        else:
            vdo_pic_div = re.findall(vdo_reg_tmp, p)
            for pic in vdo_pic_div:
                tmp = pic.replace('img alt="" border="0" src="', '')
                tmp = tmp.replace('" style="font-family:Simsun;', '')
                vdo_pic_list.append(tmp)
                #print vdo_pic_div

    #拼接vdopic
    vdo_str = ''
    for vdoUrl in vdo_pic_list:
        vdo_str += str(vdoUrl).strip() + ';'

    #print vdo_pic_list
    log_str += vdo_str
    logger.error(log_str)


if __name__ == '__main__':
    # for i in range(1,11980):
    #     url = 'http://5555av.co/vod/' + str(i) + '.html'
    #     print url
    #     html = get_url_result(url, 'utf-8')
    #     #print html
    #     parse_vdo_html(html)
    html = get_url_result(url, 'utf-8')
    # print html
    parse_vdo_html(html)