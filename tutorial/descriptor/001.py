class MyClass:
    def m(self):
        """
        >>> c = MyClass()
        >>> c.m()
        method
        >>> c.m = 1
        >>> print(c.m)
        1
        """
        print('method')


c = MyClass()
c.m()

c.m = 1
print(c.m)

