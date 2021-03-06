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
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='kubox.log', logger="tasker").getlog()

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

    def run(self):
        while True:
            try:
                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()

                query = Global.query_queue.get(block=True, timeout=5)
                #query = '将军'
                dii_url='http://pre.kubox.soku.proxy.taobao.org/sug?' + query
                json = self.__getKuboxJson(dii_url)

            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
