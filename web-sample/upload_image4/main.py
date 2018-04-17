from flask import Flask, render_template, request
from werkzeug import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = './img'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
   return render_template('upload.html')

@app.route('/upload2')
def upload():
   return render_template('upload2.html')

@app.route('/upload2_show')
def upload_show():
   return render_template('upload2_show.html')


@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return 'file uploaded successfully'
    return ''

if __name__ == '__main__':
   app.run(debug = True)


