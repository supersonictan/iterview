#!/usr/bin/python
#-*- coding=utf-8-*-

from optparse import OptionParser 
import requests

print 'nihao'
"""
usage = "usage: %prog [options] arg1 arg2"
parser = OptionParser(usage=usage) 
parser.add_option("-p", "--p2", action="store_true", dest="p", default=False, help="this is p help!") 
parser.add_option("-z", "--z2", action="store_false", dest="z", default=False, help="this is z help!") 
(options, args) = parser.parse_args() 
print len(args)
print 'p is ', options.p
print 'z is ', options.z
"""
r = requests.get('http://www.baidu.com')
print r.text

