# -*- coding: utf-8 -*-

#异常处理
try:
    list = [1, 2,3]
    list[5]
except Exception:
    print 'IndexErr'
except KeyError:
    print 'Exception occur'

