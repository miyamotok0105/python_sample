
# トランスポートとプロトコル (コールバックベースの API)

https://docs.python.jp/3.6/library/asyncio-protocol.html#asyncio-transport    

tcp版とudp版がある    

通信チャンネルができると、トランスポートは常に プロトコル インスタンスとのペアを作成。    

asyncio は現在 TCP、UDP、SSL およびサブプロセスパイプのトランスポートを実装    
トランスポートクラスはスレッドセーフではない。    

udp側がちょっとエラってる。    



