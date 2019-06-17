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
    u"节目": "SHOW",
u"长剧名": "LONG_SHOW",
u"子节目": "SUB_SHOW",
u"节目分类": "TYPE",
u"节目子分类": "VTYPE",
u"节目版本": "VERSION",
u"影剧综活动/赛事/奖项": "SHOW_EVENT",
u"节目类型": "GENRE",
u"歌曲/专辑": "MUSIC_SONG",
u"舞种": "MUSIC_DANCE",
u"音乐分类": "MUSIC_GENRE",
u"乐器": "MUSIC_INSTRUMENT",
u"音乐类演唱会/赛事/活动/奖项": "MUSIC_EVENT",
u"音乐其他": "MUSIC",
u"曲艺名称": "FOLKART_SHOW",
u"曲艺分类": "FOLKART_GENRE",
u"曲艺类活动/赛事/奖项": "FOLKART_EVENT",
u"曲艺其他": "FOLKART",
u"比赛项目": "SPORT_GENRE",
u"竞技团体": "SPORT_TEAM",
u"体育类赛事/活动/奖项": "SPORT_EVENT",
u"体育其他": "SPORT",
u"游戏名": "GAME_NAME",
u"播放平台":"PLAYSTATION",
u"游戏主播": "GAME_HOST",
u"游戏赛事": "GAME_EVENT",
u"游戏战队": "GAME_TEAM",
u"游戏其他": "GAME",
u"人名": "PERSON",
u"代号/昵称": "CODE_NAME",
u"性别": "SEX",
u"职业": "OCCUPATION",
u"参加动作": "ATTEND",
u"出演动作": "ACT",
u"导演动作": "DIRECT",
u"关系": "REL",
u"自频道": "ZPD",
u"要素": "FACT",
u"角色名": "ROLE",
u"比赛阶段":"SPORT_STAGE",
u"地名": "LOC",
u"机构名": "ORG",
u"电视台": "PLAYSTATION",
u"语言": "LANG",
u"字幕": "CAPTION",
u"付费状况": "PURCHASE",
u"职业": "OCCUPATION",
u"性别": "SEX",
u"评价分数": "SCORE",
u"时间": "TIME",
u"集序列号": "EPISODE",
u"部序列号": "SEASON",
u"排序": "SORT",
u"画面": "GRAPHIC",
u"聚合": "AGGREGATE",
u"数字": "NUM",
u"否定": "NOT",
u"教程教学": "COURSE",
u"播出方式": "BROADCAST",
u'other':"OTHER",
u'其他':"OTHER",
u'游戏other':"GAME",
u"出生年代":"BIRTHYEAR",
u"分辨率":"bitrate"
}



if __name__ == '__main__':
    count = 0
    res = []
    with open('/Users/tanzhen/Desktop/code/odps/bin/qt_corpus_5th', 'r') as f:
        for text in f:
            text = text.decode('utf8')
            seg = text.split('\t')

            query = seg[0]
            content = seg[1]

            if content == '':
                continue

            jsonObj = json.loads(content)
            if len(jsonObj) != 2:
                continue

            jsonList = jsonObj[1]

            if len(jsonList) == 0:
                continue

            count+=1

            term_list = []
            for item in jsonList:
                option = ''
                text = ''

                if 'text' in item:
                    text = item['text']
                else:
                    continue

                if 'option' in item:
                    option_candi = item['option']
                    if type(option_candi) == list:
                        option = [x for x in option_candi if x <> '']
                        if len(option) != 0:
                            option = option[0]
                        else:
                            continue
                    elif type(option) == str:
                        option = option_candi
                else:
                    continue

                map = {}
                map['word'] = text
                map['text'] = text
                if option in mapping_dict:
                    map['label'] = mapping_dict[option]
                    map['option'] = option
                else:
                    map['label'] = "OTHER"
                    map['option'] = option

                st = query.find(text)
                ed = st + len(text)
                map['start'] = st
                map['end'] = ed
                term_list.append(map)

            s = "%s\t%s\n" % (query.encode('utf8'), json.dumps(term_list, ensure_ascii=False).encode('utf8').strip())
            print(s)
            res.append(s)
            #print("%s\t%s" % (query, json.dumps(term_list, ensure_ascii=False).strip()))

    with open('/Users/tanzhen/Desktop/code/odps/bin/qt_corpus_5th_tz', 'w') as f:
        for s in res:
            f.write(s)