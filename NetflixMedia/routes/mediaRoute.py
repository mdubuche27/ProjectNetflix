from flask import Blueprint
from controllers.mediaController import get_medias,get_media, create_media, update_media, delete_media
#from flask_restplus import Api, Resource


medias_route = Blueprint('medias_route', __name__)
medias_route.route('/', methods=['GET'])(get_medias)
medias_route.route('/', methods=['POST'])(create_media)
medias_route.route('/<id>', methods=['GET'])(get_media)
medias_route.route('/<id>', methods=['PUT'])(update_media)
medias_route.route('/<id>', methods=['DELETE'])(delete_media)
#api = Api(medias_route)