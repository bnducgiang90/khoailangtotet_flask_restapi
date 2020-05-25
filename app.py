from flask import Flask, request
#from api import api
from api import blueprint as api_1
from api2 import blueprint as api_2
from apiv2 import blueprint as api_v2

# app = Flask(__name__)
# api.init_app(app)
app = Flask(__name__)
app.register_blueprint(api_1, url_prefix='/api/1')
app.register_blueprint(api_2, url_prefix='/api/2')
app.register_blueprint(api_v2)

if __name__ == '__main__':
    app.run(port=9000, debug=True)
