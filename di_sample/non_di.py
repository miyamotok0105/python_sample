class SSSSGridman():

    def bloadcast(self):
        return "gridman !!!"

class Jojo():

    def bloadcast(self):
        return "yareyaredaze !!!"

class Watcher():

    def in_my_heart(self):
        self.jojo = SSSSGridman() 

    def watch(self):
        print("I watchd", self.jojo.bloadcast())


if __name__ == "__main__":
    watcher = Watcher()
    watcher.in_my_heart()
    watcher.watch()
