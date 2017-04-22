#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time

exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self): #线程启动会执行run函数
        print 'Starting ', self.name
        print_time(self.name,5,self.counter)
        print 'End ', self.name


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print threadName, " ", time.strftime("%Y%m%d %H:%M:%S", time.localtime())
        counter -=1


t1 = myThread(1, "Thread-1", 5)
t2 = myThread(2, "Thread-2", 3)
t1.start()
t2.start()

print "Exit Main Thread..."