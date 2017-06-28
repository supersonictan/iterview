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




#final score
charge_show_reg = "YoukuOGCChargeShowFeatureExtractor::calScore\+end.*?\)"
time_reg = 'YoukuECBTimeDecayFeatureExtractor::calScore.*end.*?\)'
new_relan_reg = 'YoukuShowNewRelevanceFeatureExtractor::calScore.*end.*?\)'
vv_reg = 'YoukuECBShowVVFeatureExtractor::calScore.*end.*?\)'
exclusive_reg = 'YoukuECBExclusiveFeatureExtractor::calScore.*end.*?\)'
category_reg = 'YoukuCategoryRatioFeatureExtractor::calScore.*end.*?\)'
satisfaction_reg = 'YoukuSatisfactionFeatureExtractor::calScore.*end.*?\)'
ctr_reg = 'YoukuQueryCtrPredFeatureExtractor::calScore.*end.*return.*?\)'
quality_reg = 'YoukuQualityFeatureExtractor::calScore.*end.*?\)' #YoukuQualityFeatureExtractor::calScore end -> return 0.040000 YoukuECBFakeFeatureExtractor::calScore begin()
all_hit_reg = 'YoukuShowAllHitFeatureExtractor.*calScore.*end.*\(return.*?\)'

charge_show_w = 3.0
time_w = 50.0
newRelevance_w = 3.0
vv_w = 10.0
exclusive_w = 30.0
category_w = 50.0
satisfaction_w = 10.0
ctr_w = 20.0
quality_w = 5.0
allHit_w = 20.0

reg_dic = OrderedDict({})
cur_query=''

class FeatureTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def __fillRegDic(self):
        global reg_dic
        reg_dic[charge_show_reg] = charge_show_w
        reg_dic[time_reg] = time_w
        reg_dic[new_relan_reg] = newRelevance_w
        reg_dic[vv_reg] = vv_w
        reg_dic[exclusive_reg] = exclusive_w
        reg_dic[category_reg] = category_w
        reg_dic[satisfaction_reg] = satisfaction_w
        reg_dic[ctr_reg] = ctr_w
        reg_dic[quality_reg] = quality_w
        reg_dic[all_hit_reg] = allHit_w

    def __getImergerJson(self,url):
        json = None
        try:
            session = requests.session()
            session.mount('http://', HTTPAdapter(max_retries=3))
            res = session.get(url)
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
            logger.error('Http request exception, query:' + ' e:' + str(e))
        return json

    def __parseJsonData(self, json):
        ecb_data = json['ecb']  #json最外层
        youku_ecb = ecb_data['youku_ecb']
        auctions = youku_ecb['auctions']

        for docItem in auctions:
            doctrace = str(unquote(docItem['doctrace']))
            #logger.error(doctrace)
            doc_show_id = docItem['show_id']
            self.__parseAndWriteFeatureScore(doctrace, doc_show_id)

    def __parseAndWriteFeatureScore(self, doctrace, doc_show_id):
        feature_vector = cur_query.strip() + '\t' + str(doc_show_id)
        for k,v in reg_dic.items(): #遍历特征
            #logger.error(k)
            #logger.error(doctrace)
            score = 0.0
            line = k
            reg_res = re.search(k, doctrace)
            try:
                if reg_res != None:
                    line = reg_res.group().strip()
                    field = line.split('return+')
                    score = float(field[1].strip().replace(')', ''))
                    score *= float(v)
            except Exception, e:
                pass
            feature_vector += '\t' + str(score)
            #logger.error('DEBUG:' + line + '\t' + str(score))
        logger.error(feature_vector)

    def run(self):
        while True:
            try:
                global  cur_query
                cur_query = Global.query_queue.get(block=True, timeout=5)
                #cur_query = '火星情报局'
                self.__fillRegDic()
                url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=110&isFilter=16&cmd=1&ecb_sp_ip=11.173.227.22:2090&keyword='+ cur_query

                jsonRes = self.__getImergerJson(url)
                self.__parseJsonData(jsonRes)

                # 显示第几个
                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()
                logger.debug('Finished ' + str(tmpId))
            except Exception,e:
                logger.debug('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break