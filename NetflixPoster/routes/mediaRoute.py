from flask import Blueprint
from controllers.mediaController import get_medias

medias_route = Blueprint('medias_route', __name__)
medias_route.route('/', methods=['GET'])(get_medias)
