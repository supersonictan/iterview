#!/usr/bin/python
# -*- coding=utf-8-*-
import logging

"""
调用方式：logger = Logger(logname='log.txt', loglevel=1, logger="fox").getlog()
StreamHandler: 输出到控制台
 FileHandler:   输出到文件
BaseRotatingHandler 可以按时间写入到不同的日志中。比如将日志按天写入不同的日期结尾的文件文件。
SocketHandler 用TCP网络连接写LOG
DatagramHandler 用UDP网络连接写LOG
SMTPHandler 把LOG写成EMAIL邮寄出去
"""
class Logger():
    def __init__(self, logFileName, logger):
        '''
           指定保存日志的文件路径，日志级别，以及调用文件
           将日志存入到指定的文件中
        '''

        # 根据输入logger 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        fh = logging.FileHandler(logFileName)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(message)s')
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #formatter = format_dict[int(loglevel)]
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
