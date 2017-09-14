# -*- coding:utf-8 -*-
import os
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# f = open(os.path.join("img", '1.png'), 'rb')
# binary = f.read()
# f.close()
# r.set('img1', binary)

print(type(r.get('img1')))

# f = open('result.png', 'wb')
# f.write(r.get('pic'))
# f.close()
