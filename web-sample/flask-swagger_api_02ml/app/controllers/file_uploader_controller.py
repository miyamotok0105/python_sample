import six
import connexion
from datetime import datetime
from flask import make_response, abort

from ..models.file_uploader import create as file_create

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def create():
    from flask import Flask, request
    try:
        count = request.args.get('count')
        # print(count)
        # print("=====")
        file = request.files['file'].read()
        output_file_name = request.form['output_file_name']
        file_create(file, output_file_name)
        return make_response(
                "{name} successfully created".format(name="name1"), 201
            )
    except Exception as e:
        print("Exception!!")
        print(e)
        return abort(
            404, " {name} not found".format(name="name1")
        )

def create_multi_file():
    from flask import Flask, request
    try:
        # uploaded_files =request.files.getlist("files[]")
        # print(uploaded_files)
        
        # file_name = request.args.get('file_name')
        # print(file_name)

        # file = request.files['file'].read()
        # file2 = request.files['file2'].read()
        # output_file_name = request.form['output_file_name']
        # output_file2_name = request.form['output_file2_name']
        # file_create(file, output_file_name)
        # file_create(file2, outoutput_file2_nameput_file_name)
        return make_response(
                "{name} successfully created".format(name="name1"), 201
            )
    except Exception as e:
        print(e)
        return abort(
            404, " {name} not found".format(name="name1")
        )

