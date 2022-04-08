from flask_mongoengine import MongoEngine
db = MongoEngine()

class Media(db.Document):
    title = db.StringField()
    url = db.URLField()
    img = db.URLField()
    categorie = db.StringField()
    description = db.StringField()
    localisation = db.StringField()
    status = db.StringField()
    meta = {'allow_inheritance': True}

