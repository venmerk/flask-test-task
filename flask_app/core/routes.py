
from flask import Blueprint

# register section blueprint
base_routes = Blueprint('base_routes', __name__)


@base_routes.route("/", methods=['GET'])
def index_get():
    return '<a href="/admin">Admin</a>'


@base_routes.route("/", methods=['POST'])
def index_put():
    return '<a href="/admin">Admin</a>'
