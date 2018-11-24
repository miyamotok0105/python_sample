from flask import Blueprint, render_template
from flask import Flask, render_template, request, redirect, url_for
import flask_login
from models import users, User

app = Blueprint('auth', __name__)


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

