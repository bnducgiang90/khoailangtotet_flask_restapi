from flask import Flask, request
from flask_restplus import Namespace, Resource, fields, reqparse
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

ns_employees = Namespace('Employees', description="Employees operations")

# authorizations = {
#     'Bearer Auth': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     },
# }
# parser = ns_employees.parser()
# parser.add_argument("Authorization", type=str, location="headers", help="Bearer Access Token", required=True)


@ns_employees.route("/")
#@ns_employees.doc(params={'Authorization': {'in': 'header', 'description': 'An authorization token'}})
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
