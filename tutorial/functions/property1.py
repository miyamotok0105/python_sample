
class MyProperty:
    def __init__(self):
        self._x = None

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def del_x(self):
        del self._x

class MyProperty2:
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x


if __name__ == '__main__':
    print("普通の書き方")
    nopro = MyProperty()
    nopro._x = 100
    print(nopro.get_x()) # 100

    nopro.set_x(-200)
    print(nopro.get_x()) # 200

    # nopro.del_x()
    # print(nopro.get_x()) # None

    print("デコレータを使った書き方")
    pro = MyProperty2()
    pro.x = 100
    print(pro.x) # 100

    pro.x = -200
    print(pro.x) # 200

    # del pro.x
    # print(pro.x) # None
    

