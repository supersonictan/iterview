#!/usr/bin/python
#-*- coding=utf-8-*-

import json
import re

print 'nihao'

import json


class Leadership:
    def __init__(self, manager, date, country, gender,age,q1,q2,q3,q4,q5):
        self.manager = manager
        self.date = date
        self.country = country
        self.gender=gender
        self.age=age
        self.q1=q1
        self.q2=q2
        self.q3=q3
        self.q4=q4
        self.q5=q5

    # 重写排序方法
    def __cmp__(self, other):
        if self.gender == 'F' and other.gender == 'M':
            return -1
        elif self.gender == 'F' and other.gender == 'F':
            if self.age < other.age:
                return -1
            elif self.age > other.age:
                return 1
            else:
                return 0
        else:
            return 1

if __name__ == '__main__':
    list = [] # 去重数据
    duplicate_list = [] # 重复数据
    with open("filePath", 'r') as f:
        for line in f:
            if line in list:
                duplicate_list.append(line)
            else:
                list.append(line)
    print list # 打印去重后结果
    print duplicate_list # 重复数据

if __name__ == '__main__':
    with open("filePath", 'r') as f: #读取 exls文件
        for line in f:
            field = line.split('\t')
            column = field[3] # 假设第四列为 brand
            # myStr = 'AAA123 奔驰'
            re_result = re.search("^[A-Z]{3}[0-9]{3}", column)
            if re_result is not None:
                print re_result.group() #匹配成功打印对应字符
            else:
                print 'ERROR'   # 匹配失败打印 ERROR


    print list # 打印去重后结果
    print duplicate_list # 重复数据



if __name__ == '__main__':
    leadership_list = []  # 寸数据的list
    with open("filePath", 'r') as f:
        for line in f:
            field = line.split('\t')
            l = Leadership(field[0],field[1],field[2],field[3],field[4],field[5],field[6],field[7],field[8],field[9])
            leadership_list.append(l)
    sorted(leadership_list)




