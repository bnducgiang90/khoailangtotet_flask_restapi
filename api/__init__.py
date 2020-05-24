from flask_restplus import Api
from .books import ns_books
from .moves import ns_movies

api = Api(
    title='Api app version 0.1',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(ns_books, path="/api/book")
api.add_namespace(ns_movies, path="/api/movie")
