
# ctypesを使う記事

## バイトの受け渡し

- 共有ライブラリにしてビルド    


-fPIC：PIC (Position Independent Code)にするオプション。    
       PICは実行時に再配置が不要なオブジェクト。

-shared：共有ライブラリ。    


```
gcc -shared -fPIC lib1.c -o lib1.so
```

- pythonからctypesの呼び出し    


ctypes.cdll.LoadLibraryでsoファイルを読み込む。c言語のcharでは0がnullの意味で、文字列が途中で止まってしまう。そのためにctypes.POINTER(ctypes.c_char)という型を使う。    


```
python byte_reverse.py
```

## 文字列受け渡し



```
gcc -shared -fPIC lib2.c -o lib2.so
gcc -shared -fPIC lib3.c -o lib3.so
```



# 参考

バイト列、文字列の取り扱いに関する記事。    
分かり易過ぎる。    

https://www.haya-programming.com/entry/2018/11/05/023748

型について。    

https://qiita.com/everylittle/items/25d5f407f51f5e515d29