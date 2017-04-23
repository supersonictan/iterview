# -*- coding: utf-8 -*-


#默认参数
def sayHi(name, group="Alibaba", salary=40000):
    print "name " + name + " group:" +group

#可变参数-返回元祖
def varibleParam(*args):
    print args

#返回字典
def varibleParam2(**kwargs):
    print kwargs

g = lambda x,y:x**y

a = [1,2,3,4,5]
b = [1,2,3,4,5]

c = {8:'d', 9:'e', 2:'a', 4:'b'}
if __name__ == '__main__':
    print sorted(c.items(), key=lambda x:x[0], reverse=True)
    #print map(lambda x,y:x**y,a,b)
    # varibleParam("tan",'zhen',50000)
    # varibleParam2(name='tan',val='shuai')
    # sayHi("tanzhen", salary=50000)
