from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template(
        'index.html',
        title='Home Page',
        contents='インデックスです'
    )

@app.route("/sub")
def sub():
    return render_template(
        'sub.html',
        title='Sub Page',
        contents='サブページです'
    )

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, debug=True)