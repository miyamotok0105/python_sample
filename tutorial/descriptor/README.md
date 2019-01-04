
# 属性とディスクリプタ

## 属性


Pythonではメンバ変数(インスタンス変数)やメンバ関数(インスタンスメソッド)のことを属性(attribute)という。    
@propertyがゲッターで@hoge.setterがセッター。    
クラス外からのアクセスを明示する。    


```
class MyProp:

    # ここがgetter
    @property
    def hoge(self):
        return self.__hoge

    # ここがsetter
    @hoge.setter
    def hoge(self, value):
        print("set ", value)
        self.__hoge = value


c = MyProp()
c.hoge = 'hoge'

print(c.hoge)

```



プロパティがずらずら書かれてるのは、あまりスマートでないのでプロパティを抽象化する。


```
class Size:
    @property
    def width(self):
        return self.__w

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('value must be > 0')
        self.__w = value

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('value must be > 0')
        self.__h = value


s = Size()
s.width = 300
s.height = 400
print(s.width, s.height)

```

確かに同じなのであればまとめればいい。プロパティファクトリというらしい。    


```
def scale(name):
    def getter(instance):
        return instance.__dict__[name]

    def setter(instance, value):
        if value < 0:
            raise ValueError('value must be > 0')
        instance.__dict__[name] = value

    return property(getter, setter)

class Size:

    width = scale('width')
    height = scale('height')


s = Size()
s.width = 300
s.height = 400
print(s.width, s.height)
```

## ディスクリプタ

ディスクリプタでは__get__と__set__や__delete__の特殊関数を持ってる。プロパティと比べて、ディスクリプタの方が広範囲。    



```
class Prop:
    def __init__(self, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        print('get')
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        print('set')
        obj.__dict__[self.name] = value

class Obj:
    prop = Prop('prop')


obj = Obj()
obj.prop = 123
print(obj.prop)

obj.prop = 456
print(obj.prop)

```




# 参考

いい記事！前半の例使いました。

https://qiita.com/koshigoe/items/848ddc0272b3cee92134









