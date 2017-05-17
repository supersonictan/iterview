#!/usr/bin/python
# -*- coding=utf-8-*-
from Logger import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#加载Log模块
logger = Logger(logFileName='diff.log', logger="diff").getlog()

class ECBResult:

    def __init__(self, showId, showName='undefine', matchDegree='-1'):
        self.showId = showId
        self.showName = showName
        self.matchDegree = matchDegree

