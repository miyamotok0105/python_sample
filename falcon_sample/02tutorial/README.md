
# First Steps

```
mkdir look
touch look/__init__.py
touch look/app.py
```

こういうのになった

```
look
├── .venv
└── look
    ├── __init__.py
    └── app.py
```

appに書いてみる


```py:app.py
import falcon

api = application = falcon.API()
```

# Hosting Your App

--reloadオプをつけるとコード変えても読み込んでくれる。

```
gunicorn --reload look.app
```

winユーザーの時か下記。

```
$ pip install waitress
$ waitress-serve --port=8000 look:app
```

# Creating Resources

```
touch images.py
```

```py:image.py
import json

import falcon


class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200
```


```py:app.py
import falcon

from .images import Resource


api = application = falcon.API()

images = Resource()
api.add_route('/images', images)

```

```
http localhost:8000/images
```

バッチリ

```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 09 Apr 2018 17:02:28 GMT
Server: gunicorn/19.7.1
content-length: 74
content-type: application/json; charset=UTF-8

{
    "images": [
        {
            "href": "/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png"
        }
    ]
}
```

jsonと違う形式のmsgpack。文字列以外は早かったりするみたい。


```
pip install msgpack-python
```

書き換える。バイトを使うならresp.dataに入れよう。


```py:image.py
import falcon

import msgpack


class Resource(object):

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        resp.data = msgpack.packb(doc, use_bin_type=True)
        resp.content_type = falcon.MEDIA_MSGPACK
        resp.status = falcon.HTTP_200
```

叩く

```
http localhost:8000/images
```

結果

```
HTTP/1.1 200 OK
Connection: close
Date: Mon, 09 Apr 2018 17:09:32 GMT
Server: gunicorn/19.7.1
content-length: 65
content-type: application/msgpack

��images���href�0/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png
```

# Testing your application


こうなる

```
look
├── .venv
├── look
│   ├── __init__.py
│   ├── app.py
│   └── images.py
└── tests
    ├── __init__.py
    └── test_app.py
```

```
pip install pytest
mkdir tests
touch tests/__init__.py
touch tests/test_app.py
```

simulate_getでテスト


```py:test_app.py
import falcon
from falcon import testing
import msgpack
import pytest

from look.app import api


@pytest.fixture
def client():
    return testing.TestClient(api)


# pytest will inject the object returned by the "client" function
# as an additional parameter.
def test_list_images(client):
    doc = {
        'images': [
            {
                'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
            }
        ]
    }

    response = client.simulate_get('/images')
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')

    assert result_doc == doc
    assert response.status == falcon.HTTP_OK
```

テスト

```
pytest tests
```

ok

```
============================================= test session starts ==============================================
platform darwin -- Python 3.5.5, pytest-3.5.0, py-1.5.3, pluggy-0.6.0
rootdir: /Users/miyamoto/Projects/sample/python_sample/falcon_sample/02tutorial, inifile:
plugins: celery-4.1.0
collected 1 item                                                                                               

tests/test_app.py .                                                                                      [100%]

=========================================== 1 passed in 0.40 seconds ===========================================
```






