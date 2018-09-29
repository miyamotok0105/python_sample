import asyncio
from time import sleep

#asyncio.gatherで処理を混ぜる。

async def hello_world1():
    for i in range(10):
        print("h1", i)
        await asyncio.sleep(1)
        if i > 10:
            yield

async def hello_world2():
    for i in range(10):
        await asyncio.sleep(1)
        print("h2", i)
        if i > 10:
            yield

async def start1():
    async for s in hello_world1():
        print(s)

async def start2():
    async for s in hello_world2():
        print(s)


loop = asyncio.get_event_loop()

result = loop.run_until_complete(asyncio.gather(
    start1(),
    start2()
))

loop.close()
