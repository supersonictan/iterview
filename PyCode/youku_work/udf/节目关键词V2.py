#!/usr/bin/python
# -*- coding: utf-8 -*-
import json,re,time,types,datetime,sys


def yt_get_keyword(show_name):
    reg1 = r".*第([一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9]+)[季|集|部|期]"

    match_obj = re.findall(reg1, show_name)

    print(match_obj)
    # if match_obj:
    #     text = match_obj.group(0)
    #     return text

    return None




if __name__ == '__main__':
    print yt_get_keyword("第87届奥斯卡金像奖颁奖典礼第二季")