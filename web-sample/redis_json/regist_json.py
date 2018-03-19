# -*- coding:utf-8 -*-
#https://symfoware.blog.fc2.com/blog-entry-1446.html
#jsonで登録
import datetime
import json
import redis
# 登録用のデータを適用に用意(10フィールド)
map_value = {}
for i in range(10):
    map_value['value_%d' %i] = u'適当な文字列を設定しておく'
json_data = json.dumps(map_value)
start = datetime.datetime.now()
# redis client準備
r = redis.Redis(host='localhost', port=6379, db=0)
pipe = r.pipeline()
# 1000件登録
for i in range(10000):
    pipe.set('key:%d' % i, json_data)
# 登録実行
pipe.execute()
stop = datetime.datetime.now()
print(stop - start)
