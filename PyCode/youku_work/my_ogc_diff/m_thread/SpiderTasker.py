#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Logger import *
import copy
import GlobalVar
import time
import ogc_diff_mThread
from requests.adapters import HTTPAdapter
from ECBResult import *
reload(sys)
sys.setdefaultencoding('utf-8')

#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()
glb_showid_list = []


class DiffTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
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

    def __parseJsonToObjList(self, json, query):
        logger.debug('Call __parseJsonToObjList query:' + query)
        global glb_showid_list
        result_obj_dic = {}
        try:
            ecbData = json['ecb']
            youkuEcbData = ecbData['youku_ecb']
            auctionData = youkuEcbData['auctions']

            for auctionShow in auctionData:
                showId = str(auctionShow['show_id'])
                match_degree = auctionShow['match_degree']
                showObj = ECBResult(showId=showId, matchDegree=match_degree)
                glb_showid_list.append(showId)
                #result_obj_dic.append(showObj)
                result_obj_dic[showId] = showObj
        except Exception,e:
            logger.error('Exception when parse json, query:' + query + ' e:' + str(e))

        return result_obj_dic


    def run(self):

        while True:
            try:
                query = GlobalVar.queryQueue.get(block=False, timeout=10)
                logger.debug('query:'+query)
                off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&cmd=1&ecb_sp_ip=11.173.213.132:2090&qaFlow=1&keyword=' + query
                online_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&ecb_sp_ip=11.173.227.22:2090&cmd=1&qaFlow=1&keyword=' + query

                #通过Http获取imerger的json结果
                off_json = self.__getImergerJson(off_url)
                on_json = self.__getImergerJson(online_url)
                logger.debug('Query:%s Finished __getImergerJson', query)

                #解析json结果，封装为对象和showid列表
                off_resObj_dic = self.__parseJsonToObjList(off_json, query)
                off_showids_list = copy.deepcopy(glb_showid_list) #需要深拷贝
                on_resObj_dic = self.__parseJsonToObjList(on_json, query)
                on_showids_list = glb_showid_list

                #对showid取并集
                #on_more = on_showids_list - off_showids_list
                #off_more = off_showids_list - on_showids_list
                on_more = set(on_showids_list) - set(off_showids_list)
                off_more = set(off_showids_list) - set(on_showids_list)

                #打印log
                log_str = str(query) + '[' + str(len(on_showids_list)) + ':' + str(len(off_showids_list)) + ']'
                if (len(on_more) != 0 and len(off_more) != 0):
                    on_more_str = ''
                    off_more_str = ''
                    for i in on_more:
                        if on_more_str != '':
                            on_more_str += ';'
                        on_more_str += '(' + str(i) + '/' + str(GlobalVar.showIdNameDic[i]) + '/' + str(on_resObj_dic[i].matchDegree) + ')'

                    for i in off_more:
                        if off_more_str != '':
                            off_more_str += ';'
                        off_more_str += '(' + str(i) + '/' + str(GlobalVar.showIdNameDic[i]) + '/' + str(off_resObj_dic[i].matchDegree) + ')'

                    logger.info(log_str + '\tonMore:[' + on_more_str + ']\toffMore:[' + off_more_str + ']')

                elif len(on_more) != 0:
                    #diff_num += 1
                    on_more_str = ''
                    for i in on_more:
                        if on_more_str != '':
                            on_more_str += ';'
                        on_more_str += '(' + str(i) + '/' + str(GlobalVar.showIdNameDic[i]) + '/' + on_resObj_dic[i].matchDegree + ')'

                    logger.info(log_str + "\tonMore:[" + on_more_str + ']')

                elif len(off_more) != 0:
                    off_more_str = ''
                    for i in off_more:
                        if off_more_str != '':
                            off_more_str += ';'
                        off_more_str += '(' + str(i) + '/' + str(GlobalVar.showIdNameDic[i]) + '/' + off_resObj_dic[i].matchDegree + ')'
                    logger.info(log_str + '\toffMore:[' + off_more_str + ']')

                else:
                    # print log_str + '\tSame'
                    logger.debug(log_str + '\t' + 'Same')

            except Exception,e:
                logger.debug('Thread:' + self.threadName + ' Exception! e:' + str(e))
                break

