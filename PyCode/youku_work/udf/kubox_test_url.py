# -*- coding: utf-8 -*-
import os

#http://pre.kubox.soku.proxy.taobao.org/sug?s=kubox&query=%E6%9D%A8%E5%B9%82&outfmt=json&trace=info&utdid=WDf8U3xYysUDAEddIyR8%2bNRT&ip=106.11.35.153



if __name__ == '__main__':
    list = []
    s1 = 'a'
    s2 = 'b'
    list1 = ['1','2']
    list2 = ['3','4']
    tuple = (s1, list1)
    tuple2 = (s2, list2)
    list.append(tuple)
    list.append(tuple2)
    for each in list:
        a,b = each
        print a,b
    # for root ,dirs, files in os.walk('/Users/tanzhen/Desktop/code/iterview/PyCode/python_study'):
    #     print type(files)


