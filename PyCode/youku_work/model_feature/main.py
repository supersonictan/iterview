#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from FeatureTasker import *
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

if __name__ == '__main__':
    st = time.clock()

    read_query_file('data/query')
    query_num = Global.query_queue.qsize()
    logger.debug(query_num)
    # read_show_file('../data/all_show_odps')

    thread_list = []
    for i in range(20):
        thread_list.append(FeatureTasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    et = time.clock()
    cost_time = (et - st) / 60
    logger.info('Cost time:' + str(cost_time))

