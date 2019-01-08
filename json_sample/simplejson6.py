#!/usr/bin/python

import json

json_data = {"name":"Audi", "model":"2012", "price":22000, 
                 "colours":["gray", "red", "white"]}

data = json.dumps(json_data, sort_keys=True, indent=4 * ' ')

print(data)
