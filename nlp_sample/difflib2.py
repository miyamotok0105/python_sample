# -*- coding: utf-8 -*-

import difflib

str1 = "スパゲッティー"
str2 = "スパゲッティ"

s = difflib.SequenceMatcher(None, str1, str2).ratio()

print(str1)
print(str2)
print("match ratio:", s, "\n")

# >> スパゲッティー <~> スパゲティ
# >> match ratio: 0.833333333333

