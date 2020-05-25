from flask_restplus import Api
from flask import Blueprint
from .employees import ns_employees


# api = Api(
#     title='Api app version 0.1',
#     version='1.0',
#     description='A description',
#     # All API metadatas
# )
# authorizations = {
#     'Bearer Auth': {
#         'type': 'apiKey',
#         'in': 'header',
#         'name': 'Authorization'
#     },
# }

blueprint = Blueprint('api2', __name__)
# api = Api(blueprint, security='Bearer Auth', authorizations=authorizations)
api = Api(blueprint)

api.add_namespace(ns_employees, path="/api2/employee")
