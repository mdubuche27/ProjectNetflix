from flask import Blueprint
from controllers.episodeController import get_episodes,get_episode, create_episode, update_episode, delete_episode

episodes_route = Blueprint('episodes_route', __name__)
episodes_route.route('/', methods=['GET'])(get_episodes)
episodes_route.route('/', methods=['POST'])(create_episode)
episodes_route.route('/<id>', methods=['GET'])(get_episode)
episodes_route.route('/<id>', methods=['PUT'])(update_episode)
episodes_route.route('/<id>', methods=['DELETE'])(delete_episode)
