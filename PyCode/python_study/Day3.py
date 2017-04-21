#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
类
继承
"""
#类
class Employee:
    #类变量，所有实例之间共享。可在内部类或外部类使用 Employee.empCount
    empCount = 0
    __private_name = 'private'#私有属性

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print '__private_name:', self.__private_name #访问私有属性
        Employee.empCount += 1
    #析构函数
    def __del__(self):
        print "Del:",self.__class__.__name__

    #类的方法与普通的函数区别:第一个参数必为self。私有以__开头
    def __displayEmp(self):
        print self  #self是类实例,代表当前对象地址
        print self.__class__ #指向类
        print "Name:", self.name, ", Salary:", self.salary

e = Employee("tanzhen",50000)
e.age = 28 #增加属性
e.age = 27 #修改属性
del e.age   #删除属性
print e.age #查看属性
print Employee.__doc__ #类文档字符串
print Employee.__name__ #类名
print Employee.__dict__ #类的属性
print Employee.__module__ #类所在模块

#继承
# class Parent:
#     parentAttr = 100
#     def __init__(self):
#         print "Parent init"
#
# class Child(Parent):
#     childAttr = 1
#     def __init__(self):
#         print "Child init"
# c = Child()
