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
