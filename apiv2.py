from flask import Blueprint
from flask_restplus import Api
from api2.employees import ns_employees as ns_emp

blueprint = Blueprint('apiv2', __name__, url_prefix='/api/v2')
api = Api(blueprint,
          title='My Title',
          version='1.0',
          description='A description',
          # All API metadatas
          )

api.add_namespace(ns_emp, path="/api/v2/employee")
