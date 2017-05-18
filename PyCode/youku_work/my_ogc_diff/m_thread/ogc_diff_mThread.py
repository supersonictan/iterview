#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from SpiderTasker import *
from youku_work.my_ogc_diff.Logger import *
#http://www.cnblogs.com/pastgift/p/3985032.html
import GlobalVar
reload(sys)
sys.setdefaultencoding('utf-8')

#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()


#读取文件
def readQueryFile(queryFilePath):
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                GlobalVar.queryQueue.put(line.strip(), block=False)
            except Exception,e:
                logger.info('Queue put Exception, query:%s', line.strip())

def readShowFile(showFilePath):
    with open(showFilePath, 'r') as f:
        for line in f:
            field = line.strip().split('\t')
            GlobalVar.showIdNameDic[field[0]] = field[1]







if __name__ == '__main__':

    readQueryFile('E:\\code\\public\\tmp\\iterview\\PyCode\\youku_work\\my_ogc_diff\\data\\top300')
    readShowFile('E:\\code\\public\\tmp\\iterview\\PyCode\\youku_work\\my_ogc_diff\\data\\all_show_odps')


    t1 = DiffTasker('1')
    t1.start()
    t1.join()
    print 'Ha'
