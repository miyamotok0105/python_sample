import rx
from rx import Observable, Observer

Observable.from_("abcabc").to_set().subscribe(print)

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
    return x["x1"] == 1
def normalize(item):
    return {
        'x1': item["x1"],
        'x2': 20
    }
Observable.from_(l).map(normalize).filter(filter_x1).subscribe(print)
results = []



# Observable.from_(l).filter(filter_x1).to_dict().subscribe(print)

# Observable.from_("abcabc").to_set().subscribe(print)

# print(results)



# Observable.from_(frames).map(lambda s: len(s)).filter(lambda i: i == 3).subscribe(print)
# Observable.from_(frames).filter(lambda i: i == 3).subscribe(print)


