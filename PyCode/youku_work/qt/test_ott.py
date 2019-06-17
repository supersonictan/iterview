# -*- coding: utf-8 -*-

import re
import json
from collections import deque

import sys
import urllib
import urllib2
import traceback


def evaluate( query):
    result = ''
    num = 5
    while num >= 0:
        try:
            baseurl = "https://beta-youku-search.youku.com/search/query?noqc=0&appScene=imerge&appCaller=ott&is_apple=0&bucketId=5&pz=30&spDataType=7&caller=0&pg=1&nocache=1&from=text&cmd=4&keyword="

            query = query.strip()
            result_list = ""

            data = ""
            try:
                url = baseurl + urllib.quote(query)
                # print url
                data = urllib2.urlopen(url, data=None, timeout=1).read()

                jsonObj = json.loads(data)
                if 'sp' not in jsonObj:
                    return ''
                jsonObj2 = jsonObj['sp']
                if 'youku' not in jsonObj2:
                    return ''

                auctions_obj = jsonObj2['youku']['auctions']
                result = json.dumps(auctions_obj)
                if result != '':
                    return result
            except Exception, e:
                print e

        except:
            pass
        num -= 1
        print(num)
    return result



def parse(content):
    if not content:
        return ''

    result_list = []
    try:
        auctions_obj = json.loads(content)
        for item in auctions_obj:
            ottid = item['ott_id']
            if ottid not in result_list:
                result_list.append(ottid)
    except Exception, e:
        print e

    print ';'.join(result_list)



if __name__ == '__main__':
    ne_dic = {
        'FOLKART_SHOW': 1,
        'GAME_EVENT': 2,
        'GAME_HOST': 3,
        'GAME_NAME': 4,
        'GAME_TEAM': 5,
        'LOC': 6,
        'LONG_SHOW': 7,
        'MUSIC_GENRE': 8,
        'MUSIC_SONG': 9,
        'ORG': 10,
        'PERSON': 11,
        'PLAYSTATION': 12,
        'ROLE': 13,
        'SHOW': 14,
        'SPORT_EVENT': 15,
        'SPORT_GENRE': 16,
        'SPORT_TEAM': 17,
        'SUB_SHOW': 18,
        'TYPE': 19,
        'VTYPE': 20
    }
    ne_str = 'SHOW;LONG_SHOW;SUB_SHOW'
    result = []

    ne_list = ne_str.split(';')
    only_show = True
    for ne in ne_list:
        if ne != 'SUB_SHOW' and ne != 'SHOW' and ne != 'LONG_SHOW':
            only_show = False

    type_count = 0

    for ne in ne_list:
        idx = str(ne_dic[ne])
        result.append(idx)
        type_count += 1

    if type_count >= 2 and not only_show:
        label_ambiguity = 1
    else:
        label_ambiguity = 0
    print ';'.join(result) + "\t" + str(label_ambiguity)
