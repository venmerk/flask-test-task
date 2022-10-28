
from flask_app.app_utils.app_db import db


class Product(db.Model):

    __tablename__ = 'products_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    asin = db.Column(db.String(), nullable=False, unique=True)

    reviews = db.relationship("Review", backref='product', lazy=True) # one-to-many

    def __repr__(self):
        return f"{self.title[:30]} ({self.asin})"


class Review(db.Model):

    __tablename__ = 'reviews_table'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    text = db.Column(db.Text())

    asin = db.Column(db.String(), db.ForeignKey("products_table.asin"), nullable=False)

    def __repr__(self):
        return f"{self.title[:30]} ({self.product.asin})"
