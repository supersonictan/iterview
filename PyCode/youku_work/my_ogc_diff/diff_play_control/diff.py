#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from Tasker import *
from Logger import *
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

def read_show_file(showFilePath):
    with open(showFilePath, 'r') as f:
        for line in f:
            field = line.strip().split('\t')
            Global.showname_dic[field[0]] = field[1]

if __name__ == '__main__':
    read_query_file('../data/top300')
    read_show_file('../data/all_show_odps')
    t1 = Tasker('1')
    t2 = Tasker('2')
    t3 = Tasker('3')
    t4 = Tasker('4')
    t5 = Tasker('5')
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    print 'Ha'
