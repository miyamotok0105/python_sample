#!/usr/bin/python

#curl http://time.jsontest.com

import json
import urllib.request

hres = urllib.request.urlopen('http://time.jsontest.com')

data = json.loads(hres.read().decode("utf-8"))

print('Unix time: {}'.format(data['milliseconds_since_epoch']))
print('Time: {}'.format(data['time']))
print('Date: {}'.format(data['date']))
