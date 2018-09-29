import asyncio

#非同期らしい処理をする。

# 時間がかかる処理を含む関数
async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print("Task %s: Compute factorial(%s)..." % (name, i))
        await asyncio.sleep(1)
        f *= i

    print("Task %s: factorial(%s) = %s" % (name, number, f))

loop = asyncio.get_event_loop()
# 並列で実行 -> tupleで返す
# asyncio.gatherはコルーチンオブジェクトあるいは
# フューチャからの結果を1つにまとめで返す。
result = loop.run_until_complete(asyncio.gather(
    factorial("A", 2),
    factorial("B", 3),
    factorial("C", 4),
))
