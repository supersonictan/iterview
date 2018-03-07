# -*- coding=utf-8 -*-
#! /usr/bin/env python
import re

reg_list = [
        '[^0-9]+[0-9]{1,2}集(完整|免费|在线|视频|高清)'
    ]

def evaluate( key):
    for reg in reg_list:
        re_res = re.search(reg, key)
        if re_res is not None:
            print('match')
            return 1
    print(key)
    return 0

if __name__ == '__main__':
    evaluate('微微一笑很倾城第22集高清')
    # with open('/Users/tanzhen/Desktop/code/odps/bin/yellow_query_all','r') as f:
    #     for line in f:
