#!/usr/bin/python
# -*- coding=utf-8-*-
from collections import OrderedDict
import requests
import Queue
import sys
import json
import threading
from Logger import *
import copy
import re
from urllib import unquote
from requests.adapters import HTTPAdapter
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='query_tagging.log', logger="tasker").getlog()


#reg = re.compile(r'.*<title>(\S*)</title>.*')
reg = re.compile(u'\s+(.*)\(豆瓣\)')


if __name__ == '__main__':





    for i in range(27185558):
        a_url = 'https://movie.douban.com/subject/' + str(i)
        session = requests.session()
        session.mount('https://', HTTPAdapter(max_retries=3))
        res = session.get(a_url)
        res.encoding = 'utf-8'

        html_text = res.text
        #print(html_text)

        month_match = re.search(reg, html_text)
        if month_match:
            show_name = month_match.group(1).strip()
            print(show_name)
        else:
            print('no' + str(i))





