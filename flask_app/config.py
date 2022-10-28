
"""
Flask class-based configuration.
https://flask.palletsprojects.com/en/2.2.x/config/
https://hackersandslackers.com/configure-flask-applications/
"""

import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class LocalConfig:
    SECRET_KEY = "1q2w3e4r5t6y7u8i9o0p"

    POSTGRES_HOST     = "localhost"
    POSTGRES_PORT     = "5432"
    POSTGRES_DB       = "flask_test_db"
    POSTGRES_USER     = "postgres"
    POSTGRES_PASSWORD = "postgres"


class Config(object):
    """ Base configuration """

    # base
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get("SECRET_KEY", LocalConfig.SECRET_KEY)

    # folders
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    MIGRATION_FOLDER = os.path.join(basedir, 'migrations')

    # db
    POSTGRES_HOST     = os.environ.get("POSTGRES_HOST", LocalConfig.POSTGRES_HOST)
    POSTGRES_PORT     = os.environ.get("POSTGRES_PORT", LocalConfig.POSTGRES_PORT)
    POSTGRES_DB       = os.environ.get("POSTGRES_DB", LocalConfig.POSTGRES_DB)
    POSTGRES_USER     = os.environ.get("POSTGRES_USER", LocalConfig.POSTGRES_USER)
    POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD", LocalConfig.POSTGRES_PASSWORD)

    # db
    SQLALCHEMY_DATABASE_URI = f"postgresql://" \
                              f"{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                              f"@{POSTGRES_HOST}/{POSTGRES_DB}"
    # db engine
    SQLALCHEMY_DB_ENGINE_URL = f"postgresql+psycopg2://" \
                            f"{POSTGRES_USER}:{POSTGRES_PASSWORD}" \
                            f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

    # for less resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # api
    API_VERSION = "1.0"


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_ECHO = True


class TestConfig(Config):
    FLASK_ENV = 'testing'
    DEBUG = False
    TESTING = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False