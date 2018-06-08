
structは文字列からバイナリ変換、バイナリから文字列変換を担う。    


よく\xっての見るけども下の意味だよ    

```
\ ooo  8 進表記の ASCII 文字
\x hh  16 進表記の ASCII 文字
\x hhhh    このエスケープ シーケンスがワイド文字定数または Unicode 文字列リテラルで使用されている場合は、16 進表記の Unicode 文字。
```

アスキー文字コード一覧    
http://digital.ni.com/public.nsf/allkb/D831B5F2D5CA212E86257A21002055E6    


bytes型の要素アクセスはスライス使うと良い    
１要素でアクセスすると取れない    


```
print("data[:1]", data[:1])
print("data[:2]", data[:2])
print("data[:3]", data[:3])
print("data[:4]", data[:4])
print("data[:5]", data[:5])
print("data[:6]", data[:6])
print("data[:7]", data[:7])
print("data[:8]", data[:8])
>data[:1] b'\x89'
data[:2] b'\x89P'
data[:3] b'\x89PN'
data[:4] b'\x89PNG'
data[:5] b'\x89PNG\r'
data[:6] b'\x89PNG\r\n'
data[:7] b'\x89PNG\r\n\x1a'
data[:8] b'\x89PNG\r\n\x1a\n'

```

PNGのバイナリ取得において、これはいけるわけなんで    
==で比較できる。    
struct.unpack('>LL', data[16:24])のunpackはバイトから文字への変換。    
>LLは

```
< リトルエンディアン standard none
> ビッグエンディアン standard none
```

フォーマット文字列    
サイズが4になってるのでLLになると８文字分。    
サイズとるならPNG ファイルシグネチャ8バイトの続きの８文字なのでOK    
PNGフォーマットが9文字目からがサイズが入ってるって意味    
https://www.setsuki.com/hsp/ext/png.htm    
https://www.setsuki.com/hsp/ext/chunk/IHDR.htm    


```
L unsigned long 整数 4
```

その他のフォーマット文字列    
https://docs.python.jp/3.5/library/struct.html    


```
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width:', width, ',', 'height:', height)
```



# 参考

Python3書籍    
http://apprize.info/python/introducing/7.html    
https://gist.github.com/Boyden/9211dffdeac64516ac2953484f4b1f02    
今更バイナリ。。。    
http://deutschina.hatenablog.com/entry/2016/01/24/013000    
Python公式    
https://docs.python.jp/3.5/library/struct.html    
PNGフォーマット    
https://www.setsuki.com/hsp/ext/png.htm    

Python で png 画像を自力で生成するAdd Star    
http://d.hatena.ne.jp/c-yan2/20100317/1268825146    
Working with Binary Data in Python    
https://www.devdungeon.com/content/working-binary-data-python    




