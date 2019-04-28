# -*- coding: utf-8 -*-

import re
import json
from collections import deque

import sys
import urllib
import urllib2
import traceback

class GenCrfFeature():

    def __init__(self):
        self.C2F_mapping_dict = {
            "节目":"SHOW","子节目":"SUB_SHOW","长剧名":"LONG_SHOW",
            "节目分类":"TYPE", "节目子分类":"VTYPE", "节目版本":"VERSION",
            "类型":"GENRE","部序列号":"SEASON","集序列号":"EPISODE",
            "角色":"ROLE","机构名":"ORG","影剧综活动/赛事/奖项":"SHOW_EVENT",

            "音乐":"MUSIC","歌曲/专辑":"MUSIC_SONG","舞种":"MUSIC_DANCE",
            "音乐分类":"MUSIC_GENRE","音乐类演唱会/赛事/活动/奖项":"MUSIC_EVENT","音乐other":"MUSIC",

            "曲艺名称":"FOLKART_SHOW","曲艺分类":"FOLKART_GENRE","曲艺活动/赛事/奖项":"FOLKART_EVENT","曲艺other":"FOLKART",


            "体育":"SPORT","体育赛事球队":"SPORT",
            "体育项目":"SPORT_GENRE","竞技团体":"SPORT_TEAM","比赛阶段":"SPORT_STAGE",
            "体育类赛事/活动/奖项":"SPORT_EVENT","体育other":"SPORT",

            "游戏名":"GAME_NAME","游戏主播":"GAME_HOST","游戏赛事":"GAME_EVENT",
            "游戏战队":"GAME_TEAM","游戏other":"GAME",

            "人名":"PERSON",
            "自频道":"ZPD",

            "电视台":"PLAYSTATION","播放平台":"PLAYSTATION","播出方式":"BROADCAST",
            "教程/教学":"COURSE",
            "地名":"LOC",

            "其他":"OTHER","other":"OTHER",
            "要素":"FACT","时间":"TIME",
            "年龄":"AGE","出生年代":"BIRTH",
            "分数":"SCORE","评价分数":"SCORE","数字":"NUM",
            "分辨率":"BITRATE","画面":"GRAPHIC",
            "语言":"LANG","付费状态":"PURCHASE","职业":"OCCUPATION","性别":"SEX","关系":"REL",
            "排序":"SORT",
            "出演动作":"ACT","导演动作":"DIRECT","参加动作":"ATTEND",
            "聚合":"AGGREGATE",
            "否定":"NOT"
            }

    def return_list_type(self,n):
        for item in n:
            if item!='':
                return item

    def evaluate(self, corpus_seg, marked_label):
        result = ''
        try:
            seg_list = []
            mark_list = []
            result_list = []

            seg_list = corpus_seg.split(" ")
            seg_list = [x for x in seg_list if x.strip() != '']
            mark_list = json.loads(marked_label)
            mark_list.sort(key=lambda k: (k.get('start', 0)))
            i = 0
            p = 0
            for seg in seg_list:
                subseg_list = seg.split(":")
                seg_word = subseg_list[0]
                seg_pos = subseg_list[1]
                seg_start = p
                p = p + len(seg_word)
                seg_end = p
                seg_len = len(seg_word)
                seg_label = "O"

                form = ""
                position = str(i)
                i = i + 1
                word_pos = ""

                tmp_list = mark_list[:]
                for term in tmp_list:
                    if term == {}:
                        continue
                    if type(term) != dict:
                        continue
                    word = term.get('word', '').encode('utf-8').strip()
                    label = term.get('label', 'O')
                    if label == "OTHER":
                        label = "O"
                    start = term.get('start', 0)
                    end = term.get('end', 0)
                    ret = word.find(seg_word)
                    if ret == -1:
                        continue
                    if ret == 0:
                        word_pos = "B"
                    else:
                        word_pos = "I"

                    if label == "O" or label == "":
                        seg_label = "O"
                    else:
                        seg_label = word_pos + "-" + label

                    if ret + seg_len == len(word):
                        mark_list.remove(term)
                        break
                length = str(seg_len)
                form = seg_word + ":" + seg_pos + ":" + position + ":" + length + ":" + "0" + ":" + seg_label
                result_list.append(form)

            result = " ".join(result_list)

        except :
            result = "Oops:" + corpus_seg
        return result

#('[\x{0400}-\x{04FF}]|[\x{0500}-\x{052F}]|[\x{2DE0}-\x{2DFF}]|[\x{A640}-\x{A69F}]|[\x{1C80}-\x{1C8F}]')


reg = re.compile(u'(.+)(·|-)(.+)')


is_all_num_reg = re.compile(r'^\d+$')


performer = """
[{"name":"Marc Grapey","character":["鲍勃"],"id":"29983"},{"name":"弗雷德里克·福瑞斯特","character":["Paulo Tredici"],"id":"10990","thumburl":"http://r1.ykimg.com/051300005B91E209ADA2D407D9084A60"},{"name":"Rebecca Harrell","character":["Happy Buchanan"],"id":"10988","thumburl":"http://r1.ykimg.com/051300004E1D75770000010B850BFCB2"},{"name":"Jeff Puckett","character":["格雷格"],"id":"288133"},{"name":"泰恩·黛莉","character":["Aunt Aurelia"],"id":"10989","thumburl":"http://r1.ykimg.com/051300005A017226ADBC094B7B0ED901"},{"name":"安德烈亚斯·凯特苏拉斯","character":["Giuseppe Tredici"],"id":"64607","thumburl":"http://r1.ykimg.com/051300004FA5F5489792736CE20C8958"},{"name":"Robert Breuler","character":["Franco Tredici"],"id":"63078"},{"name":"Tristan Rogers","character":["Victor Hardwick"],"id":"96364","thumburl":"http://r1.ykimg.com/0513000050E66DDE979273303209F775"}]
"""

role_reg = re.compile(r'((.+)\((.+)\))')



# Series \d{1,2}.*?No\.\s{0,1}\d{1,2} Series 26, No. 6
#

head_year_reg = re.compile('^((\d{4}/\d{4})|(\d{4}/\d{2})|(\d{4}))')

sm_musicsong_reg = re.compile('(\(.+\)|（.+）)')
sm_musicsong_jp_reg = re.compile(u'[\u0800-\u4e00\uac00-\ud7ff]{2,}')


# -:+
#沈巍(黑袍使)
if __name__ == '__main__':
    test_list = ['瑞典足球超级联赛2019','2017瑞典足球超级联赛','2010/11比利时足球甲级联赛','2006国际足联世界杯','2018/2019阿根廷足球超级联赛','2012/2013俄罗斯足球超级联赛','2010/11法国足球乙级联赛','2011/2012阿根廷足球超级联赛']
    music_list = ['向日葵的约定(CCTV音乐频道)','大海(CCTV音乐频道)','那首歌','那首歌2（xxx）','九寨姑娘(mtv)','我深深期待(《一个好爸爸》电影主题曲)','おしおき feat. だんがんアイランド']

    for show_name in music_list:
        searchObj = sm_musicsong_jp_reg.search(show_name.decode('utf8'))
        if searchObj:
            print("return empty")


        tmp_name = sm_musicsong_reg.sub('', show_name).strip()
        print(tmp_name)

    print('---------------------------------')


    for show_name in test_list:
        tmp_name = head_year_reg.sub('', show_name).strip()
        print(tmp_name)