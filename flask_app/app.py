
import os

from flask import Flask
from flask_migrate import Migrate

from flask_app.core.routes import base_routes

from flask_app.app_utils import app_cashing
from flask_app.app_utils.app_db import db
from flask_app.app_utils.commands.db_load_data import cli_db_import_bp

from flask_app.admin import admin
from flask_app.api import api

migrate = Migrate()


def create_app():
    """Application-factory pattern"""

    # app + config
    app = Flask(__name__)
    app.config.from_object("flask_app.config." + os.environ.get("APP_CONFIG", "DevConfig"))

    # db setup
    db.init_app(app)

    # migrations
    from flask_app.core.models import Product, Review # needed for migrations recognition
    migrate.init_app(app, db, directory=app.config['MIGRATION_FOLDER'])

    # blueprints
    app.register_blueprint(base_routes)
    app.register_blueprint(cli_db_import_bp)

    # admin
    admin.init_admin(app)

    # api endpoints
    api.init_api(app)

    # simple cashing
    app_cashing.init_cache(app)

    return app





