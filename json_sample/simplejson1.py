#!/usr/bin/python

import json

data = {"name": "Jane", "age": 17}

with open('friends.json', 'w') as f:
    json.dump(data, f)
    
