#!/usr/bin/python
# -*- coding=utf-8-*-
import json,re
import types
import time

chnl_reg_list = [".+综艺", ".+电影", ".+电视剧", ".+视频"]
str2 = """
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
person_json = """
[{"id":"352501","name":"马思纯","thumburl":"http://r1.ykimg.com/0513000059E07FB9859B5C0493013995","character":["叶昭"]},{"id":"876764","name":"盛一伦","thumburl":"http://r1.ykimg.com/0513000059F18707859B5C04930CAB0F","character":["赵玉瑾"]},{"id":"866445","name":"丁川","thumburl":"http://r1.ykimg.com/0513000059E0241B859B5E110C08AF24","character":["胡青"]},{"id":"901303","name":"王楚然","thumburl":"http://r1.ykimg.com/0513000059E01E81859B5C04950F3342","character":["柳惜音"]},{"id":"402659","name":"芦芳生","thumburl":"http://r1.ykimg.com/0513000058982CC067BC3C68090DE702","character":["宋仁宗"]},{"id":"17265","name":"于波","thumburl":"http://r1.ykimg.com/051300005893FCD067BC3C2E910B56D1","character":["范仲淹"]},{"id":"140582","name":"王力","thumburl":"http://r1.ykimg.com/0513000059F18C7CADBC09332D08CF55","character":["秋老虎"]},{"id":"350814","name":"潘时七","thumburl":"http://r1.ykimg.com/0513000058993B7967BC3C7D54062046","character":["秋水"]},{"id":"882331","name":"王瑄","thumburl":"http://r1.ykimg.com/0513000059155952ADBDD3208C070647","character":["秋华"]},{"id":"17027","name":"朱泳腾","thumburl":"http://r1.ykimg.com/0513000059F18DF2ADBA1F4A0509CFFC","character":["祈王"]},{"id":"13880","name":"刘卫华","thumburl":"http://r1.ykimg.com/0513000059F18EA3ADBA1F36B304455D","character":["吕相爷"]},{"id":"15986","name":"刘金山","thumburl":"http://r1.ykimg.com/05130000595A0A43859B5CA4890A6C17","character":["刘太傅"]},{"id":"213807","name":"张瑶","thumburl":"http://r1.ykimg.com/0513000059F19006AD881A049306EA39","character":["赵太妃"]},{"id":"219550","name":"张雯","thumburl":"http://r1.ykimg.com/0513000059F1948DADBA1F3676065248","character":["赵王妃"]},{"id":"295951","name":"肖涵","thumburl":"http://r1.ykimg.com/0513000058A2D79AADBAC33D0A06A4F4","character":["张贵妃"]},{"id":"328831","name":"王维维","thumburl":"http://r1.ykimg.com/0513000058AA6453ADBDD3033C026AD8","character":["郭皇后"]},{"id":"11630","name":"恬妞","thumburl":"http://r1.ykimg.com/051300005A029BA2ADBC094885039DF5","character":["刘太后"]},{"id":"902953","name":"张峻鸣","thumburl":"http://r1.ykimg.com/05130000594CBEEFADBC09037F016470","character":["伊诺王子"]},{"id":"15879","name":"刘孜","thumburl":"http://r1.ykimg.com/0513000059C0E7D8ADBC0904BC046784","character":["姬玉"]},{"id":"17184","name":"倪虹洁","thumburl":"http://r1.ykimg.com/0513000059ED631DADBC09282D0BF0AA","character":["辰妃"]},{"id":"17667","name":"牟凤彬","thumburl":"http://r1.ykimg.com/0513000058A2A0AFADBA1F3985046963","character":["柳将军"]},{"id":"326304","name":"王策","thumburl":"http://r1.ykimg.com/0513000058AD00BEADBDD3C7680B5017","character":["西夏王"]},{"id":"21170","name":"邵汶","thumburl":"http://r1.ykimg.com/0513000058AAC200ADBAC3034A0152FC","character":["陆震庭"]},{"id":"880511","name":"安泳畅","thumburl":"http://r1.ykimg.com/0513000058B3CB43ADBA1F9CD10CB823","character":["杨氏"]},{"id":"710199","name":"张歆莹","thumburl":"http://r1.ykimg.com/051300005983DCCC859B5E02F90A3AB2","character":["眉娘"]},{"id":"880514","name":"郑舒环","thumburl":"http://r1.ykimg.com/0513000059488E49859B5CE44000B7C8","character":["萱儿"]},{"id":"901306","name":"张家溢","thumburl":"http://r1.ykimg.com/0513000059E025DBADBA1F58360B0DA6","character":["张珪"]},{"id":"882603","name":"向皓","thumburl":"http://r1.ykimg.com/051300005965C386ADBAC3051700773A","character":["郭元景"]},{"id":"17061","name":"张植绿","thumburl":"http://r1.ykimg.com/051300005930CD96AD881A8B840EBAED","character":["小夏子"]},{"id":"377690","name":"刘凯菲","thumburl":"http://r1.ykimg.com/0513000058AFC3EEADBA1FAD240E6C43","character":["白浪"]},{"id":"827579","name":"王翊丹","thumburl":"http://r1.ykimg.com/0513000059AFA605859B5E05730DF24A","character":["范二娘"]},{"id":"778766","name":"刘迪妮","thumburl":"http://r1.ykimg.com/05130000596858BE859B5C0530099EED","character":["野利皇后"]},{"id":"881289","name":"王铂清","thumburl":"http://r1.ykimg.com/0513000059F031EC859B5D02F60923B0","character":["郭福山"]},{"id":"21389","name":"张洪杰","thumburl":"http://r1.ykimg.com/05130000589D7DFEADBA1F0341078316","character":["胡老太爷"]},{"id":"220016","name":"宋允皓","thumburl":"http://r1.ykimg.com/0513000058AAB216ADBC0903430B303E","character":["宋真宗"]},{"id":"19903","name":"卢星宇","thumburl":"http://r1.ykimg.com/05130000589D6D62ADBC0903450C24E2","character":["叶忠"]},{"id":"354127","name":"王丹妮","thumburl":"http://r1.ykimg.com/051300005955F6FFADBC09B3C6096888","character":["红莺"]},{"id":"877715","name":"金丽婷","thumburl":"http://r1.ykimg.com/05130000595F625C859B5C05160CCA9D","character":["红蔷"]}]
"""


def evaluate_cate( jsonStr, regType):
    chnl_reg_list = [".+综艺", ".+电影", ".+电视剧"]
    episode_reg_list = ["第([\\u4e00-\\u9fa5]{0,1}|[0-9]{0,1})(部|季)"]

    if jsonStr is None or jsonStr == "":
        return 0
    if regType == 'chnl':
        for reg in chnl_reg_list:
            re_res = re.search(reg, jsonStr)
            if re_res is not None:
                return 1
        return 0
    if regType == 'episode':
        for reg in episode_reg_list:
            re_res = re.search(reg, jsonStr)
            if re_res is not None:
                return 1
        return 0


def evaluate_country(jsonStr):
    res = ""
    if jsonStr is None or jsonStr == "":
        return ""
    try:
        jsonStr = jsonStr.decode("utf-8").lower()
        country = json.loads(jsonStr)
        if country is not None:
            for c in country:
                if res != "":
                    res += " / "
                res += c
    except ValueError:
        return ""
    return res.encode('utf8')

def evaluate_scgTime(timeStr):
    a = "1970-08-17 15:01:47"
    #将其转换为时间数组
    timeArray = time.strptime(a, "%Y-%m-%d %H:%M:%S")
    #转换为时间戳:
    timeStamp = int(time.mktime(timeArray))
    diff = int(time.time()) - timeStamp
    print 1.0/diff

def evaluate_person(jsonStr):
    res = ""
    if jsonStr is None or jsonStr == "":
        return res
    try:
        personList = json.loads(jsonStr)
        cnt = 0
        for personObj in personList:
            if cnt >= 2:
                break
            if res != "":
                res += " / "
            res += personObj["name"]
            cnt += 1
    except ValueError:
        return ""
    return res.encode('utf8')

def evaluate_diiCtrlA(strA, splitStr):
    res = ""
    if strA == "" or strA is None:
        return ""
    try:
        arr = strA.split(splitStr)
        res = '\x01'.join(arr)
    except ValueError:
        return res
    return res

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
def evaluate_dup(query, chnlName, seq):
    if query is None or query == '':
        return 0
    lowWeightList = [""]

"""
数据信息：
	是否节目数据/是否搜索日志数据/是否神马数据/是否人物数据
query关键词：
	包含电影含义词/包含电视剧含义词/综艺词/动漫词/季
	有花絮词
	包含歌曲词
	包含清晰度
"""
def evaluate_fea(dataSource, key, hot):
    res = ""
    if key is None or key == "":
        return ""
    if dataSource == 1: #节目数据源
        res += '1'
    else:
        res += ',0'

    if dataSource == 2: #搜索日志数据源
        res +=  ',1'
    else:
        res += ',0'

    if dataSource == 3: #神马数据源
        res += ',1'
    else:
        res += ',0'

    if dataSource == 5: #人物数据源
        res += ',1'
    else:
        res += ',0'

    # hot值
    res += ','
    res += str(hot)

    reg_film = [".+电影.*"]
    for reg in reg_film:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
        else:
            res += ',0'

    reg_series = [".+电视剧.*"]
    for reg in reg_series:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
        else:
            res += ',0'

    reg_zongyi = [".+综艺.*"]
    for reg in reg_zongyi:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
        else:
            res += ',0'

    reg_carton = [".+动漫.*"]
    for reg in reg_carton:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
        else:
            res += ',0'

    isSeasonMatch = False
    reg_season = ["第(一|二|三|四|五|六|七|八|九|十){0,3}季|部", "第[0-9]{0,2}季|部"]
    for reg in reg_season:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
            isSeasonMatch = True
            break
    if not isSeasonMatch:
        res += ',0'


    isPianHuaMatch = False
    reg_pianhua = [".*花絮.*", ".*片花.*"]
    for reg in reg_pianhua:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
            isPianHuaMatch = True
            break
    if not isPianHuaMatch:
        res += ',0'

    reg_song = [".*歌曲.*", ".*插曲.*",".*主题曲.*", ".*片尾曲.*"]
    isSongMatch = False
    for reg in reg_song:
        re_res = re.search(reg, key)
        if re_res is not None:
            res += ',1'
            isSongMatch = True
            break
    if not isSongMatch:
        res += ',0'

    arr = res.split(',')
    return '\x01'.join(arr)

def evaluate_date_showinfo(mainland_release_date, ovs_release_date, release_date):
    year = ''
    try:
        if not release_date.startswith('0000-00-00') and release_date != '':
            year = release_date
        if not ovs_release_date.startswith('0000-00-00') and ovs_release_date != '':
            year = ovs_release_date
        if not mainland_release_date.startswith('0000-00-00') and mainland_release_date != '':
            year = mainland_release_date
        if year == 'NULL' or year == '' or year == '0000-00-00':
            return ''
        return year.split('-', 1)[0]
    except ValueError:
        return year


def evaluate_zhegnpian(jsonStr, target):
    if jsonStr is None or jsonStr == "":
        return 0
    try:
        if jsonStr is not None:
            for c in jsonStr:
                if c == target:
                    return 1
    except ValueError:
        return 0
    return 0

def evaluate_area(areas):
    res = ''
    try:
        if areas is not None:
            list_c = json.loads(areas)
            for c in list_c:
                print c
                if res != '':
                    res += '\x01'
                res += c
    except ValueError:
        return ''
    return res

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

def evaluate_dig(targetStr):
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

# def parseUGCTitle_kubox(aliasJson):
#     #["{\"alias\":\"战警也疯狂\",\"type\":0}","{\"alias\":\"暗夜奔袭狂\",\"type\":0}","{\"alias\":\"Dark Asylum\",\"type\":1}","{\"alias\":\"Return To Death Row\",\"type\":1}"]
#     res = ''
#     if aliasJson is None or aliasJson == '':
#         return ''
#     aliasJson = aliasJson.decode("utf-8").lower()
#     aliasList = json.loads(aliasJson)
#     for aliasObj in aliasList:
#         if res != '':
#             res += ','
#         res += str(aliasObj['alias'])

def parseTitle(alias_json):
    if alias_json is None or alias_json == 'NULL':
        return alias_json
    try:
        alias_json = alias_json.decode("utf-8").lower()
        alias = json.loads(alias_json)
    except ValueError:
        return alias_json

    alias_list = []
    for line in alias:
        alias_list.append(line['alias'])

    return ','.join(alias_list).encode("utf-8")

def evalue_forbid(key, source):
    if key == "" or key is None:
        return 1
    if source != 2 and source != 3:  # 只检查 神马和优酷搜索词
        print source
        return 0
    reg_downGrade = [".*(大全|全集).*", ".*(dvd版|完整版|国语版|蓝光版|免费).*", ".*(在线|哪个视频播|哪里看|哪一集).*", ".*[0-9]+集.*",
                     ".*(迅雷|yy|豆瓣|优酷|百度|爱奇艺|腾讯|土豆|搜狐|西瓜影音).*"]
    isForbid = False
    for reg in reg_downGrade:
        re_res = re.search(reg, key)
        print reg
        if re_res is not None:
            return 1
    if not isForbid:
        return 0


if __name__ == '__main__':
    print evalue_forbid("军师联盟虎啸龙吟在线看", 3)
    #print parseTitle("""[{"type":"0","alias":"美女与野兽 3D版"},{"type":"1","alias":"Beauty And The Beast 3D"}]""")
    #print evaluate_date_showinfo("0000-00-00 12:00:00", "2004-10-26 12:00:00", "2004-10-26 12:00:00")
    #print evaluate_zhegnpian(["正片", "预告片"], "正片")
    #print evaluate_area('["美国","日本"]')
    #print evaluate_dig("BBC之旅行者号 探 测器冲出太阳系")
    #evaluate_scgTime()
    # print evaluate_fea(3,"谢娜菠萝蜜歌曲", 123)
    #print evaluate_country("[\"china\",\"usa\"]")
    #print evaluate_cate("微微一笑第十季", "episode")
    #print evaluate_diiCtrlA("12;43;56", ";")
    #print evaluate_person(person_json)
    #evaluate(str, "device_disabled")


