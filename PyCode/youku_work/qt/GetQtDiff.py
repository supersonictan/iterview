# -*- coding: utf-8 -*-

import re
import json,random
from collections import deque

import sys
import urllib
import urllib2
import traceback


def get_106_diff(query):
    url_list = [
        'https://soku-qp-data01.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data02.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data03.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data04.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data05.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data06.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data07.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data08.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data09.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
        'https://soku-qp-data10.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=']

    num = 30
    result_dic = {}
    has_parse_old = False
    has_parse_merge = False

    while num >= 0:
        url = random.choice(url_list)

        data = ""
        try:
            url = url + urllib.quote(query.decode('utf-8').encode('utf-8'))
            data = urllib2.urlopen(url, data=None, timeout=60).read()
            if not data:
                continue
            data = data.decode('utf8')
            jsonObj = json.loads(data)

            module_list = jsonObj['conf']['result']['module']

            for each_module in module_list:
                if each_module['name'] == 'query_tagging' and not has_parse_old:
                    old_qt_result = each_module['p']
                    tmp = json.dumps(old_qt_result, ensure_ascii=False).encode('utf8')
                    if tmp:
                        has_parse_old = True
                        result_dic['old'] = tmp
                elif each_module['name'] == 'query_tagging_recursion' and not has_parse_merge:
                    merge_qt_result = each_module['p']
                    tmp = json.dumps(merge_qt_result, ensure_ascii=False).encode('utf8')
                    if tmp:
                        has_parse_merge = True
                        result_dic['merge'] = tmp
                if has_parse_old and has_parse_merge:
                    break
        except Exception, e:
            print e

        if has_parse_old and has_parse_merge and len(result_dic) == 2:
            return result_dic
        num -= 1
    return result_dic


def parse_106qt_json(json_str, type):
    result_dic = {}
    if json_str == '':
        return result_dic
    if type == 'merge':
        merge_data = json_str.decode('utf8')
        merge_obj = json.loads(merge_data)
        for each in merge_obj:
            if 'tag' not in each:
                print 'not in'
                continue
            tag = each['tag']
            for item in tag:
                if 'sub_tag' in item and len(item['sub_tag']) > 0:
                    for sub_item in item['sub_tag']:
                        word = sub_item['word'].encode('utf8')
                        label = sub_item['label'].encode('utf8')

                        if label in result_dic:
                            result_dic[label] += '_' + word
                        else:
                            result_dic[label] = word
                else:
                    word = item['word'].encode('utf8')
                    label = item['label'].encode('utf8')

                    if label in result_dic:
                        result_dic[label] += '_' + word
                    else:
                        result_dic[label] = word
    elif type == 'old':
        old_data = json_str.decode('utf8')
        old_obj = json.loads(old_data)
        if 'seg_list_level2' in old_obj:
            level2_list = old_obj['seg_list_level2']
            for item in level2_list:
                word = item['word'].encode('utf8')
                label = item['label'].encode('utf8')
                print word + '--->' + label

                if label in result_dic:
                    result_dic[label] += '_' + word
                else:
                    result_dic[label] = word

    return result_dic


def evaluate(query):
    result_dic = get_106_diff(query)
    merge_data = result_dic.get('merge', '')
    merge_data_dic = parse_106qt_json(merge_data, 'merge')
    print merge_data_dic
    merge_data = merge_data_dic.get('SHOW', '')

    old_data = result_dic.get('old', '')
    old_data_dic = parse_106qt_json(old_data, 'old')
    print old_data_dic
    old_data = old_data_dic.get('SHOW', '')

    # 差集
    has_diff = 0
    ret_list = list(set(merge_data.split('_')) ^ set(old_data.split('_')))
    return '_'.join(ret_list)    #     print(data_merge_data)

if __name__ == '__main__':
    print evaluate('1001夜第一季')