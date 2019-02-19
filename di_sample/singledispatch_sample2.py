#http://momijiame.tumblr.com/post/93303753531/python-%E3%81%AE-singledispatch-%E3%81%A7%E5%BC%95%E6%95%B0%E3%81%AE%E5%9E%8B%E3%81%94%E3%81%A8%E3%81%AB%E5%87%A6%E7%90%86%E3%82%92%E5%88%86%E3%81%91%E3%82%8B

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import singledispatch

#singledispatchでコレータを使うと
#argに入ってきた引数によって処理を分けれる。

@singledispatch
def accept_int_and_list(arg):
    print('type error')


@accept_int_and_list.register(int)
def _accept_int(arg):
    print('int')


@accept_int_and_list.register(list)
def _accept_list(arg):
    print('list')


if __name__ == '__main__':
    accept_int_and_list(0)
    accept_int_and_list([])
    accept_int_and_list(object())