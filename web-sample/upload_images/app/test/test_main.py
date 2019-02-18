import six
from six import BytesIO
import logging
import connexion
import requests
from flask import json
from flask import request, jsonify

from flask import abort, url_for
from flask_testing import TestCase

# from swagger_server.encoder import JSONEncoder

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/', port=8888)
        # app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        return app.app


class TestMain(BaseTestCase):

    # def test_api_v2_upload(self):
    #     data = {}
    #     print(__file__)
    #     IMAGE_PATH = "./app/test/dog1.png"
    #     # f = open(IMAGE_PATH, "rb")
    #     # print(f)
    #     # f.close()
    #     # IMAGE_PATH = "./app/test/dog1.png"
    #     multiple_files = [('images', ('foo.png', open(IMAGE_PATH, "rb"), 'image/png')),
    #                   ('images', ('bar.png', open(IMAGE_PATH, "rb"), 'image/png'))]
    #     # data['files'] = multiple_files
    #     print(multiple_files)
    #     data = {
    #         'file': multiple_files
    #     }
    #     print(data)
    #     response = self.client.open(
    #         '/api_v2/upload',
    #         method='POST',
    #         data=data,
    #         content_type='application/json')
    #     self.assertEqual(response.status_code, 201)

    def test_api_v2_upload(self):
        REST_API_URL = "http://localhost:8080/api_v2/upload"
        IMAGE_PATH = "./app/test/dog1.png"
        headers = {
          'Accept': 'application/json'
        }
        multiple_files = [('images', ('foo.png', open(IMAGE_PATH, "rb"), 'image/png')),
                              ('images', ('bar.png', open(IMAGE_PATH, "rb"), 'image/png'))]
        response = requests.post(REST_API_URL, files=multiple_files, headers=headers)
        print(response.status_code)
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    import unittest
    unittest.main()

