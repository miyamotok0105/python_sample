#!/usr/bin/python
#coding:utf-8
import cv2
import os
import sys
import base64
import json
import requests
api_url = 'https://vision.googleapis.com/v1/images:annotate?key='
api_key = os.environ.get('GOOGLE_API')

with open(sys.argv[1], 'rb') as image:
    base64_image = base64.b64encode(image.read())

    data = {
        'requests': [{
            'image': {
                'content': base64_image,
            },
            'features': [{
                'type': 'FACE_DETECTION',
                'maxResults': 50,
            }]

        }]
    }

    header = {'Content-Type': 'application/json'}
    response = requests.post(api_url + api_key,  json.dumps(data), header)

    if response.status_code == 200:
        #print response.text
        json_response = json.loads(response.text)
        if json_response['responses'][0].has_key('faceAnnotations'):
            for i, face in enumerate(json_response['responses'][0]['faceAnnotations']):
                vertices = [(v.get('x', 0.0), v.get('y', 0.0)) for v in face['fdBoundingPoly']['vertices']]
                #print vertices
                src = cv2.imread(sys.argv[1])
                dst = src[vertices[0][1]:vertices[2][1], vertices[0][0]:vertices[2][0]]
                root, ext = os.path.splitext(sys.argv[1])
                face_image_path = root + '_face' + str(i) + ext
                cv2.imwrite(face_image_path , dst)
        else:
            print("not detec")
    else:
        print('Http response error')
