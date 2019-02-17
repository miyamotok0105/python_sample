import six
import connexion
from datetime import datetime
from flask import make_response, abort

from ..models.user import read_all as user_read_all
from ..models.user import insert as user_insert

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    try:
        user = user_read_all()
        return make_response(
                "{name} successfully created".format(name=user), 201
            )
    except Exception as e:
        print(e)
        return abort(
            404, " {name} not found".format(name="name1")
        )

def insert():
    try:
        user_insert()
        return make_response(
                "{name} successfully created".format(name=user), 201
            )
    except Exception as e:
        print(e)
        return abort(
            404, " {name} not found".format(name="name1")
        )
