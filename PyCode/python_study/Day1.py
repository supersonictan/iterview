# -*- coding: utf-8 -*-
import os
import sys

"""
Day1内容：
    1. import:
        导入模块 improt是导入整个模块
        from os improt *从某个模块导入特定方法。
        别名: import moduleName as newName
    2. 交互输入:
        row_input("Please input ....")
    3. 缩进:
        缩进在linux下tab是8个空格，win下是4个。
    4. 类型:
        查看变量类型：print type(var)
        强制类型转换: int("123")
    5. if:
	    python的true:True
	    if age>50:
        elif age=0:
        else:
    6: 循环
	     for i in range(1,100),会打印[1,99], 
	     range也可以range(100)
	     range(1,100,2)-->间隔2

Day2内容：
    1: 文件创建 file('test.txt','r/w/a'),与open一样,r不存在报错，w文件不存在创建
        with open('pythonFile.txt','r') as f --不需要关闭文件
    2: 写文件:
        w+:读写, wb:二进制方式,处理win到unix的^M
        f = file('pythonFile.txt','w');
        f.write("test\n");
        f.close()需要关闭才能写入,可以强制写入f.flush()
    3. 读文件:
        f.read():全部显示到一行，全部加载到内存。
        f.readlines():#返回list形式，for i in readlines()会加载全部数据到内存
        f.xreadlines():迭代器，一行一行往内存读,大文件需要xreadlines
    4. 列表:
        4.1 定义:names = ['MS', 'Google', 'Ali']
        4.2 API:
            names.append()->后面追加
            names.insert(1,'txt')->插入到制定位置
            names.count('IBM')->有多少个IBM
            names.index('MS')   ->第一个MS位置
            '-'.join(names)    ->按照-将列表拼接为string
            del names[6:10]    ->从内存删除6到10内存
            names.sort
            names.revert
        4.3 查找:
            names[0:10]
            names[:5] 前5个
            names[-5:]最后5个
    5. 元祖
        5.1 定义元祖： tuple = ('a','b')
        5.2 转换
            列表转元祖：tuple(list)
    6. 字典
        6.1 API
            has_key()
            clear()清空




"""


# -------------------------------Day2:1
a = ['a', 'b', 'c']
b = ['1', 2, 3, 4]
print zip(a, b)
c = map(None, a, b)
print c

# 字典
dic = {
    'supersonic': ['good', 'nice', 'intelligent'],
    'john': ['jgood', 'jnice', 'jintelligent']
}
dic2 = {
    't': 300
}
dic.setdefault('t', 100)
dic['t'] = 200
dic.update(dic2)
print dic.get("t")
print dic.keys()

print dic['supersonic']

names = ['MS', 'MS', 'Google', 'Ali']
names.append('JD')
names.insert(1, 'MS2')
names.reverse()
for i, v in enumerate(names):
    print i
print names.count('MS')
print names.index('MS')
print names
print '-'.join(names)

# 写入
f = file('pythonFile.txt', 'a')
f.write("test\n22222\n3333333\n4444444444\n5555555\n666666666\n")
f.flush()
f.close()

# 使用with open打开文件
# with open('pythonFile.txt','r') as f:
#     for i in f.readlines():
#         print i,

# 读取
# f = file('pythonFile.txt','r')
# for i in f.read():
#     print i
# print "f.read():" + f.read() #读全部

# print  f.readlines() #list形式，for i in readlines()会加载全部数据到内存
#
# print f.tell()
# f.seek(1)
# print "f.readline():" + f.readline()




# -----------------------------------------Day1:Part_2:
# name = raw_input("Input something")
# print "Hello " + name
#
# #Day1:Part_6:
# for i in range(0,10,2):
#     print i
