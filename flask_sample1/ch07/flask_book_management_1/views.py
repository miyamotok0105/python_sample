"""
FlaskアプリケーションのRouteとView
"""

from datetime import datetime
from flask import render_template
from flask_book_management_1 import app

# @app.route('/')
# @app.route('/home')
# def home():
#     """インデックスページの表示"""
#     return render_template(
#         'index.html',
#         title='Home Page',
#         year=datetime.now().year,
#     )
