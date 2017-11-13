#!/usr/bin/python
# -*- coding=utf-8-*-
import json

str = """
{"site_disabled":["tudou","test"],"device_disabled":["IPTV","PC","Pad","TV","mobile"],"ua_disabled":["App","Web"]}
"""
str2 = """
{"user_domain_disabled":[{"domainRangeType":3,"userId":"347980356"},{"domainRangeType":3,"userId":"503712794"},{"domainRangeType":3,"userId":"703241937"}]}
"""
str3 = """
{"ccode_disabled":["010101500003","010102500003"],"watchtime_disabled":1,"site_disabled":["tmall","tudou","youku"],"area_disabled":["level1"],"user_applied":["vip"]}
"""
str4 = """
{"site_disabled":["youku"],"area_disabled":["other_abroad","level1"],"device_disabled":["Pad"],"ua_disabled":["Web"]}
"""

def evaluate(jsonStr, keyName):
    res = ""
    json_str = json.loads(jsonStr)
    if json_str.has_key(keyName):
        res = '\x1D'.join(json_str[keyName])
    print res

def evaluate2(arrayStr, splitStr):
    res = ""
    if arrayStr == "" or arrayStr is None:
        return res
    s = list(set(arrayStr.split(splitStr)))
    return '\x1D'.join(s)


if __name__ == '__main__':
    print evaluate2(",", ",")
    #evaluate(str, "device_disabled")


