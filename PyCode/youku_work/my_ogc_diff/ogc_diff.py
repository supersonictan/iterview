#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json

def get_query(query_file):
    urls = []
    with open(query_file, 'r') as f:
        line = f.readline()
        if line != "" or line != None:
            urls.append(line)
    return  urls

def get_url_result(url):
    json = None
    try:
        session = requests.session()
        res = session.get(url)
        json = res.json()
        print json

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
    for query in querys:
        cur_query = query.strip('\n')
        off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=110&qaFlow=3&keyword='+cur_query
        online_url = 'http://imerge.soku.proxy.taobao.org/i/s?rankFlow=110&qaFlow=3&keyword='+cur_query

        on_json = get_url_result(online_url)
        print on_json
        off_json = get_url_result(off_url)
        #on_keys = on_json.keys()
        #off_keys = off_json.keys()

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

        onShowIds = []
        offShowIds = []
        for on_item in on_auctions_data:
            onShowid = on_item['show_id']
            onShowIds.append(onShowid)

        for off_item in off_auctions_data:
            offShowid = off_item['show_id']
            offShowIds.append(offShowid)

        print onShowIds

if __name__ == '__main__':
    start('query.file')