from flask import Blueprint, render_template

app = Blueprint('admin', __name__)

@app.route('/admin/<user_url_slug>')
def timeline(user_url_slug):
    return render_template('admin/timeline.html')

@app.route('/admin/<user_url_slug>/photos')
def photos(user_url_slug):
    return render_template('admin/photos.html')

@app.route('/admin/<user_url_slug>/about')
def about(user_url_slug):
    return render_template('admin/about.html')

