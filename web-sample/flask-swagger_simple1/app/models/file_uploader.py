

def create(file):
    import io
    import numpy as np
    from PIL import Image
    from flask import Flask, request
    from werkzeug.utils import secure_filename
    # f = request.files['file']
    # f.save(secure_filename(f.filename))

    data = request.files['file'].read()
    stream = io.BytesIO(data)
    img = Image.open(stream)
    print(img)
    img.save('./app/static/img/test_dog1.png')


