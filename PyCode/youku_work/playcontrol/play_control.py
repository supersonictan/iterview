#!/usr/bin/python
# -*- coding=utf-8-*-
import json,re

chnl_reg_list = [".+综艺", ".+电影", ".+电视剧", ".+视频"]
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



if __name__ == '__main__':
    print evaluate_cate("微微一笑第十季", "episode")
    #print evaluate_diiCtrlA("12;43;56", ";")
    #print evaluate_person(person_json)
    #evaluate(str, "device_disabled")


