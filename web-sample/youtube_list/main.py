# -*- coding: utf-8 -*-
#http://www.compjour.org/lessons/flask-single-page/simple-youtube-viewing-flask-app/
#run like this
#http://localhost:5000/videos/dQw4w9WgXcQ
from flask import Flask
from string import Template
import requests

def is_url_ok(url):
    return 200 == requests.head(url).status_code

IFRAME_TEMPLATE = Template("""
    <iframe src="https://www.youtube.com/embed/${youtube_id}?autoplay=0" width="853" height="480" frameborder="0" allowfullscreen></iframe>""")

app = Flask(__name__)
@app.route('/')
def homepage():
    return "Hello world"

@app.route('/videos/<vid>')
def videos(vid):
    youtube_url = 'https://www.youtube.com/watch?v=' + vid
    if True == is_url_ok(youtube_url):
        hed = """<h2><a href="{url}">YouTube video: {id}</a></h2>""".format(url=youtube_url, id=vid)
        iframe = IFRAME_TEMPLATE.substitute(youtube_id=vid)
    else:
        # when the youtube video id is not found
        hed = """<h2>Youtube video {id} <strong>does not exist</strong></h2>""".format(id=vid)
        # note that we substitute a specific YouTube ID for the template
        iframe = IFRAME_TEMPLATE.substitute(youtube_id='dQw4w9WgXcQ')

    return hed + iframe


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
