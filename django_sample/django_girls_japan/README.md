
# django girlsの内容をdjango2系に変更してやってみた。

https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/

# プロジェクトを作成しよう

## 新規作成


```
django-admin startproject mysite
```

これができる

```
djangogirls
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


```py:mysite/settings.py
LANGUAGE_CODE = 'ja-JP'

TIME_ZONE = 'Asia/Tokyo'

USE_TZ = False
```

## DB作成

すでにsqlite3で設定されてる。DBを変えたい時はここを変える。    

```py:mysite/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

DB作成

```
python manage.py migrate
```

サイトの動作確認。    

```
python manage.py runserver
```


# Djangoモデル

整理するためにアプリ内に別のアプリを作る。    


```
python manage.py startapp blog
```


```
djangogirls
├── blog
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


アプリケーションを作ったら、Djangoにそれを使うように伝える。    


```py:mysite/settings.py
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
)
```

ブログの投稿を保存するモデル。    
下記に書き換える。    
__形式の特殊関数系のことをダンダーと呼ぶらしい。    
クラス名は大文字で始める。
models.Modelを継承してDjangoにdbに保存するものだと認識させる。    
django2系になってon_deleteが必須になってるので、適当に追加しといた。     


```py:blog/models.py
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
```


## データベースにモデル用のテーブルを作る

新しいモデルをデータベースに追加する    


```
#マイグレーションファイルを作って
python manage.py makemigrations blog
#マイグレート
python manage.py migrate blog
```

ポストモデルがデータベースに入った。    


# ログインページを作ろう

モデルをadminページで見れるようにする。    

```py:blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

superuser （サイトの全てを管理するユーザー）を作る    


```
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password:
Password (again):
Superuser created successfully.
```

実行してみる    


```
python manage.py runserver
```



http://127.0.0.1:8000/admin/login/?next=/admin/    
にアクセス。    


postに面白そうな記事を入れてみる。    

タイトル:動物園で「自分は神に守られている」と叫び飼育地帯に侵入した男性、ライオンの爪で絶命―ウクライナ
本文：これはもう単純に、彼を守る神＜＜＜ライオンだったんだろうね。
いったいどんな神様に守られていたんだろう。江頭2：50かな。ムツゴロウさんでもライオン相手じゃきついよね、だって指食われてるし。
Published date：今の時刻

https://matome.naver.jp/odai/2125413327996181928


# デプロイ

ここは一旦飛ばす    
https://djangogirlsjapan.gitbooks.io/workshop_tutorialjp/deploy/    


# Django urlsって何？

URL_conf（URL設定）と呼ばれるものを使います。これは、指定されたURLに合わせてDjangoがどのviewを返したらいいか判断する仕組み。
mysite/urls.py ファイルは簡潔なままにしておきたいので、mysite/urls.pyではblogアプリからURLをインポートするだけ。
django2からadminをincludeしなくて良くなってるみたいなので消しといた。


```py:mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),
]
```

## blog.urls


```
touch blog/urls.py
```


```py:blog/urls.py
#Djangoのメソッドと、blogアプリの全てのビューをインポート
from django.conf.urls import include, url
from . import views
#URLパターンを追加
#^$というパターンのURLをpost_listというビューに割り当てた
#^$は空文字
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]
```


# Django Viewって何？


```py:blog/views.py
from django.shortcuts import render

def post_list(request):
    return render(request, 'blog/post_list.html', {})

```

# HTMLをやってみよう


```
mkdir blog/templates
mkdir blog/templates/blog
touch blog/templates/blog/post_list.html
```



```html:post_list.html
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="">Django Girls Blog</a></h1>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My first post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut fermentum massa justo sit amet risus.</p>
        </div>

        <div>
            <p>published: 14.06.2014, 12:14</p>
            <h2><a href="">My second post</a></h2>
            <p>Aenean eu leo quam. Pellentesque ornare sem lacinia quam venenatis vestibulum. Donec id elit non mi porta gravida at eget metus. Fusce dapibus, tellus ac cursus commodo, tortor mauris condimentum nibh, ut f.</p>
        </div>
    </body>
</html>
```



# DjangoのORMとクエリセット

クエリセットとはモデルが提供しているオブジェクトのリスト。
動かしてみる。


```
python manage.py shell
```

- All objects

```
from blog.models import Post
Post.objects.all()
```

- Create object


```
from django.contrib.auth.models import User
User.objects.all()
me = User.objects.get(username='admin')
Post.objects.create(author=me, title='Sample title', text='Test')
Post.objects.all()
```

記事が一つ増えた。    


- Filter objects

```
#ユーザーで絞る
Post.objects.filter(author=me)
#titleにtitleという文字が入ってるものに絞る
Post.objects.filter(title__contains='title')
#公開済み
from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())
#追加した記事を公開する
post = Post.objects.get(id=2)
post.publish()
#確認
Post.objects.filter(published_date__lte=timezone.now())
```

- Ordering objects


```
Post.objects.order_by('created_date')
#新しく追加した順に並べ替える
Post.objects.order_by('-created_date')
```

# Djangoクエリセット

Djangoのデータベース接続方法と、データストアについて。    
ビュー が モデルとテンプレートの橋渡しをする。
{'posts': posts} の前方のコロンで囲まれたpostsは名前。
後ろのposts は値、クエリセット。


```py:blog/views.py
from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
```


# テンプレートに表示してみよう


```html:post_list.html
<html>
    <head>
        <title>Django Girls blog</title>
    </head>
    <body>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        {% for post in posts %}
            <div>
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    </body>
</html>
```


# cssでかわいくしよう

stylesheetを追加


```html:post_list.html
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
    </head>
    <body>
        <div>
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        {% for post in posts %}
            <div>
                <p>published: {{ post.published_date }}</p>
                <h1><a href="">{{ post.title }}</a></h1>
                <p>{{ post.text|linebreaks }}</p>
            </div>
        {% endfor %}
    </body>
</html>
```


```
mkdir static
mkdir static/css
touch static/css/blog.css
```


```py:mysite/settings.py
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```


```:static/css/blog.css
/*リンクの色を変えてみる*/
h1 a {
    color: #FCA205;
}

/*見にくいので左にスペースを*/
body {
    padding-left: 15px;
}

/*linkで読み込み、新しいフォントを変えてみる*/
h1 a {
    color: #FCA205;
    font-family: 'Lobster';
}


.page-header {
    background-color: #ff9400;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
}

.page-header h1, .page-header h1 a, .page-header h1 a:visited, .page-header h1 a:active {
    color: #ffffff;
    font-size: 36pt;
    text-decoration: none;
}

.content {
    margin-left: 40px;
}

h1, h2, h3, h4 {
    font-family: 'Lobster', cursive;
}

.date {
    color: #828282;
}

.save {
    float: right;
}

.post-form textarea, .post-form input {
    width: 100%;
}

.top-menu, .top-menu:hover, .top-menu:visited {
    color: #ffffff;
    float: right;
    font-size: 26pt;
    margin-right: 20px;
}

.post {
    margin-bottom: 70px;
}

.post h1 a, .post h1 a:visited {
    color: #000000;
}

```


```html:post_list.html
{% load staticfiles %}
<html>
    <head>
        <title>Django Girls blog</title>
        <!--ブートストラップ-->
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <!--独自cssをあててみる-->
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
        <!--新しいフォント-->
        <link href="http://fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext" rel="stylesheet" type="text/css">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>

        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                    {% for post in posts %}
                        <div class="post">
                            <div class="date">
                                {{ post.published_date }}
                            </div>
                            <h1><a href="">{{ post.title }}</a></h1>
                            <p>{{ post.text|linebreaks }}</p>
                        </div>
                    {% endfor %}
                </div>
            </div>
        </div>
    </body>
</html>
```


# テンプレートを拡張しよう


```
touch blog/templates/blog/base.html
```

base側に下記を。    
{% block content %}    
{% endblock %}    
呼び出す側に    
{% block content %} と {% endblock content %}    
を書く必要がある。    


```:blog/templates/blog/base.html
{% load staticfiles %}
<html>
    <head>
        <title>Django Girls blog</title>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
        <link href='//fonts.googleapis.com/css?family=Lobster&subset=latin,latin-ext' rel='stylesheet' type='text/css'>
        <link rel="stylesheet" href="{% static 'css/blog.css' %}">
    </head>
    <body>
        <div class="page-header">
            <h1><a href="/">Django Girls Blog</a></h1>
        </div>
        <div class="content container">
            <div class="row">
                <div class="col-md-8">
                {% block content %}
                {% endblock %}
                </div>
            </div>
        </div>
    </body>
</html>
```


```:blog/templates/blog/post_list.html
{% extends 'blog/base.html' %}

{% block content %}
    {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaks }}</p>
        </div>
    {% endfor %}
{% endblock content %}

```


# アプリケーションを拡張しよう

## Create a link in the template


{% %}という表記はDjangoのテンプレートタグを使っているということを意味。
{% url 'post_detail' pk=post.pk %}はurlに変換される。    

<h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>の場合は
post_detailビューへのパス。    


ルーティングする。
URL: http://127.0.0.1:8000/post/1/にアクセスしたい。    


```:blog/urls.py
from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
```

^で始まるのは文字開始の意味。post/ はURLにpostと/を含んでいる。(?P<pk>[0-9]+) はdef post_detail(request, pk):のviewの引数と繋がってる。
pathでも書き換えれるし、re_pathなども使える。    


```:blog/urls.py
from django.conf.urls import include, url
from . import views
urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
]
```

## post_detail view


```
touch blog/templates/blog/post_detail.html
```


```:blog/templates/blog/post_detail.html
{% extends 'blog/base.html' %}

{% block content %}
    <div class="post">
        {% if post.published_date %}
            <div class="date">
                {{ post.published_date }}
            </div>
        {% endif %}
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaks }}</p>
    </div>
{% endblock %}

```



# フォームを作ろう

フォームを追加


```
touch blog/forms.py
```


```:blog/forms.py
from django import forms

from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
```

ルーティングを追加


```:blog/urls.py
# coding: utf-8
#Djangoのメソッドと、blogアプリの全てのビューをインポート
from django.conf.urls import include, url
from django.urls import path
from . import views
#URLパターンを追加
#^$というパターンのURLをpost_listというビューに割り当てた
#^$は空文字
urlpatterns = [
    # url(r'^$', views.post_list, name='post_list'),
    path('', views.post_list, name='post_list'),
    # url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    path('post_list_at_order/<int:order>', views.post_list_at_order, name='post_list_at_order'),
]

```

viewを追加

post_newメソッド追加とforms.pyのインポート。


```:blog/views.py
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_list_at_order(request, order):
    #orderの場所から20post表示する
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')[order:20]
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

```

テンプレート追加


```
touch blog/templates/blog/post_edit.html
```

csrf_tokenがformをセキュアにしてる。


```:blog/templates/blog/post_edit.html
{% extends 'blog/base.html' %}

{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}
```



