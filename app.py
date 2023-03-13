from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

app = Flask(__name__)
# TODO: homework -> get_config this from env
app.config.from_object('config.DevelopmentConfig')

api = Api(app)
migrate = Migrate(app, db)

with app.app_context():
    db.init_app(app)


[api.add_resource(*route) for route in routes]

if __name__ == '__main__':
    app.run()
