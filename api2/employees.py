from flask import Flask, request
from flask_restplus import  Namespace, Resource, fields

ns_employees = Namespace('Employees', description="Employees operations")


@ns_employees.route("/")
class BooksList(Resource):
    def get(self):
        pass

    def post(self):
        pass


@ns_employees.route("/<string:title>")
class Book(Resource):
    def put(self, title):
        pass

    def delete(self, title):
        pass
