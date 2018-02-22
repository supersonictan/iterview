# -*- coding: utf-8 -*-

import string
import types
import datetime
import time
import sys as _sys,re



CN_NUM = {
    u'〇' : 0, u'一' : 1, u'二' : 2, u'三' : 3, u'四' : 4, u'五' : 5, u'六' : 6, u'七' : 7, u'八' : 8, u'九' : 9, u'零' : 0,
    u'壹' : 1, u'贰' : 2, u'叁' : 3, u'肆' : 4, u'伍' : 5, u'陆' : 6, u'柒' : 7, u'捌' : 8, u'玖' : 9, u'貮' : 2, u'两' : 2,
}
CN_UNIT = {
    u'十' : 10,
    u'拾' : 10,
    u'百' : 100,
    u'佰' : 100,
    u'千' : 1000,
    u'仟' : 1000,
    u'万' : 10000,
    u'萬' : 10000,
    u'亿' : 100000000,
    u'億' : 100000000,
    u'兆' : 1000000000000,
}
CN_NUM_SET = CN_NUM
CN_NUM_SET.update(CN_UNIT)
CN_NUM_SET = set(CN_NUM_SET)


def pickChineseNum(text):
    if not text:
        return []
    result = []
    tmp = ''
    i = 0
    while i < len(text):
        cn = text[i]
        if cn in CN_NUM_SET:
            tmp = ''
            while i < len(text) and text[i] in CN_NUM_SET:
                tmp += text[i]
                i = i + 1
            i = i - 1
            all_unit = 1
            for each in tmp:
                if each not in CN_UNIT:
                    all_unit = 0
                    break
            if all_unit:
                if tmp[0] == u'十':
                    if len(tmp) > 1:
                        result.append((False, tmp[-1:]))
                    else:
                        result.append((False, tmp[0]))
                else:
                    result.append((False, tmp))
            else:
                if len(tmp) >= 2:
                    has_unit = False
                    for each in tmp:
                        if each in CN_UNIT:
                            has_unit = True
                            break
                    if has_unit:
                        result.append((True, tmp))
                    else:
                        for each in tmp:
                            result.append((True, each))
                else:
                    result.append((True, tmp))
        else:
            tmp = ''
            while i < len(text) and text[i] not in CN_NUM_SET:
                tmp += text[i]
                i = i + 1
            i = i - 1
            result.append((False, tmp))
        i = i + 1
    return result



uselessWord_list = ["先导预告片","新剧场版序","新剧场版","攻略版","剧场版","大陆版","香港版","日本版",
            "加长版","印度版","美国版","剪辑版","法国版","电影版","英国版","内地版","真人版","胡歌版",
            "特别版","韩语版","日华版","卡通版","动画版","日版","假日版","台湾版","现场版","中文版",
            "巡演版","成人版","虐杀版","第二版","游戏版","僵尸版","公映版","冬季版","DVD版","日语版",
            "TV版","韩国版","英文版","英语解说版","纯音乐版","有声漫画版","十二星座版","粤语版",
            "世界版","澳洲版","国际版","国语版","FLASH版","幼儿版","演出版","完整版","分集版",
            "中国版","明星版","未删减版","人教版","北师大版","苏教版","外研版","精编版","网络版",
            "泰国版","短剧版","日文版","VR版","弹幕版","方言版","Web版","闽南语版","亚洲版","启蒙版",
            "纪念版","终结版","荷兰版","阿拉伯语版","傍晚版","午间版","晚间版","动漫版","tv版","q版",
            "迷你版","彩色版","PC版","好莱坞版","舞蹈版","英语版","3D版","OVA版","重制版","真实版",
            "奥地利版","德国版","街球版","巴西版","江华版","张智霖版","周渝民版","温碧霞版","国内版",
            "胡军版","歌舞版","改编版","激情版","收藏版","家装版","日播版","音乐配音版","央视版","宁夏版",
            "成长版","特摄版","北京卫视版","卫视版","秋季版","先行版","OTT版","春季版","古装版","会员独享版",
            "范冰冰版","东映版","浙江版","贺岁版","紀念版","最终版","泰语版","现代版","上午版","早间版",
            "经典版","黑白版","俄罗斯版","终极版","李亚鹏版","林家栋版","焦恩俊版","好男儿版","蒋勤勤版","郑少秋版",
            "日剧版","周润发版","赵文卓版","丹麦版","复刻版","偷情版","情色版","年轻版","英文字幕版","珍藏版","夏季版",
            "周播版","海外版","录象带版","原声版","精华版","修改版","限量版","网络放送版","澳大利亚版","周间版","周末版",
            "2D版","贴剧版","高清版","少年版","暑期版","现实版","时装版","京都版","西班牙版","爱尔兰版","川话版","ova版",
            "新版","豪华版","抢鲜版","张艾嘉版","吴启华版","裴勇俊版","吕颂贤版","古天乐版","精简版","陈小艺版本","乔振宇版","邓超版",
            "梁朝伟版","陈小春版","苏有朋版","浙版","韩版","陈楚河版","未删版","新加坡版","金在元版","英文原版","免费版","陈德容版",
            "马景涛版","官方版","范文芳","TVB版","原音版","20年代版","梅婷版","修复版","清晰版","改头换面版","墨西哥版","甄子丹版",
            "內地版","网友版","潘迎紫版","周杰版","何超仪版","波兰版","刘晓庆版","流畅版","萧蔷版","480P版","土豆版","周星驰版","张国荣版",
            "贾静雯版","港版","正式版","韩剧版","刘德华版","张卫健版","黄晓明版","刘德凯版","汤镇宗版","意大利版","李钊版","国语+英语",
            "梁家仁版","高力强版","TV","日剧","OVA","国语","粤语","加拿大版","音乐版","牛人"]
def evaluate_keyword(show_keyword, show_name):
    if show_keyword == "" or show_keyword is None:
        return show_keyword
    arr = show_keyword.split(',')
    res = []
    if "之" in show_name or ":" in show_name or "：" in show_name:
        if len(arr) == 1:
            return show_keyword

        for key in arr:
            if len(key.decode('utf-8')) <= 2:
                continue
            if key not in res:
                res.append(key.strip())

        # 去除版本
        for useless in uselessWord_list:
            if useless in show_name:
                show_name = show_name.replace(useless, "")
                # break

        # 去除 第几季
        replace_reg = re.compile(r'第(一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9)*(季|集|部|期)')
        show_name = replace_reg.sub('', show_name)

        # TODO 去除数字结尾

        if show_name not in res:
            res.append(show_name.strip())

        replace_name = show_name
        replace_word = ""
        if "之" in show_name:
            replace_word = "之"
        elif ":" in show_name:
            replace_word = ":"
        elif "：" in show_name:
            replace_word = "："

        replace_name = replace_name.replace(replace_word, "")

        if replace_name not in res:
            res.append(replace_name.strip())
        return ','.join(res)
    else:
        return show_keyword


def evaluate_spell_check( input_str):
    if input_str == "" or input_str is None:
        return input_str

        # 去除 版本 信息
    for useless in uselessWord_list:
        if useless in input_str:
            input_str = input_str.replace(useless, "")
            # break

        # 去除 第几季
    replace_reg_season = re.compile(r'第(一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9)*(季|集|部|期|篇|章)')
    input_str = replace_reg_season.sub('', input_str)

    # 去除 数字结尾
    replace_reg_season = re.compile(r'([0-9]|一|二|三|四|五|六|七|八|九|十)*$')
    input_str = replace_reg_season.sub('', input_str)

    # 去除数字开头


    return input_str

def evaluate4( title1, title2):
    title1 = title1.decode('utf8').strip()
    title2 = title2.decode('utf8').strip()
    if title1 == title2:
        return 1
    else:
        return 0



if __name__ == '__main__':
    qid = 3357378705
    data = 100000
    if qid is not None and data is not None:
        # print(bin(3))
        qid = qid & 0xffffffff
        qid = qid << 31
        print(bin(qid))
        print(bin(data))
        if (data & 0x80000000) != 0:
            data = data & 0x7fffffff
        res = qid | data
        #print bin(res)
        print(res)

        mask = 1
        for i in range(31):
            mask |= 1 << i
        print(bin(res >> 32))
        print(bin(res & mask))
    else:
        print None

