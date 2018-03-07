#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib

s = "s=kubox&outfmt=json&query=%F0%A6%AC%A3&utdid=sMFw9NFxwwcDAIq2+TdmHbse&ip=49.90.46.209"
ss = 's=kubox&outfmt=json&'

def parseTestData():
    with open('query0220_05', 'r') as fq, open('utdid0220_05', 'r') as fid, open('ip700w', 'r') as fip, open('result_url', 'w') as fw:
        for qline in fq:
            qline = qline.strip()
            idline = fid.readline().strip()
            ipline = fip.readline().strip()
            dic =  {}
            dic['query'] = qline
            dic['utdid'] = idline
            dic['ip'] = ipline

            res = ss + urllib.urlencode(dic) + '\n'
            #url = ss % (qline, idline, ipline)
            #url = url.encode('utf-8','replace')
            #url = urllib.urlencode(url)
            fw.writelines(res)
            fw.flush()
            #print(res)



if __name__ == '__main__':
    parseTestData()