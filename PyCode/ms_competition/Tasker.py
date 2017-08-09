#!/usr/bin/python
# -*- coding=utf-8-*-
from collections import OrderedDict
import requests
import Queue
import sys
import threading
from Logger import *
import Global
import re
import lxml
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='ms_competition.log', logger="tasker").getlog()

reg_dic = OrderedDict({})

homePage_reg = r'<h3 class="r">.*?</h3>'
title_reg = r'<a href.*?>(.*?)<'
email_reg_list = [r'\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z0-9]{2,4}\b']

#<img alt="Keith C. Schwab" src="http://d39s7jey1vv9fu.cloudfront.net/eas_directory/users/schwab/photos/keith-schwab-original.jpg?1464024708" />
#<img  width="275" height="275" alt="Raquel  Hill" src="https://www.soic.indiana.edu/img/people/ralhill.jpg">
pic_reg_list = [r'img.*?\bhttp:.+\.jpg[0-9-_?%~]+\b', r'img.*?\bhttp:.+\.png[0-9-_?%~]+\b'] #http https #-_?%~

class Tasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def __get_homepage_list(self, text):
        homePage_list = []
        title_list = []
        print text
        res = re.findall(homePage_reg, text, re.S)
        for each_res in res:
            homePage_url = re.findall(r'"http.*?"', each_res)[0]
            title_str = re.findall(title_reg, each_res)[0]
            homePage_list.append(homePage_url)
            title_list.append(title_str)
        return homePage_list


    def __get_email_list(self, text):
        res_list = []
        for reg in email_reg_list:
            #print reg
            res = re.findall(reg, text)
            res_list.append(res)
        return res_list

    def __get_img_list(self, text):
        res_list  =[]
        for reg in pic_reg_list:
            res = re.findall(reg, text)
            res_list.append(res)
        return res_list


    def __get_url_result(self, url):
        # headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        # r = requests.get(list_url,headers=headers)
        session = requests.session()
        session.mount('http://', HTTPAdapter(max_retries=5))
        r = session.get(url)
        r.encoding = 'utf-8'
        return r.text

    def __parse_html(self, html):
        soup = BeautifulSoup(html, 'lxml')
        # print html

        main_text = soup.find("div", {"class": "srg"})

        return main_text



    def run(self):
        #while True:
            try:
                #cur_query = Global.query_queue.get(block=True, timeout=5)
                #cur_query = '火星情报局'
                #url = str(cur_query).strip()

                url = 'http://ifang.ml:8081/542b5c8adabfae23313e5e5b.html'
                html = self.__get_url_result(url)
                main_txt = self.__parse_html(html)

                print self.__get_homepage_list(str(main_txt))


                # 显示第几个
                # Global.lock_curId.acquire()
                # Global.cur_id += 1
                # tmpId = Global.cur_id
                # Global.lock_curId.release()
                # logger.debug('Finished ' + str(tmpId))
            except Exception,e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                #break