from abc import ABCMeta, abstractmethod

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

    def receive_fashion(self, animation):
        if not isinstance(animation, Animation) and not isinstance(animation, Animation2):
            raise Exception("It's not ANIME")
        self.animation = animation 

    def watch(self):
        if isinstance(self.animation, Animation):
            print("I watchd", self.animation.bloadcast())
        elif isinstance(self.animation, Animation2):
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
    