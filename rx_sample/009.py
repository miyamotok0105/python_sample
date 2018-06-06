
import rx
import signal
from rx.subjects import Subject
from rx import Observable, Observer

def myprint(*args):
  print(*args)
  return None

# drive = Observable.from_list(list(range(33))).publish()
# reg = Subject().buffer_with_count(8).do_action(myprint)
# drive.subscribe(reg)
# drive.connect()

#publish:普通のObservableを接続可能なObservableに変換する
drive = Observable.from_list(list(range(33))).publish()

s = Subject()
#buffer_with_count
#観測可能なシーケンスの各要素を要素数情報に基づいて生成された0個以上のバッファに投影する
#→ 8個ずつ次のストリームに渡す
s.buffer_with_count(8).do_action(myprint).subscribe()

drive.subscribe(s)
#connectでストリーム同士を繋ぐ？
#これがないと結果が表示されない
drive.connect()
