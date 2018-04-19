# -*- coding=utf-8 -*-
#! /usr/bin/env python
import re,sys,math

reg_list = [
        '[^0-9]+[0-9]{1,2}集(完整|免费|在线|视频|高清)'
    ]

def blankMerge():
    res = re.sub(',+', ',', 'rick,,,and,morty,s,')
    print(res)

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

def cos(a_vec, b_vec):
    avec = a_vec.split(',')
    bvec = b_vec.split(',')
    vector1 = map(float, avec)
    vector2 = map(float, bvec)
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a,b in zip(vector1, vector2):
        dot_product += a*b
        normA += a**2
        normB += b**2
    if normA == 0.0 or normB == 0.0:
        return None
    else:
        return dot_product / ((normA*normB)**0.5)

def zhangkun(show_name, meta_keyword, split_char):
    reg = "[！|\!|·|、|,|▪|－|，| ]+".decode("utf8")
    show_name = show_name.decode('utf8')
    meta_keyword = meta_keyword.decode('utf8')
    # 边界处理
    if meta_keyword is None or show_name is None:
        return ''

    main_keyword = ''
    sub_keyword = ''
    if ',' in show_name or '，'.decode('utf8') in show_name:
        main_keyword = re.sub(reg, "".decode("utf8"), show_name)
    elif ',' not in meta_keyword:
        main_keyword = re.sub(reg, "".decode("utf8"), meta_keyword)
    else:
        key_idx = -1
        i = 0
        idx = 10000
        field = list(set(meta_keyword.split(split_char)))
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
        main_keyword = re.sub("[！|\!|·|、|,|▪|－|，| ]+".decode("utf8"), "".decode("utf8"), main_keyword)
        field.pop(key_idx)

        sub_list = []
        for sub in field:
            if re.search(".*(篇)$".decode("utf8"), sub) is None:
                sub_list.append(sub)

        sub_keyword = ','.join(list(set(sub_list)))
        sub_keyword = re.sub("[！|\!|·|、|▪|－|，| ]+".decode("utf8"), "".decode("utf8"), sub_keyword)

    main_keyword = main_keyword.encode('utf8')
    sub_keyword = sub_keyword.encode('utf8')
    print(main_keyword)
    print(sub_keyword)


if __name__ == '__main__':
    zhangkun('春天的十七个瞬间:25年后', '成败论乾隆;百家讲坛', ';')
    #evaluate('微微一笑很倾城第22集高清')
    # with open('/Users/tanzhen/Desktop/code/odps/bin/yellow_query_all','r') as f:
    #     for line in f:
    #print fun('sfasdf 2018')
    #print evaluate2('蒙德维地亚:梦之味（上）', '蒙德维地亚,梦之味')
    #process("阪妻：阪东妻三郎的一生","阪妻,阪东妻三郎的一生")
    #print fun("乱马1/2 热斗歌合战")
    ss = '嘿啦啦啦嘿哈嘿'.decode('utf8')
    print(len(ss))
    print(ss[:int(len(ss)/2)])
    blankMerge()
    print cos("-416,691,-351,127,1263,369,0,246,150,0,0,-123,419,518,-9,730,365,-612,282,59,0,913,0,386,418,-460,0,0,0,-1005,0,-674,0,184,-124,-213,-252,0,274,-1972,192,0,-1492,1029,0,-734,0,0,-123,-615,-1326,-124,419,-611,-418,-7,934,0,123,893,487,-133,0,0,-2103,-195,-692,1554,-540,-1569,0,1621,-136,-26,-137,-701,419,2103,2103,1,-1479,-486,-192,1874,136,2100,418,-5,1137,-1621,1800,774,1299,-943,-1128,-920,2103,-326,-1940,1614,1741,652,418,701,1645,1728,294,-1479,-418,952,0,630,-701,-538,-837,-688,-611,275,-418,397,0,-1088,1732,-486,-157,-1569,-700,-419"
                 ,"-359,292,-298,-275,1917,0,298,350,-24,687,-299,-356,-647,-322,-21,-292,292,-240,-583,-311,0,838,0,-299,0,-290,-292,0,0,353,0,26,-465,0,292,0,-578,-541,631,-1106,40,290,-1726,1724,898,-623,-290,0,643,-497,-698,287,-646,210,0,-62,1408,-521,-10,354,-292,315,-187,-581,-1314,-621,-1036,1691,-40,-1393,-1,1751,895,292,-1267,-290,-671,2133,1367,795,-932,-904,-356,1281,535,1731,668,646,2119,-1546,1148,1668,1751,-290,-978,-875,1808,37,-994,1497,1089,1284,-318,907,-283,932,317,-1316,-39,1280,-292,569,-396,-464,-1314,156,-344,27,62,38,1174,-1626,1603,-1007,-63,-1590,-2127,-1270"
              )


