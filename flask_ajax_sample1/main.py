import json
from flask import Flask, redirect, url_for, request, session, g, redirect, url_for, \
     abort, render_template, flash, make_response
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template(
        'index.html',
        title='Home Page',
        contents='インデックスです'
    )

@app.route('/api/hello', methods=['GET', 'POST'])
def api_hello():
     data = request.form['keyword']
     resp = make_response(json.dumps(data))
     resp.status_code = 200
     resp.headers['Access-Control-Allow-Origin'] = '*'
     return resp

if __name__ == '__main__':
   app.run(debug = True, port=8080)

