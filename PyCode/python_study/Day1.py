# -*- coding: utf-8 -*-
import os
import sys
"""
内容：
    Part_1: 导入模块 improt是导入整个模块
            from os improt *从某个模块导入特定方法。
            别名: import moduleName as newName
    Part_2: row_input("Please input ....")
    Part_3: 缩进在linux下tab是8个空格，win下是4个。
    Part_4: 查看变量类型：print type(var)
            强制类型转换: int("123")
    Part_5: 
	    python的true:True
	    if age>50:
            elif age=0:
            else:
    Part_6: 循环
	     for i in range(1,100),会打印[1,99], 
	     range也可以range(100), 
	     range(1,100,2) 
	     
"""


#Part_2:
name = raw_input("Input something")
print "Hello " + name

#Part_6:
for i in range(0,10,2):
    print i
