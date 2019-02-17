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

from ..models import files

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../models/', port=8080)
        # app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yml')
        return app.app

class TestFileUploaderModel(BaseTestCase):

    def test_create(self):
        file_name = "./app/test/dog1.png"
        data = {}
        image_raw = open(file_name, 'rb')
        data['file'] = (image_raw, file_name)
        data['output_file_name'] = "test_dog1.png"
        data['count'] = 2
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 201)

    # def test_create_multi_file(self):
    #     file_name = "./app/test/dog1.png"
    #     data = {}
    #     image_raw = open(file_name, 'rb')
    #     file = (image_raw, file_name)
    #     files = files()
    #     files.add_file("test_dog1.png", file)
    #     files.add_file("test_dog2.png", file)
    #     data['files'] = files.file_array
        
    #     # data['output_file_name'] = ""
    #     # data['output_file2_name'] = ""
    #     response = self.client.open(
    #         '/file_uploader_2file',
    #         method='POST',
    #         data=data,
    #         content_type='multipart/form-data')
    #     self.assertEqual(response.status_code, 201)

    def test_create_no_file(self):
        data = {}
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

    def test_create_ather_type_param(self):
        data = {}
        data['file'] = "string!!!"
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

    def test_create_ather_type_param2(self):
        data = {}
        data['file'] = 11111
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

    def test_create_other_param(self):
        data = {}
        data['file1'] = 11111
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)

    def test_create_other_param2(self):
        data = {}
        data['file'] = 11111
        data['file2'] = 11111
        response = self.client.open(
            '/file_uploader',
            method='POST',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 400)



if __name__ == '__main__':
    import unittest
    unittest.main()

