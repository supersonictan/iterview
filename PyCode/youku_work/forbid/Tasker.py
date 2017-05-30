#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json
import threading
from Logger import *
import copy
import re
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import lxml
import Common
import sys
import urllib
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='tasker.log', logger="tasker").getlog()

class Tasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def get_url_result(self, list_url, encoding):
        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        # r = requests.get(list_url,headers=headers)
        session = requests.session()
        session.mount('http://', HTTPAdapter(max_retries=5))
        r = session.get(list_url)
        r.encoding = encoding
        return r.text

    def parse_vdo_html(self, html, index):
        log_str = '' + str(index) + '\t'
        soup = BeautifulSoup(html, 'lxml')
        # print html

        p = str(soup)

        # title
        title_tmp = soup.find('h1')
        if title_tmp and title_tmp.string:
            title = title_tmp.string
            log_str += title + '\t'
        else:
            log_str += '\t'
            logger.error(str(index) + ' title error')
        # print title

        # download
        download_reg_1 = '"ed2k:.*?/"'
        download_reg_2 = '<a href="thunder.*?"'
        download_link = re.search(download_reg_1, p)
        if download_link:
            download_link = download_link.group().replace('"', '')
        else:
            download_link = re.search(download_reg_2, p)
            if download_link:
                download_link = download_link.group().replace('<a href="', '').replace('"', '')
            else:
                download_link = ''
        download_link = urllib.unquote(download_link)
        log_str += download_link + '\t'
        # print download_link

        # area
        try:
            area_tmp = re.search('<li><span>影片类型：.*?</a>', p).group()
            area = re.search('title=".+?"', area_tmp).group().replace('title="', '').replace('"', '')
            log_str += area + '\t'
        except Exception,e:
            log_str += '\t'
            logger.error(str(index) + ' area error')
        # print area

        # time 案例：更新日期：</span>2017-04-18</div>
        try:
            time = re.search('更新日期：.*?</div>', p).group().replace('更新日期：</span>', '').replace('</div>', '')
            log_str += time + '\t'
        except Exception,e:
            log_str += '\t'
            logger.error(str(index) + ' time error')
        # print time


        # main-pic
        try:
            reg_main_pic_reg = '<div class="pic">.*?jpg'
            reg_main_pic_2 = '//.*?.jpg'
            # main_pic = re.search(reg_main_pic_reg, p).group().replace('<div class="pic"><img src="//', '')
            main_pic_tmp = re.search(reg_main_pic_reg, p).group()
            main_pic = 'http:' + re.search(reg_main_pic_2, main_pic_tmp).group()
            log_str += main_pic + '\t'
            # print 'mian pic:' + main_pic
        except Exception,e:
            log_str += '\t'
            logger.error(str(index) + ' main-pic error')

        # vdo_pic
        try:
            #<img src="//i2.1100lu.xyz/month_1508/15082607361d55d1256780f5c5.jpg" border="0" />
            vdo_pic_reg = 'endtext vodimg.*'
            vdo_pic_reg_old = '<img.*'
            vdo_reg_tmp = 'img.*?Simsun;'
            vdo_pic_div = re.search(vdo_pic_reg, p)
            vdo_pic_list = []
            if vdo_pic_div:
                res_list = re.findall('//.*?.jpg', vdo_pic_div.group())
                if res_list:
                    for pic in res_list:
                        # vdo_pic_list.append(pic.replace('src="', '').replace('http://', '').replace('//', ''))
                        vdo_pic_list.append(pic.replace('src="', ''))
                else:
                    vdo_pic_div = re.findall(vdo_reg_tmp, p)
                    for pic in vdo_pic_div:
                        tmp = pic.replace('img alt="" border="0" src="', '')
                        tmp = tmp.replace('" style="font-family:Simsun;', '')
                        vdo_pic_list.append(tmp)
                        # print vdo_pic_div

            # 拼接vdopic
            vdo_str = ''
            for vdoUrl in vdo_pic_list:
                vdo_str += str(vdoUrl).strip() + ';'

            # print vdo_pic_list
            log_str += vdo_str

        except Exception,e:
            logger.error(str(index) + ' vdo_pic error')

        logger.info(log_str)

    def run(self):
        while True:
            i = Common.query_queue.get(block=True, timeout=5)
            url = 'http://5555av.co/vod/' + str(i) + '.html'
            print  url
            html = self.get_url_result(url, 'utf-8')
            self.parse_vdo_html(html, i)