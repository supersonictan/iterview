#!/usr/bin/python
# -*- coding=utf-8-*-
import Queue
import threading

q = Queue.Queue()


if __name__ == '__main__':
    q.get(block=True, timeout=3)
    print 'Ha'
