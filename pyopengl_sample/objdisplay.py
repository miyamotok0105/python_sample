import sys

fp = open(sys.argv[1], 'r')
for line in fp.readlines():
	print line
fp.close()
