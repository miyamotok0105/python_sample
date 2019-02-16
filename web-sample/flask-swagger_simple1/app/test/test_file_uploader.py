import io
from PIL import Image
import six
from six import BytesIO
import logging
import requests
import connexion
from flask import json
from flask import request, jsonify

from flask_testing import TestCase


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../models/', port=8080)
        # app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yml')
        return app.app

class TestFileUploaderModel(BaseTestCase):

    def test_create(self):
        content_type = 'image/png'
        file_name = "./app/test/dog1.png"
        data = {}
        image_raw = open(file_name, 'rb')
        data['file'] = (image_raw, file_name)
        
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    import unittest
    unittest.main()

