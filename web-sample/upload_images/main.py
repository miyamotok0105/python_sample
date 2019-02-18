import os
import io
import connexion
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug import secure_filename
from werkzeug import FileStorage

app_connexion = connexion.App(__name__, specification_dir='./app/swagger/')
app_connexion.add_api('swagger.yaml')

app = app_connexion.app
app.config['UPLOAD_FOLDER'] = 'app/uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_files = request.files.getlist("images")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
    return render_template('upload.html', filenames=filenames)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/api/upload', methods=['POST'])
def api_upload():
    uploaded_files = request.files.getlist("images")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            filenames.append(filename)
    return "success"

@app.route('/api_v2/upload', methods=['POST'])
def api_v2_upload():
    uploaded_files = request.files.getlist("images")
    filenames = []
    for file in uploaded_files:
        if file and allowed_file(file.filename):
            stream = io.BytesIO(file.stream.read())
            img = Image.open(stream)
            filename = secure_filename(file.filename)
            img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return "success"


if __name__ == '__main__':
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )
