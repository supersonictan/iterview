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
#http://www.cnblogs.com/pastgift/p/3985032.html
import Global
reload(sys)
sys.setdefaultencoding('utf-8')



#加载Log模块
logger = Logger(logFileName='diff.log', logger="diffb").getlog()

#读取文件
def read_query_file(queryFilePath):
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                Global.query_queue.put(line.strip(), block=False)
            except Exception,e:
                logger.error('Queue put Exception, query:%s', line.strip())

# def read_show_file(showFilePath):
#     with open(showFilePath, 'r') as f:
#         for line in f:
#             field = line.strip().split('\t')
#             Global.showname_dic[field[0]] = field[1]

if __name__ == '__main__':
    st = time.clock()

    read_query_file(Global.query_file)
    query_num = Global.query_queue.qsize()
    #read_show_file('../data/all_show_odps')

    thread_list = []
    for i in range(Global.thread_num):
        thread_list.append(Tasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    et = time.clock()
    cost_time = (et-st)/60
    diff_ratio = float(Global.diff_num) / float(query_num) * 100.0

    logger.info('All Diff Finished, diff_ratio:' + str(diff_ratio) + '%, cost:' + str(cost_time) + 'min')