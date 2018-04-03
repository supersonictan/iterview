#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,re,time,types,datetime,sys
import json


def yt_get_keyword2(show_name):
    reg1 = r"[^0-9]+([0-9]+)$"

    match_obj = re.search(reg1, show_name)

    print(match_obj.group(1))
    # if match_obj:
    #     text = match_obj.group(0)
    #     return text

    return None

def splitMaoHao(word):
    word = word.decode('utf-8')
    print(word)
    word = word.encode('utf-8')
    print(word)


def yt_get_keyword(show_name, meta_keyword):
    meta_keyword = str(meta_keyword)
    meta_keyword = meta_keyword.decode('utf-8')
    # list = [',', '，', ':', '：', ';', '；', '!', '！']
    # 去除数字结尾
    res = []
    field = meta_keyword.split(',')
    for i in field:
        i = re.sub(r'\b\d{1}$|\d{4}$', "", i)
        res.append(i)

    return ','.join(res)




if __name__ == '__main__':
    s = "[10020,10021,10023,20716,49161]"
    res = json.loads(s)
    for i in res:
        print(i)
    print(yt_get_keyword("恶魔咆哮3:地狱门前", '地狱s门前2,恶魔咆哮'))
    #print yt_get_keyword("第87届奥斯卡金像奖颁奖典礼第二季")