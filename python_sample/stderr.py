#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from io import BytesIO
#------------------------------------

# sys.stdout.write('success hoge\n')
# sys.exit(0) #success

try:
    num1   = 5
    num2   = '7'
    answer = num1 + num2
     
    print('num1 + num2 = {}'.format(answer))
except Exception as e:
    sys.stderr.write(e.args)
    print(file=sys.stderr)

sys.exit(1)

#------------------------------------
# io = BytesIO()

# # 標準出力を io に結びつける
# sys.stdout = io
# print('hoge')

# # 標準出力を元に戻す
# sys.stdout = sys.__stdout__
# print('captured: {}'.format(io.getvalue())) # captured: hoge\n

#------------------------------------
