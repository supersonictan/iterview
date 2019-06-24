# -*- coding: utf-8 -*-

import re
import json




class Corpus(object):
    def __init__(self, item_list):
        self.item_list = item_list

class Term(object):
    def __init__(self, start, end, word, text, label, option):
        self.start = start
        self.end = end
        self.word = word
        self.text = text
        self.label = label
        self.option = option


def json2Corpus(d):
    return Term(d['start'], d['end'], d['word'], d['text'], d['label'], d['option'])



target_map = {
      u'春节联欢晚会': u'SHOW',
      u'上海国际电影节': u'SHOW',
      u'春节晚会': u'SHOW',
      u'元旦晚会': u'SHOW',
      u'环球春节联欢晚会': u'SHOW',
      u'中秋晚会': u'SHOW',
      u'亚洲电影大奖': u'SHOW',
      u'国剧盛典': u'SHOW',
      u'网络春节联欢晚会': u'SHOW',
      u'电影华表奖颁奖典礼': u'SHOW',
      u'金马奖颁奖典礼': u'SHOW',
      u'香港电影金像奖': u'SHOW',
      u'金鹰节颁奖晚会': u'SHOW',
      u'少儿春晚': u'SHOW',
      u'跨年晚会': u'SHOW',
      u'万千星辉贺台庆': u'SHOW',
      u'万千星辉颁奖典礼': u'SHOW',
      u'亚洲电影大奖颁奖典礼': u'SHOW',
      u'天猫双11狂欢夜': u'SHOW',
      u'北京国际电影节': u'SHOW',
      u'微博之夜': u'SHOW',
      u'wwe': u'SHOW',
      u'皇家大战': u'SHOW',
      u'斯诺克大师赛':u'SHOW',
      u'春晚': u'SHOW',
      u'电视剧品质盛典': u'SHOW',
      u'中国电影华表奖颁奖典礼': u'SHOW',
      u'315晚会': u'SHOW',
      u'斯诺克德国大师赛': u'SHOW',
      u'达喀尔拉力赛': u'SHOW',
      u'元宵晚会': u'SHOW'
}


count_dic = {}
if __name__ == '__main__':
    i = 0
    term_list = {}
    res_list = []
    with open('/Users/tanzhen/Desktop/code/odps/bin/qt_train_corpus_adjust', 'r') as f:
        for text in f:
            text = text.decode('utf8')
            seg = text.split(u'\t')
            query = seg[0]
            corpus = seg[1]
            if corpus == '[]':
                continue

            json_list = json.loads(corpus)

            term_list = []
            b_find = False
            try:
                for item in json_list:
                    map = {}
                    map[u'word'] = item[u'word']
                    map[u'text'] = item[u'text']


                    # test
                    if item[u'label'] == u'LOC':
                        if item[u'word'] in count_dic:
                            count_dic[item[u'word']] += 1
                        else:
                            count_dic[item[u'word']] =1

                        # print query + "\t" + item[u'word']
                    # end test


                    if map[u'word'] in target_map:
                        b_find = True
                        map[u'label'] = target_map[map[u'word']]
                    else:
                        map[u'label'] = item[u'label']
                    map[u'start'] = item[u'start']
                    map[u'end'] = item[u'end']

                    term_list.append(map)

                s = "%s\t%s\n" % (query.encode('utf8'), json.dumps(term_list, ensure_ascii=False).encode('utf8').strip())
                res_list.append(s)
            except Exception,e:
                print(query)

    sorted(count_dic.items(), key=lambda d: d[1], reverse=True)
    for (k,v) in count_dic.items():
        print k + '\t' + str(v)

    # with open('/Users/tanzhen/Desktop/code/odps/bin/qt_train_corpus_adjust', 'w') as f:
    #     for s in res_list:
    #         f.write(s)


    # print "---------------------------------"
    # # testSet
    # term_list = {}
    # res_list = []
    # count_dic = {}
    # with open('/Users/tanzhen/Desktop/code/odps/bin/qt_test_corpus', 'r') as f:
    #     for text in f:
    #         text = text.decode('utf8')
    #         seg = text.split(u'\t')
    #         query = seg[0]
    #         corpus = seg[1]
    #         if corpus == '[]':
    #             continue
    #
    #         json_list = json.loads(corpus)
    #
    #         term_list = []
    #         b_find = False
    #         try:
    #             for item in json_list:
    #                 map = {}
    #                 map[u'word'] = item[u'word']
    #                 map[u'text'] = item[u'text']
    #
    #
    #                 # test
    #                 if item[u'label'] == u'GENRE':
    #                     if item[u'word'] in count_dic:
    #                         count_dic[item[u'word']] += 1
    #                     else:
    #                         count_dic[item[u'word']] =1
    #                 # end test
    #
    #
    #                 if map[u'word'] in target_map:
    #                     b_find = True
    #                     map[u'label'] = target_map[map[u'word']]
    #                 else:
    #                     map[u'label'] = item[u'label']
    #                 map[u'start'] = item[u'start']
    #                 map[u'end'] = item[u'end']
    #
    #                 term_list.append(map)
    #
    #             s = "%s\t%s\n" % (query.encode('utf8'), json.dumps(term_list, ensure_ascii=False).encode('utf8').strip())
    #             res_list.append(s)
    #         except Exception,e:
    #             print(query)
    #
    # for (k,v) in count_dic.items():
    #     print k + '\t' + str(v)


    # with open('/Users/tanzhen/Desktop/code/odps/bin/qt_test_corpus_adjust', 'w') as f:
    #     for s in res_list:
    #         f.write(s)