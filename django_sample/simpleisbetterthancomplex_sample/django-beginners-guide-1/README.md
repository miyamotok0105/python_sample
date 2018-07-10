

```
django-admin startproject myproject
cd myproject
python manage.py migrate
python manage.py runserver
```


```
django-admin startapp boards
```

view.pyを書く。urls.pyを書く。    

モデルを書く。    
マイグレートする。    

```
python manage.py makemigrations
python manage.py sqlmigrate boards 0001
python manage.py migrate
```

データ入れる    

```
python manage.py shell
from boards.models import Board
board = Board(name='Django', description='This is a board about Django.')
board.save()
board = Board.objects.create(name='Python', description='General discussion about Python.')
Board.objects.all()
exit()
```

view.pyでデータを表示できるようにする。    

templatesフォルダ作ってhtml作る。    

settings.pyでtemplatesも見るように設定する。    

home2 home3も思い思いに作って見る。    

テストを書く。boards/tests.pyで200番が返ってくること。    

```
python manage.py test
```

もーちょっと細かく出すこともできる    


```
python manage.py test --verbosity=2
```


cssを落とす。    

https://getbootstrap.com/docs/4.0/getting-started/download/#compiled-css-and-js

static、cssフォルダを作ってsettings.pyに設定する。    


ユーザー作る。    


```
python manage.py createsuperuser
admin
admin@example.com
```

admin.pyに追加すると、編集できるようになるよ。    


```
admin.site.register(Board)
```


http://127.0.0.1:8000/admin
    

とりまマイグレーとしとく。    


```
python manage.py makemigrations
python manage.py migrate
```


url.pyで<pk>付きのを作る。view.pyでdef board_topics(request, pk):って感じに書くとurlでクエリパラメータ渡せる。    


http://127.0.0.1:8000/boards/1/


テスト書く。
クエリパラメータ入れて200番返ってくること。
桁が多いパラメータはエラーなること。


```
python manage.py test --verbosity=2
```



formを作る    

http://127.0.0.1:8000/boards/1/new

http://127.0.0.1:8000/boards/2/new
    

formタグに入力系のタグ入れて、nameを指定する。    

```html:
<input type="text" class="form-control" id="id_subject" name="subject">
<textarea class="form-control" id="id_message" name="message" rows="5"></textarea>
```

nameで指定した名前をviews.pyでrequest.POSTで取得する。


```py:views.py
subject = request.POST['subject']
message = request.POST['message']
```






