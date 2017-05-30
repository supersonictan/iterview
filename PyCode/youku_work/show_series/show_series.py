#!/usr/bin/python
# -*- coding=utf-8-*-
from Logger import *

logger = Logger(logFileName='series.log', logger="feature_score").getlog()

"""
思路：
1. 自动发现新系列
2. 给未标注系列的show补充系列id
    a.必须showname、alias、包含系列名
    b.节目chnel_id一致

实现：
1.求出已存有series的show的类型属性

"""


series_dic = {} #series_id------series_name
series_name_list = []
series_chnnel_dic = {}  #seriesid----chnnelid

def read_series():
    with open('/Users/tanzhen/Documents/software/odps/bin/series_id_name', 'r') as f:
        for line in f.xreadlines():
            line = line.strip().split('\t')
            series_dic[line[0]] = line[1]
            series_name_list.append(line[1])

    series_name_list.sort(key=lambda x:len(x), reverse=True)



#检查是否某个series对应的chnnel都是固定的---fail,焦点访谈资讯和综艺
def check_series_chnnel():
    global series_dic
    print len(series_dic)
    with open('/Users/tanzhen/Documents/software/odps/bin/series_base', 'r') as f:
        for line in f.xreadlines():
            line = line.strip()
            field = line.split('\t')
            show_id = field[0]
            show_name = field[1]
            series_id = field[5]
            chnnel_id = field[3]

            if series_id == '0':
                continue

            if series_id in series_chnnel_dic:
                old_chnnel_id = series_chnnel_dic[series_id]
                if old_chnnel_id != chnnel_id:
                    #print series_dic[series_id] + '\told_chnnel:' + old_chnnel_id + '\tnew:' + chnnel_id
                    pass
            else:
                series_chnnel_dic[series_id] = chnnel_id



def tag_new_series():
    show_list = []
    with open('/Users/tanzhen/Documents/software/odps/bin/show_series', 'r') as f:
        for line in f.xreadlines():
            line = line.strip()
            show_list.append(line)


    i = 0
    for id, name in series_dic.items():
        name = str(name).strip()
        series_str = '系列名:' + name + '\n'

        for line in show_list:
            line = line.strip()
            field = line.split('\t')
            show_id = field[0]
            show_name = field[1].strip()
            series_name = str(field[2]).strip()

            #if len(name) >= 3 and (name in show_name):
            if len(name.decode('utf-8'))>=3 and (name in show_name):
                series_str += '\t' + show_name + '|' + show_id
                if name != series_name:
                    series_str += '\tnew'
                series_str += '\n'
        #print name + '---' + show_name
        logger.info(series_str)
        i += 1
        print i


def get_series_num():
    pass




if __name__ == '__main__':
    read_series()
    check_series_chnnel()
    tag_new_series()