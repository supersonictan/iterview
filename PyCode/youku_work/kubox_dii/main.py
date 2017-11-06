#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from KuboxTasker import *
from Logger import *
import time
#http://www.cnblogs.com/pastgift/p/3985032.html
import Global
reload(sys)
sys.setdefaultencoding('utf-8')




def read_query_file(queryFilePath):
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                Global.query_queue.put(line.strip(), block=False)
            except Exception,e:
                logger.error('Queue put Exception, query:%s', line.strip())

if __name__ == '__main__':
    read_query_file('sug_log')
    thread_list = []
    for i in range(10):
        thread_list.append(KuboxTasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    logger.info('All Diff Finished')