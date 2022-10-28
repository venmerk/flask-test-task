"""
Init db in separate file to prevent circular imports.
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
