import unittest
from unittest import mock

def hoge():
    return fuga()
 
def fuga():
    return 'Here is Fuga!'
 
def main():
    res = hoge()
    print(res)
 
if __name__ == '__main__':
    main()
    
