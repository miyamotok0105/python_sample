#!/usr/bin/python

import json

with open('friends.json') as f:
    config = json.load(f)
    
    print('name: {}'.format(config['name']))
    print('age: {}'.format(config['age']))
