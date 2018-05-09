#coding=utf-8 
import fcntl
import sys

lock_filename = '19.txt'
lock_file = open(lock_filename, 'w')

try:
    fcntl.lockf(lock_file, fcntl.LOCK_EX | fcntl.LOCK_NB)
except IOError:
    print('Cannot lock: ' + lock_filename)
    sys.exit(1)

print('Locked! Running code...')

quit = False
while quit is not True:
    quit = input('Press q to quit ')
    quit = str(quit) == 'q'

print('Bye!')
sys.exit(0)
