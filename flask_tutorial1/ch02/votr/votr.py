from flask import Flask
from models import db

votr = Flask(__name__)

# config.py読み込み
votr.config.from_object('config')

# db初期化
db.init_app(votr)
db.create_all(app=votr)

@votr.route('/')
def home():
    return 'hello world'

if __name__ == '__main__':
    votr.run()
