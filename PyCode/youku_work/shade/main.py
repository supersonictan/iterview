#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import Queue
import sys
import json,re
import threading
from Logger import *
import time
#http://www.cnblogs.com/pastgift/p/3985032.html
import Global
reload(sys)
sys.setdefaultencoding('utf-8')


porn_reg_str1 = r'(脱裤子|避孕|一夜情|激情|夫妻|内内|肚兜|床叫|叫床|床叫|女仆|骄喘|不雅|呻呤|呻吟|叫春|活儿好|女大学生|亲热|接吻|激吻|强吻|凸点|外阴|咪咪|车震|下体|小便|床戏|网站|黄网|黄色视频|色情|情色|成人|看片|生孩子|性戏|精液|灌肠|诱|妓女|女服务员' \
             r'|伦奸|车震|脫衣服|上床全脱|无内见毛|在卫生间|性服务|偷情|齐b|日本激情|韩国激情|激情片|情色电影|舌吻激情|占新娘便宜|床战|飞机杯|男同性|女同性|阴茎|睡觉玩脚|乳晕|上吊自杀|紧身透明|掐脖子勒死|床上观戏|日皮|进入肚子里|穿白丝|乳胶真空床|陪睡|抓要害|滚床|挠脚心|无内|见毛|捉奸在床|奸尸|啊啊|啊不要|公交车上|胸模|车模|丝袜|自慰|保射|性关系|性生活|高潮|性爱|性器官|xxx|性伴侣|性教育|亲吻|性生活|坐台|我操|我曹|你妹的|你大爷|妈逼|你妈的|黑社会|邪恶|基情|g奶|r戏|R戏|早恋|怀孕了|女性|男女|女老师|秘书' \
             r'|宋梓馨后入|上过床|去宾馆|开宾馆|开酒店|美乳|没穿衣服|乱伦|乱仑|通奸|情乳|母子不论|姐弟不论|胖次|揉胸|婶婶与|嫂子与|寂寞的寡妇|乳沟|性姿势|被下了药|踢裆|小姐|性侵|色诱|体位|十八禁|十九禁|18禁|19禁|肛交|女主播|大尺度|成人用品|g点|G点|猥亵|夜店|睡了|迷药|艳门照|艳照门|劈腿|女优|交配|寡妇|大保健|大宝剑|生殖器|做爱|男女|三级片|三及片|三彶|a片|强女干|滚床单' \
             r'|a 片|钻裤裆|上床片|脱戏|露沟|卫生间激战|房事|丁丁|情趣|欺负|性感|开房|野战|上床|诱惑|性奴|男人模女人|撕衣|女人被|美女被|帅哥被|女孩儿被|男孩儿被|男人被|搞鸡|搞基|会阴|阴道|分娩|应召女郎|射精|卖淫|口交|性交|乳交|嫖娼|打炮|艹|胸罩|激凸' \
             r'|在办公室|在车上做|在飞机卫生间|在床做|在酒吧卫生间|写真乳|直播换衣|车上激情|虐|模胸吻|帅哥|鬼子|约炮|强奸|凌辱|强暴|迷奸|强歼|第一次|插不进去|初夜|处男|处女|色舞|熟女|美女|男人和|输一次脱一件|女人和|亲嘴|美胸|美足|美脚|宅男福利|深夜福利|洗澡|情欲|卵巢|按摩|露点|爱爱|情侣|震动棒|振动棒' \
             r'|衣服脱|借种生子|轮干|自拍|成年人|暴露|男女|性生|约女|迷晕|日比|日逼|污污|日笔|日批|爱情动作|情趣内衣|艳舞|美臀|丰臀|强干|啪啪|潜规则完整|露b|露逼|小三|喂奶|诱人|床上戏|黑丝|禁果|长腿|直播怀孕|接客|性早熟|的胸|二货|电臀|母乳|乳腺' \
             r'|A片|欲情|深喉|荡妇|真空透明|抓胸|性大片|黄片|片黄|奶秀|抖奶|明见毛|明见奶|禁播|裸戏|小女孩洗澡|玷污|裸体|裸男|裸女|人妻|大奶|大胸|大屌|拐卖|掐死|杀死|杀人|碎尸|g奶|g罩|e奶|罩杯|小姐|模特|黄色|sex|sm|捆绑' \
             r'|糟蹋|羞羞事|羞羞的事|男女羞羞|护士|床片|mmd|mm踩踏|勾引|mp4|导尿管|私阴|乳胶衣|爱情片段|日本女人|6间房|六间房|00后|调戏|小鸡|几把|鸡巴|阳具|滴蜡|扒光|跳蛋|性玩具|日本鬼子|女学生|扇耳光|xxoo|扇耳光|袭胸|伴娘|摸xiong|欲望|上了床|偷窥|三点|全露' \
             r'|裸|两女一杯|动作片爱情|生下了孩子|女沐浴|男孩鸡鸡|岁以下不可看|直播没穿内衣|直播福利|直播桃子|17禁|乳液晶|岁以下不准看|羞羞视频|岁以下禁看|女破处|18摸|级毛骗|毛片|色性片|露毛|女同舌吻|3g片最黄|3彶片|3及大片|一级片|三级|性和爱|a级|吃人奶|打屁屁|截肢|吻戏|湿身|舔耳|撸管|小姨|车震|下药|大乳|翘臀|傻逼|傻b|煞笔|沙比|污段子|杜蕾斯|字幕版|裸露|裸下体|乳环|阴环|鸭片|大波|波霸|啊啊啊|好爽|受不了|不要啊|不要停|嫂子|小叔子|脱衣|pornhub|同性恋|男男|少妇|站街女|尿|屎|女人|男人|三片级|三片及|打pp' \
             r'|装逼|搞g|靠逼|禁片|好色|尺度|扯裙子|裙底|胸大|胸器|军妓|慰安妇|被轮|被干|被草|被操|被艹|被亲|被吻|上了大嫂|取精|包养|钢管舞|冰毒|冰妹|臀|吸毒|男公关|女公关|淫荡|卖淫|甩臀|淫|光身子|骂|绑架|屁股|打孩子|骚|帅哥|裸奔|透视|变态|色妹|杂交|脱光|丝袜|黑丝|做片爱|空姐' \
             r'|吻床|小弟弟|激情过后|柳岩床|柳岩床|柳岩内衣|不伦之恋|丈母娘和女婿|女婿和丈母娘|色剧情片|性全过程|成年大片|三激片|欲爱|性片|性过程|国文版|床爱|特殊服务|上小树林|十八摸|娇喘|床事|性生性活|一丝不挂|艳情|小姨妹|黄片|小姨子|传销|色狗|女秘书|脱衣舞|短裙|乳摇|一起睡觉|女生脱|女人脱|屏蔽|禁播|大便|乳房|短裤|妹子|洞洞|黄段子|便秘|腹部|jj|寂寞|发生关系|性行为|脱了|人和狗|大腿|强奷|出轨|色欲|妈妈的朋友|强行|被脱|被带走|色狼|爽片|少儿不宜|强行|伦理片|被强|制服|巨乳|丰满' \
             r'|无打底|嘿咻|被日本人|被人睡|被别人玩|电影激戏|韩国性与爱|韩国戏吻|显鲍鱼|甩奶舞|爱情床|招嫖|禁放片|三汲|最露的一次|人配狗|狗配人|狗配猪|人配人种|马配驴|牛配驴|人配人|人狗交|狗配猫|狗日人|马配牛|性姣配|人日母|狗与猪|马交马配|马驴交|公狗|母狗|晕倒|勒死|人日母|人狗交|咬配|性配|柳岩奶|柳岩胸|老公不在家|最想删掉的|全过程|太黄了|床胸戏|床激日本|激床情|舌吻|边亲边搞|西门庆与潘金莲|私密处|三片|老公轻点|忍不住射|摸上去|边亲边|边脱边|一边亲|一边摸|一边脱|色亲|爽到|黄8昂|好痛轻点|色亲|爽啊|叫爽|两性|柳岩露|性胶|胸衣|激床|床激|床性|做艾|床胸戏|猛干|性叫|爱床|性教欲|性感尤物|性爱娃娃|做性|动态图|性技巧|成年用品|后入式|两性动态图|性叫声|色爽|同房|爽爽|叫爱床声|三急片|性生活|情爱片|性ao|做受|又色又|又黄又|成人|性开放|黄带|成片人|日本性|日本x片|日本小姐|日本a优|床色|性用品|性满足|日本av|包小姐|日本小妞|性动作|男妓|鸭子男|男奴|女奴|富婆|寂寞难耐|偷汉子|男妓女娼|性派对|抢奸|女犯|绑起来|情人|色字当头|三j片|爱情片全黄|性插|全黄|最黄|十八岁|三节片|情片色|日本一片级|黄i色1及|全脱|色女|色男|片段色|日本伦俚片电影|偷奸|水浒传色|色爱|假戏真做|污视频|做羞羞|很黄|很污|很色|一吻二脱三床|色床|偷倩|色黄|最污|18岁|脱吻|骗财骗色|亲觜视频|视频黄|电影黄i色|卖身|全黄带|删减|男和女|奸情|干逼片|最黄|最色|充气娃|三机片|卫生间|配种|逼|按在桌子上干|搞b|人日人|找鸭|三爱|办公室|在飞机上干|性本爱|三纪片|一片级|黄碟|被别人干|三经片|红灯区|嗯啊轻点|被鞭打|在车上|浴室|脚搓脚|春药|蒙汗药|发情|闺蜜|潜规则|妓院|在沙发|不堪入目|试衣间|灌醉|禽兽|陪酒女|骗奸|开苞|女子被|失身|遭蹋|强迫|采花贼|醉酒女|施暴|女子醉酒|胶带kb|挠痒痒|绑起来|女子不反抗)'
# v+n
porn_reg_str2 = "(伸进|侵犯|捏|扒|晃|榨|秀|撕|露|亲|推倒|推导|偷|脱|吻|摸|揉|抖|蹭|蹂躏|摇|奸|强脱|失足|上床|舔|强|插).*(下半身|穴|衣服|丰满|奶|女|黑丝|超短|裤|内|衣|胸|鲍|衣裤|裙子|袜子|乳|腿|肚脐|脐|脚|妹子|短裙|臀|逼|不进去|下身|下体|下面|下边|全身|pp)"
# n+(n/v)
porn_reg_str3 = "(车展|车模|女|男|情侣|mm|小姐|大嫂|嫂子|嫂嫂|男子|老公|闺蜜|导演|上司|护士|老头|大叔|养父|哥哥|老师|老汉|服务员|丈母娘|岳母|婶子|管家|姨太太|弟媳).*(与|找|包|打|奸|上|强上|被|和|洗浴|拉客|干|喝醉|三兄弟|灌醉|失足|床|双飞|露|透明|无打底|丰满|奶|黑丝|超短|裤子|内|衣|胸|鲍|衣裤|裙子|袜子|乳|腿|肚脐|脐|脚|妹子|短裙|臀|逼|不进去|下身|下体|下面|全身|衣服)"
# adj开头
porn_reg_str4 = "^(女上|之|av).*"
# 黄色
porn_reg_str5 = "(色|黄|性|三级|成年|情爱片|三片|强上|床系|城人|污).*(视频|电影|电视剧|片|直播|录像带|技巧|姿势|过程)"
# str2的倒过来
porn_reg_str6 = "(衣服|丰满|奶|女|黑丝|超短|裤|内|衣|胸|鲍|衣裤|裙子|袜子|乳|腿|肚脐|脐|脚|妹子|短裙|臀|逼|不进去|下身|下体|下面|全身|pp).*(侵犯|插|捏|扒|晃|榨|秀|撕|露|亲|推倒|推导|偷|脱|吻|摸|揉|抖|蹭|蹂躏|摇|奸|强脱|失足|上床|舔|强)"
#str3倒过来
porn_reg_str7 = "(奸|强上|洗浴|拉客|喝醉|三兄弟|灌醉|失足|床|双飞|露|透明|无打底|丰满|奶|黑丝|超短|裤子|内|衣|胸|鲍|衣裤|裙子|袜子|乳|腿|肚脐|脐|脚|妹子|短裙|臀|逼|不进去|下身|下体|下面|全身|衣服).*(婶子|管家|姨太太|丈母娘|岳母|车展|车模|女|男|情侣|mm|小姐|大嫂|嫂子|嫂嫂|男子|老公|闺蜜|导演|上司|护士|老头|大叔|养父|哥哥|老师|老汉)"

# 预编译
porn_pat_1 = re.compile(porn_reg_str1)
porn_pat_2 = re.compile(porn_reg_str2)
porn_pat_3 = re.compile(porn_reg_str3)
porn_pat_4 = re.compile(porn_reg_str4)
porn_pat_5 = re.compile(porn_reg_str5)
porn_pat_6 = re.compile(porn_reg_str6)
porn_pat_7 = re.compile(porn_reg_str7)

porn_reg_list = [porn_pat_6, porn_pat_1, porn_pat_2, porn_pat_3, porn_pat_4, porn_pat_5, porn_pat_7]


def fun(text1, text2):
    text1 = text1.decode('utf8')
    text2 = text2.decode('utf8')

    text_min_len = min(len(text1), len(text2))
    for i in range(text_min_len):
        if text1[i] != text2[i]:
            print(i)
            break


class CrfTerm(object):
    def __init__(self,term, position, label):
        self.term = term
        self.position = position
        self.label = label


if __name__ == '__main__':
    terms = "者###魔法战队###魔法###连"
    positions = "3###0###1###2"
    labels = "I-SHOW###B-SHOW###B-SHOW###I-SHOW"

    term_list = terms.split('###')
    pos_list = positions.split('###')
    label_list = labels.split('###')

    crf_term_list = []

    if len(term_list) != len(pos_list) or len(term_list) != len(label_list):
        pass

    for i in range(len(term_list)):
        crf_term_list.append(CrfTerm(term_list[i], pos_list[i], label_list[i]))

    crf_term_list.sort(cmp=None, key=lambda x: x.position, reverse=False)

    bmerge = False

    for i in len(crf_term_list):
        label = crf_term_list[i].label

        if '-' in label:
            curBI = label.split('-')[0]
            curTag = label.split('-')[1]

        else:
            bmerge = False




    # 当前B:判断next是I，追加。next是B
    preBI = ''
    preTag = ''
    curBI = ''
    curTag = ''
    nxtBI = ''
    nxtTag = ''
    hasBeginPre = False

    res = []

    for i in len(crf_term_list):
        label = crf_term_list[i].label

        if '-' in label:
            curBI = label.split('-')[0]
            curTag = label.split('-')[1]
        else:
            curBI = ''
            curTag = label

        if i != len(crf_term_list) - 1:
            labelNxt = crf_term_list[i + 1].label

            if '-' in labelNxt:
                nxtBI = labelNxt.split('-')[0]
                nxtTag = labelNxt.split('-')[1]
            else:
                nxtBI = ''
                nxtTag = labelNxt
        else:
            nxtBI = ''
            nxtTag = ''

        # 逻辑



        # 结尾处理
        preBI = curBI
        preTag = curTag
        curBI = ''
        curTag = ''
        nxtBI = ''
        nxtTag = ''

#
# 追剧特征
# 追剧模型
# 宣发剧找人
#
# trigger select