#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json
import threading
from youku_work.my_ogc_diff.Logger import *
from youku_work.my_ogc_diff.ogc_diff_mThread import *
reload(sys)
sys.setdefaultencoding('utf-8')

#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()

class DiffTasker(threading.Thread):
    def __init__(self, threadName):
        self.threadName = threadName

    def run(self):
        while True:

