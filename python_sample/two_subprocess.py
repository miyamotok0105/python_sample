import time
import datetime
import subprocess
import threading


# for i in range(20):
#     mkdir_proc("A", i)
#     print(i)

# print("-------------------")


class TestThread(threading.Thread):

    """docstring for TestThread"""

    def __init__(self, n, t):
        super(TestThread, self).__init__()
        self.n = n
        self.t = t

    def mkdir_proc(ctg, num):
        cmd = "mkdir data/%s%s;"%(ctg, num)
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = proc.communicate()

    def run(self):
        print " === start sub thread (sub class) === "
        for i in range(self.n):
            time.sleep(self.t)
            mkdir_proc(self.n,i)
            print "sub thread (sub class) : " + str(datetime.datetime.today())
        print " === end sub thread (sub class) === "

class TestThread2(threading.Thread):
    def __init__(self, n, name):
        super(TestThread2, self).__init__()
        self.n = n
        self.name = name

    def mkdir_proc(self, ctg, num):
        cmd = "mkdir data/%s%s"%(ctg, num)
        proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout_data, stderr_data = proc.communicate()

    def run(self):
        for i in range(self.n):
            time.sleep(1)
            self.mkdir_proc(self.name,i)
            print("sub thread (sub class %s ) : "%(self.name) + str(datetime.datetime.today()))

if __name__ == '__main__':
    th_cl = TestThread2(5, "A")
    th_cl.start()
    th_cl = TestThread2(5, "B")
    th_cl.start()

    # time.sleep(1)

    # print " === start main thread (main) === "
    # for i in range(5):
    #     time.sleep(10)
    #     print "main thread : " + str(datetime.datetime.today())
    # print " == end main thread === "
