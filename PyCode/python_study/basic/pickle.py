# -*- coding: utf-8 -*-
from trace import pickle
import json
import time
"""
pickle、json序列化
时间
"""
account_info = {
    'tanzhen':[10000,10001,10002],
    'tz':[20000,20001,20002],
}
#序列化到文件
with open('account_pickle', 'wb') as f:
    pickle.dump(account_info, f)
#反序列化到对象
with open('account_pickle', 'rb') as f:
    obj = pickle.load(f)

#序列化为字符串\反序列化
print pickle.loads(pickle.dumps(account_info))
print obj


#序列化为json
print json.dumps(account_info)

#时间戳
st = time.clock()
time.sleep(1)
print "执行花费时间:", time.clock()-st
print "时间戳:", time.time()
print "结构化时间:", time.localtime(time.time())
print "可读时间:", time.asctime(time.localtime(time.time()))
print "格式化成2016-03-20 11:45:39形式:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print "时间转时间戳:", time.mktime(time.strptime("2017-04-20 13:55:50","%Y-%m-%d %H:%M:%S"))