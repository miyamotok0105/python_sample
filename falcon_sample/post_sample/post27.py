# -*- coding:utf-8 -*-
import json
import urllib2
values = {'name' : 'symfo'}
data = json.dumps(values)
response = urllib2.urlopen('http://0.0.0.0:8000', data)
body = response.read()
response.close()
data = json.loads(body)
print(data['message'])