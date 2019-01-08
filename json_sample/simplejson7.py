#!/usr/bin/python

import json

class Person(object):
    
    def __init__(self, name, age):
    
        self.name = name
        self.age = age
        
p = Person("Lucy", 23) 

json_data = json.dumps(p.__dict__)

print(repr(json_data))
