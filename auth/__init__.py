from flask_restplus import Api
from flask import Blueprint
from .authencation import ns_auths

blueprint = Blueprint('api_auth', __name__)
api = Api(blueprint)

api.add_namespace(ns_auths, path="/auth")
