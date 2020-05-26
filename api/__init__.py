from flask_restplus import Api
from flask import Blueprint
from .books import ns_books
from .moves import ns_movies


# api = Api(
#     title='Api app version 0.1',
#     version='1.0',
#     description='A description',
#     # All API metadatas
# )
_authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

blueprint = Blueprint('api1', __name__)
api = Api(blueprint, authorizations=_authorizations, security='Bearer Auth')

api.add_namespace(ns_books, path="/api1/book")
api.add_namespace(ns_movies, path="/api1/movie")
