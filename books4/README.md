
# ch03構成パターン

## 単一モジュール
001フォルダ。
URLルーティングが数個。ソースコードが100行以下の急速プロジェクト。

```
../001
├── app.py
├── config.py
├── requirements.txt
├── static
└── templates
    ├── base.html
    └── index.html
```

## パッケージ

もう少し複雑な場合はモデルやフォームのためのクラスを定義する。URLルーティング処理や設定ファイルも分離する。


```
002
├── instance
│   └── config.py
├── myapp
│   ├── __init__.py
│   ├── forms.py
│   ├── models.py
│   ├── static
│   ├── templates
│   │   ├── base.html
│   │   └── index.html
│   └── views.py
├── requirements.txt
└── run.py
```

# ch04設定

flaskではconfig.py設定を書く。

本番環境の設定を管理    
- APIキーを秘密にする
- 開発と本番で異なる設定をする

## 単純な例


## 環境変数を利用した設定の切り替え

configフォルダ以下に設定ファイルを分けておいてる。    
development.py：開発に使用する設定ファイル。データベースの設定URIをlocalhostにしたりする。    
production.py：本番用。    
staging.py：開発時のテスト環境など。    


```
002
├── app.py
├── config
│   ├── config.py
│   ├── development.py
│   ├── production.py
│   └── staging.py
├── requirements.txt
├── static
└── templates
    ├── base.html
    └── index.html
```

# ch05ビューとルーティングの高度なパターン

## ビューデコレータ

デコレータは関数を他の関数に変換するPythonの機能。デコレータでは処理を行ったり、引数を変更、処理の中断、元々の関数を実行したりできる。



## キャッシュ

デコレータをつけることで、DBアクセスを全部するのではなくなる。


```
@cache.cached(timeout=60)
```


## URL変換規則

002フォルダ。    

jinja2を使ってHTMLに値を渡す。
組み込みURL変換規則    
string：スラッシュを除く文字列    
int：整数    
float：浮動小数点    
path：スラッシュを含めた文字列    


```
@app.route('/user/<string:user_name>')
def profile(user_name):
    return render_template('index.html', username=user_name)
```

## カスタム変換規則
003フォルダ。

複数カテゴリのurl変換規則を作りたい場合。

flaskのurl_mapのlistに規則を登録する。
http://localhost:5000/r/a,a　のようにしてアクセスすると、a,aの部分がListConverterで区切られる。


```py:app.py
app.url_map.converters['list'] = ListConverter


@app.route('/r/<list:subreddits>')
def subreddit_home(subreddits):
    posts = []
    for subreddit in subreddits:
        posts.extend(subreddit)
    return render_template('index.html', posts=posts)

```


```py:util.py
from werkzeug.routing import BaseConverter

class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):
        return ','.join(super(ListConverter, self).to_url(value)
                        for value in values)

```


# ch06 ブループリント

ブループリントとはビュー、テンプレート、静的ファイルなどをまとめる機能。
例えばtwitterだとindex.htmlやabout.htmlといったページを含むブループリントを持つ想定。


## どう配置する？


### 機能別構造



```
001
├── app.py
├── config
│   ├── config.py
│   ├── development.py
│   ├── production.py
│   └── staging.py
├── models.py
├── requirements.txt
├── static
├── templates
│   ├── account.html
│   ├── admin
│   │   ├── about.html
│   │   ├── photos.html
│   │   └── timeline.html
│   ├── base.html
│   ├── control_panel
│   ├── home
│   └── index.html
├── util.py
└── views
    ├── __init__.py
    │   ├── admin.cpython-35.pyc
    │   ├── auth.cpython-35.pyc
    │   └── home.cpython-35.pyc
    ├── admin.py
    ├── auth.py
    ├── control_panel.py
    └── home.py
```



