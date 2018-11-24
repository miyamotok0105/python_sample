from flask import Blueprint, render_template

app = Blueprint('home', __name__)

@app.route('/')
# @cache.cached(timeout=60)
def index():
    return render_template('index.html')
