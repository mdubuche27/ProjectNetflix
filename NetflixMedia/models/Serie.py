from models.Media import Media
from flask_mongoengine import MongoEngine
db = MongoEngine()

class Serie(Media):
    episodes = db.ListField(db.StringField())

