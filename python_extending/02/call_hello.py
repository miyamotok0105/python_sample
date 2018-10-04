
path = "./build/lib.macosx-10.12-x86_64-2.7/hello.so"
import ctypes
lib = ctypes.cdll.LoadLibrary(path)

print(lib.hello_world())

