#!/usr/bin/python
# -*- coding=utf-8-*-
import Queue
import threading

cur_id=0
query_queue = Queue.Queue()
lock_curId = threading.RLock()