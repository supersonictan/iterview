#!/usr/bin/python
# -*- coding: utf-8 -*-

def evaluate(tmpStr, split_delimeter, org_rank_delimeter, rank_delimeter):
    res = ''
    if tmpStr is None or split_delimeter is None or rank_delimeter is None or org_rank_delimeter is None:
        return ''

    tmpStr = tmpStr.strip()
    split_delimeter = split_delimeter.strip()
    rank_delimeter = rank_delimeter.strip()
    org_rank_delimeter = org_rank_delimeter.strip()

    try:
        str_arr = tmpStr.split(split_delimeter)
        for i in range(len(str_arr)):
            res = res + str(str_arr[i]) + org_rank_delimeter + rank_delimeter + str(i + 1) + split_delimeter

    except ValueError:
        return ''

    return res


if __name__ == '__main__':
    txt = '3_36843684_doc_source=3$eng_source=1$iranker_score=991.858!!99_413632019_49900632_doc_source=99$pid=49900632$eng_source=5$copyright=0$show_id=0$iranker_score=990.858!!99_445919766_49885039_doc_source=99$pid=49885039$eng_source=5$copyright=0$show_id=0$iranker_score=974.504!!2_461669750_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=949.685!!99_563233819_49751159_doc_source=99$pid=49751159$eng_source=5$copyright=0$show_id=0$iranker_score=949.665!!99_193371398_50073680_doc_source=99$pid=50073680$eng_source=5$copyright=0$show_id=0$iranker_score=948.106!!2_708298136_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=933.044!!99_396999284_49662721_doc_source=99$pid=49662721$eng_source=5$copyright=0$show_id=0$iranker_score=911.899!!99_700193576_49596720_doc_source=99$pid=49596720$eng_source=5$copyright=0$show_id=0$iranker_score=907.784!!2_708129725_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=900.723!!2_710056935_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=896.926!!2_710398910_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=896.158!!2_710301829_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=891.168!!2_334809780_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=889.675!!2_336606460_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=889.655!!2_707705797_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=889.635!!2_701142754_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=888.691!!2_708107526_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=888.254!!2_638129259_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=887.297!!0_0!!2_408916170_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=885.285!!2_710601603_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=883.554!!99_164918802_27393388_doc_source=99$pid=27393388$eng_source=5$copyright=0$show_id=0$iranker_score=882.272!!2_708455386_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=879.603!!2_710308802_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=878.572!!2_708702689_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=878.289!!2_710305526_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=877.817!!2_674456311_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=877.465!!2_316572966_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=872.703!!2_694261913_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=872.592!!2_708446844_doc_source=2$eng_source=5$copyright=0$show_id=0$iranker_score=871.965'
    str_tmp = evaluate(txt, '!!', '$', 'rank=')
    print str_tmp