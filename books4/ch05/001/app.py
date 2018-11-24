from flask import Flask, render_template, request, redirect, url_for
from flask.ext.login import login_required, current_user
import flask_login

app = Flask(__name__)
app.config.from_object("config.config")

login_manager = flask_login.LoginManager()
login_manager.init_app(app)
users = {'foo@bar.tld': {'password': 'secret'}}

class User(flask_login.UserMixin):
    pass

@app.route('/')
def index():
    return render_template('index.html')

#user_loaderで認証ユーザーのチェック方法
@login_manager.user_loader
def user_loader(email):
    #ユーザー情報にemailがない場合
    if email not in users:
        return
    #ユーザーidはemail
    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    user = User()
    user.id = email
    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == users[email]['password']
    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    email = request.form['email']
    #パスワードあってればリダイレクト
    if request.form['password'] == users[email]['password']:
        user = User()
        user.id = email
        #flask_loginのlogin_userにユーザー情報を入れる。
        flask_login.login_user(user)
        return redirect(url_for('protected'))
    return 'Bad login'

#login_requiredデコレータを入れると認証済みのユーザーのみがアクセスできる。
@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id

@app.route('/dashboard')
@login_required
def account():
    return render_template('account.html')

if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0')

