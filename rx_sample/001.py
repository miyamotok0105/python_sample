import signal
import rx
from rx.subjects import Subject
from rx import Observable, Observer

Observable.from_("abcabc").to_set().subscribe(print)

print("===================")




print("===================")

xs = Observable.from_([1,2,3])
d = xs.map(lambda x:x*2).subscribe(print)
print("===================")

def append_list(nums):
    results.append(nums)
l = [1,2,3,4,5]
results = []
#Noneが返って来る
Observable.from_(l).map(append_list).subscribe(print) 

print("===================")
def append_list(nums):
    results.append(nums)
    return nums #ここを書かないと処理が途切れてNoneが返って来る

l = [1,2,3,4,5]
results = []
Observable.from_(l).map(append_list).subscribe(print)
print(results)

print("===================")

l = []
d = {"x1":1,"x2":2}
l.append(d)
l.append(d)
d = {"x1":2,"x2":2}
l.append(d)
d = {"x1":3,"x2":2}
l.append(d)
l.append(d)
l.append(d)

def filter_x1(x):
    if x["x1"] == 1:
        return True
    else:
        return False
Observable.from_(l).filter(filter_x1).subscribe(print)
results = []

print("===================")

l = []
d = {"x1":1,"x2":2}
l.append(d)
l.append(d)
d = {"x1":2,"x2":2}
l.append(d)
d = {"x1":3,"x2":2}
l.append(d)
l.append(d)
l.append(d)

#もっと簡潔に
def filter_x1(x):
    return x["x1"] == 1
Observable.from_(l).filter(filter_x1).subscribe(print)
results = []

print("===================")
l1 = []
d = {"x1":1,"x2":2}
l1.append(d)
l1.append(d)
d = {"x1":2,"x2":2}
l2 = []
l2.append(d)
d = {"x1":3,"x2":2}
l2.append(d)
l2.append(d)
l2.append(d)

x1 = Observable.from_(l1)
x2 = Observable.from_(l2)

xc = Observable.combine_latest(x1, x2, lambda a1, a2: [a1, a2])
xc.subscribe(lambda s: print(s))


print("===================")
from rx.subjects import Subject
print("50以下は無効化してしまう壁\n")

stream = Subject()
d = stream.do_action(lambda x: print(x)) \
    .filter(lambda param: param>50) \
    .subscribe(lambda result: print("壁を貫通！{0}のダメージ".format(result)))

# 攻撃！
stream.on_next(0)
stream.on_next(50)
stream.on_next(51)
stream.on_next(49)
stream.on_next(100)
stream.on_next(-50)
stream.dispose()

print("===================")

stream = Subject()
d = stream.do_action(lambda x: print(x)).subscribe()
stream.on_next(0)
stream.on_next(-50)
stream.dispose()
print("===================")
from rx import Observable
from rx.subjects import Subject

# l1 = [1,2,3,4,5]
# l = Subject()
# grouped = l.group_by(lambda x: x % 2).do_action(lambda x: print(x)).subscribe()
# grouped.subscribe()


# Observable.from_(["alpha", "apple", "apple", "beta", "bat", "gamma"]) \
#     .group_by(lambda s: s[0]) \
#     .merge_all() \
#     .subscribe(print)

# Observable.from_(["alpha", "apple", "apple", "beta", "bat", "gamma"]) \
#     .group_by(lambda s: s[0]) \
#     .map(lambda grp: grp.to_list()) \
#     .merge_all() \
#     .subscribe(print)

Observable.from_(["alpha", "apple", "beta", "bat", "gamma"]) \
                              .group_by(lambda s: s[0]) \
                              .map(lambda group: group.to_list()) \
                              .merge_all() \
                              .subscribe(print)


print("===================")

Observable.from_("alphabetagammadeltaepsilon") \
    .group_by(lambda s: s) \
    .map(lambda grp: grp.count().map(lambda ct: "{0}-{1}".format(grp.key,ct))) \
    .merge_all() \
    .subscribe(print)

print("===================")
l1 = [
  { 'x' : 'x1', 'y': 200},
  { 'x' : 'x2', 'y': 90},
  { 'x' : 'x3', 'y': 120},
  { 'x' : 'x4', 'y': 150},
  { 'x' : 'x5', 'y': 70},
  { 'x' : 'x6', 'y': 0}
]

def stock_events(observer):
  for l in l1:
    if(l['y'] > 100):
      observer.on_next(l['x'])
    elif(l['y'] <= 0):
      observer.on_error(l['x'])
  observer.on_completed()

source = Observable.create(stock_events) 

source.subscribe(on_next=lambda value: print("Received {0}".format(value)),
                on_completed=lambda: print("Completed"),
                on_error=lambda e: print(e))


print("===================")

print("===================")
print("===================")
print("===================")


print("end")


