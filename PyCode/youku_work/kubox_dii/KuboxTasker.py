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

                a_url = 'https://soku-qp-pre01.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&q=' + query + '&is_qt_ab=1'
                qp_json_a = self.__getQpJson(a_url)
                a_dic = self.__parse_qp_json(qp_json_a, query)

                b_url = 'https://soku-qp-pre01.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&q=' + query
                qp_json_b = self.__getQpJson(b_url)
                b_dic = self.__parse_qp_json(qp_json_b, query)

                # 比较 diff
                is_same = cmp(a_dic, b_dic)
                if is_same != 0:
                    a_result = ''
                    for key in a_dic.keys():
                        a_tmp = "%s--->%s" % (key, a_dic[key])
                        if a_result != "":
                            a_result += "    "
                        a_result += a_tmp

                    b_result = ''
                    for key in b_dic.keys():
                        b_tmp = "%s--->%s" % (key, b_dic[key])
                        if b_result != "":
                            b_result += "    "
                        b_result += b_tmp
                    logger.error('%s\tA[%s]\tB[%s]' % (query, a_result, b_result))



                    # else:
                    #     has_diff = False
                    #     logger.error(term + "-->" + a_dic[term])


                # dii_list = self.__get_dii_sug(qp_json_a, query)
                # res_str = ''
                # for dii_s  in dii_list:
                #     res_str += dii_s + '\t'
                # logger.error(res_str)

                # old_url='http://tip.soku.com/searches/ykapp/kubox/v4/by_keyword.json?query=' + query + '&site=55'
            except Exception, e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
