#coding:utf-8

import json
import types
import re
import string
import sys as _sys
import urllib
import urllib2
import traceback




if __name__ == '__main__':
    query = '刘德华'
    try:
        baseurl = "https://beta-youku-search.youku.com/search/query?noqc=0&appScene=imerge&appCaller=ott&is_apple=0&bucketId=5&pz=30&spDataType=7&caller=0&pg=1&nocache=1&from=text&cmd=4&keyword="

        query = query.strip()
        result_list = ""

        data = ""
        try:
            url = baseurl + urllib.quote(query)
            # print url
            data = urllib2.urlopen(url, data=None, timeout=1).read()
            print data

            data = json.dump(data)
            jsonObj = json.loads(data)
            if 'sp' not in jsonObj:
                pass
            jsonObj2 = jsonObj['sp']
            if 'youku' not in jsonObj2:
                pass

            auctions_obj = jsonObj2['youku']['auctions']

            for item in auctions_obj:
                print item['ott_id']


        except Exception, e:
            print e


        # result = json.dumps(result_list, ensure_ascii=False).encode('utf-8').strip()
        # return self.forward(query, result_list)
    except:
        pass
