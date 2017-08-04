#!/usr/bin/python
#-*- coding=utf-8-*-

import _json

a = 'qwer'


seed = 20170101
key = bytearray( a.encode() )
print key

length = len( key )
nblocks = int( length / 4 )



