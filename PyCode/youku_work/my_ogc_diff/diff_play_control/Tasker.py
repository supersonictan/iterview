#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Logger import *
import copy
import Global
from requests.adapters import HTTPAdapter
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='diff.log', logger="tasker").getlog()

class Tasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def __getImergerJson(self, url, params):
        json = None
        try:
            session = requests.session()
            session.mount('http://', HTTPAdapter(max_retries=3))
            res = session.get(url, params=params)
            json = res.json()
            # retry
            i = 0
            while len(res.content) == 0 and i < 2:
                res = session.get(url, params=params)
                if len(res.content) > 0:
                    json = res.json()
                i += 1
            return json
        except Exception, e:
            logger.error('Http request exception, query:' + params['keyword'] + ' e:' + str(e))
        return json


    def __get_showids(self, json, query):
        showIds = []
        try:
            ecb_data = json['ecb']
            ecb_merge_arr = ecb_data['ecbMergeArray']

            for entity in ecb_merge_arr:
                #是否有节目大词
                if entity.has_key('shows'):
                    wide_query_arr = entity['shows']
                    for wide in wide_query_arr:
                        show_id = str(wide['programmeId'])
                        showIds.append(show_id)
                    continue

                show_id = str(entity['programmeId'])
                showIds.append(show_id)
        except Exception,e:
            logger.error('parse json exception, query:' + query + ", e:" + str(e))
        return showIds


    def run(self):
        while True:
            try:
                query = Global.query_queue.get(block=True, timeout=10)

                #拼装url
                on_params = {'rankFlow': Global.on_expid, 'isFilter': '16', 'cmd': '1', 'ecb_sp_ip':Global.on_ip, 'qaFlow':Global.on_qa, 'nocache': '1', 'keyword':query}
                off_params = {'rankFlow': Global.off_expid, 'isFilter': '16', 'cmd': '1', 'ecb_sp_ip':Global.off_ip, 'qaFlow':Global.off_qa, 'nocache': '1', 'keyword':query}

                off_json = self.__getImergerJson(Global.off_url, off_params)
                on_json = self.__getImergerJson(Global.on_url, on_params)

                off_showids_list = self.__get_showids(off_json, query)
                on_showids_list = self.__get_showids(on_json, query)

                on_more = set(on_showids_list) - set(off_showids_list)
                off_more = set(off_showids_list) - set(on_showids_list)

                # 打印log
                log_str = str(query) + '[' + str(len(on_showids_list)) + ':' + str(len(off_showids_list)) + ']'

                if (len(on_more) != 0 and len(off_more) != 0):
                    on_more_str = ''
                    off_more_str = ''
                    for i in on_more:
                        i = str(i)
                        if on_more_str != '':
                            on_more_str += '; '
                        on_more_str += '' + str(i) + '|' + str(Global.showname_dic[i]) + ''

                    for i in off_more:
                        i = str(i)
                        if off_more_str != '':
                            off_more_str += '; '
                        off_more_str += '' + str(i) + '|' + str(Global.showname_dic[i]) + ''

                    logger.info(log_str + '\tonMore:[' + on_more_str + ']\toffMore:[' + off_more_str + ']')

                elif len(on_more) != 0:
                    # diff_num += 1
                    on_more_str = ''
                    for i in on_more:
                        if on_more_str != '':
                            on_more_str += '; '
                        on_more_str += str(i) + '|' + str(Global.showname_dic[i])

                    logger.info(log_str + "\tonMore:[" + on_more_str + ']')

                elif len(off_more) != 0:
                    off_more_str = ''
                    for i in off_more:
                        if off_more_str != '':
                            off_more_str += '; '
                        off_more_str += '' + str(i) + '|' + str(Global.showname_dic[i]) + ''
                    logger.info(log_str + '\toffMore:[' + off_more_str + ']')

                else:
                    # print log_str + '\tSame'
                    logger.debug(log_str + '\t' + 'Same')

            except Exception, e:
                logger.debug('Thread:' + self.threadName + " Finished. e:" + str(e))
                break;