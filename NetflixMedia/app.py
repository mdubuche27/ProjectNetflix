from flask import Flask, request
from flask_mongoengine import MongoEngine
from routes.serieRoute import series_route
from routes.filmRoute import films_route
from routes.mediaRoute import medias_route
from routes.episodeRoute import episodes_route
from routes.swaggerRoute import swagger_route
import requests

app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(episodes_route, url_prefix='/episodes')
app.register_blueprint(series_route, url_prefix='/series')
app.register_blueprint(films_route, url_prefix='/films')
app.register_blueprint(medias_route, url_prefix='/medias')
app.register_blueprint(swagger_route)
db = MongoEngine()
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.before_request
def before_request_func():
    try:
        r = requests.get(f'http://127.0.0.1:5001/users/{request.headers.get("idUser")}/authorized')
        if r.json():
            pass
        else:
            return "400"
    except Exception:
        return "500"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)