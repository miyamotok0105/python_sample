
動かしてみる

```
#インストール
pip install falcon
pip install gunicorn
pip install waitress
pip install requests
#gunicornかuWSGIかそれっぽいものを使ってみる。
gunicorn things:app
or
waitress-serve --port=8000 things:app
#叩く
curl http://127.0.0.1:8000/things
#httpieで叩く
pip install --upgrade httpie
http localhost:8000/things
```

結果

```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 09 Apr 2018 16:48:47 GMT
Server: gunicorn/19.7.1
content-length: 100
content-type: application/json; charset=UTF-8

Two things awe me most, the starry sky above me and the moral law within me.

    ~ Immanuel Kant

```

モォちょい特徴をつける

```
gunicorn things2:app
#叩く
http localhost:8000/1/things authorization:custom-token
```

結果だよ

```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 09 Apr 2018 16:49:20 GMT
Server: gunicorn/19.7.1
content-length: 66
content-type: application/json; charset=UTF-8
powered-by: Falcon

[
    {
        "color": "green", 
        "id": "465ae727-ce88-48a9-8a97-def64b4dcdaf"
    }
]
```

# 参考

http://falcon.readthedocs.io/en/stable/user/quickstart.html
