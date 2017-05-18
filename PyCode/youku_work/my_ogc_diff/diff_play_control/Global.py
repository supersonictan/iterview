#!/usr/bin/python
# -*- coding=utf-8-*-
import Queue

#HTTP Get 参数
on_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s'
on_expid = '112'
on_ip = ''
on_qa = '1'

off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s'
off_expid = '112'
off_ip = '11.173.213.132:2090'
off_qa = '1'



showname_dic = {}
query_queue = Queue.Queue()
diff_num = 0 #同步

