from flask import Flask
from flask_mongoengine import MongoEngine
from routes.posterRoute import posters_route
from routes.mediaRoute import medias_route
from routes.posterTimeOfDayRoute import posters_by_hours_route
from routes.swaggerRoute import swagger_route


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(posters_route, url_prefix='/posters')
app.register_blueprint(posters_by_hours_route, url_prefix='/currentposters')
app.register_blueprint(medias_route, url_prefix='/medias')
app.register_blueprint(swagger_route)
db = MongoEngine()
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5002, debug=True)