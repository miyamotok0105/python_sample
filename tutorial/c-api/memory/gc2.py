import gc
import sys
import resource

def mem():
    print('Memory usage         : % 2.2f MB' % round(
        resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0/1024.0,1)
    )

print('GC collected objects : %d' % gc.collect())
print(sum(sys.getsizeof(i) for i in gc.get_objects()))
print(gc.garbage)
#print(gc.get_objects())
#mem()

#gc.disable()
a = range(100000)
a = None
#del a

#print(gc.get_objects())

print(gc.garbage)
print(sum(sys.getsizeof(i) for i in gc.get_objects()))
print('GC collected objects : %d' % gc.collect())

print(gc.garbage)
#mem()



