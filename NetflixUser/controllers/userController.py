from flask import request, jsonify
from models.User import User

def get_users():
    if request.get_json():
        return jsonify( User.objects(**request.get_json())), 200
    return jsonify(User.objects()), 200

def get_user(id):
    return jsonify(User.objects.get_or_404(id=id)), 200


def get_user_authorized(id):
    user = User.objects.get_or_404(id=id)
    if user.status == 'on':
        return jsonify(True)
    return jsonify(False)

def create_user():
    body = request.get_json()
    user = User(**body).save()

    return jsonify(user), 201

def update_user(id):
    body = request.get_json()
    user = User.objects.get_or_404(id=id)
    user.update(**body)
    return jsonify(User.objects.get_or_404(id=id)), 201

def delete_user(id):
    user = User.objects.get_or_404(id=id)
    user.delete()
    return jsonify(str(user.id)), 200
