# -*- coding: utf-8 -*-

import re
import json
from collections import deque

import sys
import urllib
import urllib2
import traceback

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

mapping_dict = {
    "节目":"SHOW","子节目":"SUB_SHOW","长剧名":"LONG_SHOW","节目分类":"TYPE", "节目子分类":"VTYPE", "节目版本":"VERSION","类型":"GENRE","部序列号":"SEASON","集序列号":"EPISODE",
    "角色":"ROLE","机构名":"ORG","影剧综活动/赛事/奖项":"SHOW_EVENT","音乐":"MUSIC","歌曲/专辑":"MUSIC_SONG","舞种":"MUSIC_DANCE","音乐分类":"MUSIC_GENRE","音乐类演唱会/赛事/活动/奖项":"MUSIC_EVENT","音乐other":"MUSIC",
    "曲艺名称":"FOLKART_SHOW","曲艺分类":"FOLKART_GENRE","曲艺活动/赛事/奖项":"FOLKART_EVENT","曲艺other":"FOLKART","体育":"SPORT","体育赛事球队":"SPORT","体育项目":"SPORT_GENRE","竞技团体":"SPORT_TEAM","比赛阶段":"SPORT_STAGE",
    "体育类赛事/活动/奖项":"SPORT_EVENT","体育other":"SPORT","游戏名":"GAME_NAME","游戏主播":"GAME_HOST","游戏赛事":"GAME_EVENT","游戏战队":"GAME_TEAM","游戏other":"GAME",
    "人名":"PERSON","自频道":"ZPD","电视台":"PLAYSTATION","播放平台":"PLAYSTATION","播出方式":"BROADCAST","教程/教学":"COURSE","地名":"LOC","其他":"OTHER","other":"OTHER",
    "要素":"FACT","时间":"TIME","年龄":"AGE","出生年代":"BIRTH","分数":"SCORE","评价分数":"SCORE","数字":"NUM","分辨率":"BITRATE","画面":"GRAPHIC",
    "语言":"LANG","付费状态":"PURCHASE","职业":"OCCUPATION","性别":"SEX","关系":"REL","排序":"SORT","出演动作":"ACT","导演动作":"DIRECT","参加动作":"ATTEND","聚合":"AGGREGATE","否定":"NOT"
}


text = """
[{"index": "0", "end": 5, "label": "TIME", "start": 0, "finger": 574609111, "word": "05年"}, {"index": "1,", "end": 11, "label": "OTHER", "start": 5, "finger": 2939188112, "word": "十大"}, {"index": "2,", "end": 17, "label": "LANG", "start": 11, "finger": 1204280811, "word": "中文"}, {"index": "3,", "end": 23, "label": "OTHER", "start": 17, "finger": 2527054841, "word": "金曲"}, {"index": "4,", "end": 32, "label": "OTHER", "start": 23, "finger": 1032392174, "word": "颁奖礼"}]
"""


if __name__ == '__main__':

    yu = 6%2
    print yu

    test = u'abc哈'
    print len(test)

    mapping_dict_reverse = dict([val, key] for key, val in mapping_dict.items())

    final_list = []
    reserve_dic = {}
    final_list.append(reserve_dic)

    jsonObj = json.loads(text)

    convert_list = []
    for item_dic in jsonObj:
        new_dic = {}
        for k,v in item_dic.items():
            new_dic[k] = v

            if k == "word":
                new_dic['text'] = v

            if k == "label":
                if v in mapping_dict_reverse:
                    reverse_v = mapping_dict_reverse[v]
                    new_dic['option'] = reverse_v.decode('utf8')

        convert_list.append(new_dic)
    final_list.append(convert_list)

    print json.dumps(final_list, ensure_ascii=False).encode('utf-8').strip()

