#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json
from Logger import *
import copy
import re
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import lxml
import MySQLdb
import Common
from Tasker import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='app.log', logger="app").getlog()




if __name__ == '__main__':

    for i in range(1, 11980):
    #for i in range(3049, 3050):
        Common.query_queue.put(str(i), block=False)

    print Common.query_queue.qsize()
    thread_list = []
    for i in range(20):
        t = Tasker(i)
        t.setDaemon(True)
        thread_list.append(t)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()
