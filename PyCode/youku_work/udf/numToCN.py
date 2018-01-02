#!/usr/bin/python
# -*- encoding: utf-8 -*-
import re,types

patStr=u'(第)([一二三四五六七八九十百千]*)([季集部期])'
pat = re.compile(patStr)

dict_trans = {
    u'一':1,
    u'二':2,
    u'三':3,
    u'四':4,
    u'五':5,
    u'六':6,
    u'七':7,
    u'八':8,
    u'九':9,
}


def evaluate(targetStr):
    if targetStr is None:
        return None
    line = unicode(targetStr, 'utf8')
    for match in re.finditer(pat, line):
        targetStr = match.group(0)
        str1 = match.group(1)
        str2 = match.group(2)
        str3 = match.group(3)
        targetNum = 0
        totalNum = 0
        for uni in str2:
            if u'十' == uni:
                if targetNum == 0:
                    targetNum += 10
                else:
                    targetNum *= 10
                totalNum += targetNum
                targetNum = 0
            elif u'百' == uni:
                totalNum += targetNum * 100
                targetNum = 0
            elif u'千' == uni:
                totalNum += targetNum * 1000
                targetNum = 0
            else:
                targetNum += dict_trans[uni]
        totalNum += targetNum

        tranStr = '%s%d%s' % (str1, totalNum, str3)
        line = line.replace(targetStr, tranStr)
    if not line:
        return ''
    if type(line) != types.UnicodeType:
        line = line.decode('utf8')
        # text = text.decode('utf8')
    return ''.join([i for i in line if not ord(i) == 32]).encode('utf8')



if __name__ == '__main__':
    #print evaluate('第三部')
    print len("微微一笑a".decode('utf-8'))