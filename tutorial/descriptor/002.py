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




