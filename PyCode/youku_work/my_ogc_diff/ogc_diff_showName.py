#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json

show_dic = {}

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
        print 'Exception ', e
        return None
    return json

def start(query_file):
    querys = get_query(query_file)
    print len(querys)
    for query in querys:
        cur_query = query.strip('\n')
        off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=111&cmd=1&qaFlow=3&keyword='+cur_query
        online_url = 'http://imerge.soku.proxy.taobao.org/i/s?rankFlow=111&cmd=1&qaFlow=3&keyword='+cur_query

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

        #计算online多的showid
        on_more = onShowIds - offShowIds
        off_more = offShowIds - onShowIds

        if (len(on_more) != 0 and len(off_more) != 0):	
            print cur_query + '\tonMore:[' + ','.join(on_more) + ']\toffMore:[' + ','.join(off_more)+']'

        if len(on_more) != 0:
            print cur_query + "\tonMore:[" +','.join(on_more) + ']'

        if len(off_more) != 0:
            print cur_query + '\toffMore:[' + ','.join(off_more) + ']'

def read_show_file(show_file):
    with open(show_file,'r') as f:
        for line in f:
            field = line.split('\t')
            print line[0] + ',' + line[1]
            #show_dic[]


if __name__ == '__main__':
    read_show_file('all_show_odps')
    #start('query_all.file')
