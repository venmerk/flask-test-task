
# sys
from flask_admin import Admin

# database entities
from flask_app.core.models import Product, Review
from flask_app.app_utils.app_db import db

# view models
from flask_app.admin.views import ProductModelView, ReviewModelView
from flask_admin import AdminIndexView


def init_admin(app):

    # create admin
    admin = Admin(
        app,
        name=':)',
        template_mode='bootstrap3',
        index_view=AdminIndexView(url='/admin')
    )

    # register views
    admin.add_view(ProductModelView(Product, db.session))
    admin.add_view(ReviewModelView(Review, db.session))




