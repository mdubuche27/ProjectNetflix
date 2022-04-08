from flask import request, jsonify
from models.Poster import Poster
import datetime

def get_posters():
    if request.get_json():
        return jsonify( Poster.objects(**request.get_json())), 200
    return jsonify(Poster.objects()), 200

def get_poster(id):
    return jsonify(Poster.objects.get_or_404(id=id)), 200

def get_posters_by_hours():
    now = datetime.datetime.now()
    if now.hour in [4,5, 6,7,8,9,10,11]:
        time_of_the_days = "morning"
    elif now.hour in [12, 13, 14]:
        time_of_the_days = "midday"
    elif now.hour in [ 15, 16, 17, 18, 19, 20]:
        time_of_the_days = "afternoon"
    else:
        time_of_the_days = "night"

    return jsonify(Poster.objects(time_of_the_days=time_of_the_days)), 200

def create_poster():
    body = request.get_json()
    poster = Poster(**body).save()

    return jsonify(poster), 201

def update_poster(id):
    body = request.get_json()
    poster = Poster.objects.get_or_404(id=id)
    poster.update(**body)
    return jsonify(Poster.objects.get_or_404(id=id)), 201

def delete_poster(id):
    poster = Poster.objects.get_or_404(id=id)
    poster.delete()
    return jsonify(str(poster.id)), 200
