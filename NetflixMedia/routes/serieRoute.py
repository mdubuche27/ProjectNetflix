from flask import Blueprint
from controllers.serieController import get_series,get_serie, create_serie, update_serie, delete_serie
#from flask_restplus import Api, Resource


series_route = Blueprint('series_route', __name__)
#api = Api(series_route)
series_route.route('/', methods=['GET'])(get_series)
series_route.route('/', methods=['POST'])(create_serie)
series_route.route('/<id>', methods=['GET'])(get_serie)
series_route.route('/<id>', methods=['PUT'])(update_serie)
series_route.route('/<id>', methods=['DELETE'])(delete_serie)

