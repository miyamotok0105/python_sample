
# DJangoでAPI的なものを作るをやってみるメモ

http://djangoproject.jp/doc/ja/1.0/intro/tutorial01.html


##インストール

```
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
```

##djangoプロジェクトを作成。

mysiteは決めた名前。    


```
django-admin startproject mysite
cd mysite
python manage.py runserver
```

これで繋がる。    
http://127.0.0.1:8000    



##言語と時間の設定

```py:setting.py
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

##モデルの作成


```
python manage.py startapp polls
```

下記が出来上がる。    


```
polls/
    __init__.py
    models.py
    views.py
```



簡単のため、投票アプリケーションを mysite ディレクトリの中に作ります。    
pollsモデルを作成する    


```py:polls/models.py
from django.db import models

class Poll(models.Model):
    #Fieldはテーブルのフィールド
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    #ForeignKeyは外部キー制約
    poll = models.ForeignKey(Poll)
    choice = models.CharField(max_length=200)
    votes = models.IntegerField()

```

##モデルを有効にする


モデルの定義が終わったらDBに反映。    
makemigrationsをするとmigrationsにマイグレーションファイルができる。マイグレーションはdjangoではmodels.py → DBへの変換。    


```
python manage.py makemigrations
python manage.py migrate
```


```py:polls/admin.py

from django.contrib import admin
 
# Register your models here.
 
from .models import Task,TaskStatus
 
admin.site.register(Task)
admin.site.register(TaskStatus)
 

```

##管理画面用のユーザーを作る


```
python manage.py createsuperuser
```


http://127.0.0.1:8000/admin    


これ以降はエラーで動かせなかった。
バージョン違うので動かしちゃったのかも。    


