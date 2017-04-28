#!/usr/bin/env python
# -*- coding: utf-8 -*-

common_keyword = {}
def readFile():
    with open("E:\\odps-cli\\odpscmd\\bin\\keyword0426", "r") as f:
        for line in f.xreadlines():
            list = line.split('\t')
            showid = list[0]
            show_name = list[1]
            keywords = list[2]
            keyword_list = keywords.split(',')
            for k in keyword_list:
                common_keyword.setdefault(k,0)
                common_keyword[k] += 1

readFile()
with open("common_keyword","w") as f:
    for k,v in common_keyword.iteritems():
        f.write(k + '\t' + str(v) + '\n')