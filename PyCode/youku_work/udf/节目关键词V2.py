#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,re,time,types,datetime,sys
import json


def yt_get_keyword2(show_name):
    reg1 = r"[^0-9]+([0-9]+)$"

    match_obj = re.search(reg1, show_name)

    print(match_obj.group(1))
    # if match_obj:
    #     text = match_obj.group(0)
    #     return text

    return None

def splitMaoHao(word):
    word = word.decode('utf-8')
    print(word)
    word = word.encode('utf-8')
    print(word)


def yt_get_keyword(show_name, meta_keyword):
    meta_keyword = str(meta_keyword)
    meta_keyword = meta_keyword.decode('utf-8')
    # list = [',', '，', ':', '：', ';', '；', '!', '！']
    # 去除数字结尾
    res = []
    field = meta_keyword.split(',')
    for i in field:
        i = re.sub(r'\b\d{1}$|\d{4}$', "", i)
        res.append(i)

    return ','.join(res)



uselessWord_list = ["）","（", ")", "(", "蓝光版","先导预告片","新剧场版序","新剧场版","攻略版","剧场版","大陆版","香港版","日本版",
            "加长版","印度版","美国版","剪辑版","法国版","电影版","英国版","内地版","真人版","胡歌版","粤语中字",
            "特别版","韩语版","日华版","卡通版","动画版","日版","假日版","台湾版","现场版","中文版",
            "巡演版","成人版","虐杀版","第二版","游戏版","僵尸版","公映版","冬季版","DVD版","日语版",
            "TV版","韩国版","英文版","英语解说版","纯音乐版","有声漫画版","十二星座版","粤语版",
            "世界版","澳洲版","国际版","国语版","FLASH版","幼儿版","演出版","完整版","分集版",
            "中国版","明星版","未删减版","人教版","北师大版","苏教版","外研版","精编版","网络版",
            "泰国版","短剧版","日文版","VR版","弹幕版","方言版","Web版","闽南语版","亚洲版","启蒙版",
            "纪念版","终结版","荷兰版","阿拉伯语版","傍晚版","午间版","晚间版","动漫版","tv版","q版",
            "迷你版","彩色版","PC版","好莱坞版","舞蹈版","英语版","3D版","OVA版","重制版","真实版",
            "奥地利版","德国版","街球版","巴西版","江华版","张智霖版","周渝民版","温碧霞版","国内版",
            "胡军版","歌舞版","改编版","激情版","收藏版","家装版","日播版","音乐配音版","央视特别版","央视版","宁夏版",
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
            "梁家仁版","高力强版","TV","日剧","OVA","国语","粤语","加拿大版","音乐版","牛人","豪华篇","恩氏传媒","欧洲篇上","欧洲篇下","08圣诞特别篇","金鹰纪实",
            "最终章","特别篇","粤语","音乐篇","名胜篇","工艺篇","美食篇","幻影篇","自立篇","现代篇","完结篇","青云篇", "爱憎篇", "怒涛篇","袭击篇",
            "最终篇","终篇","争斗篇","魔像解决篇","劳动篇","关东篇","乐园篇","过去篇","工场记活剧篇","中篇","田园篇","战争篇","教育篇","产业篇","恋爱篇","OAD",
            "II", "III","特辑","续集","前集","后集","前部","后部","千禧特辑","赏花特别篇","自然原声版","新篇","中文中字","中字","电视特别篇","高清重制版","自然原声版",
            "赏花特别篇","特典","湖北卫视版","普通话版","(UHD版)","完整普通话版","普通话版"]

def show_keyword_long_new(show_name, keyword, sub_keyword):
    show_name = show_name.decode('utf8')
    # keyword = keyword.decode('utf8')
    # sub_keyword = sub_keyword.decode('utf8')
    show_name_trim = show_name
    res = []

    # 去除无用词
    for useless in uselessWord_list:
        useless = useless.decode('utf8')
        if useless in show_name:
            show_name = show_name.replace(useless, "")

    # 去除第n部
    replace_reg = re.compile(u'第(一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9)*(季|集|部|期|卷)')
    show_name = replace_reg.sub('', show_name)

    # 去除数字
    show_name = re.sub(r'\b\d{1}$|\d{4}', "", show_name)

    # 去除乱七八糟
    reg = "[！|\!|·|、|,|▪|－|，| |・|\-|:]+".decode("utf8")
    show_name_trim = re.sub(reg, "".decode("utf8"), show_name)
    #show_name = re.sub(reg, "".decode("utf8"), show_name)

    # 解析 sub keyword
    if sub_keyword is not None and sub_keyword <> '':
        sub_field = sub_keyword.split(',')
        keyword_field = keyword.split(',')
        res_keyword = ''.join(keyword_field)
        res_keyword += ''.join(sub_field)
        res.append(res_keyword)

    res.append(show_name.encode('utf8'))
    res.append(show_name_trim.encode('utf8'))

    # 最终结果和keyword、sub_keyword 去重
    res = list(set(res))
    if keyword in res:
        res.remove(keyword)
    if sub_keyword in res:
        res.remove(sub_keyword)

    return '###'.join(res)




def alias_keyword(show_alias):




#in (21918, 219189, 222904, 224358,217589,227117,238046,274271,276185,55715,181845,)


if __name__ == '__main__':
    # s = ['早间新闻-新疆 2010','火影忍者 晓之卷','醉生梦死之湾仔之虎','铃铛猫娘 星之旅 剧场版', '湾仔之虎之醉生梦死',
    #      "耶鲁大学公开课:资本主义的成功 危机和改革"]
    # for show_name in s:
    print show_keyword_long_new('牛群: 2017', "萌学园" ,"")
    # s = "[10020,10021,10023,20716,49161]"
    # res = json.loads(s)
    # for i in res:
    #     print(i)
    # print(yt_get_keyword("恶魔咆哮3:地狱门前", '地狱s门前2,恶魔咆哮'))
    #print yt_get_keyword("第87届奥斯卡金像奖颁奖典礼第二季")