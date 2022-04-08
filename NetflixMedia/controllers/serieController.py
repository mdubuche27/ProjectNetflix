from flask import request, jsonify
from models.Serie import Serie
from models.Episode import Episode

def get_series():
    if request.get_json():
        return jsonify( Serie.objects(**request.get_json())), 200
    return jsonify(Serie.objects()), 200


def get_serie(id):
    return jsonify(Serie.objects.get_or_404(id=id)), 200


def create_serie():
    body = request.get_json()
    serie = Serie(**body).save()
    if "episodes" in body:
        for idEpisode in body["episodes"]:
            episode = Episode.objects.get_or_404(id=idEpisode)
            if episode.idSerie != str(serie.id):
                episode.idSerie = str(serie.id)
                episode.save()
    return jsonify(serie), 201


def update_serie(id):
    body = request.get_json()
    serie = Serie.objects.get_or_404(id=id)
    serie.update(**body)
    if "episodes" in body:
        for idEpisode in body["episodes"]:
            episode = Episode.objects.get_or_404(id=idEpisode)
            if episode.idSerie != id:
                episode.idSerie = id
                episode.save()

    return jsonify(Serie.objects.get_or_404(id=id)), 201


def delete_serie(id):
    serie = Serie.objects.get_or_404(id=id)
    for idEpisode in serie.episodes:
        episode = Episode.objects.get_or_404(id=idEpisode)
        episode.delete()
    Serie.delete()
    return jsonify(str(serie.id)), 200
