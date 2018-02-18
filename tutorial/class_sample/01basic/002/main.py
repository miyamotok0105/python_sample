import callee

#2回目以降はキャッシュ
import callee

#別モジュールから読み込みでもキャッシュを使う
import caller


#importはモジュールサーチパスから該当のモジュールを探し出し、実行するという比較的重い処理なのでキャッシュされる
