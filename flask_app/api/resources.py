

# import time
from flask import jsonify, request
from flask_restful import Resource

from flask_app.api.methods import update_or_create
from flask_app.app_utils.app_cashing import cache

from flask_app.core.models import Product, Review


class ProductsResource(Resource):

    # GET request for this resource
    @cache.cached(timeout=600)
    def get(self, id):

        # to check cashing uncomment
        # time.sleep(10)

        # get pagination params
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per-page", 100, type=int)

        # get product and paginated reviews
        product = Product.query.filter_by(id=id).first_or_404()

        reviews = Review.query.filter_by(asin=product.asin)
        paginated_reviews = reviews.paginate(page=page, per_page=per_page)

        # response
        res = {
            'product': {
                'title': product.title,
                'asin': product.asin
            },

            'reviews': [
                {
                    'title': _.title,
                    'text': _.text,
                } for _ in paginated_reviews],

            "pagination": {
                "count": paginated_reviews.total,
                "page": page,
                "per_page": per_page,
                "pages": paginated_reviews.pages,
            },
        }

        return jsonify(res)


class ReviewsResource(Resource):

    # GET request for this resource
    def get(self, id):

        review = Review.query.filter_by(id=id).first()

        res = {
            'review': review.id,
            'title': review.title,
            'text': review.text,
            'asin': review.product.asin
        }

        return jsonify(res)

    # PUT request for this resource
    def put(self, id):

        # get args for updating
        content_type = request.headers.get('Content-Type')
        if content_type == 'application/json':
            request_args = request.json
        else:
            return jsonify({'Error': 'Specify PUT json -d arguments'})

        # update review
        review = update_or_create(Review, id, request_args)

        res = {
            'updated_review': review.id,
            'title': review.title,
            'text': review.text,
            'asin': review.asin
        }

        return jsonify(res)

