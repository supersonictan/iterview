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
    i = 0
    with open(queryFilePath, 'r') as f:
        for line in f:
            try:
                Global.query_queue.put(line.strip(), block=False)
                i += 1
                if i >= 1:
                    break
            except Exception,e:
                logger.error('Queue put Exception, query:%s', line.strip())
    print((Global.query_queue.qsize()))


def cal_report(file_path):
    more_num = 0
    less_num = 0

    with open(file_path, 'r') as f:
        for line in f:
            if not line:
                continue
            seg = line.split('\t')
            if len(seg) != 2:
                continue

            num = seg[1].strip()
            if num == '1':
                more_num += 1
            elif num == '0':
                less_num += 1

    print(more_num)
    print(less_num)
    #print('more_num:%d less_num:%d'%(more_num, less_num))

if __name__ == '__main__':
    read_query_file('sug_log')
    thread_list = []
    for i in range(10):
        thread_list.append(KuboxTasker(i))

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    # time.sleep(10)
    print 'loss_pv:' + str(Global.loss_pv)
    print 'total_pv:' + str(Global.total_pv)
    logger.info('All Spider Finished')

    # cal_report('qt_flag5_test.log')
