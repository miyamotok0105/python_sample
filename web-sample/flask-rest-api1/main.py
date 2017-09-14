#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from functools import wraps

from flask import Flask, jsonify, request, url_for, abort, Response

app = Flask(__name__)

# ダミーデータ (DB の代わり)
id_index = 3
users = {1: {'id': 1, 'name': 'foo'},
         2: {'id': 2, 'name': 'bar'}}


def consumes(content_type):
    def _consumes(function):
        @wraps(function)
        def __consumes(*argv, **keywords):
            if request.headers['Content-Type'] != content_type:
                abort(400)
            return function(*argv, **keywords)
        return __consumes
    return _consumes


@app.route('/users', methods=['GET'])
def index():
    # ユーザ一覧からレスポンスを作る
    response = jsonify({'results': users.values()})
    # ステータスコードは OK (200)
    response.status_code = 200
    return response


@app.route('/users', methods=['POST'])
@consumes('application/json')
def create():
    global id_index
    # Content-Body を JSON 形式として辞書に変換する
    content_body_dict = json.loads(request.data)
    # ID を付与する
    content_body_dict['id'] = id_index
    # ID をインクリメントする
    id_index += 1
    # ユーザ一覧に追加する
    users[content_body_dict['id']] = (content_body_dict)
    # レスポンスオブジェクトを作る
    response = jsonify(content_body_dict)
    # ステータスコードは Created (201)
    response.status_code = 201
    # 作成したリソースを Location ヘッダを設定する
    response.headers['Location'] = url_for('read',
                                           user_id=content_body_dict['id'])
    return response


def _get_user(user_id):
    user = users.get(user_id)
    if user is None:
        abort(404)
    return user


@app.route('/users/<user_id>', methods=['GET'])
def read(user_id):
    # リクエストされたパスと ID を持つユーザを探す
    found_user = _get_user(user_id)
    # レスポンスオブジェクトを作る
    response = jsonify(found_user)
    # ステータスコードは Created (201)
    response.status_code = 200
    return response


@app.route('/users/<user_id>', methods=['PUT'])
@consumes('application/json')
def update(user_id):
    # Content-Body を JSON 形式として辞書に変換する
    content_body_dict = json.loads(request.data)
    # リクエストされたパスと ID を持つユーザを探す
    found_user = _get_user(user_id)
    # ユーザ名を書き換える
    found_user['name'] = content_body_dict['name']
    # レスポンスオブジェクトを作る
    response = jsonify(found_user)
    # ステータスコードは Created (201)
    response.status_code = 200
    return response


@app.route('/users/<user_id>', methods=['DELETE'])
def delete(user_id):
    # リクエストされたパスと ID を持つユーザを探す
    _get_user(user_id)
    # ユーザがいれば削除する
    users.pop(user_id)
    # レスポンスオブジェクトを作る
    response = Response()
    # ステータスコードは NoContent (204)
    response.status_code = 204
    return response

if __name__ == '__main__':
    app.run()

