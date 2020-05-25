from flask import Flask
from api import blueprint as api_1
from api2 import blueprint as api_2
from apiv2 import blueprint as api_v2
from auth import blueprint as api_auth
from flask_jwt_extended import (
    JWTManager
)
# app = Flask(__name__)
# api.init_app(app)
# Setup the Flask-JWT-Extended extension

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '\xdb\x1a\xd3O\xd6%\xb9\xbe\xa2\xdf\n\x05v\x82\xb6\x1a\xe1T[\x13\xe6\xc7e\x8a' # 'super-secret'  # Thay đổi chỗ này sau
jwt = JWTManager(app)

app.register_blueprint(api_1, url_prefix='/api/1')
app.register_blueprint(api_2, url_prefix='/api/2')
app.register_blueprint(api_auth, url_prefix='/api/auth')
app.register_blueprint(api_v2)

if __name__ == '__main__':
    app.run(port=9000, debug=True)
