# -*- coding:utf-8 -*-
import json
import falcon
class HelloResource(object):
    
    # postされた時の動作
    def on_post(self, req, res):
        
        # postパラメーターを取得
        body = req.stream.read()
        data = json.loads(body)
        
        # パラメーターの取得
        name = data['name']
        
        msg = {
            "message": "Hello, " + name
        }
        res.body = json.dumps(msg)
app = falcon.API()
app.add_route("/", HelloResource())
if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8000, app)
    httpd.serve_forever()
