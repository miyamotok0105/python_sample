import asyncio
from time import sleep

async def hello_world1():
    for i in range(10):
        print("h1", i)
        if i > 10:
            break

async def hello_world2():
    for i in range(10):
        print("h2", i)
        if i > 10:
            break

#イベントループを定義
loop = asyncio.get_event_loop()

#run_until_completeで実行
#hello_world1が終わったらhello_world2を実行してる！
loop.run_until_complete(hello_world1())
loop.run_until_complete(hello_world2())
loop.close()
