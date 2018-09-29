import asyncio

#asyncioの主役はイベントループ
#イベントループは処理を順番に処理します。

#非同期メソッド
async def hello_world():
    print("Hello World!")

#イベントループを定義
loop = asyncio.get_event_loop()

#run_until_completeで実行
#ここではhello_worldのみ実行
loop.run_until_complete(hello_world())
loop.close()
