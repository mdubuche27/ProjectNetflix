from flask import Flask
from flask_mongoengine import MongoEngine
from routes.userRoute import users_route
from  routes.swaggerRoute import swagger_route


app = Flask(__name__)
app.config.from_object('config')
app.register_blueprint(users_route, url_prefix='/users')
app.register_blueprint(swagger_route)
db = MongoEngine()
db.init_app(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)