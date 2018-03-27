#__len__など特殊メソッドはpythonインタプリタから呼び出すように作られていない。
#obj.__len__()とは書かない。len(obj)と書く。
#len()はメソッド呼び出しより高速に動く。lenが良く呼び出される機能のために特別扱いされた。
#特殊メソッドは暗黙的に呼び出される。for i in x:はiter(x)を呼び出しx.__iter__()を呼び出す。
#__init__はスーパークラスのイニシャライザ呼び出しで、よく呼ばれる。
#len iter strはある程度使われる。
#特殊メソッド
#https://docs.python.jp/3.3/reference/datamodel.html
from math import hypot

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #reprと似てる
    # def __str__(self):
    #     return '__str__ Vector(%r, %r)' % (self.x, self.y)

    def __repr__(self):
        #__repr__はオブジェクトそのものの文字列を取得する。オブジェクトの中身をチェック。
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == '__main__':
    v1 = Vector(2, 4)
    v2 = Vector(2, 1)

    print("ベクトルの足し算")
    #__add__がないとエラになるよー
    print(v1 + v2)

    v = Vector(3, 4)
    print("absは整数及び浮動小数点の絶対値または複素数の大きさを返す。")
    print("ここではVector(3, 4)ベクトルの大きさを計算する")
    print(v)
    #__abs__がないとエラーになるよ。
    print(abs(v))
    print("3倍する")
    print(v * 3)
    print(abs(v * 3))


