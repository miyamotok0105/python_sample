import falcon

from .images import Resource


api = application = falcon.API()

images = Resource(storage_path='.')
api.add_route('/images', images)
