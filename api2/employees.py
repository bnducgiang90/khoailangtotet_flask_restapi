from flask import Flask, request
from flask_restplus import Namespace, Resource, fields, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}
ns_employees = Namespace('Employees', description="Employees operations")
# parser = ns_employees.parser()
# parser.add_argument("Authorization", type=str, location="headers", help="Bearer Access Token", required=True)

@ns_employees.route("/")
class BooksList(Resource):
    @jwt_required
    # @ns_employees.doc(parser=parser)
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
