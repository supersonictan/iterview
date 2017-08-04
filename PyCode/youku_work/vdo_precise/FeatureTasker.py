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

logger = Logger(logFileName='feature.log', logger="tasker").getlog()

bkt = """{"bts":{"soku_engine_master":{"bucket":{"groups":{"soku":""},"id":10052,"name":"110"},"end":1593878400},"soku_imerge_person":{"bucket":{"groups":{"soku":""},"id":10079,"name":"A"},"end":1594339200},"soku_imerge_showcate":{"bucket":{"groups":{"soku":""},"id":9737,"name":"A"},"end":1589587200},"soku_irank":{"bucket":{"groups":{"soku":""},"id":10058,"name":"204"},"end":1593878400},"soku_irank_test":{"bucket":{"groups":{"soku":""},"id":10024,"name":"A"},"end":1593216000},"soku_ogc":{"bucket":{"groups":{"soku":""},"id":10061,"name":"303"},"end":1593878400},"soku_qp":{"bucket":{"groups":{"soku":""},"id":9632,"name":"2"},"end":1606780800},"soku_resultpage_pic":{"bucket":{"groups":{"soku":""},"id":9732,"name":"A"},"end":1589472000},"soku_test_chenlin":{"bucket":{"groups":{"soku":""},"id":9591,"name":"1"},"end":1523980800},"soku_ugc":{"bucket":{"groups":{"soku":""},"id":10062,"name":"401"},"end":1593878400},"soku_version_test":{"bucket":{"groups":{"soku":""},"id":9641,"name":"2"},"end":1524844800}},"status":{"code":0},"tracker":{"sid":"6je7L2qr4FA"}}"""



reg_dic = OrderedDict({})

class FeatureTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName



    def __getImergerJson(self,url):
        json = None
        try:
            session = requests.session()
            session.mount('http://', HTTPAdapter(max_retries=3))
            res = session.get(url)
            json = res.json()
            print json
            # retry
            i = 0
            while len(res.content) == 0 and i < 2:
                res = session.get(url)
                if len(res.content) > 0:
                    json = res.json()
                i += 1
            return json
        except Exception, e:
            logger.error('Http request exception, query:' + ' e:' + str(e))
        return json

    def __parseJsonData(self, json, cur_query):
        sp_data = json['sp']

        if sp_data :
            youku_data = sp_data['youku']
            if youku_data:
                aux = youku_data['auxiliary']
                if aux['vdo_precise']:
                    logger.error(cur_query + '\t' + aux['vdo_precise'])
                else:
                    logger.error(cur_query + '\t' + '0')
            else:
                logger.error(cur_query + '\t' + 'youku data error')
        else:
            logger.error(cur_query + '\t' + 'sp_data error')

        # ecb_data = json['ecb']  #json最外层
        # youku_ecb = ecb_data['youku_ecb']
        # auctions = youku_ecb['auctions']
        #
        # for docItem in auctions:
        #     doctrace = str(unquote(docItem['doctrace']))
        #     #logger.error(doctrace)
        #     doc_show_id = docItem['show_id']
        #     self.__parseAndWriteFeatureScore(doctrace, doc_show_id, cur_query)



    def run(self):
        while True:
            try:
                cur_query = Global.query_queue.get(block=True, timeout=5)
                #cur_query = '火星情报局'
                url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?cmd=1&keyword='+ str(cur_query)
                print url

                jsonRes = self.__getImergerJson(url)
                print str(jsonRes)
                self.__parseJsonData(jsonRes, cur_query)

                # 显示第几个
                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()
                logger.debug('Finished ' + str(tmpId))
            except Exception,e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break