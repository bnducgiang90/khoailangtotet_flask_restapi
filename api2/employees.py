from flask import Flask, request
from flask_restplus import Namespace, Resource, fields
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

ns_employees = Namespace('Employees', description="Employees operations")


@ns_employees.route("/")
class BooksList(Resource):
    @jwt_required
    def get(self):
        current_user = get_jwt_identity()
        task = {'hello': 'Hello world!' + current_user}
        return task

    def post(self):
        pass


@ns_employees.route("/<string:title>")
class Book(Resource):
    def put(self, title):
        pass

    def delete(self, title):
        pass
