
# ブログ写経

途中で詰んだ。一応メモ。    

```
https://qiita.com/ryo_mt09sp/items/1b36c414af3001d548e7
https://qiita.com/ryo_mt09sp/items/574bed236f3128cf97cd
```

結論vueとdjango繋ぐ公式見た方がいい。    

```
https://github.com/djstein/vue-django-webpack/tree/master/app
```



djangoインストール

```
pip install django==2.2.2
pip install django-rest-framework
```

プロジェクト作成

```
django-admin startproject sample
cd sample
```

マイグレート

```
python manage.py makemigrations
python manage.py migrate

```

起動    

```
python manage.py runserver
```


```py:sample/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]
```


```py:sample/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
]

```


http://127.0.0.1:8000/api/

に接続。    


# spotアプリ追加


```
django-admin startapp myapp
or
django-admin startapp spot
```


```py:sample/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'spot',
]
```



```py:spot/models.py
blog参照
```


```
touch spot/serializers.py
touch spot/renderers.py
```

シリアライザーとレンダラーもblog参照。
json化する処理をレンダラーでまとめてる。



view.pyを変更。rest_frameworkとdjangoの書き方を知っとく必要あり。    


```
touch spot/urls.py
```

spotアプリ側のview.pyとurlを繋げる。    



```py:sample/urls.py
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework import routers
from spot import urls

router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/', include(router.urls)),
    url('api/', include(urls, namespace='spot')),
]

```




```
python manage.py shell

from spot.models import Spot

Spot.objects.create(name="秋葉原UDX", category="オフィス", genre="" , address_prefecture="東京都", address_city="千代田区", address_street="外神田4丁目14-1", latitude="35.700689", longitude="139.772498")

Spot.objects.create(name="東京タワー", category="観光地", genre="" , address_prefecture="東京都", address_city="港区", address_street="芝公園4丁目2-8", latitude="35.658816", longitude="139.745476")

Spot.objects.create(name="東京スカイツリー", category="観光地", genre="" , address_prefecture="東京都", address_city="墨田区", address_street="押上1丁目1-2", latitude="35.710385", longitude="139.810743")

quit()

```


http://localhost:8000/api/spots/2


```
{"spots": {"name": "\u6771\u4eac\u30bf\u30ef\u30fc", "category": "\u89b3\u5149\u5730", "genre": "", "address_prefecture": "\u6771\u4eac\u90fd", "address_city": "\u6e2f\u533a", "address_street": "\u829d\u516c\u57124\u4e01\u76ee2-8", "latitude": "35.658816", "longitude": "139.745476"}}
```

動いた。    



# vue

djangoのプロジェクトディレクトリ直下にvueの環境を作る。    
django_vuejs1/sample/. ←ここに作った。    


```
npm install -g vue-cli
vue init webpack-simple
```

sassで作った。    


```
npm install
npm run dev
```


Vue.jsとDjangoを統合する。


```
npm install webpack-bundle-tracker --save-dev
npm install write-file-webpack-plugin --save-dev
```

webpack.config.jsをいじる。
詳細blog参照。    


```
npm run build
```


djangoのプラグインを入れる。    


```
pip install django-webpack-loader
```


sample/settings.pyを変更    


mkdir sample/templates
touch sample/templates/index.html

npm run build

静的ファイルを一箇所に集める
python manage.py collectstatic


結局distのエラーで詰んだ。
公式見ろって感じ。    

