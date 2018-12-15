

- flask使う
- Flask Blueprints使う
- SQLAlchemy ORM使う
- ReactJS使う
- Celeryバックグラウンドジョブ使う


```
pip install flask
pip install flask_sqlalchemy
```

# ch01 flaskシンプルなやつ


```
mkdir votr
cd votr
touch votr.py
```

# ch02 Flask SQLAlchemy使ってみる


```
mkdir votr
cd votr
touch votr.py
touch models.py
```

![図1](https://danidee10.github.io/images/votr.png "図1")


```
from votr import db, votr
from models import Options, Topics, Polls

topic = Topics(title='Which side is going to win the EPL this season')
arsenal = Options(name='Arsenal')
spurs = Options(name='Spurs')
poll = Polls(topic=topic, option=arsenal)
poll1 = Polls(topic=topic, option=spurs)  
topic.options.all()

poll.vote_count = 3
poll1.vote_count = 2

for option in topic.options.all():
    print(option, option.vote_count)
```

# 参考

https://danidee10.github.io/2016/09/18/flask-by-example-1.html
https://danidee10.github.io/blog/page2/


