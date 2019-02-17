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

class TestUserModel(BaseTestCase):

    def test_read_all(self):
        data = {}
        response = self.client.open(
            '/user',
            method='GET',
            data=data,
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 201)

    def test_insert(self):
        from datetime import datetime
        def get_timestamp():
            return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))
        
        data = {}
        user = {}
        user["lname_new1"] = {
                "lname": "lname",
                "fname": "fname",
                "timestamp": get_timestamp(),
        }
        print(type(user))
        print(json.dumps(user))
        print(type(json.dumps(user)))

        response = self.client.open(
            '/user',
            method='POST',
            data=json.dumps(user),
            content_type='multipart/form-data')
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    import unittest
    unittest.main()

