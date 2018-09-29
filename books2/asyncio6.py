import asyncio

#シーケンス図あり
#https://docs.python.jp/3/library/asyncio-task.html

#cumpute()はprint_sum()にチェーンされます。
#print_sum()コルーチンはcompute()が完了するまで待ちます。


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y

async def print_sum(x, y):
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))

loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
