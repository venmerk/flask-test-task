"""
Basic flask cashing
https://flask-caching.readthedocs.io/en/latest/
"""

from flask_caching import Cache

config = {
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 300
}

cache = Cache(config=config)

def init_cache(app):
    cache.init_app(app)