# -*- coding: utf-8 -*-

import re
import json,random
from collections import deque

import sys
import urllib
import urllib2
import traceback


reg = re.compile("((第)*(一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9)+(季|部|集|章|届|期|弹|卷|场|番|轮|册|回合|回))|(\\d+$)|(^\\d+)|(全集|大全|吻戏|床戏|大结局)")


def evaluate(query):
    base_url_list = ['https://soku-qp-data.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&q=', 'https://soku-qp-pre01.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&q=']
    num = 5
    result_dic = {}
    has_parse_old = False
    has_parse_merge = False
    has_parse_crf = False

    while num >= 0:
        baseurl = random.choice(base_url_list)
        print(baseurl)

        data = ""
        try:
            url = baseurl + urllib.quote(query.decode('utf-8').encode('utf-8'))
            data = urllib2.urlopen(url, data=None, timeout=1).read()
            data = data.decode('utf8')
            jsonObj = json.loads(data)

            module_list = jsonObj['conf']['result']['module']

            for each_module in module_list:
                if each_module['name'] == 'query_tagging':
                    old_qt_result = each_module['p']
                    has_parse_old = True
                    result_dic['old'] = json.dumps(old_qt_result).encode('utf8')
                elif each_module['name'] == 'qt_crf_debug':
                    crf_qt_result = each_module['p']
                    has_parse_crf = True
                    result_dic['crf'] = json.dumps(crf_qt_result).encode('utf8')
                elif each_module['name'] == 'query_tagging_recursion':
                    merge_qt_result = each_module['p']
                    has_parse_merge = True
                    result_dic['merge'] = json.dumps(merge_qt_result).encode('utf8')

                if has_parse_old and has_parse_merge and has_parse_crf:
                    break
        except Exception, e:
            print e

        if has_parse_old and has_parse_merge and has_parse_crf:
            return result_dic
        num -= 1


blank_tail_reg = re.compile(r'\s(\d{1,2}月\d{1,2}日|\S+(篇|版)|上集|下集|一集|二集|三集|四集|五集|上|下|大结局|全集|精彩视频|ova新|映画|短视频|直播视频|新番|讲座|儿歌|教程|电影|电视剧|番外|系列片|北京站|上海站|广州站|下部|大结局|中班|大班|小班|微电影|大电影|丁媛媛|丰胜|付琼|何萍|倪娜|周丽娜|刘丽琴|刘红英|匡雅楠|吴文涛|周伟|周傲|周文华|胡姗|胡珊|周秀君|姚利霞|姚捷|孙小玲|孙金芳|孙雯雯|庄四化|张梅|张琼|张齐宇|余德春|操娜|文慧芳|方卫华|易红辉|童玲|曾慧霞|朱丽华|朱全华|李洁|李红梅|李艳|李霞|杨娜|杨银梅|汪丽芳|汪学军|汪春芳|沈园|王学兵|王小平|王小敏|王洁|王琛|王琴|王瑜芳|王秀珞|王绪珍|申梦香|秦娴|童爱武|管小玲|綦琴|胡晓晏|董少华|谢琰|谭耀华|贾秋菊|赵千山|赵正良|邱晓颖|陈奥林|陈琼|陈瑜|陈秀梅|龙婷|陈芳|陶小华|雷佳丽|黄梅|王小彬|黄浩|汤瑜)$')

split_maohao_reg1 = re.compile(u'([0-9\u4e00-\u9fa5]{4,})(：)([0-9\u4e00-\u9fa5]{4,})')
split_maohao_reg2 = re.compile(u'([0-9\u4e00-\u9fa5]{4,})(:)([0-9\u4e00-\u9fa5]{4,})')
split_zhi_reg2 = re.compile(u'([0-9\u4e00-\u9fa5]{4,})(之)([0-9\u4e00-\u9fa5]{4,})')
new_split_reg_list = [split_maohao_reg1, split_maohao_reg2, split_zhi_reg2]

cut_tail_num = re.compile(r'(.*)(\d+)$')

if __name__ == '__main__':

    text = '蜘蛛侠2asdf'
    match = re.search(cut_tail_num, text)
    if match:
        print match.group(1)
        print match.group(2)

    text = u'国家地理之十万火急：丛林救援'
    part1 = ''
    part2 = ''

    idx = 0
    min_idx = 100
    if u'：' in text:
        min_idx = text.index(u'：')
        idx = 0

    if u':' in text:
        idx_tmp = text.index(u':')
        if idx_tmp < min_idx:
            min_idx = idx_tmp
            idx = 1

    if u'之' in text:
        idx_tmp = text.index(u'之')
        if idx_tmp < min_idx:
            min_idx = idx_tmp
            idx = 2

    print(idx)
    find_reg = new_split_reg_list[idx]

    match = re.search(find_reg, text)
    if match:
        print match.group(1) + "---" + match.group(3)

    # dic = evaluate('第22条婚规2部')
    # print dic.get('old', '')