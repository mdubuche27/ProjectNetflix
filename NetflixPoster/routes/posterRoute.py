from flask import Blueprint
from controllers.posterController import get_posters, get_poster, create_poster, update_poster, delete_poster
#from flask_restplus import Api, Resource


posters_route = Blueprint('posters_route', __name__)
posters_route.route('/', methods=['GET'])(get_posters)
posters_route.route('/', methods=['POST'])(create_poster)
posters_route.route('/<id>', methods=['GET'])(get_poster)
posters_route.route('/<id>', methods=['PUT'])(update_poster)
posters_route.route('/<id>', methods=['DELETE'])(delete_poster)
#api = Api(films_route)