from abc import ABCMeta, abstractmethod
from functools import singledispatch

#思った動きをしてくれてない。
#一旦保留。
#使い方がわかってないと思われる。
#https://github.com/seequent/methoddispatch

class Animation(metaclass=ABCMeta):
    @abstractmethod
    def bloadcast(self):
        pass

class Animation2(metaclass=ABCMeta):
    @abstractmethod
    def bloadcast(self, num):
        pass

class SSSSGridman(Animation):
    def bloadcast(self):
        return "gridman !!!"

class Jojo(Animation):
    def bloadcast(self):
        return "yareyaredaze !!!"

class SSSSGridman2(Animation2):
    def bloadcast(self, num):
        return "gridman !!!"+str(num)

class Watcher():

    def __init__(self):
        self.animation = None

    @singledispatch
    def receive_fashion(self, animation):
        # raise Exception("It's not ANIME")
        print("It's not ANIME")

    @receive_fashion.register(SSSSGridman)
    @receive_fashion.register(Jojo)
    def _(self, animation):
        print('animation')
        self.animation = animation

    @receive_fashion.register(SSSSGridman2)
    def _(self, animation):
        print('animation2')
        self.animation = animation

    @singledispatch
    def watch(self):
        print("It's not ANIME")

    @watch.register(SSSSGridman)
    @watch.register(Jojo)
    def _(self):
        print("I watchd", self.animation.bloadcast())

    @watch.register(SSSSGridman2)
    def _(self):
        print("I watchd", self.animation.bloadcast(1))


if __name__ == "__main__":
    watcher = Watcher()
    watcher.receive_fashion(Jojo())
    watcher.watch()
    print("====")
    watcher.receive_fashion(SSSSGridman())
    watcher.watch()
    print("====")
    watcher.receive_fashion(SSSSGridman2())
    watcher.watch()
    # watcher.receive_fashion("あにめじゃないもの")
    