# -*- coding: utf-8 -*-

import re
import json
from collections import deque


text = """
[{"end": 12, "option": "节目", "auto": 0, "label": "SHOW", "start": 0, "text": "知青家庭", "word": "知青家庭"}]
"""

# 去掉结尾 2(节目名不去掉)
# 两边非中文去掉空格
blank_num = re.compile(u'\s\d+$')
only_blank = re.compile(u'^( | |　)$')
# 极限挑战 第五季张云雷
if __name__ == '__main__':
    text = '极限挑战 第五季张云雷 '
    text = text.strip().decode('utf8')
    #text = blank_num.sub('', text).strip()

    result_list = []
    text_len = len(text)
    for i in range(len(text)):
        month_match = re.search(only_blank, text[i])
        if month_match:
            print('match')
            # 如果左边右边都是英文则保留空格
            # 左右都数字保留
            # 做英文右数字保留
            pre_char = text[i-1]  # 先trim不会两端空格
            next_char = ' '
            if i+1<text_len:
                next_char = text[i + 1]

            is_pre_en = (True if (97<=ord(pre_char) and ord(pre_char)<=122) or (65<=ord(pre_char) and ord(pre_char)<=190) else False)
            is_next_en = (True if (97<=ord(next_char) and ord(next_char)<=122) or (65<=ord(next_char) and ord(next_char)<=190) else False)
            if is_pre_en and is_next_en:
                print('1')
                pass
            elif pre_char.isdigit() and next_char.isdigit():
                print('2')
                pass
            elif is_pre_en and next_char.isdigit():
                print('3')
                pass
            else:
                continue
        result_list.append(text[i])

    print ''.join(result_list).encode('utf8')