

def create(file, file_name):
    import io
    import numpy as np
    from PIL import Image
    from flask import Flask, request
    from werkzeug.utils import secure_filename
    # f = request.files['file']
    # f.save(secure_filename(f.filename))
    # print("====>")
    # print("model")
    # print(request.method)
    # print(request.path)

    # print(request.args.get('file'))
    # print(request.args.get('file2'))
    # print(request.args.get('name1'))

    if file is None:
        print("file error!!")
    # print(request.files['file'])
    # print(request.files['file2'])
    # print(request.form['file'])
    # print(request.form['file2'])
    # print(request.form.get('file'))
    # print(request.form.get('file2'))

    if file is not None:
        data = file
        stream = io.BytesIO(data)
        img = Image.open(stream)
        img.save('./app/static/img/{file_name}'.format(file_name=file_name))
    # name1 = request.form['name1']
    # print(name1)


