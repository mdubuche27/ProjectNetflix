from flask import Blueprint
from controllers.filmController import get_films,get_film, create_film, update_film, delete_film
#from flask_restplus import Api, Resource

films_route = Blueprint('films_route', __name__)
films_route.route('/', methods=['GET'])(get_films)
films_route.route('/', methods=['POST'])(create_film)
films_route.route('/<id>', methods=['GET'])(get_film)
films_route.route('/<id>', methods=['PUT'])(update_film)
films_route.route('/<id>', methods=['DELETE'])(delete_film)
#api = Api(films_route)