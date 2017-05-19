#!/usr/bin/python
# -*- coding=utf-8-*-
import requests
import json
from Logger import *
import copy
import re
from requests.adapters import HTTPAdapter
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

logger = Logger(logFileName='diff.log', logger="feature_score").getlog()

match_reg = 'YoukuOGCShowTermMatchFeatureExtractor::calScore end.*?\)'
noMatch_reg = 'YoukuOGCShowNoMatchTermRatioFeatureExtractor::calScore end.*?\)'
idExt_reg = 'YoukuShowIdExtFeatureExtractor::calScore end.*?\)' #maybe null
min_window_reg = 'YoukuOGCShowTermMinwindowFeatureExtractor::calScore end.*?\)'
match_idx_reg = 'YoukuECBQueryMatchIdxFeatureExtractor::calScore end.*?\)'
key_value_reg = 'YoukuShowKeyValueMultiMatchFeatureExtractor::calScore end.*?\)'
episode_reg = 'YoukuShowEpisodeFeatureExtractor::calScore end.*?\)'

time_w = 50.0
newRelevance_w = 3.0
vv_w = 10.0
exclusive_w = 30.0
category_w = 50.0
satisfaction_w = 10.0
ctr_w = 20.0
quality_w = 5.0
allHit_w = 20.0

#final score
time_reg = 'YoukuECBTimeDecayFeatureExtractor::calScore end.*?\)'
new_relan_reg = 'YoukuShowNewRelevanceFeatureExtractor::calScore end.*?\)'
vv_reg = 'YoukuECBShowVVFeatureExtractor::calScore end.*?\)'
exclusive_reg = 'YoukuECBExclusiveFeatureExtractor::calScore end.*?\)'
category_reg = 'YoukuCategoryRatioFeatureExtractor::calScore end.*?\)'
satisfaction_reg = 'YoukuSatisfactionFeatureExtractor::calScore end.*?\)'
ctr_reg = 'YoukuQueryCtrPredFeatureExtractor::calScore end \(return .*?\)'
quality_reg = 'YoukuQualityFeatureExtractor::calScore end.*?\)' #YoukuQualityFeatureExtractor::calScore end -> return 0.040000 YoukuECBFakeFeatureExtractor::calScore begin()
all_hit_reg = 'YoukuShowAllHitFeatureExtractor calScore end \(return.*?\)'
#all_hit_reg = 'YoukuShowAllHitFeatureExtractor::.*all_hit:[0,1]{1}'

str1 = """
[TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=1 [TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=1 [TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=2 [TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=1 [TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=1 [TRACE1] [build/release64/ha3/rank/DefaultScorer.cpp:69]tf=1 relation info debug start: aliasSeg1TermsTotal size:11 YoukuECBTimeDecayFeatureExtractor::calScore begin latestTime -> 1460908800 latestTime:-> 1460908800 diffYear:--->1.101300 YoukuECBTimeDecayFeatureExtractor::calScore end -> (return 0.782119) YoukuOGCShowTermMatchFeatureExtractor::calScore begin ###QueryTerm-> term_id:1532352141, term_weight:5 ###flag2_term-> term_id:1532352141, term_weight:5 ###flag2_finger-> finger:1532352141 doc_type:1, showId:300647 ###showName_term: 1532352141:151866 ###Show_0_Alias_Seg1: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 ###Show_0_Alias_Seg3: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 ###showSubTitle_term: 2057756809:123027,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241^1753666375:67396,1649084386:30000,1720877358:97842,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241 ###Doc Semantics--->1532352141 semantic_match_rate=1.000000 ###Semantic_Full_Match YoukuOGCShowTermMatchFeatureExtractor::calScore end (return 111.000000) YoukuOGCShowNoMatchTermRatioFeatureExtractor::calScore begin YoukuOGCShowNoMatchTermRatioFeatureExtractor::show alias ###Show_0_Alias_Seg1: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 ###Show_0_Alias_Seg3_0: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 queryInfo-> term_id:1532352141, term_weight:5 doc_type:1, vdoId:0, showId:300647 showName : 1532352141:151866 showSubTitle : 2057756809:123027,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241^1753666375:67396,1649084386:30000,1720877358:97842,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241 begin calculate Query&Show Name textStr:1532352141:151866 need term min seg : 0 Show Name Seg1 textTermSum:1, noMatchTextTerm:0 -> noMatchTextTermRatio:0.000000 Show Name Seg1 textTermWeightSum:15.186600, noMatchTextTermWeight:0.000000 -> noMatchTextWeightRatio:0.000000 Show Name Seg3 textTermSum:0, noMatchTextTerm:0 -> noMatchTextTermRatio:0.000000 Show Name Seg3 textTermWeightSum:0.000000, noMatchTextTermWeight:0.000000 -> noMatchTextWeightRatio:0.000000 Show Name queryTermSum is 1, noMatchQueryTerm is 0, noMatchQueryTermRatio is 0.000000 Show Name queryTermWeightSum is 5, noMatchQueryWeight is 0, noMatchQueryWeightRatio is 0.000000 Show Name queryTermSum is 1, noMatchQueryTerm is 0, noMatchQueryTermRatio is 0.000000 Show Name queryTermWeightSum is 5, noMatchQueryWeight is 0, noMatchQueryWeightRatio is 0.000000 begin calculate Query&Show Alias Alias Name 1 textTermSum:5, noMatchTextTerm:5 -> noMatchTextTermRatio:1.000000 Alias Name 1 textTermWeightSum:24.675000, noMatchTextTermWeight:24.675000 -> noMatchTextWeightRatio:1.000000 Alias Name 1 queryTermSum is 1, noMatchQueryTerm is 1, noMatchQueryTermRatio is 1.000000 Alias Name 1 queryTermWeightSum is 5, noMatchQueryWeight is 5, noMatchQueryWeightRatio is 1.000000 Alias Name 3 textTermSum:5, noMatchTextTerm:5 -> noMatchTextTermRatio:1.000000 Alias Name 3 textTermWeightSum:24.675000, noMatchTextTermWeight:24.675000 -> noMatchTextWeightRatio:1.000000 Alias Name 3 queryTermSum is 1, noMatchQueryTerm is 1, noMatchQueryTermRatio is 1.000000 Alias Name 3 queryTermWeightSum is 5, noMatchQueryWeight is 5, noMatchQueryWeightRatio is 1.000000 ###Show_0_Alias_Seg: showAliasNoMatchRatio1: 1.000000,showAliasNoMatchRatio3: 1.000000 begin calculate Query&Show SubTitle textStr:2057756809:123027,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241^1753666375:67396,1649084386:30000,1720877358:97842,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241 need term min seg : 1 SubTitle Name Seg1 textTermSum:6, noMatchTextTerm:6 -> noMatchTextTermRatio:1.000000 SubTitle Name Seg1 textTermWeightSum:32.923700, noMatchTextTermWeight:32.923700 -> noMatchTextWeightRatio:1.000000 SubTitle Name Seg3 textTermSum:7, noMatchTextTerm:7 -> noMatchTextTermRatio:1.000000 SubTitle Name Seg3 textTermWeightSum:37.144800, noMatchTextTermWeight:37.144800 -> noMatchTextWeightRatio:1.000000 SubTitle Name queryTermSum is 1, noMatchQueryTerm is 1, noMatchQueryTermRatio is 1.000000 SubTitle Name queryTermWeightSum is 5, noMatchQueryWeight is 5, noMatchQueryWeightRatio is 1.000000 SubTitle Name queryTermSum is 1, noMatchQueryTerm is 1, noMatchQueryTermRatio is 1.000000 SubTitle Name queryTermWeightSum is 5, noMatchQueryWeight is 5, noMatchQueryWeightRatio is 1.000000 YoukuOGCShowNoMatchTermRatioFeatureExtractor showNameNoMatchRatio 0.000000 YoukuOGCShowNoMatchTermRatioFeatureExtractor showAliasNoMatchRatio 1.000000 YoukuOGCShowNoMatchTermRatioFeatureExtractor showSubTitleNoMatchRatio 1.000000 YoukuOGCShowNoMatchTermRatioFeatureExtractor::calScore end (return 11.000000) YoukuShowIdExtFeatureExtractor::calScore begin YoukuShowAllHitFeatureExtractor::calScore begin query all hit info-> finger:1532352141, str:欢乐颂 doc_type:1, vdoId:0, showId:300647 show all_hit has 2 index:0 show all_hit:1532352141 index:1 show all_hit:3998240685 all_hit:1 YoukuOGCShowTermMinwindowFeatureExtractor::calScore begin YoukuOGCShowNoMatchTermRatioFeatureExtractor::show alias ###Show_0_Alias_Seg1: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 ###Show_0_Alias_Seg3_0: termId:1714778771, weight:67346 termId:3370521906, weight:36000 termId:564197844, weight:49339 termId:3370521906, weight:36000 termId:3140873220, weight:58065 queryInfo-> term_id:1532352141, term_weight:5 doc_type:1, vdoId:0, showId:300647 showName : 1532352141:151866 showAlias : 1714778771:67346,3370521906:0,564197844:49339,3370521906:0,3140873220:58065 showSubTitle : 2057756809:123027,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241^1753666375:67396,1649084386:30000,1720877358:97842,1359667248:28207,4124399468:31729,3961377943:61033,1649084386:30000,2287749998:55241 begin calculate Query&Show Name max term : matchNum=1 querySize:1, startPos:0, endPos:0, minTermWindow:0 YoukuOGCShowTermMinwindowFeatureExtractor:: Show Name -> score:0.000000 begin calculate Query&Show Alias max term : matchNum=0 querySize:1, startPos:5, endPos:-1, minTermWindow:0 min term : matchNum=0 querySize:1, startPos:5, endPos:-1, minTermWindow:0 YoukuOGCShowTermMinwindowFeatureExtractor:: Alias Name 1 -> score:0.000000 ###Show_0_Alias_Seg: match num: 0,showAliasTermWinScore: 0.000000 final match num: 0,showAliasTermWinScore: 0.000000 begin calculate Query&Show SubTitle max term : matchNum=0 querySize:1, startPos:6, endPos:-1, minTermWindow:0 min term : matchNum=0 querySize:1, startPos:8, endPos:-1, minTermWindow:0 YoukuOGCShowTermMinwindowFeatureExtractor:: SubTitle Name -> score:0.000000 YoukuOGCShowTermMinwindowFeatureExtractor::calScore end (return 0.000000) YoukuECBQueryMatchIdxFeatureExtractor::calScore begin #####queryInfo-> term_id:1532352141, term_weight:5 showName : 1532352141:151866 showAlias : 1714778771:67346,3370521906:0,564197844:49339,3370521906:0,3140873220:58065 textStr:1532352141:151866 need term min seg : 0 #####ShowNameTerm-> Min_ShowName_term_id:1532352141 #####QueryTerm-> Query_term_id:1532352141 match_idx_min:0, match_idx_max:-1 QueryLength:1.000000, Query_len_weight:1.000000, Doc_len1, Match_idx:0, idx_weight:1.000000 YoukuECBQueryMatchIdxFeatureExtractor::calScore end (return 1.000000) YoukuShowKeyValueMultiMatchFeatureExtractor::calScore begin queryInfo(people)-> YoukuShowKeyValueMultiMatchFeatureExtractor::calScore end (people empty) YoukuShowEpisodeFeatureExtractor::calScore begin query Episode info-> doc_type:1, vdoId:0, showId:300647 YoukuShowEpisodeFeatureExtractor::calScore end (return 0.000000) YoukuShowNewRelevanceFeatureExtractor::calScore begin() vecDependFeature.size() = 8 YoukuShowNewRelevanceFeatureExtractor score: 96.454545 all_hit_score 90.000000 YoukuShowNewRelevanceFeatureExtractor::calScore end (return 96.454545) YoukuECBShowVVFeatureExtractor::calScore begin YoukuECBShowVVFeatureExtractor::calScore end -> (vv is:5275111383, log_score:3.922232, return 0.980587) YoukuECBExclusiveFeatureExtractor::calScore begin isExclusive:0 show_site_val:0 YoukuECBExclusiveFeatureExtractor::calScore end (exlusiveScore:0.000000,showSiteScore:0.500000, return 0.500000) YoukuCategoryRatioFeatureExtractor::calScore begin channelId:97 categoryMap-> (85:0.149200 (86:0.058500 (95:0.124700 (96:0.109000 (97:0.520900 YoukuCategoryRatioFeatureExtractor is Max Category YoukuCategoryRatioFeatureExtractor::calScore end -> (return 1.562700) YoukuSatisfactionFeatureExtractor::calScore begin YoukuSatisfactionFeatureExtractor::calScore end (return 1.500000) YoukuQueryCtrPredFeatureExtractor::calScore begin queryId:1532352141, queryCtrStr:3067344942:0.0;1530377101:0.03;2046740228:0.0;1962263989:0.0;270710806:0.0;3450018683:0.0;740261241:0.03;4183155011:0.0;2750506925:0.0;1390482775:0.0;2267211695:0.0;3635012015:0.0;1295846182:0.0;1528685227:0.0;1478394882:0.03;1997136871:0.0;3293856324:0.0;137822786:0.0;3838459053:0.0;2957745602:0.03;3815827783:0.0;1718498078:0.08;2174261894:0.0;729291228:0.0;2997629431:0.03;2570114574:0.0;200487603:0.0;3821395712:0.0;202590613:0.0;1768957092:0.0;3154201067:0.0;1736649041:0.0;1971976145:0.0;3263667325:0.0;4154238371:0.0;4203640926:0.0;2065150489:0.0;3606657242:0.0;1895848748:0.0;874430485:0.0;2483283694:0.07;1426688665:0.0;2792812793:0.0;121577671:0.0;1952495000:0.0;1089450564:0.0;3637807218:0.0;1261472684:0.13;196416596:0.08;949883535:0.03;1583813489:0.0;3908788708:0.0;1205988542:0.17;3778574284:0.0;1983287729:0.0;825374345:0.0;1728199988:0.0;1959746782:0.0;2480638161:0.0;1179919438:0.0;4099420386:0.0;2151156929:0.28;1705020062:0.0;3077515678:0.22;1016500716:0.0;1000977180:0.0;1727603452:0.0;2786152981:0.0;2408725923:0.14;2674094040:0.0;3784917102:0.0;3642656707:0.2;2253662641:0.06;1659211071:0.0;1225168711:0.0;2470246216:0.03;288419237:0.18;1837405848:0.0;1173289779:0.0;348833707:0.0;1017347700:0.03;2048530456:0.05;3913931648:0.0;3516518304:0.03;910155325:0.0;1563787201:0.0;220469584:0.0;26369217:0.0;84139288:0.0;3591075172:0.0;3466155095:0.0;2330764011:0.03;1689278521:0.0;520089095:0.03;721171101:0.0;1380928075:0.0;1083164897:0.0;1280687328:0.0;1914469231:0.0;1101065261:0.38;564033558:0.06;1603709929:0.0;3377874191:0.0;1090561057:0.0;2850924381:0.0;2516990734:0.05;2080792998:0.06;494566796:0.0;3483773697:0.03;2347601457:0.0;2005458920:0.0;2228741307:0.03;1655128063:0.09;3437323666:0.0;772775261:0.09;2630556335:0.05;391355059:0.0;43326778:0.32;352949551:0.37;406599990:0.0;3543952445:0.03;534835134:0.22;3141262273:0.0;4291022585:0.03;1430379429:0.0;214359637:0.11;2571529130:0.0;1979912953:0.0;3523444326:0.11;2925385748:0.0;2736249844:0.0;1604477434:0.03;219494910:0.0;1268079457:0.03;3244584129:0.43;4273897350:0.0;3811061722:0.05;2719930315:0.0;3077244739:0.0;4241944642:0.03;3872580956:0.0;1780345002:0.0;3775000711:0.0;1515402415:0.07;4194745904:0.34;922083540:0.06;2617268191:0.05;2197153053:0.0;260024147:0.0;515015205:0.0;3651041188:0.16;3062423122:0.03;1384401148:0.0;2112475829:0.0;837167779:0.03;1239404974:0.05;3738726614:0.0;166018268:0.21;2151285239:0.0;3296173756:0.06;665833013:0.0;1568456459:0.0;3310705110:0.0;1619828095:0.0;2277294202:0.0;1312283598:0.03;1854257753:0.0;1034148369:0.29;1523304141:0.0;103383824:0.24;3950136263:0.03;1903427038:0.0;244969176:0.0;1217273766:0.0;3755387923:0.0;3348987065:0.0;2901060280:0.0;3753576034:0.0;299592099:0.0;3476505723:0.0;1110227806:0.0;309752166:0.0;1335507678:0.0;1607600434:0.0;201957754:0.28;3460961700:0.47;947021594:0.0;1291547971:0.23;2609084431:0.0;3866175095:0.0;1590156854:0.0;1859384793:0.12;642863900:0.0;2673500979:0.38;3838018122:0.51;1144133059:0.0;2096577266:0.0;3342942893:0.05;3401016198:0.06;3144507072:0.13;3838732498:0.0;2857617218:0.05;3111513102:0.0;1279979042:0.0;976173111:0.0;960753216:0.0;1592834383:0.14;429493579:0.13;2045202569:0.11;2637809948:0.08;2822809911:0.03;1358854194:0.03;4067534243:0.0;1494766745:0.09;3657124426:0.0;1136856185:0.03;1913523282:0.0;54399409:0.06;2855348477:0.0;65870184:0.13;3629761194:0.0;3815893154:0.0;1439309301:0.03;3915022114:0.0;4167847191:0.0;1308178560:0.0;1894226516:0.0;75558512:0.0;4115246677:0.0;3749429758:0.0;994850594:0.0;1210134493:0.0;805707558:0.12;3409155395:0.08;1668180578:0.0;466045469:0.0;2057122224:0.0;4137841450:0.17;914522121:0.0;807807347:0.05;2116943528:0.0;2952867992:0.03;3594277627:0.0;4059549279:0.0;1505990033:0.0;700503553:0.03;2347264198:0.0;996210035:0.03;307193495:0.09;2414211238:0.0;1609871936:0.0;1785931205:0.0;1256118282:0.0;4180490761:0.0;4293087681:0.06;1452020369:0.0;907321928:0.0;695972858:0.1;4244307534:0.05;2349000771:0.0;2916150637:0.0;1244022102:0.0;631769340:0.0;983790642:0.06;1356451122:0.0;1666378447:0.24;4034445285:0.0;3750919411:0.0;2810352243:0.0;3274 YoukuQueryCtrPredFeatureExtractor::calScore end (return 0.830000) YoukuQualityFeatureExtractor::calScore begin doc_type:1, vdoId:0, showId:300647, plylstId:0 vdoBlack:0, limited:0 vdoVV:0, vdoLen:0.000000, hasVdoType:-1, vdoFormat:1, mbrScore:23184960 formatScore:0.200000, vvScore:0.000000, lenScore:0.000000, mbrScore:0.000000 YoukuQualityFeatureExtractor::calScore end -> return 0.040000 YoukuECBFakeFeatureExtractor::calScore begin() YoukuECBFakeFeatureExtractor::calScore end (return 0.000000) In PureLinerRanker Process: final mlrScore : 483.210480 final score:[ 483.21 ] final group:[ 0 ] user score:[ 0 ] ",
"""

outputIds = []
showname_dic = {}
reg_dic = {}
trace_dic = {}

def getImergerJson(url):
    json = None
    try:
        session = requests.session()
        session.mount('http://', HTTPAdapter(max_retries=3))
        res = session.get(url)
        json = res.json()
        # retry
        i = 0
        while len(res.content) == 0 and i < 2:
            res = session.get(url)
            if len(res.content) > 0:
                json = res.json()
            i += 1
        return json
    except Exception, e:
        logger.error('Http request exception, query:' +  ' e:' + str(e))
    return json

def get_showids(json):
    global trace_dic
    global outputIds
    outputIds = []
    trace_dic = {}
    try:
        ecb_data = json['ecb']
        ecbMerge = ecb_data['ecbMergeArray']
        for ecbM in ecbMerge:
            outputId = ecbM['programmeId']
            outputIds.append(outputId)

        youku_ecb = ecb_data['youku_ecb']
        auctions = youku_ecb['auctions']

        for item in auctions:
            doctrace = item['doctrace']
            show_id = item['show_id']

            trace_dic[str(show_id)] = str(doctrace)

    except Exception, e:
        logger.error('parse json exception, query:' + ", e:" + str(e))
    return trace_dic

def read_show_file(showFilePath):
    global showname_dic
    with open(showFilePath, 'r') as f:
        for line in f:
            field = line.strip().split('\t')
            showname_dic[field[0]] = field[1]

def fill_reg():
    global reg_dic
    reg_dic[time_reg] = time_w
    reg_dic[new_relan_reg] = newRelevance_w
    reg_dic[vv_reg] = vv_w
    reg_dic[exclusive_reg] = exclusive_w
    reg_dic[category_reg] = category_w
    reg_dic[satisfaction_reg] = satisfaction_w
    reg_dic[ctr_reg] = ctr_w
    reg_dic[quality_reg] = quality_w
    reg_dic[all_hit_reg] = allHit_w


if __name__ == '__main__':
    #global outputIds
    #global trace_dic
    fill_reg()
    read_show_file('show_file')

    query = '越狱'
    url = 'http://imerge-pre.soku.proxy.taobao.org/i/s?rankFlow=112&isFilter=16&cmd=1&ecb_sp_ip=11.173.213.132:2090&qaFlow=1&keyword=' + query
    res_json = getImergerJson(url)

    get_showids(res_json)

    i = 1
    for item in outputIds:
        logger.error(item)
        doctrace = trace_dic[str(item)]
        for reg in reg_dic:
            logger.error(reg)
            line = re.search(reg, doctrace).group().strip()
            logger.error(line)
            score = ''
            if 'return' in line:
                field = line.split('return')
                score = field[1].strip().replace(')','')

                if 'calScore' in score:
                    field2 = score.split('YoukuECBFakeFeatureExtractor')
                    score = field2[0]

                logger.error(score)
            else:
                field = line.split('hit:')
                score = field[1].strip()
                logger.error(score)
        i += 1
    logger.error('Finish i:' + str(i))
#print re.search(match_reg, str).group()
