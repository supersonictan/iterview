#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Logger import *
import time
#http://www.cnblogs.com/pastgift/p/3985032.html
import Global
from GameTasker import *

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
    read_query_file('game_log')
    thread_list = []
    for i in range(5):
        thread_list.append(GameTasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    logger.info('All Diff Finished')
