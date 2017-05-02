#!/usr/bin/python
# -*- coding=utf-8-*-
import ConfigParser
from optparse import OptionParser
import os
import json
#import log
import logging
from urllib import unquote
import requests
import time


# 读取urllist文件
def get_urls(url_file):
    urls = list()
    try:
        file = open(url_file, "r")
    except:
        print "open file %s fail!" % url_file
        return urls
    while True:
        line = file.readline()
        if line == "" or line == None:
            break
        urls.append(line)
    file.close()
    return urls


# 获取url的返回数据
def get_url_result(url):
    json = None
    try:
        session = requests.session()
        res = session.get(url)
        json = res.json()
        # retry
        i = 0
        while len(res.content) == 0 and i < 2:
            res = session.get(url)
            if len(res.content) > 0:
                json = res.json()
            i += 1
        return json
    except:
        print url
        print "RES-EXCEPTION!!! %s" % url
        return None
    return json


def check_status_host(online_host, offline_host, url):
    flag = True

    on_url = 'http://' + online_host + '&qaFlow=1&keyword=' + url
    off_url = 'http://' + offline_host + '&qaFlow=1&keyword=' + url
    on_json = get_url_result(on_url)
    off_json = get_url_result(off_url)
    if on_json == None or off_json == None:
        flag = False
    return flag


def write_dict(dict_name, key, val):
    if key in dict_name:
        dict_name[key].append(val)
    else:
        dict_name[key] = list()


def start(online_host, offline_host, url_file, precision, diff_fields, json_fail, more_fields, less_fields):
    urls = get_urls(url_file)
    flag = check_status_host(online_host, offline_host, urls[0])
    if flag == False:
        print "DIFF ERR!! online_host or offline_host is not ready"
        return None
    ugc_null = list()
    ##env is normal
    for url in urls:
        msg = list()
        cur_url = url.strip('\n')
        on_url = 'http://' + online_host + '&qaFlow=1&keyword=' + cur_url
        off_url = 'http://' + offline_host + '&qaFlow=1&keyword=' + cur_url
        pri_url = 'online_url=' + on_url + '    offline_url=' + off_url
        on_json = get_url_result(on_url)
        off_json = get_url_result(off_url)
        if on_json == None or off_json == None:
            msg.append('json is none,%s' % pri_url)
            json_fail.append(pri_url)
        elif on_json != off_json:
            on_fileds = on_json.keys()
            off_fileds = off_json.keys()

            for key in (set(off_fileds) & set(on_fileds)):
                on_data = on_json[key]
                off_data = off_json[key]

                if key == 'resultList':
                    if on_data != off_data:
                        on_source = dict()
                        off_source = dict()

                        for video in on_data:
                            index = on_data.index(video)
                            try:
                                doc_source = video['doc_source']
                            except:
                                print video
                                continue
                            if doc_source not in on_source:
                                on_source[doc_source] = list()
                            on_source[doc_source].append(index)
                        for video in off_data:
                            index = off_data.index(video)
                            try:
                                doc_source = video['doc_source']
                            except:
                                print video
                                continue
                            if doc_source not in off_source:
                                off_source[doc_source] = list()
                            off_source[doc_source].append(index)
                        ##diff doc_source
                        doc_s_on = on_source.keys()
                        doc_s_off = off_source.keys()
                        if len(set(doc_s_on) - set(doc_s_off)) != 0:
                            for tmp in set(doc_s_on) - set(doc_s_off):
                                if 'resultList->doc_source_' + str(tmp) not in less_fields:
                                    less_fields['resultList->doc_source_' + str(tmp)] = list()
                                less_fields['resultList->doc_source_' + str(tmp)].append(pri_url)
                                msg.append('  --resultList->doc_source_%s FAIL. %s missed' % (
                                tmp, str(set(doc_s_on) - set(doc_s_off))))
                        if len(set(doc_s_off) - set(doc_s_on)) != 0:
                            for tmp in set(doc_s_off) - set(doc_s_on):
                                if 'resultList->doc_source_' + str(tmp) not in more_fields:
                                    more_fields['resultList->doc_source_' + str(tmp)] = list()
                                more_fields['resultList->doc_source_' + str(tmp)].append(pri_url)
                                msg.append('  --resultList->doc_source_%s FAIL. %s redundancy' % (
                                tmp, str(set(doc_s_off) - set(doc_s_on))))

                        for doc_type in set(doc_s_on) & set(doc_s_off):
                            if on_source[doc_type] == off_source[doc_type]:
                                continue
                            if len(on_source[doc_type]) != len(off_source[doc_type]):
                                if 'resultList->doc_source_' + str(doc_type) + '_length' not in diff_fields:
                                    diff_fields['resultList->doc_source_' + str(doc_type) + '_length'] = list()
                                diff_fields['resultList->doc_source_' + str(doc_type) + '_length'].append(pri_url)
                                msg.append('    --resultList->doc_source_%s_length FAIL. online=%s, offline=%s' % (
                                doc_type, len(on_source[doc_type]), len(off_source[doc_type])))
                            else:
                                if on_source[doc_type] != off_source[doc_type]:
                                    if 'resultList->doc_source_' + str(doc_type) + '_rank' not in diff_fields:
                                        diff_fields['resultList->doc_source_' + str(doc_type) + '_rank'] = list()
                                    diff_fields['resultList->doc_source_' + str(doc_type) + '_rank'].append(pri_url)
                                    msg.append('    --resultList->doc_source_%s_rank FAIL. onine=%s,offline=%s' % (
                                    doc_type, str(on_source[doc_type]), str(off_source[doc_type])))

                            if doc_type == 2:
                                on_video_list = list()
                                for ind in on_source[doc_type]:
                                    on_video_list.append(on_data[ind]['vid'])
                                off_video_list = list()
                                for ind in off_source[doc_type]:
                                    off_video_list.append(off_data[ind]['vid'])
                                same_len = len(set(on_video_list) & set(off_video_list))
                                if same_len < len(set(on_video_list)) * int(precision) / 100:
                                    if 'resultList->doc_source_2_ugc' not in diff_fields:
                                        diff_fields['resultList->doc_source_2_ugc'] = list()
                                    diff_fields['resultList->doc_source_2_ugc'].append(pri_url)
                                    msg.append(
                                        '    --rresultList->doc_source_2_ugc FAIL. online=%s, offline=%s, same=%s' % (
                                        len(on_source[doc_type]), len(off_source[doc_type]), same_len))
                                if len(off_source[doc_type]) == 0:
                                    ugc_null.append(pri_url)
                            elif doc_type == 1:
                                on_video_list = list()
                                for ind in on_source[doc_type]:
                                    on_video_list.append(on_data[ind]['programmeId'])
                                off_video_list = list()
                                for ind in off_source[doc_type]:
                                    off_video_list.append(off_data[ind]['programmeId'])
                                same_len = len(set(on_video_list) & set(off_video_list))
                                if on_video_list != off_video_list:
                                    if 'resultList->doc_source_1_show' not in diff_fields:
                                        diff_fields['resultList->doc_source_1_show'] = list()
                                    diff_fields['resultList->doc_source_1_show'].append(pri_url)
                                    msg.append('    --resultList->doc_source_1_show FAIL.online=%s,offline=%s' % (
                                    str(on_video_list), str(off_video_list)))

                            elif doc_type == 12:
                                for ind in on_source[doc_type]:
                                    for check_key in ['allId', 'movieId', 'varietyId', 'releplayId']:
                                        if check_key in on_data[ind]:
                                            if check_key in off_data[ind] and on_data[ind][check_key] != off_data[ind][
                                                check_key]:
                                                if 'resultList->doc_source_12_' + check_key not in diff_fields:
                                                    diff_fields['resultList->doc_source_12_' + check_key] = list()
                                                diff_fields['resultList->doc_source_12_' + check_key].append(pri_url)
                                                msg.append('resultList->doc_source_12_%s FAIL.online=%s,offline=%s' % (
                                                check_key, on_data[ind][check_key], off_data[ind][check_key]))
                                            if check_key not in off_data[ind]:
                                                if 'resultList->doc_source_12_' + check_key not in less_fields:
                                                    less_fields['resultList->doc_source_12_' + check_key] = list()
                                                less_fields['resultList->doc_source_12_' + check_key].append(pri_url)
                                                msg.append(
                                                    'resultList->doc_source_12_%s FAIL.online=%s,offline=none' % (
                                                    check_key, on_data[ind][check_key]))

                                    if 'relations' in on_data[ind]:
                                        if 'relations' in off_data[ind] and on_data[ind]['relations'] != off_data[ind][
                                            'relations']:
                                            if 'resultList->doc_source_12_relations' not in diff_fields:
                                                diff_fields['resultList->doc_source_12_relations'] = list()
                                            diff_fields['resultList->doc_source_12_relations'].append(pri_url)
                                            msg.append(
                                                '    --resultList->doc_source_12_relations FAIL.online=%s,offline=%s' % (
                                                doc_type, on_data[ind]['relations'], off_data[ind]['relations']))
                                        elif 'relations' not in off_data[ind]:
                                            if 'resultList->doc_source_12_relations' not in less_fields:
                                                less_fields['resultList->doc_source_12_relations'] = list()
                                            less_fields['resultList->doc_source_12_relations'].append(pri_url)
                                            msg.append(
                                                'resultList->doc_source_12_relations FAIL.online!=none,offline=none')



                elif key == 'total':
                    if abs(on_data - off_data) >= int(precision) * on_data / 100:
                        if 'total' not in diff_fields:
                            diff_fields['total'] = list()
                        diff_fields['total'].append(pri_url)
                        msg.append('  --%s FAIL.online=%s,offline=%s' % (key, on_data, off_data))

                else:
                    if on_data != off_data:
                        if key not in diff_fields:
                            diff_fields[key] = list()
                        diff_fields[key].append(pri_url)
                        msg.append('  --%s FAIL.online=%s,offline=%s' % (key, on_data, off_data))


                        ##print 详细信息

        if len(msg) != 0:
            print pri_url
            for m in msg:
                print m

                # 单机check
    if len(ugc_null) != 0:
        for m in ugc_null:
            print m
            print "  --ugc=none"
    print '#############################################'
    print '##################统计信息####################'
    print '#############################################'
    ##print 统计信息
    url_count = len(urls)

    if len(json_fail) != 0:
        print '\njson无结果率：%s' % str(len(json_fail) * 100 / url_count)
    if len(ugc_null) != 0:
        print "\nugc空结果率：%s" % str(len(ugc_null) * 100 / url_count)
    if len(less_fields) != 0:
        print '\n          丢字段                  百分比'
        for k in less_fields:
            print  '%20s\t%10s' % (k, str(len(less_fields[k]) * 100 / url_count))
    if len(more_fields) != 0:
        print '\n         多余字段                  百分比'
        for k in more_fields:
            print  '%20s\t%10s' % (k, str(len(more_fields[k]) * 100 / url_count))
    if len(diff_fields) != 0:
        print '\n         DIFF字段                  百分比'
        for k in diff_fields:
            print  '%20s\t%10s' % (k, str(len(diff_fields[k]) * 100 / url_count))


if __name__ == "__main__":
    # 处理命令行参数
    st = time.time()

    usage = "usage: %prog [options]"
    parser = OptionParser(usage=usage)
    # 配置文件
    parser.add_option("-t", "--test ip", action="store", dest="test_ip",
                      default="imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=110", help="The test ip")
    parser.add_option("-o", "--online vip", action="store", dest="online_ip",
                      default="imerge.soku.proxy.taobao.org/i/s?rankFlow=110", help="The online vip")
    parser.add_option("-f", "--url file", action="store", dest="url_file", default="query.file", help="url file")
    parser.add_option("-p", "--proprecision num", action="store", dest="precision", default="20", help="precision")

    (options, args) = parser.parse_args()

    more_fields = dict()
    less_fields = dict()
    diff_fields = dict()
    json_fail = list()
    print options.test_ip

    start(options.online_ip, options.test_ip, options.url_file, options.precision, diff_fields, json_fail, more_fields,
          less_fields)
