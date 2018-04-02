#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd
import csv

csv_data = pd.read_csv('csv1.csv')
print(csv_data.shape)
print(csv_data)

csv_data = pd.read_csv('csv1.csv', index_col=0)
print(csv_data.shape)
print(csv_data)

csv_data = pd.read_csv('csv1.csv', header=None)
print("len:", len(csv_data.columns))
print(type(csv_data))
print(csv_data)

print("=======")
csv0 = [c for c in csv_data[0]]
csv1 = [c for c in csv_data[1]]
csv2 = [c for c in csv_data[2]]
csv3 = [c for c in csv_data[3]]
csv4 = [c for c in csv_data[4]]
csv5 = [c for c in csv_data[5]]
csv6 = [c for c in csv_data[6]]

for row in zip(csv0, csv1, csv2, csv3, csv4, csv5, csv6):
    print(row)

print("=======")
def gen_list(data):
    l = [c for c in data]
    return l

for i in range(len(csv_data.columns)):
    print(gen_list(csv_data[i]))

# lambda i:i**2,range(1,11)



