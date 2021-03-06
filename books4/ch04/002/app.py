from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config.from_object("config.config")
#app.config["変数名"]で変数にアクセスできる。

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    print("configは："+app.config["SECRET_KEY"])
    app.debug = True # デバッグモード有効化
    app.run(host='0.0.0.0')