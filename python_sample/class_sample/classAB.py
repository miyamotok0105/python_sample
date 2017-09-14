

class A(object):
    def __new__(cls):
        print('new')
        # return super().__new__(cls)

    def __init__(self):
        print('init')
        super().__init__()

class B(A):
    pass

A()


class C(object):

    # def __init__(self):
    #     # raise
    #     print('c init')
        # super().__init__()
    def func1(self):
        print("func1")

try:
    c_obj = C()
except Exception as e:
    print(c_obj)
    # print(str(e.message))



