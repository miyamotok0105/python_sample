#! /usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import print_function

import difflib
import time

#http://blog.mudatobunka.org/entry/2016/05/08/154934

#日本語の処理をしているときに厄介なのが表記揺れだそう。
#「コンピューター」と「コンピュータ」、「問い合わせ」と「問い合せ」の違いなどらしい。


#単語間の類似度を算出する
print("結論：始めの方が違うと後が全部ずれて類似度が下がる")

text1 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
やゆよ
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''
text2 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
やゆよら
りるれろ
わをん
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ァィゥェォ
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''

print("どっかが違う")
s = difflib.SequenceMatcher(None, text1, text2)
#シーケンスのどこがマッチしているか
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
print("match ratio:", s.ratio(), "\n")





text1 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''
text2 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''

print("全部同じ")
s = difflib.SequenceMatcher(None, text1, text2)
#シーケンスのどこがマッチしているか
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
print("match ratio:", s.ratio(), "\n")





text1 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''
text2 = '''あいうえお
かきくけ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''

print("始めの方を変えた")
s = difflib.SequenceMatcher(None, text1, text2)
#シーケンスのどこがマッチしているか
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
print("match ratio:", s.ratio(), "\n")






text1 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブベボ
パピプペポ'''
text2 = '''あいうえお
かきくけこ
さしすせそ
たちつてと
なにぬねの
はひふへほ
まみむめも
らりるれろ
わをん
がぎぐげご
ざじずぜぞ
だぢづでど
ばびぶべぼ
ぱぴぷぺぽ
アイウエオ
カキクケコ
サシスセソ
タチツテト
ナニヌネノ
ハヒフヘホ
マミムメモ
ヤユヨ
ラリルレロ
ワヲン
ガギグゲゴ
ザジズゼゾ
ダヂヅデド
バビブボ
パピプペポ'''

print("最後の方を変えた")

s = difflib.SequenceMatcher(None, text1, text2)
#シーケンスのどこがマッチしているか
for block in s.get_matching_blocks():
    print("a[%d] and b[%d] match for %d elements" % block)
print("match ratio:", s.ratio(), "\n")


#いろいろな単語同士を比較する

# -*- coding: utf-8 -*-

import difflib


# 互いに類似度を比較する文字列のリスト
strs = [
    "スパゲッティー",
    "ｽﾊﾟｹﾞｯﾃｨ",
    "スパゲティ",
    "カペッリーニ",
]

# リスト内包表記で strs の中の文字列から重複なしの組み合わせを作る
for (str1, str2) in [
        (str1, str2)
        for str1 in strs
        for str2 in strs
        if str1 < str2
    ]:
    print(str1)
    print(str2)

    # 類似度を計算、0.0~1.0 で結果が返る
    s = difflib.SequenceMatcher(None, str1, str2).ratio()
    print("match ratio:", s, "\n")





