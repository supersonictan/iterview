#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json,re
import threading
from Logger import *
import time
#http://www.cnblogs.com/pastgift/p/3985032.html
import Global
reload(sys)
sys.setdefaultencoding('utf-8')


expoQueryReg = re.compile(r'(object_title:)(.*?)(;)')
expoPosReg = re.compile(r'(object_num:)(.*?)(;)')
expoTypeReg = re.compile(r'(search_kq:)(.*?)(;)')

onlyCN = re.compile(u'^[/<>~×《》“”"、&ⅫⅡⅢⅣⅤⅥⅦⅧⅠ·•(),，（）+=%—！!a-zA-Z0-9_\.\-\ :：\u4e00-\u9fa5]+$')

def evaluate(othertipsinfo):
    print list(othertipsinfo)


if __name__ == '__main__':
    query = '你好 中国'
    query = query.decode('utf8')
    char_list = list(query)
    new_list = [x.encode('utf8') for x in char_list if x != ' ']
    print ' '.join(new_list)





#
# 追剧特征
# 追剧模型
# 宣发剧找人
#
# trigger select