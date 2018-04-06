
# DJangoでAPI的なものを作るをやってみるメモ

1系のdjango    
http://djangoproject.jp/doc/ja/1.0/intro/tutorial01.html    
2系のdjango    
https://docs.djangoproject.com/ja/2.0/intro/    

バージョン注意。    

##インストール

```
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
```

このチュートリアルはDjango 2.0 と Python 3.4 以降を対象    

```
python -m django --version
```

##djangoプロジェクトを作成。

mysiteは決めた名前。    


```
django-admin startproject mysite
```

下記が出来上がる。    


```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

```
cd mysite
python manage.py runserver
or
python manage.py runserver 8000
```

これで繋がる。    
http://127.0.0.1:8000    


##言語と時間の設定

```py:setting.py
LANGUAGE_CODE = 'ja'
TIME_ZONE = 'Asia/Tokyo'
```

##投票(polls)アプリケーションをつくる


```
python manage.py startapp polls
```

下記が出来上がる。    


```
polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

簡単のため、投票アプリケーションを mysite ディレクトリの中に作ります。    
pollsモデルを作成する    

```py:polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```


ビューを呼ぶために、 URL を対応付けしてやる必要があります。そのためには URLconf が必要です。    

polls ディレクトリに URLconf を作るには urls.py というファイルを作ります。    


```
touch polls/urls.py
```

```py:polls/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

ルートのURLconfに polls.urls モジュールの記述を反映    

```py:mysite/urls.py
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

```
python manage.py runserver
```

http://localhost:8000/polls/    


##DB設定

```
python manage.py migrate
```

詳細は参照    
https://docs.djangoproject.com/ja/2.0/intro/tutorial02/    

##モデルを作成

poll アプリケーションでは、投票項目 (Question) と選択肢 (Choice) の二つのモデルを作成します。 Poll には質問事項 (question) と公開日 (publication date) の情報があります。 Choice には選択肢のテキストと投票数 (vote) という二つのフィールドがあります。各 Choice は一つの Question に関連づけられています。    

モデルの定義が終わったらDBに反映。    
マイグレーションはdjangoではmodels.py → DBへの変換。    
Fieldはテーブルのフィールド。ForeignKeyは外部キー制約。    

```py:polls/models.py
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

モデルを有効にする    
アプリケーションをプロジェクトに含めるには、構成クラスへの参照を INSTALLED_APPS 設定に追加する必要があります。     

```py:mysite/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```
python manage.py makemigrations polls
```

マイグレーションの中身を返す    

```
python manage.py sqlmigrate polls 0001
```

DB反映。    

```
python manage.py migrate
```

##API で遊んでみる

対話モード    

```
python manage.py shell
```


```
>>> from polls.models import Question, Choice   # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```


ちょっと待ってください。 <Question: Question object (1)> は、このオブジェクトの表現としてまったく役に立ちません。(polls/models.py ファイル内にある) Question モデルを編集してこれを修正しましょう。 __str__() メソッドを Question と Choice の両方に追加します。    

```polls/models.py

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


