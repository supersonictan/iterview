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
