#!/usr/bin/python

import json

json_data = '{"name": "Jane", "age": 17}'

data = json.loads(json_data)

print(type(json_data))
print(type(data))

print(data)
