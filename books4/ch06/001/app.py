from flask import Flask, render_template, request, redirect, url_for
from flask import Blueprint
import flask_login
from flask_caching import Cache

from util import ListConverter
from models import users, User
from views import admin, home, auth

app = Flask(__name__)
app.register_blueprint(home.app)
app.register_blueprint(admin.app)
app.register_blueprint(auth.app)
app.config.from_object("config.config")

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# app.url_map.converters['list'] = ListConverter

# cache = Cache(app,config={'CACHE_TYPE': 'simple'})
# cache.init_app(app)



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

#login_requiredデコレータを入れると認証済みのユーザーのみがアクセスできる。
@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


# @app.route('/dashboard')
# @flask_login.login_required
# def account():
#     return render_template('account.html')

# @app.route('/user/<string:user_name>')
# def profile(user_name):
#     return render_template('index.html', username=user_name)

# @app.route('/r/<list:subreddits>')
# def subreddit_home(subreddits):
#     posts = []
#     for subreddit in subreddits:
#         posts.extend(subreddit)
#     return render_template('index.html', posts=posts)


if __name__ == '__main__':
    app.debug = True
    
    app.run(host='0.0.0.0')

