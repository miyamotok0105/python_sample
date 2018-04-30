
# Get Started

マイグレーションする。    

```
python manage.py migrate
```

uploadの方もやっとく。    


```
#マイグレーションファイルを作って
python manage.py makemigrations upload
#マイグレート
python manage.py migrate upload
```

動かす。    


```
python manage.py runserver
```


# 初めから作る時メモ

プロジェクト作って中にアプリを作る。    

```
django-admin startproject mysite
python manage.py startapp upload
```

mediaフォルダを作って、settings.pyにパスを設定。

mysiteフォルダのurlsでuploadフォルダ内のurlと紐づける。

upload内のurl設定、modelを定義、viewとtemplateを紐づける。

html側でformでpostできる処理と、getでリストを表示する処理を書く。

view側でformからpostをされた時のmodelの更新と、getされた時のmodelからのデータ受け渡しを書く。

これで動くはず。

ちなみにここのモデルでは比較のために、画像のファイルパスを保持するカラムと、画像情報自体を保持するカラムを両方持たせた。


# 参考

こちらの記事は非常に勉強になりました。

https://qiita.com/felyce/items/57421ea191ab89175e9e







