from flask import request, jsonify
from models.Film import Film

def get_films():
    if request.get_json():
        return jsonify( Film.objects(**request.get_json())), 200
    return jsonify( Film.objects()), 200

def get_film(id):
    return jsonify(Film.objects.get_or_404(id=id)), 200


def create_film():
    body = request.get_json()
    film = Film(**body).save()
    return jsonify(film), 201


def update_film(id):
    body = request.get_json()
    film = Film.objects.get_or_404(id=id)
    film.update(**body)
    return jsonify(Film.objects.get_or_404(id=id)), 201


def delete_film(id):
    film = Film.objects.get_or_404(id=id)
    film.delete()
    return jsonify(str(film.id)), 200