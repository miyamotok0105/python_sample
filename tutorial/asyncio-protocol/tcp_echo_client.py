import asyncio




#asyncio.Protocol型はストリーミングプロトコルを実装する基底クラス
#例えば TCP や SSL トランスポートとともに使用する
class EchoClientProtocol(asyncio.Protocol):
    def __init__(self, message, loop):
        self.message = message
        self.loop = loop

    #通信が確立されたら呼ばれる
    def connection_made(self, transport):
        #write
        #トランスポートにバイト列 data を書き込みます。
        #このメソッドはブロックしません; データをバッファーし、非同期に送信する準備を行います。
        #バイナリなのでエンコードしとく
        transport.write(self.message.encode())
        print('Data sent: {!r}'.format(self.message))

    #データを受信したときに呼び出されます。
    def data_received(self, data):
        print('Data received: {!r}'.format(data.decode()))

    #コネクションが切れたら呼ばれる
    def connection_lost(self, exc):
        print('The server closed the connection')
        print('Stop the event loop')
        self.loop.stop()

loop = asyncio.get_event_loop()
message = 'Hello World!'
#create_connectionでコネクションの作成
#1.コネクションを確立し、それを表す トランスポート が作成される。
#2.protocol_factory が引数なしで呼び出され、プロトコル のインスタンスを返す。
#3.プロトコルインスタンスはトランスポートと紐付けられ、それの connection_made() メソッドが呼び出される。
#4.コルーチンは (トランスポート, プロトコル) のペアを返す。
coro = loop.create_connection(lambda: EchoClientProtocol(message, loop),
                              '127.0.0.1', 8888)
#run_until_completeでcoroが終わるまで実行
loop.run_until_complete(coro)
loop.run_forever()
loop.close()

