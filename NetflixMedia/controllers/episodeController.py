from flask import request, jsonify
from models.Episode import Episode
from models.Serie import Serie

def get_episodes():
    if request.get_json():
        return jsonify( Episode.objects(**request.get_json())), 200
    return jsonify( Episode.objects()), 200


def get_episode(id):
    return jsonify(Episode.objects.get_or_404(id=id)), 200


def create_episode():
    body = request.get_json()
    episode = Episode(**body).save()
    if "idSerie" in body:
        serie = Serie.objects.get_or_404(id=body["idSerie"])
        if str(episode.id) not in serie.episodes:
            serie.episodes.append(str(episode.id))
            serie.save()

    return jsonify(episode), 201


def update_episode(id):
    body = request.get_json()
    episode = Episode.objects.get_or_404(id=id)
    episode.update(**body)
    if "idSerie" in body:
        serie = Serie.objects.get_or_404(id=body["idSerie"])
        if id not in serie.episodes:
            serie.episodes.append(id)
            serie.save()

    return jsonify(Episode.objects.get_or_404(id=id)), 201


def delete_episode(id):
    episode = Episode.objects.get_or_404(id=id)
    if episode.idSerie:
        serie = Serie.objects.get_or_404(id=episode.idSerie)
        serie.episodes.remove(str(episode.id))
        serie.save()

    episode.delete()
    return jsonify(str(episode.id)), 200