from controllers.posterController import get_posters_by_hours
from flask import Blueprint

posters_by_hours_route = Blueprint('posters_by_hours_route', __name__)
posters_by_hours_route.route('/', methods=['GET'])(get_posters_by_hours)