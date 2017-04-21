# -*- coding: utf-8 -*-
import time





def time_counter(func):
    def wrapper():
        st = time.clock()
        func()
        end = time.clock()
        print "Cost time: ", end-st ,"s"
    return wrapper

@time_counter
def sayHi():
    print "Call sayHi...."
    time.sleep(2)

sayHi()


