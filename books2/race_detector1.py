
import threading

x = 0     # A shared value

#並列プログラミングにはレースコンディション（race condition）問題がある。
#2つの並行するスレッドやプロセスがリソースを共有しているので
#タイミングによって結果が変わる。

#この例ではグローバルな変数xを使用してるので
#別スレッドに変わった時にxが置き換わってる。

# bar -29227 -1
# bar -29228 -1
# bar -29229 ここと
# foo -29185 
# foo -29229 ここが同じ
# foo -29228
# foo -29227
# foo -29226　ここと
# bar -29230
# bar -29226　ここが同じ
# bar -29227
# bar -29228
# bar -29229

COUNT = 10000000
def foo():
    global x
    for i in range(COUNT):
        print("foo", x)
        x += 1

def bar():
    global x
    for i in range(COUNT):
        print("bar", x)
        x -= 1

t1 = threading.Thread(target=foo)
t2 = threading.Thread(target=bar)
t1.start()
t2.start()
t1.join()
t2.join()
print(x)


