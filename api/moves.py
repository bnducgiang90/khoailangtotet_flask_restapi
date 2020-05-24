from flask import Flask, request
from flask_restplus import  Namespace, Resource, fields

ns_movies = Namespace('movies', description="Movies operations")


@ns_movies.route("/")
class MoviesList(Resource):
    def get(self):
        pass

    def post(self):
        pass


@ns_movies.route("/<string:title>")
class Movie(Resource):
    def put(self, title):
        pass

    def delete(self, title):
        pass
