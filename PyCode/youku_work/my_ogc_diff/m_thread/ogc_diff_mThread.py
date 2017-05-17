#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from youku_work.my_ogc_diff.Logger import *
reload(sys)
sys.setdefaultencoding('utf-8')

#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()


showIdNameDic = {}
q = Queue.Queue()


#读取文件
def readQueryFile(queryFilePath):
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                q.put(line.strip(), block=False)
            except Exception,e:
                logger.info('Queue put Exception, query:%s', line.strip())

def readShowFile(showFilePath):
    with open(showFilePath, 'r') as f:
        for line in f:
            field = line.strip().split('\t')
            showIdNameDic[field[0]] = showIdNameDic[field[1]]








if __name__ == '__main__':
    q.get(block=True, timeout=3)
    print 'Ha'
