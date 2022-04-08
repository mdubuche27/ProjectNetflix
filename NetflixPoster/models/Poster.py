from flask_mongoengine import MongoEngine
db = MongoEngine()


class Poster(db.Document):
    img = db.URLField()
    time_of_the_days = db.StringField()



