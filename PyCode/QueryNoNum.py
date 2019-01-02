# -*- coding: utf-8 -*-

import string
import types
import datetime
import time
import re,json
import sys as _sys,re




useless_reg_str1 = r'^(一|二|三|四|五|六|七|八|九|十|0|1|2|3|4|5|6|7|8|9)+(季|集|部|期|章)'
useless_reg_str2 = r"(一|二|三|四|五|六|七|八|九|十|0|1|2|3|4|5|6|7|8|9)+(集)"
useless_reg_str3 = r"第(一|二|三|四|五|六|七|八|九|十|0|1|2|3|4|5|6|7|8|9)+(季|集|部|期|章)$"

useless_pat_1 = re.compile(useless_reg_str1)
useless_pat_2 = re.compile(useless_reg_str2)
useless_pat_3 = re.compile(useless_reg_str3)


useless_reg_list = [useless_pat_1, useless_pat_2, useless_pat_3]
text = ""

txt = '{"人名":["冯提莫"],"音乐":["大声说爱你"]}'

if __name__ == '__main__':
    obj = json.loads(txt)
    for k in obj:

        print k
    # for match in re.finditer(useless_reg_str3, text):
    #     targetStr = match.group(0)
    #     str1 = match.group(1)
    #     str2 = match.group(2)
    #     str3 = match.group(3)
    #     totalNum = num_convter.evaluate(str2)
    #     tranStr = '%s%s%s' % (str1, totalNum.decode('utf8'), str3)
    #     text = text.replace(targetStr, tranStr)