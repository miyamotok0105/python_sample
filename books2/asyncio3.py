import asyncio
from time import sleep


#python3.6から非同期ジェネレータが導入されました。
async def hello_world1():
    for i in range(10):
        print("h1", i)
        if i > 10:
            yield

async def hello_world2():
    for i in range(10):
        print("h2", i)
        if i > 10:
            yield

async def start1():
    async for s in hello_world1(): #非同期forループ
        print(s)

async def start2():
    async for s in hello_world2(): #非同期forループ
        print(s)

#イベントループを定義
loop = asyncio.get_event_loop()


loop.run_until_complete(start1())
loop.run_until_complete(start2())
loop.close()
