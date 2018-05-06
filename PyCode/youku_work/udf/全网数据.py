#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,re,time,types,datetime,sys
import json


yt_show = []
out_show = []
label = {}
res_out = []
def load_ytshow():
    global yt_show
    with open('/Users/tanzhen/Desktop/code/odps/bin/internal', 'r') as f:
        for line in f.readlines():
            arr = line.split('\t')
            show_id = arr[0].strip()
            show_name = arr[1].strip()
            douban_id = arr[2].strip()
            directors = arr[3].strip()
            actors = arr[4].strip()
            years = arr[5].strip()
            country = arr[6].strip()
            all_name = arr[8].strip()

            # 导演数组
            arr_directors = json.loads(directors)
            # 演员数组
            arr_actors = json.loads(actors)
            # 年份数组
            arr_years = json.loads(years)
            # 全部名字
            arr_all_name = json.loads(all_name)
            yt_show.append((show_id, arr_all_name, arr_directors, arr_actors, arr_years, douban_id))


def load_outshow():
    global out_show
    with open('/Users/tanzhen/Desktop/code/odps/bin/external', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            arr = line.split('\t')
            if len(arr) != 10:
                ln = len(arr)
                print(str(ln) + "," +line)
                continue
            show_id = arr[0].strip()
            show_name = arr[1].strip()
            douban_id = arr[2].strip()
            directors = arr[3].strip()
            actors = arr[4].strip()
            years = arr[5].strip()
            country = arr[6].strip()
            all_name = arr[8].strip()

            # 导演数组
            try:
                arr_directors = json.loads(directors)
            except Exception, e:
                print line
                print(e)

            # 演员数组
            arr_actors = json.loads(actors)
            # 年份数组
            arr_years = json.loads(years)
            # 全部名字
            arr_all_name = json.loads(all_name)
            out_show.append((show_id, arr_all_name, arr_directors, arr_actors, arr_years, douban_id))

def load_label():
    global label
    with open('/Users/tanzhen/Desktop/code/odps/bin/label', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            arr = line.split('\t')
            label[arr[0]] = arr[1]


def cal_jaccard(txt1, txt2):
    if isinstance(txt1, str) and isinstance(txt2, str):
        if txt1 == '' or txt2 == '' or txt1 == ' ' or txt2 == ' ':
            return 0.0
        common = len(set(txt1) & set(txt2))
        total = len(set(txt1 + txt2))
        if total == 0:
            return 0
        else:
            return float(common) / float(total)

    else:  # 两个list
        if len(txt1) == 0 or len(txt2) == 0:
            return 0.0
        common = len(set(txt1) & set(txt2))
        total = len(set(txt1 + txt2))
        if total == 0:
            return 0
        else:
            return float(common) / float(total)


def cal_sim():
    global res_out
    global label
    count = 0
    with open('/Users/tanzhen/Desktop/code/odps/bin/mapping_res', 'w') as f:
        since = time.time()
        for each_out in out_show:
            count += 1
            # if count % 1000 == 0:
            #     print(count)
            #     print(time.time() - since)

            out_id, arr_alias_out, arr_direct_out, arr_actors_out, arr_year_out, douban_id_out = each_out
            # if out_id != 'fc5fe984-7092-11e5-86ac-d43d7e6fab60':
            #     continue
            # 站内数据
            cnt = 0
            for each in yt_show:
                in_id, arr_all_name, arr_direct, arr_actors, arr_year, douban_id = each
                # if in_id != '260125':
                #     continue
                # print('hahahah')

                sim_name = 0.0
                sim_year = 0.0
                sim_direct = 0.0
                sim_actor = 0.0

                # 计算 name 相似度
                for name1 in arr_all_name:
                    for name2 in arr_alias_out:
                        sim_tmp = cal_jaccard(name1, name2)
                        if sim_tmp >= 0.98:
                            sim_name = sim_tmp
                            break
                        if sim_tmp > sim_name:
                            sim_name = sim_tmp
                    if sim_name >= 0.98:
                        break
                if sim_name <= 0.5:
                    if in_id in label:
                        out_id_label = label[in_id]
                        if out_id_label == out_id:
                            print(in_id + '--' + out_id)
                    continue

                # 计算导演相似
                sim_direct = cal_jaccard(arr_direct, arr_direct_out)

                # 计算演员相似
                if len(arr_actors) != 0 and len(arr_actors_out) != 0:
                    sim_actor = cal_jaccard(arr_actors, arr_actors_out)

                # 计算年份相似
                sim_year = cal_jaccard(arr_year, arr_year_out)

                out_str = out_id + '\t' + in_id + '\t' + str(sim_name) + '\t' + str(sim_year) + '\t' + str(sim_actor) + '\t' \
                          + str(sim_direct) + '\t' + str(douban_id_out) + '\t' + str(douban_id) + '\n'
                print(out_str)
                f.write(out_str)



def levenshtein(first, second):
    if len(first) > len(second):
        first, second = second, first
    if len(first) == 0:
        return len(second)
    if len(second) == 0:
        return len(first)
    first_length = len(first) + 1
    second_length = len(second) + 1
    distance_matrix = [range(second_length) for x in range(first_length)]
    # print distance_matrix
    for i in range(1, first_length):
        for j in range(1, second_length):
            deletion = distance_matrix[i - 1][j] + 1
            insertion = distance_matrix[i][j - 1] + 1
            substitution = distance_matrix[i - 1][j - 1]
            if first[i - 1] != second[j - 1]:
                substitution += 1
            distance_matrix[i][j] = min(insertion, deletion, substitution)
    return distance_matrix[first_length - 1][second_length - 1]






if __name__ == '__main__':
    test = '["中国","中国","中国香港","中国台湾"]'
    #test = unicode(test, errors='ignore')
    #test = test.decode('utf8')
    arr = json.loads(test)
    for a in arr:
        print(a)

    #l1 = '[[3441871646], [624079299]]'
    #l2 = '[[3693753202, 2172806945, 3728790948]]'
    #in_name = json.loads(l1)
    #out_name = json.loads(l2)

    # sim_name = 0.0
    # flag = False
    # for name1 in in_name:
    #     for name2 in out_name:
    #         print(name1)
    #         print(name2)
    #         tmp_sim = cal_jaccard(name1, name2)
    #         if tmp_sim == 1:[[3693753202, 2172806945, 3728790948]]
    #             sim_name = tmp_sim
    #             flag = True
    #             break
    #         if tmp_sim > sim_name:
    #             sim_name = tmp_sim
    #     if flag:
    #         break
    # print(sim_name)

    # load_ytshow()
    # load_outshow()
    # load_label()
    # print('load finished....')
    # cal_sim()
    # print('cal finished....')


    # print(len(yt_show))
    # print(len(out_show))
    #
    # cal_sim()