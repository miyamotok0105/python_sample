import ctypes

cptr = ctypes.POINTER(ctypes.c_char)  # charポインタ型として型を定義しておく
#！！！！ctypes.cdll.LoadLibraryでsoファイルを読み込む！！！！
lib = ctypes.cdll.LoadLibrary('./lib1.so') 
lib.reverse_bytes.argtypes = (ctypes.c_int, cptr)  # 引数の型
lib.reverse_bytes.restype = cptr  # 返り値の型

def reverse_bytes(buf):
    """ラッパー関数
    """
    n = len(buf)
    result = lib.reverse_bytes(n, buf)[:n]  # スライス操作によってpythonのbytes型に変換される
    lib.free_result()  # mallocした領域をfree
    return result

if __name__ == "__main__":
    print(b"\x00\x01\x02\x03")
    print(reverse_bytes(b"\x00\x01\x02\x03"))  # b"\x00\x01\x02\x03"というバイト列をreverseしてみる|
    # => b'\x03\x02\x01\x00'
