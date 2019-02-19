from abc import ABCMeta, abstractmethod

class Animation(metaclass=ABCMeta):
    @abstractmethod
    def bloadcast(self):
        pass

class SSSSGridman(Animation):

    def bloadcast(self):
        return "gridman !!!"


class Jojo(Animation):

    def bloadcast(self):
        return "yareyaredaze !!!"

class Watcher():

    def receive_fashion(self, animation):
        if not isinstance(animation, Animation):
            raise Exception("It's not ANIME")
        self.animation = animation 

    def watch(self):
        print("I watchd", self.animation.bloadcast())


if __name__ == "__main__":
    watcher = Watcher()
    watcher.receive_fashion(Jojo())
    watcher.watch()
    watcher.receive_fashion(SSSSGridman())
    watcher.watch()
    # watcher.receive_fashion("あにめじゃないもの")
    