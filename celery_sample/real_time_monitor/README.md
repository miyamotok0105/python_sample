

# 概要

インストール

```
pip install -r requirements.txt
```

用意する。    

```
redis-server
celery worker --concurrency=10
celery flower
```

タスク実行。    


```
python main.py
```


モニタリング    

http://localhost:5555


# 参照

https://qiita.com/xecus/items/9722b287cc6aee4083ae
