# -*- coding=utf-8 -*-
#! /usr/bin/env python
import re,sys,math

reg_list = [
        '[^0-9]+[0-9]{1,2}集(完整|免费|在线|视频|高清)'
    ]

def evaluate( key):
    for reg in reg_list:
        re_res = re.search(reg, key)
        if re_res is not None:
            print('match')
            return 1
    print(key)
    return 0

def fun (word):
    meta_keyword = str(word)
    meta_keyword = meta_keyword.decode('utf-8')
    # list = [',', '，', ':', '：', ';', '；', '!', '！']
    # 去除数字结尾
    res = []
    field = meta_keyword.split(',')
    for i in field:
        if '\\/' not in i:
            i = re.sub(r'\b\d{1}$|\d{4}$', "", i)
        if i not in res:
            res.append(i.encode('utf-8'))

    return ','.join(res)

def test():
    s1 = "笨蛋·测验·召唤兽 第一季"
    s1 = s1.decode('utf8')
    s1 = re.sub("[！|\!|·|,|▪|－]+".decode("utf8"), "".decode("utf8"), s1)
    print(s1.encode('utf8'))

def evaluate2(show_name, meta_keyword):
    show_name = show_name.decode('utf8')
    meta_keyword = meta_keyword.decode('utf8')
    if meta_keyword is None:
        return ''
    # meta_keyword = str(meta_keyword)
    res = ''.decode('utf8')
    idx = 10000
    if ',' not in meta_keyword:
        meta_keyword = re.sub("[！|\!|·|,|▪|－| ]+".decode("utf8"), "".decode("utf8"), meta_keyword)
        return meta_keyword.encode('utf8')

    field = meta_keyword.split(',')
    for key in field:
        find_idx = show_name.find(key)
        if find_idx < idx:
            idx = find_idx
            res = key
    # res = re.sub(ur'！|\!|·|,|▪|－', "", res)
    res = re.sub("[！|\!|·|,|▪|－| ]+".decode("utf8"), "".decode("utf8"), res)
    return res.encode('utf-8')


def process(show_name, meta_keyword):
    show_name = show_name.decode('utf8')
    meta_keyword = meta_keyword.decode('utf8')
    # 边界处理
    if meta_keyword is None or show_name is None:
        return ''

    main_keyword = ''
    sub_keyword = ''
    if ',' not in meta_keyword:
        main_keyword = re.sub("[！|\!|·|,|▪|－| ]+".decode("utf8"), "".decode("utf8"), meta_keyword)
        main_keyword = main_keyword.encode('utf8')
    else:
        key_idx = -1
        i = 0
        idx = 10000
        field = list(set(meta_keyword.split(',')))
        for key in field:
            if key == '' or key is None:
                continue
            startChar = key[0]
            find_idx = show_name.find(startChar)
            if find_idx < idx and find_idx != -1:
                idx = find_idx
                main_keyword = key
                key_idx = i
            i += 1
        main_keyword = re.sub("[！|\!|·|,|▪|－|，| ]+".decode("utf8"), "".decode("utf8"), main_keyword)
        field.pop(key_idx)

        sub_list = []
        for sub in field:
            if re.search(".*(篇)$".decode("utf8"), sub) is None:
                sub_list.append(sub)

        sub_keyword = ','.join(list(set(sub_list)))
        sub_keyword = re.sub("[！|\!|·|▪|－|，| ]+".decode("utf8"), "".decode("utf8"), sub_keyword)

        main_keyword = main_keyword.encode('utf-8')
        sub_keyword = sub_keyword.encode('utf8')

    print(main_keyword)
    print(sub_keyword)
    # self.forward(main_keyword, sub_keyword)


def cosine(a_vec, b_vec):
    avec = a_vec.split(',')
    bvec = b_vec.split(',')

    if len(avec) != len(bvec) != 128:
        return -2

    idx = 0
    fenzi = 0.0
    for i in avec:
        fenzi += float(i) * float(bvec[idx])

    sqrt_str1 = math.sqrt(sum(float(x) ** 2 for x in avec))
    sqrt_str2 = math.sqrt(sum(float(x) ** 2 for x in bvec))

    return fenzi / (sqrt_str1 * sqrt_str2)

def cos(a_vec,b_vec):
    avec = a_vec.split(',')
    bvec = b_vec.split(',')
    vector1 = map(float, avec)
    vector2 = map(float, bvec)
    dot_product = 0.0;
    normA = 0.0;
    normB = 0.0;
    for a,b in zip(vector1,vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB==0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)


if __name__ == '__main__':
    #evaluate('微微一笑很倾城第22集高清')
    # with open('/Users/tanzhen/Desktop/code/odps/bin/yellow_query_all','r') as f:
    #     for line in f:
    #print fun('sfasdf 2018')
    #print evaluate2('蒙德维地亚:梦之味（上）', '蒙德维地亚,梦之味')
    #process("阪妻：阪东妻三郎的一生","阪妻,阪东妻三郎的一生")
    #print fun("乱马1/2 热斗歌合战")
    print cos("-304,579,-302,351,1573,316,-405,199,129,-180,0,-106,361,444,-267,913,313,-524,228,51,0,710,0,573,358,-679,-242,0,0,-863,0,-384,242,158,-106,-183,-456,0,464,-1847,377,0,-1742,816,0,-854,241,-421,-106,-528,-1330,-106,359,-524,-359,-6,917,0,348,766,176,-365,0,423,-2277,185,-486,1488,-704,-1281,-181,1625,50,54,-131,-829,359,2277,1721,317,-1760,-355,-164,1842,130,2177,359,-4,1131,-1627,1720,560,1297,-615,-954,-1089,2039,-279,-1820,1480,1413,789,359,1114,1507,1738,10,-1204,-359,1070,0,540,-587,-396,-1122,-422,-766,13,-331,340,0,-1423,1977,-598,-279,-1530,-1092,-116"
                 ,"-343,848,-315,113,1424,332,0,465,135,0,0,-111,376,466,-27,971,608,-550,511,53,0,788,0,587,376,-414,0,0,0,-903,280,-919,280,165,-111,-192,-420,0,205,-1685,453,0,-1621,845,0,-642,280,-280,169,-552,-1484,-111,666,-549,-188,-287,1123,0,111,802,438,-120,0,280,-1726,-222,-788,1677,-485,-1443,0,1369,-165,-5,-165,-587,375,2171,1802,368,-1297,-375,-172,1596,446,2152,376,-285,1303,-1738,1820,588,1368,-805,-1309,-691,2171,-293,-1656,1857,1943,863,657,1123,1769,1892,264,-1297,-95,824,-281,285,-590,-451,-860,-445,-549,128,-376,356,0,-946,1894,-717,5,-1378,-966,-376")


