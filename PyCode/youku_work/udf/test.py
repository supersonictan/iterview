#!/usr/bin/python
# -*- coding=utf-8-*-
import math,json,re

#print math.log(-0.984,10)
# print math.log(0.8)
# print math.log(0.5)
#
# print 10 ** -0.984
#
# print("龙珠Z番外篇：五大超级".find('七龙珠'))
txt = '["{\"ctype\":\"contentad\",\"start\":119856,\"title\":\"\",\"desc\":\"\"}","{\"ctype\":\"story\",\"start\":518509,\"title\":\"郭照求曹丕相助 肌肤为纸任流连\",\"desc\":\"\"}","{\"ctype\":\"standard\",\"start\":860874,\"title\":\"\",\"desc\":\"\"}","{\"ctype\":\"contentad\",\"start\":935660,\"title\":\"\",\"desc\":\"\"}","{\"ctype\":\"story\",\"start\":1115478,\"title\":\"司马懿囹圄探父 解暗语得知秘闻\",\"desc\":\"\"}","{\"ctype\":\"story\",\"start\":1407337,\"title\":\"司马懿施瞒天计 杨修摧毁衣带诏\",\"desc\":\"\"}","{\"ctype\":\"standard\",\"start\":1722605,\"title\":\"\",\"desc\":\"\"}","{\"ctype\":\"story\",\"start\":1865042,\"title\":\"荀彧遭杨修要挟 允合谋夺人性命\",\"desc\":\"\"}","{\"ctype\":\"story\",\"start\":2107835,\"title\":\"暗夜渡口起杀机 荀彧谋杀司马懿\",\"desc\":\"\"}"]'
# txt = txt.replace("\"{", "{")
# txt = txt.replace("}\"", "}")
# j = json.loads(txt)
# resStr = ''
# for obj in j:
#     if obj['title'] is not None and obj['title'] != '':
#         resStr += obj['title']
# print(resStr)
#
# list = []
# map = {"a": "a1", "b": "b1"}
# list.append(map)
# j = json.dumps(list)
# print(j)


def evaluate(txt):
    try:
        if txt is None or txt.strip() == '':
            return ''
        txt = txt.decode('utf8')
        resStr = ''
        txt = txt.replace("\"{", "{")
        txt = txt.replace("}\"", "}")
        reg = "(\"start\".*?,)"
        txt = re.sub(reg, "", txt)
        print(txt)
        jsonObj = json.loads(txt)
        print(json.dumps(jsonObj))
        for obj in jsonObj:
            if obj['title'] is not None and obj['title'] != '':
                resStr += obj['title'].encode('utf8')
        return resStr
    except Exception, e:
        return str(e.message)

if __name__ == '__main__':
    txt = txt.replace("\\", '')
    print(txt)
    #print evaluate(txt)