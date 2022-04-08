from flask import request, jsonify
from models.Media import Media

def get_medias():
    if request.get_json():
        return jsonify( Media.objects(**request.get_json())), 200
    return jsonify( Media.objects()), 200


def get_media(id):
    return jsonify(Media.objects.get_or_404(id=id)), 200


def create_media():
    body = request.get_json()
    media = Media(**body).save()
    return jsonify(media), 201


def update_media(id):
    body = request.get_json()
    media = Media.objects.get_or_404(id=id)
    media.update(**body)
    return jsonify(Media.objects.get_or_404(id=id)), 201


def delete_media(id):
    media = Media.objects.get_or_404(id=id)
    media.delete()
    return jsonify(str(media.id)), 200