#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,re,time,types,datetime,sys
import json


yt_show = []
out_show = []
def load_ytshow():
    global yt_show
    with open('/Users/tanzhen/Desktop/code/odps/bin/internal', 'r') as f:
        for line in f.readlines():
            arr = line.split('\t')
            show_id = arr[0].strip()
            show_name = arr[1].strip().decode('utf8')
            douban_id = arr[2].strip()
            directors = arr[3].strip().decode('utf8')
            actors = arr[4].strip().decode('utf8')
            years = arr[5].strip()
            countries = arr[6].strip()
            alias = arr[8].strip().decode('utf8')

            # 导演数组
            arr_directors = []
            if directors is not None and directors != '':
                arr_directors = directors.split('###')
            # 演员数组
            arr_actors = []
            if actors is not None and actors != '':
                arr_actors = actors.split('###')
            # 年份数组
            arr_years = []
            if years != '-1' and years is not None and years != '':
                arr_years = years.split('###')

            arr_alias = alias.split('###')
            arr_alias.append(show_name)
            yt_show.append((show_id, arr_alias, arr_directors, arr_actors, arr_years))


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
            show_name = arr[1].strip().decode('utf8')
            douban_id = arr[2].strip()
            directors = arr[3].strip().decode('utf8')
            actors = arr[4].strip().decode('utf8')
            years = arr[5].strip()
            countries = arr[6].strip()
            alias = arr[8].strip().decode('utf8')

            arr_directors = directors.split('###')
            arr_actors = actors.split('###')
            arr_years = years.split('###')
            arr_alias = alias.split('###')
            arr_alias.append(show_name)
            out_show.append((show_id, arr_alias, arr_directors, arr_actors, arr_years))


def cal_jaccard(txt1, txt2):
    if isinstance(txt1, str) and isinstance(txt2, str):
        if txt1 == '' or txt2 == '' or txt1 == ' ' or txt2 == ' ':
            return 0.0
        return levenshtein(txt1, txt2)
        # common = len(set(txt1) & set(txt2))
        # total = len(set(txt1 + txt2))
        # if total == 0:
        #     return 0
        # else:
        #     return float(common) / float(total)

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
    count = 0
    for each_out in out_show:
        count += 1
        if count % 1000 == 0:
            print(count)


        out_id, arr_alias_out, arr_direct_out, arr_actors_out, arr_year_out = each_out
        # 站内数据
        for each in yt_show:
            id, arr_alias, arr_direct, arr_actors, arr_year = each
            sim_name = 0.0
            sim_year = 0.0
            sim_direct = 0.0
            sim_actor = 0.0

            # 计算 name 相似度
            # for name1 in arr_alias:
            #     for name2 in arr_alias_out:
            #         sim_tmp = cal_jaccard(name1, name2)
            #         if sim_tmp >= 0.98:
            #             sim_name = sim_tmp
            #             break
            #         if sim_tmp > sim_name:
            #             sim_name = sim_tmp
            #     if sim_name >= 0.98:
            #         break

            # 计算导演相似
            sim_direct = cal_jaccard(arr_direct, arr_direct_out)

            # 计算演员相似
            if len(arr_actors) != 0 or len(arr_actors_out) != 0:
                sim_actor = cal_jaccard(arr_actors, arr_actors_out)

            # 计算年份相似
            sim_year = cal_jaccard(arr_year, arr_year_out)

            if sim_actor > 0.1:
                # a = '###'.join(arr_actors)
                # b = '###'.join(arr_actors_out)
                #print(a + '---' + b)
                print(arr_actors)
                print(id)


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
    # load_ytshow()
    # load_outshow()
    # print(len(yt_show))
    # print(len(out_show))
    #
    # cal_sim()
    # a = "['rodionnakhapetov', 'rnakhapetov', 'rodionrafailovichnakhapetov']"
    # print json.loads(a)
    s = ["abc", "bcd"]
    res = json.dumps(s)
    a = json.loads(res)
    print(a)