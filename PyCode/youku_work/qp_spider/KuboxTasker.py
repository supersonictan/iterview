#!/usr/bin/python
# -*- coding=utf-8-*-
from collections import OrderedDict
import requests
import Queue
import sys
import json
import threading
from Logger import *
import copy
import Global
import re
from urllib import unquote
from requests.adapters import HTTPAdapter
import urllib
reload(sys)

sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='qt_flag10_test.log', logger="tasker").getlog()

class KuboxTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def __getKuboxJson(self, url):
        json = None
        try:
            session = requests.session()
            session.mount('http://', HTTPAdapter(max_retries=3))
            res = session.get(url)
            res.encoding = 'utf-8'
            json = res.json()
            # retry
            i = 0
            while len(res.content) == 0 and i < 2:
                res = session.get(url)
                if len(res.content) > 0:
                    json = res.json()
                i += 1
            return json
        except Exception, e:
            logger.error('Http request exception, query:' + url + ' e:' + str(e))
        return json

    def __getQpJson(self, url):
        json = None
        try:
            session = requests.session()
            session.mount('http://', HTTPAdapter(max_retries=3))
            res = session.get(url)
            res.encoding = 'utf-8'
            json = res.json()
            # retry
            i = 0
            while len(res.content) == 0 and i < 2:
                res = session.get(url)
                if len(res.content) > 0:
                    json = res.json()
                i += 1
            return json
        except Exception, e:
            logger.error('Http request exception, query:' + url + ' e:' + str(e))
        print(json)
        return json

    # parse json
    def __get_old_sug(self, json, query):
        queryList = []
        try:
            sugList = json['r']
            for sug in sugList:
                if sug.has_key('w') and sug['w'] not in queryList:
                    queryList.append(sug['w'])
        except Exception,e:
            logger.error('Old parse json exception, query:' + query + ", e:" + str(e))
        return queryList

    def __get_dii_sug(self, json, query):
        queryList = []
        try:
            data = json['data']
            dii = data['dii']
            sugList = dii['r']
            for sug in sugList:
                if sug.has_key('w') and sug['w'] not in queryList:
                    queryList.append(sug['w'])
        except Exception,e:
            logger.error('DII parse json exception, query:' + query + ", e:" + str(e))
        return queryList

    def __parse_qp_json(self, decodejson, query):
        result = 0
        try:
            if len(decodejson['conf']['result']['module']) == 0:
                return result

            d2_res = decodejson['conf']['result']['module']
            for seg in d2_res:
                if seg['name'] == "ali_seg":
                    ali_seg_p_list = seg['p']

                    for each_p in ali_seg_p_list:
                        flag_val = each_p['flag']
                        if flag_val == 10:
                            result = 1
                            return result

        except Exception,e:
            logger.error('Json Parser Error, query:' + query + ", e:" + str(e))
        return result

    def run(self):
        while True:
            try:
                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()

                if tmpId % 500 == 0:
                    print(tmpId)

                query = Global.query_queue.get(block=True, timeout=5)
                # query = urllib.urlencode(query)

                a_url = 'https://soku-qp.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&is_qt_ab=1&q=' + query
                qp_json_a = self.__getQpJson(a_url)
                a_has_flag = self.__parse_qp_json(qp_json_a, query)

                b_url = 'https://soku-qp.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&is_qt_ab=0&q=' + query
                qp_json_b = self.__getQpJson(b_url)
                b_has_flag = self.__parse_qp_json(qp_json_b, query)


                # 新版多的1，少的0
                flag = -1
                if a_has_flag == 1 and b_has_flag == 0:
                    flag = 1
                elif a_has_flag == 0 and b_has_flag == 1:
                    flag = 0

                if flag != -1:
                    logger.error('%s\t%d' % (query, flag))

            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
