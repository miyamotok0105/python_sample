import struct
valid_png_header = b'\x89PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'


print("data[:1]", data[:1])
print("data[:2]", data[:2])
print("data[:3]", data[:3])
print("data[:4]", data[:4])
print("data[:5]", data[:5])
print("data[:6]", data[:6])
print("data[:7]", data[:7])
print("data[:8]", data[:8])

#\x89の\xは16進数のasciiなので一心同体。

if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width:', width, ',', 'height:', height)
else:
    print('Not a valid PNG')

