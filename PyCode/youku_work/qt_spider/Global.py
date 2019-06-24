#!/usr/bin/python
# -*- coding=utf-8-*-
import Queue
import threading

#HTTP Get 参数
off_url = 'http://imerge-pre.soku.proxy.taobao.org/i/s'
off_expid = '110'
off_ip = '11.134.231.181:2090'
#off_ip = '11.173.213.132:2090'
off_qa = '1'

on_url = 'http://imerge.soku.proxy.taobao.org/i/s'
on_expid = '110'
on_ip = '11.173.227.22:2090'
on_qa = '1'



query_file='../data/top8000'
thread_num=20
#is_log_need_id=0


total_pv = 0
loss_pv = 0
cur_id=0
query_queue = Queue.Queue()
diff_num = 0 #同步
lock = threading.RLock()
lock_curId = threading.RLock()

lock_pv = threading.RLock()
lock_losspv = threading.RLock()

