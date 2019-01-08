#!/usr/bin/python

import json

data = [{"name": "Jane", "age": 17}, {"name": "Thomas", "age": 27}]

json_data = json.dumps(data)
print(repr(json_data))
