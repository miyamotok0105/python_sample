import requests

# REST_API_URL = "http://localhost:8080/api/upload"
# IMAGE_PATH = "./app/test/dog1.png"

# headers = {
#   'Accept': 'application/json'
# }
# multiple_files = [('images', ('foo.png', open(IMAGE_PATH, "rb"), 'image/png')),
#                       ('images', ('bar.png', open(IMAGE_PATH, "rb"), 'image/png'))]
# r = requests.post(REST_API_URL, files=multiple_files, headers=headers)
# print(r.text)


REST_API_URL = "http://localhost:8080/api_v2/upload"
IMAGE_PATH = "./app/test/dog1.png"

headers = {
  'Accept': 'application/json'
}
multiple_files = [('images', ('foo.png', open(IMAGE_PATH, "rb"), 'image/png')),
                      ('images', ('bar.png', open(IMAGE_PATH, "rb"), 'image/png'))]
r = requests.post(REST_API_URL, files=multiple_files, headers=headers)
print(r.text)



