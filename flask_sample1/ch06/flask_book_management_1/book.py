"""
書籍一覧の取得・新規追加・編集・削除を行う
"""

from datetime import datetime
from flask import (
    Blueprint, flash, redirect, render_template, request, url_for, session
)
from werkzeug.exceptions import abort
from flask_book_management_1.auth import login_required
from flask_book_management_1.db import get_db

bp = Blueprint('book', __name__, url_prefix='/book')


@bp.route('/')
@login_required
def index_book():
    """書籍の一覧を取得する"""
    pass


@bp.route('/create_book', methods=('GET', 'POST'))
@login_required
def create_book():
    """
    GET ：書籍登録画面に遷移
    POST：書籍登録処理を実施
    """
    pass


@bp.route('/<int:book_id>/update_book', methods=('GET', 'POST'))
@login_required
def update_book(book_id):
    """
    GET ：書籍更新画面に遷移
    POST：書籍更新処理を実施
    """
    pass


@bp.route('/<int:book_id>/delete_book', methods=('GET', 'POST'))
@login_required
def delete_book(book_id):
    """
    GET ：書籍削除確認画面に遷移
    POST：書籍削除処理を実施
    """
    pass


def get_book_and_check(book_id):
    """書籍の取得と存在チェックのための関数"""
    pass
