#!/usr/bin/python
#-*- coding=utf-8-*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import _json

a = 'qwer'


# seed = 20170101
# key = bytearray( a.encode() )
# print key
#
# length = len( key )
# nblocks = int( length / 4 )


def evaluate(jsonData):
    res = 0
    if jsonData == '{}' or jsonData == '' or jsonData == 'null' or jsonData == 'NULL':
        return str(res)

    text = json.loads(jsonData)
    if text != None and 'VIDEO' in text:
        video_content = text['VIDEO']
        if video_content != None:
            itemList_content = video_content['itemList']
            if itemList_content != None:
                for item in itemList_content:
                    if item != None and item['id'] != None and item['id'] == 175:
                        data_map = eval(item['data'])
                        index = 0
                        for k in data_map:
                            if index == 0:
                                res = k
                                break
    return str(res)


print evaluate("{}")