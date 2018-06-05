import signal
import rx
from rx.subjects import Subject
from rx import Observable, Observer

print("===================")
xs = Observable.from_([1,2,3])
ys = Observable.from_([4,5,6])
zs = xs + ys
zs.subscribe(print)

print("===================")

#中身でなくストリーム自体が４倍になってる。
xs = Observable.from_([1,2,3])
ys = xs * 4
ys.subscribe(print)

print("===================")

xs = Observable.from_([1,2,3,4,5,6])
ys = xs[1:-1]
ys.subscribe(print)

print("===================")
print("blocking")
xs = Observable.from_([1,2,3,4,5,6])
ys = xs.to_blocking() #ナニコレ
ys.subscribe(print)

print("===================")

xs = Observable.from_([1,2,3,4,5,6])
ys = xs.to_blocking()
zs = (x*x for x in ys if x > 3)
for x in zs:
    print(x)


print("===================")

xs = Observable.from_([1,2,2,2,3,3,4,5,6])
xs.to_blocking().subscribe(print)
xs.to_iterable().subscribe(print)


print("===================")


def myprint(*args):
  print(*args)
  return None

drive = Observable.from_list(list(range(10))).publish()

s = Subject()
xs = s.buffer_with_count(3).do_action(myprint)
xs.subscribe()

drive.subscribe(s)
drive.connect()


print("===================")

xs = Observable.from_([1,2,3,4,5,6])
ys = xs.to_blocking()
print(type(ys))
zs = (x*x for x in ys if x > 3)
print(zs)
zs = list(zs)
print(zs)
Observable.from_list(zs).subscribe(print)

print("===================")
#値が変わったタイミングを知りたい時
#一個ずらしたリストを先に作成しておくってのもあり。
#[1,2,2,2,3,3,4,5,6]
#[2,2,2,3,3,4,5,6,0]

#この書き方だと別にobservableにする必要全然無いね。
x1 = Observable.from_([1,2,2,2,3,3,4,5,6]).to_blocking()
x2 = Observable.from_([2,2,2,3,3,4,5,6,0]).to_blocking()
l1 = []
for x1,x2 in zip(x1, x2):
    if x1 != x2:
        l1.append(x1)
Observable.from_list(l1).subscribe(print)

print("===================")
#zip使えばいいね。

x1 = Observable.from_([1,2,2,2,3,3,4,5,6]).to_blocking()
x2 = Observable.from_([2,2,2,3,3,4,5,6,0]).to_blocking()

x1.zip(x2, lambda x, y: x if x!=y else None).filter(lambda x: x != None).subscribe(print)

print("===================")
#リストの中にあるかを確認したい

# x1 = Observable.from_([1,2,2,2,3,3,4,5,6]).to_blocking()
# x2 = Observable.from_([2,2,2,3,3,4,5,6,0]).to_blocking()

# x1.to_set().subscribe(print)


l1 = [
  { 'x' : 'x1', 'y': 200},
  { 'x' : 'x2', 'y': 90},
  { 'x' : 'x3', 'y': 200},
  { 'x' : 'x4', 'y': 200},
  { 'x' : 'x5', 'y': 70},
  { 'x' : 'x6', 'y': 0},
  { 'x' : '0', 'y': 0},
]

l2 = [
  { 'x' : '0', 'y': 0},
  { 'x' : 'x1', 'y': 200},
  { 'x' : 'x2', 'y': 90},
  { 'x' : 'x3', 'y': 200},
  { 'x' : 'x4', 'y': 200},
  { 'x' : 'x5', 'y': 70},
  { 'x' : 'x6', 'y': 0}
]

x1 = Observable.from_(l1).to_blocking()
x2 = Observable.from_(l2).to_blocking()

for x1,x2 in zip(x1, x2):
    print(x1["y"])
    print(x2["y"])
    # if x1 != x2:
    #     l1.append(x1)

















