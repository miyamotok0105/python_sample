# -*- coding:utf-8 -*-
#https://symfoware.blog.fc2.com/blog-entry-1446.html
import datetime
import json
import redis
start = datetime.datetime.now()
# redis client準備
r = redis.Redis(host='localhost', port=6379, db=0)
# 検索だけ実行
for i in range(10000):
    ret = json.loads(r.get('key:%d' % i).decode('utf-8'))
    # ret = json.loads()
stop = datetime.datetime.now()
print(stop - start)

dic = json.loads(r.get('key:%d' % 1).decode('utf-8'))

print(dic)
print(dic["value_6"])

