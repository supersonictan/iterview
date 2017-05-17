#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Logger import *
from ogc_diff_mThread import *
from requests.adapters import HTTPAdapter
from ECBResult import *
reload(sys)
sys.setdefaultencoding('utf-8')

#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()



class DiffTasker(threading.Thread):

    def __init__(self, threadName):
        self.threadName = threadName

    def __getImergerJson(self, url):
        url = str(url).strip()
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
            logger.error('Http request exception, query:' + url + ' e:' + str(e))
        return json

    def __parseJsonToECBResult(self, json, query):
        ecb_result_list = []
        try:
            ecbData = json['ecb']
            youkuEcbData = ecbData['youku_ecb']
            auctionData = youkuEcbData['auctions']

            for auctionShow in auctionData:
                showId = auctionShow['show_id']
                match_degree = auctionShow['match_degree']
                show = ECBResult(showId=showId, matchDegree=match_degree)

                ecb_result_list.append(show)
        except Exception,e:
            logger.error('Exception when parse json, query:' + query + ' e:' + str(e))

        return ecb_result_list


    def run(self):
        while True:
            try:
                query = queryQueue.get(block=True, timeout=10)
                off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&cmd=1&ecb_sp_ip=11.173.213.132:2090&qaFlow=1&keyword=' + query
                online_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&ecb_sp_ip=11.173.227.22:2090&cmd=1&qaFlow=1&keyword=' + query

                off_json = self.__getImergerJson(off_url)
                on_json = self.__getImergerJson(online_url)

                self.__parseJsonToECBResult(off_json)
                self.__parseJsonToECBResult(on_json)



            except Exception,e:
                logger.debug('Thread:' + self.threadName + ' Finish!')
                break

