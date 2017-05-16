#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import sys
from Logger import *
reload(sys)
sys.setdefaultencoding('utf-8')
import json


logger = Logger(logFileName='diff.log', logger="diff").getlog()
show_dic = {}

i = 1
diff_num = 0

def get_query(query_file):
    urls = []
    with open(query_file, 'r') as f:
        for line in f:
            urls.append(line)
    return  urls

def get_url_result(url):
    json = None
    try:
        session = requests.session()
        res = session.get(url)
        json = res.json()
        #retry
        i=0
        while len(res.content) == 0 and i<2:
            res = session.get(url)
            if len(res.content) > 0:
                json = res.json()
            i += 1
        return json
    except Exception,e:
        logger.debug('Exception ' + str(e))
        return None
    return json

def start(query_file):
    querys = get_query(query_file)
    global i
    global diff_num

    for query in querys:
        query = query.strip()
        try:
            cur_query = query.strip('\n')
            #off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&cmd=1&qaFlow=1&keyword=' + cur_query
            off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&cmd=1&ecb_sp_ip=11.173.213.132:2090&qaFlow=1&keyword='+cur_query
            online_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&ecb_sp_ip=11.173.227.22:2090&cmd=1&qaFlow=1&keyword=' + cur_query
            # online_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&isFilter=16&cmd=1&qaFlow=1&keyword='+cur_query

            on_json = get_url_result(online_url)
            off_json = get_url_result(off_url)

            on_ecb_data = on_json['ecb']
            off_ecb_data = off_json['ecb']
            if on_ecb_data == None or off_ecb_data == None:
                print 'ecb_data is None'
                continue

            on_youku_data = on_ecb_data['youku_ecb']
            off_youku_data = off_ecb_data['youku_ecb']
            if on_youku_data == None or off_youku_data == None:
                print 'youku_data is None'
                continue

            on_auctions_data = on_youku_data['auctions']
            off_auctions_data = off_youku_data['auctions']
            if on_auctions_data == None or off_auctions_data == None:
                print 'youku_data is None'
                continue

            onShowIds = set()
            offShowIds = set()
            for on_item in on_auctions_data:
                onShowid = on_item['show_id']
                onShowIds.add(onShowid)

            for off_item in off_auctions_data:
                offShowid = off_item['show_id']
                offShowIds.add(offShowid)

            # 计算online多的showid
            on_more = onShowIds - offShowIds
            off_more = offShowIds - onShowIds
            on_more_name = []
            off_more_name = []
            for id in on_more:
                if id in show_dic:
                    on_more_name.append(show_dic[id])
                else:
                    on_more_name.append(id)

            for id in off_more:
                if id in show_dic:
                    off_more_name.append(show_dic[id])
                else:
                    off_more_name.append(id)

            log_str = str(i) + '.' +  cur_query + '[' + str(len(onShowIds)) + ':' + str(len(offShowIds)) + ']';
            if (len(on_more) != 0 and len(off_more) != 0):
                # print log_str + '\tonMore:[' + ', '.join(on_more_name) + ']\toffMore:[' + ','.join(off_more_name)+']'
                diff_num +=1
                logger.info(log_str + '\tonMore:[' + ', '.join(on_more_name) + ']\toffMore:[' + ','.join(off_more_name) + ']')

            elif len(on_more) != 0:
                # print log_str + "\tonMore:[" +', '.join(on_more_name) + ']'
                diff_num += 1
                logger.info(log_str + "\tonMore:[" + ', '.join(on_more_name) + ']')

            elif len(off_more) != 0:
                # print log_str + '\toffMore:[' + ', '.join(off_more_name) + ']'
                diff_num +=1
                logger.info(log_str + '\toffMore:[' + ', '.join(off_more_name) + ']')
            else:
                # print log_str + '\tSame'
                logger.debug(log_str + '\t' + 'Same')

        except Exception,e:
            logger.info('Exception query:' + query)
        i+=1
    logger.info('diff_ratio=' + str(float(diff_num)/float(i)))

def read_show_file(show_file):
    with open(show_file,'r') as f:
        for line in f:
            field = line.split('\t')
            show_dic[field[0]] = field[1].strip()


if __name__ == '__main__':
    read_show_file('data/all_show_odps')
    #start('data/top300')
    start('data/mid700')
