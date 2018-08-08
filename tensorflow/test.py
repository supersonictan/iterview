#coding:utf-8
import sys
import re,json
import types,datetime,math


patStr=u'(第)([一二三四五六七八九十百千万零]+)([季集套部届期章节课级场讲个关轮局话题站盘番]|乐章|单元)'
pat = re.compile(patStr)




useless_reg_str1 = r'(正片|中文版|tv版|DVD版|TV版|dvd版|会员|删版|全集|免费|全是集|可观看|在线|不是预告片|最新一期|完整版|下载|电视剧版|电影版|国语版|粤语版|未删版|丶|中文版|微信|抖音|电影天堂|腾讯|爱奇艺|搜狐|土豆|高清|蓝光版|标清|1080|720)'
useless_reg_str2 = r"(一|二|三|四|五|六|七|八|九|十|0|1|2|3|4|5|6|7|8|9)+(集)"
useless_reg_str3 = r"第(一|二|三|四|五|六|七|八|九|十|0|1|2|3|4|5|6|7|8|9)+(季|集|部|期|章)$"
useless_reg_str4 = r"\d{6,}"
useless_reg_str5 = r'(红海行动3|彳微微一笑)'
useless_reg_str6 = r'(可看)$'




useless_pat_1 = re.compile(useless_reg_str1)
useless_pat_2 = re.compile(useless_reg_str2)
useless_pat_3 = re.compile(useless_reg_str3)
useless_pat_4 = re.compile(useless_reg_str4)
useless_pat_5 = re.compile(useless_reg_str5)
useless_pat_6 = re.compile(useless_reg_str6)

useless_reg_list = [useless_pat_1, useless_pat_2, useless_pat_3, useless_pat_4, useless_pat_5, useless_pat_6]





if __name__ == '__main__':
    ss = '[{"type": "location", "pos": [38], "entity": "江苏省"}, {"type": "person", "pos": [22], "entity": "朱傲雪"}]'
    obj = json.loads(ss)
    for item in obj:
        print(item['type'])


