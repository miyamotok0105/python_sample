import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# ベースを継承してる。ベースはid、作成時間、更新時間といった一般的カラムを持つ。
class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
            onupdate=db.func.current_timestamp())

# トピック
class Topics(Base):
    title = db.Column(db.String(500))

    # user friendly way to display the object
    def __repr__(self):
        return self.title

# オプション
class Options(Base):
    name = db.Column(db.String(200))

# 投稿モデル
class Polls(Base):

    topic_id = db.Column(db.Integer, db.ForeignKey('topics.id'))
    option_id = db.Column(db.Integer, db.ForeignKey('options.id'))
    vote_count = db.Column(db.Integer, default=0)
    status = db.Column(db.Boolean) # to mark poll as open or closed

    # リレーションが貼られてる
    topic = db.relationship('Topics', foreign_keys=[topic_id],
            backref=db.backref('options', lazy='dynamic'))
    option = db.relationship('Options',foreign_keys=[option_id])

    def __repr__(self):
            # a user friendly way to view our objects in the terminal
        return self.option.name

if __name__ == '__main__':
    DB_PATH = os.path.join(os.path.dirname(__file__), 'votr.db')
    SECRET_KEY = 'development_key' # keep this key secret during production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(DB_PATH)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    topic = Topics(title='Which side is going to win the EPL this season')
    print(topic.options.all())
    
