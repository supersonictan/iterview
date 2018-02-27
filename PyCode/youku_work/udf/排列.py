# -*- coding=utf-8 -*-
#! /usr/bin/env python
import re



import itertools


def evaluate2( splitor):
    if splitor is None or splitor == "":
        return ''
    res = ['国语版', '电影版', '电影完整版', '下载', '电影完整版下载', '全集免费版下载', '在线全集', '高清全集']
    return splitor.join(res)

def evaluate(key):
    isSeriesMatch = False
    reg_series = [".*完整版电影.*", ".*不是预告片.*",".*可观看.*",".*可看$",".*全是集.*",".*红海行动3.*",".*电视剧全集.*",".*[0-9]{2}$"]
    for reg in reg_series:
        re_res = re.search(reg, key)
        if re_res is not None:
            isSeriesMatch = True
            break
    if not isSeriesMatch:
        0
    else:
        1

if __name__ == '__main__':
    print evaluate(',')