import struct

# - struct.unpack(フォーマット, 値)
#バッファ buffer を、 offset の位置から書式化文字列 fmt に従ってアンパック

# struct.pack(フォーマット, 値)


png_data = open("sample.png", "rb").read()
print(png_data[13:40])

# #PNGファイルは頭の8バイトはヘッダ
# print(struct.unpack_from(">I4sIIBB", png_data, 1))
# print(struct.unpack_from(">I4sIIBB", png_data, 2))
# print(struct.unpack_from(">I4sIIBB", png_data, 3))
# print(struct.unpack_from(">I4sIIBB", png_data, 4))
# print(struct.unpack_from(">I4sIIBB", png_data, 5))
# print(struct.unpack_from(">I4sIIBB", png_data, 6))
# print(struct.unpack_from(">I4sIIBB", png_data, 7))
# print(struct.unpack_from(">I4sIIBB", png_data, 8))




