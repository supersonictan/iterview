#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import datetime
reload(sys)

sys.setdefaultencoding('utf8')
import urllib

list = []
s = set('WsbIBwjQFnsDANlypmNEVhET')

if __name__ == '__main__':

    end = datetime.datetime.now()
    timestamp = '1532331174'
    start = datetime.datetime.fromtimestamp(timestamp)
    diff_day = (end - start).days
    print(diff_day+1)
    #print len("ni好")
    # for i in range(2):
    #     i+=1
    #     print(i)
    # list = [0,1,2,3,4,5,6,7,8,9]
    # length = len(list)
    # for index in range(length):
    #     if index + 2 > length:
    #         break
    #
    #     subList = list[index: index+2]
    #     print(subList)
    #     index+=1

