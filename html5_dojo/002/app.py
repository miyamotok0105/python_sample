from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mdl1_index')
def mdl1_index():
    return render_template('mdl1_index.html')

@app.route('/next.html')
def next():
    return render_template('next.html')

@app.route('/tutorialspoint1')
def tutorialspoint1():
    return render_template('tutorialspoint1.html')


if __name__ == '__main__':
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0')
