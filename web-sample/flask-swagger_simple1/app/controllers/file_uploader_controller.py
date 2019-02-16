import six
import connexion
from datetime import datetime
from flask import make_response, abort

from ..models.file_uploader import create as file_create

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def create(file):
    try:
        file_create(file)
        return make_response(
                "{name} successfully created".format(name="name1"), 201
            )
    except Exception as e:
        print(e)
        return abort(
            404, " {name} not found".format(name="name1")
        )
