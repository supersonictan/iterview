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

logger = Logger(logFileName='query_tagging.log', logger="tasker").getlog()

class GameTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def __getKuboxJson(self, url):
        json = None
        try:
            session = requests.session()
            session.mount('https://', HTTPAdapter(max_retries=3))
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

    def __getBaikeHtml(self, url):
        json = None
        try:
            session = requests.session()
            session.mount('https://', HTTPAdapter(max_retries=3))
            res = session.get(url)
            res.encoding = 'utf-8'
            print(res.text)
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
        result_dic = {}
        try:
            if len(decodejson['conf']['result']['module']) == 0:
                result_dic

            d2_res = decodejson['conf']['result']['module']
            for seg in d2_res:
                if seg['name'] == "query_tagging":
                    d2_qt = seg['p']
                    # print d2_qt['seg_list']
                    qt_list = d2_qt['seg_list_level1']

                    for qt in qt_list:
                        word = qt['word'].encode('utf8')
                        label = qt['label'].encode('utf8')
                        result_dic[word] = label
                    # result = query+ "," + str(qt_result).encode('utf-8').strip() + "\n"
                    # result = json.dumps(qt_result, ensure_ascii=False).encode('utf-8').strip()
                    # print result

        except Exception,e:
            logger.error('Json Parser Error, query:' + query + ", e:" + str(e))
        return result_dic

    def run(self):
        while True:
            try:
                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()

                query = Global.query_queue.get(block=True, timeout=5)
                #query = '将军'
                # dii_url='http://pre.kubox.soku.proxy.taobao.org/sug?s=soku_sug_v1&query=' + query + '&outfmt=qp_json_a'
                # qp_json_a = self.__getKuboxJson(dii_url)

                # a_url = 'https://baike.baidu.com/item/' + query
                a_url = 'https://movie.douban.com/subject/26100958/'
                qp_json_a = self.__getBaikeHtml(a_url)
                print(qp_json_a)
            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
