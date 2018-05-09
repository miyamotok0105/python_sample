#coding=utf-8 
import fcntl
import threading

def task():
    lock_filename = '19.txt'
    lock_file = open(lock_filename, 'w')
    try:
        fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError:
        print('Cannot lock: ' + lock_filename)
        return False
    print('Locked! Running code...')
    quit = False
    while quit is not True:
        quit = input('Press q to quit ')
        quit = str(quit) == 'q'
    print('Bye!')
    return True

if __name__ == '__main__':
    print('creating threads')
    first_thread = threading.Thread(target=task, args=())
    second_thread = threading.Thread(target=task, args=())

    print('starting threads')
    first_thread.start()
    second_thread.start()

    print('joining threads')
    first_thread.join()
    second_thread.join()

    print('closing')