import six
import connexion
from datetime import datetime
from flask import make_response, abort, jsonify

from ..models.user import read_all as user_read_all
from ..models.user import insert as user_insert

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def read_all():
    try:
        user = user_read_all()
        return make_response(
                jsonify(user), 201
            )
    except Exception as e:
        print(e)
        return abort(
            jsonify(user), 404
        )

def insert():
    try:
        user_insert()
        return make_response(
                jsonify(user), 201
            )
    except Exception as e:
        print(e)
        return abort(
            jsonify(user), 404
        )
