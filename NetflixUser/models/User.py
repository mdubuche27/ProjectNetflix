from flask_mongoengine import MongoEngine
db = MongoEngine()


class User(db.Document):

    name = db.StringField()
    address = db.StringField()
    country = db.StringField()
    status = db.StringField()
    admin = db.BooleanField()


