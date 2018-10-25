#!/usr/bin/python
#coding:utf-8
# https://a244.hateblo.jp/entry/2018/06/02/224659
#python ocr_api_sample.py
import os
import base64
import json
from requests import Request, Session
 
import requests
import json
import base64  # 画像はbase64でエンコードする必要があるため

API_KEY = os.environ["GOOGLE_VISION_API"]


def text_detection(image_path):
    api_url = 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(API_KEY)
    with open(image_path, "rb") as img:
        image_content = base64.b64encode(img.read())
        req_body = json.dumps({
            'requests': [{
                'image': {
                    'content': image_content.decode('utf-8')  # base64でエンコードしたものjsonにするためdecodeする
                },
                'features': [{
                    'type': 'TEXT_DETECTION'
                }]
            }]
        })
        res = requests.post(api_url, data=req_body)
        return res.json()


if __name__ == "__main__":
    img_path = "eng-768x1024.jpg"
    res_json = text_detection(img_path)
    # print(res_json)
    res_text = res_json["responses"][0]["textAnnotations"][0]["description"]
    print(json.dumps(res_json, indent=4, sort_keys=True, ensure_ascii=False))
    print(res_text)
    with open("data.json", "w") as js:
        #json.dump(res_json, js, indent=4, ensure_ascii=False)
        js.write(res_text)



