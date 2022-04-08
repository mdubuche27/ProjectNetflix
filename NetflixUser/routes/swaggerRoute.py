from flask import Flask, Blueprint
from flask_restx import Api

app = Flask(__name__)
swagger_route = Blueprint('api', __name__, url_prefix='/api')
api = Api(swagger_route, doc='/doc/')


