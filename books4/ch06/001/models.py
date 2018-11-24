import flask_login

users = {'foo@bar.tld': {'password': 'secret'}}


class User(flask_login.UserMixin):
    pass
