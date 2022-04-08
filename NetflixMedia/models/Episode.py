from flask_mongoengine import MongoEngine
db = MongoEngine()


class Episode(db.Document):
    number = db.IntField()
    url =  db.URLField()
    idSerie = db.StringField()
    status = db.StringField()

