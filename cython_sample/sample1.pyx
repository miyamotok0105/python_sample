#! -*- coding: utf-8 -*-

c = 0
def add( a, b ) :
    global c
    c = a + b
    return c

def printResult() :
    print c
