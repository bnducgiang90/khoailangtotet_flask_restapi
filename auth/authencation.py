import datetime

from flask import Flask, request
from flask_restplus import Namespace, Resource, fields
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)
from werkzeug.security import safe_str_cmp

ns_auths = Namespace('auths', description="authencations operations")
auth_model = ns_auths.model('auth_model', {
    'username': fields.String(description="Tài khoản đăng nhập", required=True),
    'password': fields.String(description="Mật khẩu đăng nhập", required=True)
})


@ns_auths.route('/login')
class Login(Resource):
    # Payload validation disabled
    @ns_auths.expect(auth_model, validate=True)
    def post(self):
        json_data = request.json
        _username = json_data["username"]
        if json_data["username"] is None or json_data["username"] == "" \
                or json_data["password"] is None or json_data["password"] == "":
            return ns_auths.abort(400, "username or password is required!")

        if json_data["username"] != 'test' or json_data["password"] != 'test':
            return ns_auths.abort(401, "Loi username or password")

        # Identity can be any data that is json serializable
        _access_token = create_access_token(identity=json_data["username"]
                                            , expires_delta=datetime.timedelta(minutes=30))
        _result = {"access_token": _access_token}
        return _result, 200
