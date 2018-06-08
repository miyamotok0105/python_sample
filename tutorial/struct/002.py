import struct

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)#bytesに変換できてる:イミュータブル
print(the_bytes)

#\ ooo  8 進表記の ASCII 文字
#\x hh  16 進表記の ASCII 文字
#\x hhhh    このエスケープ シーケンスがワイド文字定数または Unicode 文字列リテラルで使用されている場合は、16 進表記の Unicode 文字。


#アクセスすると\xが消えるのね
print(the_bytes[0])
print(the_bytes[1])
print(the_bytes[2])


the_byte_array = bytearray(blist)#bytesarrayってのもあるのね:ミュータブル
print(the_byte_array)



print(b'\x61')
print(b'\x01abc\xff')#ascii文字はそのままabc
