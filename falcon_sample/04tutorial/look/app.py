import falcon

from .images import ImageStore, Resource


api = application = falcon.API()

image_store = ImageStore('.')
images = Resource(image_store)
api.add_route('/images', images)