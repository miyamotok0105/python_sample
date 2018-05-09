# codeing:utf-8
#デッドロックできなかった

import os
import random
from tqdm import tqdm
from time import sleep
import threading
tqdm.monitor_interval = 0

def make_file(index):
    f = open("{}.txt".format(index), "w")
    for n in range(100):
        f.write(str(random.uniform(-2, 5)) + "\n")
    f.close()

def make_file_loop():
    while True:
        # for i in tqdm(range(100) ,desc="make:"):
        for i in range(10):
            make_file(i)
        print("make")
        sleep(0.1)

def remove_file(index):
    if os.path.exists("{}.txt".format(index)):
        os.remove("{}.txt".format(index))

def remove_file_loop():
    while True:
        # for i in tqdm(range(100), desc="remove:"):
        for i in range(10):
            remove_file(i)
        print("remove")
        sleep(0.1)

thread_make = threading.Thread(target=make_file_loop)
thread_make2 = threading.Thread(target=make_file_loop)
thread_make3 = threading.Thread(target=make_file_loop)
thread_remove = threading.Thread(target=remove_file_loop)
thread_remove2 = threading.Thread(target=remove_file_loop)
thread_remove3 = threading.Thread(target=remove_file_loop)

thread_make.start()
thread_remove.start()

thread_make2.start()
thread_remove2.start()

thread_make3.start()
thread_remove3.start()


#joinでスレッドが終わるのを待つ
# thread_make.join(1)
# print(thread_make.isAlive())
# print("finished make files!!!")





