import timeit
import ctypes

lib2 = ctypes.cdll.LoadLibrary('./lib2.so')
lib2.reverse_bytes.argtypes = (ctypes.c_int, ctypes.c_char_p)  # 型が変わる
lib2.reverse_bytes.restype = ctypes.c_char_p

lib3 = ctypes.cdll.LoadLibrary('./lib3.so')
lib3.reverse_str.argtypes = (ctypes.c_int, ctypes.c_wchar_p)  # 型が変わる
lib3.reverse_str.restype = ctypes.c_wchar_p

def reverse_bytes(buf):
    n = len(buf)
    result = lib2.reverse_bytes(n, buf)
    lib2.free_result()
    return result

def reverse_str(buf):
    n = len(buf)
    result = lib3.reverse_str(n, buf)
    lib3.free_result()
    return result


if __name__ == "__main__":
    print("========")
    print(b"hoge")
    print(reverse_bytes(b"hoge"))  # => b'egoh'

    print("========")
    s = "hogefugaほげふが"*(10**3)
    print(s[::-1] == reverse_str(s))
    print(timeit.timeit(lambda : reverse_str(s), number=10**3))
    print(timeit.timeit(lambda : s[::-1], number=10**3))