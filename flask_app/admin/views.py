
from flask_admin.contrib.sqla import ModelView


class ProductModelView(ModelView):
    column_list = ['title', 'reviews', 'asin']


class ReviewModelView(ModelView):
    column_list = ['id', 'title', 'text', 'asin']
    column_searchable_list = ['title', 'text', 'asin']

