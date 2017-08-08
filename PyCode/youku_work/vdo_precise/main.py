#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Tasker import *
from Logger import *
import time
import Global
#http://www.cnblogs.com/pastgift/p/3985032.html

reload(sys)
sys.setdefaultencoding('utf-8')


logger = Logger(logFileName='main.log', logger="main").getlog()
def read_query_file(queryFilePath):
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                Global.query_queue.put(line.strip(), block=False)
            except Exception,e:
                logger.error('Queue put Exception, query:%s', line.strip())



def __getImergerJson(url):

    json = None
    try:
        session = requests.session()
        session.mount('http://', HTTPAdapter(max_retries=3))
        res = session.get(url)
        json = res.json()
        #print json
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


def __parseJsonData(json, cur_query):
    sp_data = json['sp']
    #print sp_data

    if sp_data != None:
        youku_data = sp_data['youku']
        if youku_data != None:
            auctions_list = youku_data['auctions']
            count = 0
            for auction_item in auctions_list:
                sort_id = auction_item['auction_label']
                if sort_id == "32":
                    count += 1
            logger.error(cur_query + '\t' + str(count))


        else:
            logger.error(cur_query + '\t' + 'youku data error')
    else:
        logger.error(cur_query + '\t' + 'sp_data error')



if __name__ == '__main__':
    st = time.clock()

    read_query_file('query')
    query_num = Global.query_queue.qsize()
    logger.debug(query_num)

    thread_list = []
    for i in range(20):
        thread_list.append(Tasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    # while True:
    #     try:
    #         cur_query = Global.query_queue.get(block=True, timeout=5)
    #         # cur_query = '火星情报局'
    #         url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?cmd=1&keyword=' + str(cur_query)
    #         #print url
    #
    #         jsonRes = __getImergerJson(url)
    #         __parseJsonData(jsonRes, cur_query)
    #
    #         # 显示第几个
    #         Global.lock_curId.acquire()
    #         Global.cur_id += 1
    #         tmpId = Global.cur_id
    #         Global.lock_curId.release()
    #         logger.debug('Finished ' + str(tmpId))
    #     except Exception, e:
    #         logger.debug('Thread:' + repr(e))
    #         break

