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
import re
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

    # st = time.clock()
    #
    # read_query_file('query')
    # query_num = Global.query_queue.qsize()
    # logger.debug(query_num)
    #
    thread_list = []
    for i in range(1):
        thread_list.append(Tasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

