
# for i in range(1000):
#     f = open("hoge.txt", "a") # ★読み書きモードに変更


# for i in range(100):
#     aa = open('/dev/null', 'w')
#     print(aa)


# aa = open('/dev/null', 'w')
# print(aa)

# for i in range(1000):
#     f = open("hoge.txt", "r+") # ★読み書きモードに変更


import threading
import time
import datetime

class TestThread(threading.Thread):

    def __init__(self, n):
        super(TestThread, self).__init__()
        self.n = n

    def run(self):
        for i in range(100):
            aa = open('/dev/null', 'w')
            print("n : " + str(self.n) + str(aa))

if __name__ == '__main__':
    th_cl1 = TestThread(1)
    th_cl1.start()
    th_cl2 = TestThread(2)
    th_cl2.start()

    time.sleep(1)

    # for i in range(5):
    #     time.sleep(1)
    #     print("main thread : " + str(datetime.datetime.today()))





