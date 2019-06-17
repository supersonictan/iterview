#!/usr/bin/python
# -*- coding=utf-8-*-
from collections import OrderedDict
import requests
import Queue
import sys
import json
import threading

import time

from Logger import *
import copy
import Global
import re
from urllib import unquote
from requests.adapters import HTTPAdapter
import urllib
reload(sys)

sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='qt_flag_test.log', logger="tasker").getlog()

class KuboxTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName


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
            #logger.error('Http request exception, query:' + url + ' e:' + str(e))
            pass
        return json


    def __parse_qp_json(self, decodejson, query):
        result = {}
        try:
            if len(decodejson['conf']['result']['module']) == 0:
                return result

            d2_res = decodejson['conf']['result']['module']

            is_find_5 = False
            is_find_10 = False

            for seg in d2_res:
                if seg['name'] == "ali_seg":
                    ali_seg_p_list = seg['p']

                    for each_p in ali_seg_p_list:

                        flag_val = each_p['flag']

                        if flag_val == 10:
                            result[10] = 1
                            is_find_10 = True

                        if flag_val == 5:
                            result[5] = 1
                            is_find_5 = True

                        if is_find_5 or is_find_10:
                            return result

                    break
        except Exception,e:
            # logger.error('Json Parser Error, query:' + query + ", e:" + str(e))
            pass
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

                start = time.time()
                print(start)

                a_url = 'https://soku-qp.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&is_qt_ab=1&q=' + query
                qp_json_a = self.__getQpJson(a_url)
                end = time.time()
                print end - start

                a_has_flag = self.__parse_qp_json(qp_json_a, query)


                b_url = 'https://soku-qp.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&is_qt_ab=0&q=' + query
                qp_json_b = self.__getQpJson(b_url)
                b_has_flag = self.__parse_qp_json(qp_json_b, query)


                # 新版多1，少0
                if a_has_flag.has_key(10) and not b_has_flag.has_key(10):
                    logger.error('%s\t%d\t%d' % (query, 1, 10))
                elif not a_has_flag.has_key(10) and b_has_flag.has_key(10):
                    logger.error('%s\t%d\t%d' % (query, 0, 10))

                if a_has_flag.has_key(5) and not b_has_flag.has_key(5):
                    logger.error('%s\t%d\t%d' % (query, 1, 5))
                elif not a_has_flag.has_key(5) and b_has_flag.has_key(5):
                    logger.error('%s\t%d\t%d' % (query, 0, 5))

            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
