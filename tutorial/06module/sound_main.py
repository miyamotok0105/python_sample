
input = 1
output = 2

#フルパスでインポート
import sound.effects.echo
sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

#サブモジュールechoをロードする。echoをパッケージ名なしに呼び出せる。
from sound.effects import echo
echo.echofilter(input, output, delay=0.7, atten=4)

#サブモジュールechoをロード。echofilterを直接利用できるようにする。
from sound.effects.echo import echofilter
echofilter(input, output, delay=0.7, atten=4)
