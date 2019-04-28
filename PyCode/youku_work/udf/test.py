#!/usr/bin/python
# -*- coding=utf-8-*-
import math,json,re
import sys
import urllib
import urllib2
import traceback
from collections import deque

# coding=utf-8

KIND = 16


nil = object()    # used to distinguish from None

class TrieNode(object):
    # Node of trie/Aho-Corasick automaton

    __slots__ = ['char', 'output', 'fail', 'children']

    def __init__(self, char):
        # Constructs an empty node
        self.char = char        # character
        self.output = nil        # an output function for this node
        self.fail = nil            # fail link used by Aho-Corasick automaton
        self.children = {}        # children

    def __repr__(self):
        # Textual representation of node.

        if self.output is not nil:
            return "<TrieNode '%s' '%s'>" % (self.char, self.output)
        else:
            return "<TrieNode '%s'>" % self.char

class Automaton(object):
    # Automaton/Aho-Corasick automaton.

    def __init__(self):
        # Construct an empty trie
        self.root = TrieNode('')


    def __get_node(self, word):
        """
        Private function retrieving a final node of trie
        for given word

        Returns node or None, if the trie doesn't contain the word.
        """

        node = self.root
        for c in word:
            try:
                node = node.children[c]
            except KeyError:
                return None

        return node


    def get(self, word, default=nil):
        """
            Retrieves output value associated with word.

            If there is no word returns default value,
            and if default is not given rises KeyError.
            """

        node = self.__get_node(word)
        output = nil
        if node:
            output = node.output

        if output is nil:
            if default is nil:
                raise KeyError("no key '%s'" % word)
            else:
                return default
        else:
            return output


    def keys(self):
        """
            Generator returning all keys (i.e. word) stored in trie
            """

        for key, _ in self.items():
            yield key


    def values(self):
        """
            Generator returning all values associated with words stored in a trie.
            """

        for _, value in self.items():
            yield value


    def items(self):
        """
            Generator returning all keys and values stored in a trie.
            """

        L = []

        def aux(node, s):
            s = s + node.char
            if node.output is not nil:
                L.append((s, node.output))

            for child in node.children.values():
                if child is not node:
                    aux(child, s)

        aux(self.root, '')
        return iter(L)


    def __len__(self):
        """
            Calculates number of words in a trie.
            """

        stack = deque()
        stack.append(self.root)
        n = 0
        while stack:
            node = stack.pop()
            if node.output is not nil:
                n += 1

            for child in node.children.values():
                stack.append(child)

        return n


    def add_word(self, word, value):
        """
            Adds word and associated value.

            If word already exists, its value is replaced.
            """
        if not word:
            return

        node = self.root
        for c in word:
            try:
                node = node.children[c]
            except KeyError:
                n = TrieNode(c)
                node.children[c] = n
                node = n

        node.output = value


    def clear(self):
        """
            Clears trie.
            """

        self.root = TrieNode('')


    def exists(self, word):
        """
        Checks if whole word is present in the trie.
        """

        node = self.__get_node(word)
        if node:
            return bool(node.output != nil)
        else:
            return False


    def match(self, word):
        """
        Checks if word is a prefix of any existing word in the trie.
        """

        return (self.__get_node(word) is not None)


    def make_automaton(self):
        """
        Converts trie to Aho-Corasick automaton.
        """
        print('Start make ac')
        queue = deque()

        # 1.
        for i in range(256):
            c = chr(i)
            if c in self.root.children:
                node = self.root.children[c]
                node.fail = self.root  # f(s) = 0
                queue.append(node)
            else:
                self.root.children[c] = self.root

        # 2.
        while queue:
            r = queue.popleft()
            for node in r.children.values():
                queue.append(node)
                state = r.fail
                while node.char not in state.children:
                    state = state.fail

                node.fail = state.children.get(node.char, self.root)


    def iter(self, string):
        """
        Generator performs Aho-Corasick search string algorithm, yielding
        tuples containing two values:
        - position in string
        - outputs associated with matched strings
        """
        state = self.root
        for index, c in enumerate(string):
            while c not in state.children:
                state = state.fail

            state = state.children.get(c, self.root)

            tmp = state
            output = []
            while tmp is not nil:
                if tmp.output is not nil:
                    output.append(tmp.output)

                tmp = tmp.fail

            if output:
                yield (index, output)


    def iter_long(self, string):
        """
        Generator performs a modified Aho-Corasick search string algorithm,
        which maches only the longest word.
        """
        state = self.root
        last = None

        index = 0
        while index < len(string):
            c = string[index]

            if c in state.children:
                state = state.children[c]

                if state.output is not nil:
                    # save the last node on the path
                    last = (state.output, index)

                index += 1
            else:
                if last:
                    # return the saved match
                    yield last

                    # and start over, as we don't want overlapped results
                    # Note: this leads to quadratic complexity in the worst case
                    index = last[1] + 1
                    state = self.root
                    last = None
                else:
                    # if no output, perform classic Aho-Corasick algorithm
                    while c not in state.children:
                        state = state.fail

        # corner case
        if last:
            yield last


    def find_all(self, string, callback):
        # Wrapper on iter method, callback gets an iterator result
        for index, output in self.iter(string):
            callback(index, output)



# BASE = ord('a')


def max_match_segment(line, dic):
    window_size = 20
    # write your code here
    chars = line.decode("utf8")
    words = []
    idx = 0
    # 判断索引是否超过chars的长度
    while idx < len(chars):
        matched = False
        for i in xrange(window_size, 0, -1):
            cand = chars[idx:idx + i].encode("utf8")
            if cand in dic:
                words.append(cand)
                matched = True
                break
        # 判断for中是否匹配到数据
        if not matched:
            i = 1
            words.append(chars[idx].encode("utf8"))
        idx += i

    return words

def gen_crf_feature(corpus_seg, marked_label):
    result = ''
    try:
        seg_list = []
        mark_list = []
        result_list = []

        seg_list = corpus_seg.split(" ")
        mark_list = json.loads(marked_label)
        mark_list.sort(key=lambda k: (k.get('start', 0)))
        i = 0
        p = 0
        for seg in seg_list:
            subseg_list = seg.split(":")
            seg_word = subseg_list[0]
            seg_pos = subseg_list[1]
            seg_start = p
            p = p + len(seg_word)
            seg_end = p
            seg_len = len(seg_word)
            seg_label = "O"

            form = ""
            position = str(i)
            i = i + 1
            word_pos = ""

            tmp_list = mark_list[:]
            for term in tmp_list:
                if term == {}:
                    continue
                if type(term) != dict:
                    continue
                word = term.get('word', '').encode('utf-8').strip()
                label = term.get('label', 'O')
                if label == "OTHER":
                    label = "O"
                start = term.get('start', 0)
                end = term.get('end', 0)
                ret = word.find(seg_word)
                if ret == -1:
                    continue
                if ret == 0:
                    word_pos = "B"
                else:
                    word_pos = "I"

                if label == "O" or label == "":
                    seg_label = "O"
                else:
                    seg_label = word_pos + "-" + label

                if ret + seg_len == len(word):
                    mark_list.remove(term)
                    break
            length = str(seg_len)
            form = seg_word + ":" + seg_pos + ":" + position + ":" + length + ":" + "0" + ":" + seg_label
            result_list.append(form)

        result = " ".join(result_list)

    except Exception as e:
        result = str(e.message)
    return result


head_month_reg = re.compile(r'(^(\d+年)*\d+月\d+日)')
head_year_reg = re.compile(r'(^20(08|09|10|11|12|13|14|15|16|17|18|19){1}(赛季)*)')
shu_ming_hao_reg = re.compile(r'(（.*）|【.*】|\(.*\))')
year_reg = re.compile(r'(\d+年版)|(\d{4}版)|(\d{2}版)')
year_reg2 = re.compile(r'(.*\D+)(\d{1,2}月$)')
year_start = re.compile(r'(^[0-9]{4}年)')
tail_num_reg3 = re.compile(u'(.*[^\d\.的\-\+之/(TOP)])((19|20){1}(\d{2}$)|(\d{1,2}$))')  # 猪头传媒2018、猪头传媒18
sp_reg = re.compile(u"[！|\!|·|、|,|▪|－|?|，|・]+")
season_reg = re.compile(r'第(一|二|三|四|五|六|七|八|九|十|百|千|0|1|2|3|4|5|6|7|8|9)+(季|部|集|章|届|期|弹|卷|场|番|轮|册|回合)')
tv_reg = re.compile(r'(\d+(年)*)*(台湾东风|中央|浙江|凤凰|东方|四川|广西|青海|江苏|北京|辽宁|上海|东南|深圳|湖北|贵州|旅游|安微|广东|天津|吉林|山东|河北|龙江|江西|河南|湖南|重庆|安徽)(台|卫视|电视台|卫视版)')


zhi_reg = re.compile(u'(.{3,})(之)(.{2,})')

def evaluate(show_name):
    if not show_name:
        return ''
    show_name = show_name.strip()
    key_list = show_name.split('###')

    final_list = []

    for show_name in key_list:
        ## 去除：开头月份(2018年1月1日)
        tmp_name = head_month_reg.sub('', show_name).strip()
        if tmp_name:
            show_name = tmp_name

        # 去除：开头年份
        tmp_name = head_year_reg.sub('', show_name).strip()
        if tmp_name:
            show_name = tmp_name

        # 去除：书名号内的
        show_name = shu_ming_hao_reg.sub('', show_name).strip()

        # 去除：季部期
        show_name = season_reg.sub('', show_name).strip()

        # 去除：xx卫视
        show_name = tv_reg.sub('', show_name).strip()

        # 去除：09版
        show_name = year_reg.sub('', show_name).strip()

        # 去除：2016年AVN颁奖典礼
        show_name = year_start.sub('', show_name).strip()

        # 去除：特殊符号
        show_name = sp_reg.sub('', show_name.decode('utf8')).encode('utf8').strip()

        # 去除：猪头传媒 22月
        month_match = re.match(year_reg2, show_name)
        if month_match:
            show_name = month_match.group(1).strip()

        # 去除：猪头传媒2018、猪头传媒18
        matchObj = re.match(tail_num_reg3, show_name)
        if matchObj:
            word = matchObj.group(1).strip()
            print(word)
            #len(word) >= 2
            show_name = matchObj.group(1).strip()

        # 重复上一步操作，case:出发梦之队2 2009
        matchObj = re.match(tail_num_reg3, show_name)
        if matchObj and len(matchObj.group(1).strip()) >= 2:
            show_name = matchObj.group(1).strip()

        if show_name not in final_list:
            final_list.append(show_name)

    return '###'.join(final_list)






if __name__ == '__main__':
    matchObj = re.match(zhi_reg, u'阴阳路2之我在你左右')
    if matchObj:
        word_1 = matchObj.group(1).encode('utf8').strip()
        word_3 = matchObj.group(3).strip()
        print(word_1 + word_3)
        # len(word) >= 2
        show_name = matchObj.group(1).strip()
    # print evaluate('印度传奇故事TOP啊2019')

