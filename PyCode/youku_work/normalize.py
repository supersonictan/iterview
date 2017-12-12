# coding:utf-8

import string
import types
import datetime
import time
import sys as _sys



CN_NUM = {
    u'〇' : 0, u'一' : 1, u'二' : 2, u'三' : 3, u'四' : 4, u'五' : 5, u'六' : 6, u'七' : 7, u'八' : 8, u'九' : 9, u'零' : 0,
    u'壹' : 1, u'贰' : 2, u'叁' : 3, u'肆' : 4, u'伍' : 5, u'陆' : 6, u'柒' : 7, u'捌' : 8, u'玖' : 9, u'貮' : 2, u'两' : 2,
}
CN_UNIT = {
    u'十' : 10,
    u'拾' : 10,
    u'百' : 100,
    u'佰' : 100,
    u'千' : 1000,
    u'仟' : 1000,
    u'万' : 10000,
    u'萬' : 10000,
    u'亿' : 100000000,
    u'億' : 100000000,
    u'兆' : 1000000000000,
}
CN_NUM_SET = CN_NUM
CN_NUM_SET.update(CN_UNIT)
CN_NUM_SET = set(CN_NUM_SET)


def pickChineseNum(text):
    if not text:
        return []
    result = []
    tmp = ''
    i = 0
    while i < len(text):
        cn = text[i]
        if cn in CN_NUM_SET:
            tmp = ''
            while i < len(text) and text[i] in CN_NUM_SET:
                tmp += text[i]
                i = i + 1
            i = i - 1
            all_unit = 1
            for each in tmp:
                if each not in CN_UNIT:
                    all_unit = 0
                    break
            if all_unit:
                if tmp[0] == u'十':
                    if len(tmp) > 1:
                        result.append((False, tmp[-1:]))
                    else:
                        result.append((False, tmp[0]))
                else:
                    result.append((False, tmp))
            else:
                if len(tmp) >= 2:
                    has_unit = False
                    for each in tmp:
                        if each in CN_UNIT:
                            has_unit = True
                            break
                    if has_unit:
                        result.append((True, tmp))
                    else:
                        for each in tmp:
                            result.append((True, each))
                else:
                    result.append((True, tmp))
        else:
            tmp = ''
            while i < len(text) and text[i] not in CN_NUM_SET:
                tmp += text[i]
                i = i + 1
            i = i - 1
            result.append((False, tmp))
        i = i + 1
    return result


if __name__ == '__main__':
    print pickChineseNum('三生三世第2季')