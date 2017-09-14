# -*- coding: utf-8 -*-
from datetime import datetime as dt
import os

tdatetime = dt.now()
tstr = tdatetime.strftime('%Y%m%d')
# 名前が『月日-曜日-時間』 のフォルダが作成されます
os.mkdir(tstr)
