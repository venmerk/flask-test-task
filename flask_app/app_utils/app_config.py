"""
Access configuration variables without calling 'app'.
"""

from os import environ
from flask_app import config

config_interface = getattr(config, environ.get("APP_CONFIG", "DevConfig"))
