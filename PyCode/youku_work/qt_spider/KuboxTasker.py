#!/usr/bin/python
# -*- coding=utf-8-*-
from collections import OrderedDict
import requests,random
import Queue
import sys
import json
import threading

import time

from Logger import *
import copy
import Global
import re
from urllib import unquote
import urllib2
from requests.adapters import HTTPAdapter
import urllib
reload(sys)

sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='qt_diff.log', logger="tasker").getlog()

class KuboxTasker(threading.Thread):

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.threadName = threadName

    def get_http_data(self, query, cluster):
        a_url_list = [
            'https://soku-qp-cover01.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
            'https://soku-qp-cover02.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
            'https://soku-qp-cover03.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
            'https://soku-qp-cover04.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=',
            'https://soku-qp-cover05.proxy.taobao.org/qp?s=ykapp_bts&utdid=0&debug_qt_crf=1&old_qt_debug=1&q=']

        b_url_list = [
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
        has_parse_crf = False

        while num >= 0:
            a_url = []
            if cluster == 'cover':
                a_url = random.choice(a_url_list)
            else:
                a_url = random.choice(b_url_list)

            data = ""
            try:
                url = a_url + urllib.quote(query.decode('utf-8').encode('utf-8'))
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
                    elif each_module['name'] == 'qt_crf_debug' and not has_parse_crf:
                        crf_qt_result = each_module['p']['seg_list_sub']
                        tmp = json.dumps(crf_qt_result, ensure_ascii=False).encode('utf8')
                        if tmp:
                            has_parse_crf = True
                            result_dic['crf'] = tmp
                    elif each_module['name'] == 'query_tagging_recursion' and not has_parse_merge:
                        merge_qt_result = each_module['p']
                        tmp = json.dumps(merge_qt_result, ensure_ascii=False).encode('utf8')
                        if tmp:
                            has_parse_merge = True
                            result_dic['merge'] = tmp
                    if has_parse_old and has_parse_merge and has_parse_crf:
                        break
            except Exception, e:
                print e

            if has_parse_old and has_parse_merge and has_parse_crf and len(result_dic) == 3:
                return result_dic
            num -= 1
        return result_dic

    def parse_qt_json(self, json_str, type):
        result_dic = {}
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
        elif type == 'crf':
            crf_data = json_str.decode('utf8')
            crf_obj = json.loads(crf_data)
            for item in crf_obj:
                word = item['word'].encode('utf8')
                label = item['label'].encode('utf8')

                if label in result_dic:
                    result_dic[label] += '_' + word
                else:
                    result_dic[label] = word

        return result_dic

    def run(self):
        while True:
            try:

                Global.lock_curId.acquire()
                Global.cur_id += 1
                tmpId = Global.cur_id
                Global.lock_curId.release()

                if tmpId % 500 == 0:
                    print(tmpId)

                line = Global.query_queue.get(block=True, timeout=5)
                seg = line.split('\t')

                # if len(seg) == 2:
                query = seg[0]
                # query = urllib.urlencode(q)
                pv = int(seg[1])
                Global.lock_pv.acquire()
                Global.total_pv += pv
                Global.lock_pv.release()

                compare_label = ['PERSON', 'SHOW']
                try:
                    cover_dic = self.get_http_data(query, 'cover')
                    cover_merge_dic = self.parse_qt_json(cover_dic['merge'], 'merge')
                    cover_crf_dic = self.parse_qt_json(cover_dic['crf'], 'crf')

                    data_dic = self.get_http_data(query, 'data')
                    data_merge_dic = self.parse_qt_json(data_dic['merge'], 'merge')
                    data_crf_dic = self.parse_qt_json(data_dic['crf'], 'crf')

                    has_diff = False
                    for label in compare_label:
                        cover_crf_data = cover_crf_dic.get(label, '')
                        data_crf_data = data_crf_dic.get(label, '')
                        cover_merge_data = cover_merge_dic.get(label, '')
                        data_merge_data = data_merge_dic.get(label, '')

                        if cover_crf_data:
                            list = cover_crf_data.split("_")
                            list.sort()
                            cover_crf_data = '_'.join(list)

                        if data_crf_data:
                            list = data_crf_data.split("_")
                            list.sort()
                            data_crf_data = '_'.join(list)

                        if cover_merge_data:
                            list = cover_merge_data.split("_")
                            list.sort()
                            cover_merge_data = '_'.join(list)

                        if data_merge_data:
                            list = data_merge_data.split("_")
                            list.sort()
                            data_merge_data = '_'.join(list)


                        if cover_merge_data != data_merge_data:
                            has_diff = True

                        if cover_crf_data or data_crf_data or cover_merge_data or data_merge_data:
                            logger.error('%s\t%s\t%s\t%s\t%s\t%s\t%s', query, pv, cover_crf_data, data_crf_data, cover_merge_data, data_merge_data, label)

                    # update loss
                    if has_diff:
                        Global.lock_losspv.acquire()
                        Global.loss_pv += pv
                        Global.lock_losspv.release()

                except Exception, e:
                    print "Exception: " + query + ", Cause:" + str(e)

            except Exception, e:
                logger.error('Thread:' + str(self.threadName) + " Finished. e:" + repr(e))
                break
