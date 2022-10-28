

from flask_restful import Api
from flask_app.api.resources import ReviewsResource, ProductsResource


def init_api(app):

    # get current api version
    from flask_app.app_utils.app_config import config_interface
    API_V = config_interface.API_VERSION

    # establish api
    api = Api(
        app,
        prefix=f'/api/v{API_V}',
        default_mediatype='application/json',
    )

    # register endpoints
    api.add_resource(ReviewsResource, '/reviews/<int:id>')
    api.add_resource(ProductsResource, '/products/<int:id>')
