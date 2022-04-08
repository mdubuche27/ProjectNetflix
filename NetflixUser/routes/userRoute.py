from flask import Blueprint
from controllers.userController import get_users,get_user, create_user, update_user, delete_user, get_user_authorized
#from flask_restplus import Api, Resource


users_route = Blueprint('users_route', __name__)
users_route.route('/', methods=['GET'])(get_users)
users_route.route('/', methods=['POST'])(create_user)
users_route.route('/<id>', methods=['GET'])(get_user)
users_route.route('/<id>/authorized', methods=['GET'])(get_user_authorized)
users_route.route('/<id>', methods=['PUT'])(update_user)
users_route.route('/<id>', methods=['DELETE'])(delete_user)
#api = Api(films_route)