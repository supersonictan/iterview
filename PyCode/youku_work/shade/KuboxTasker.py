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
            data = json['data']
            dii = data['recall_debug']
            queryList = dii.split('###')
        except Exception,e:
            logger.error('Old parse json exception, query:' + query + ", e:" + str(e))
        return queryList

    def __get_dii_sug(self, json, query):
        queryList = []
        try:
            data = json['data']
            dii = data['recall_debug']
            queryList = dii.split('###')
            # sugList = dii['r']
            # for sug in sugList:
            #     if sug.has_key('w') and sug['w'] not in queryList:
            #         queryList.append(sug['w'])
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

                utdid = Global.query_queue.get(block=True, timeout=5)
                #utdid = '将军'
                # http://shadequery.online2.proxy.taobao.org/shade?s=shadequery&outfmt=json&utdid=WmBpaYFQhngDANQZHp3WMsQE&chnl_id=100480&trace=info
                dii_url='http://shadequery.online2.proxy.taobao.org/shade?s=shade_lr&utdid=' + utdid + '&outfmt=json&chnl_id=100480&trace=info'
                json = self.__getKuboxJson(dii_url)
                dii_list = self.__get_dii_sug(json, utdid)
                # res_str = ''
                # for dii_s  in dii_list:
                #     res_str += dii_s + '\t'
                # logger.error(res_str)

                old_url='http://shadequery.online2.proxy.taobao.org/shade?s=shadequery&utdid=' + utdid + '&outfmt=json&chnl_id=100480&trace=info'
                json_old = self.__getKuboxJson(old_url)
                old_list = self.__get_old_sug(json_old, utdid)

                # 比较差异
                diff_str = str(tmpId) + '.' +utdid + ' Diff:'
                if len(dii_list) == len(old_list):
                    i = 0
                    #for i in range(dii_list):



                # i=0
                # for sug in old_list:
                #     if sug not in dii_list:
                #         diff_str += '\t' + sug
                #         i+=1
                # if i==0:
                #     logger.error(diff_str + 'Same')
                # else:
                #     logger.error(diff_str)
            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
