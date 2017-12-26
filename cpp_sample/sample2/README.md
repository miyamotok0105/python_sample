
#boostを使う

## コンパイル

    g++ -I`python -c 'from distutils.sysconfig import *; print get_python_inc()'` -DPIC -bundle -fPIC -o simple.so simple.cxx -lboost_python  -framework Python

    g++ -I`python -c 'from distutils.sysconfig import *; print get_python_inc()'` -DPIC -bundle -fPIC -o simple2.so simple2.cpp -lboost_python  -framework Python


## 実行する

    python call_simple.py
    python call_simple2.py


