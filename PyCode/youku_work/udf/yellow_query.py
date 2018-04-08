# -*- coding=utf-8 -*-
#! /usr/bin/env python
import re,sys

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

def fun (word):
    char = word.decode('utf8')
    if re.search(ur"[\u4e00-\u9fa5]+", char):
        return True
    else:
        return False

def test():
    s1 = "笨蛋·测验·召唤兽 第一季"
    s1 = s1.decode('utf8')
    s1 = re.sub("[！|\!|·|,|▪|－]+".decode("utf8"), "".decode("utf8"), s1)
    print(s1.encode('utf8'))

def evaluate2(show_name, meta_keyword):
    show_name = show_name.decode('utf8')
    meta_keyword = meta_keyword.decode('utf8')
    if meta_keyword is None:
        return ''
    # meta_keyword = str(meta_keyword)
    res = ''.decode('utf8')
    idx = 10000
    if ',' not in meta_keyword:
        meta_keyword = re.sub("[！|\!|·|,|▪|－| ]+".decode("utf8"), "".decode("utf8"), meta_keyword)
        return meta_keyword.encode('utf8')

    field = meta_keyword.split(',')
    for key in field:
        find_idx = show_name.find(key)
        if find_idx < idx:
            idx = find_idx
            res = key
    # res = re.sub(ur'！|\!|·|,|▪|－', "", res)
    res = re.sub("[！|\!|·|,|▪|－| ]+".decode("utf8"), "".decode("utf8"), res)
    return res.encode('utf-8')

if __name__ == '__main__':
    #evaluate('微微一笑很倾城第22集高清')
    # with open('/Users/tanzhen/Desktop/code/odps/bin/yellow_query_all','r') as f:
    #     for line in f:
    #print fun('sfasdf 2018')
    print evaluate2('蒙德维地亚:梦之味（上）', '蒙德维地亚,梦之味')
