#!/usr/bin/python
#-*- coding=utf-8-*-
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
import json

jsonData ="""{
    "VIDEO1": {
        "policyType": "AND",
        "itemList": [
            {
                "id": 175,
                "operate": "CONTAIN",
                "data": "{'301649':'玩策论','302968':'玩策论 2016'}"
            },
            {
                "id": 15,
                "operate": "CONTAIN",
                "data": "{'301649':'玩策论','302968':'玩策论 2016'}"
            }
        ],
        "groupList": []
    }
}
"""


res = 0
text = json.loads(jsonData)
if text != None and 'VIDEO' in text:
    video_content = text['VIDEO']
    if video_content != None:
        itemList_content = video_content['itemList']
        if itemList_content != None:
            for item in itemList_content:
                if item != None and item['id'] != None and item['id'] == 175:
                    data_map = eval(item['data'])
                    index=0
                    for k in data_map:
                        if index == 0:
                            res = k
                            break

print res


