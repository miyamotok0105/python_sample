import asyncio

class EchoServerClientProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        #get_extra_infoはオプションのトランスポート情報を返します。
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    #データを受け取ったら実行される
    def data_received(self, data):
        #バイナリなのでデコード
        message = data.decode()
        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()

loop = asyncio.get_event_loop()
# 待ち受けコネクションの作成
coro = loop.create_server(EchoServerClientProtocol, '127.0.0.1', 8888)
#coroが終わるまで実行される
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()
