from resource import recipe_ns

from config import Config, DevConfig
from flask import Flask
from flask_migrate import Migrate
from flask_restx import Api, Namespace, Resource
from flask_sqlalchemy import SQLAlchemy
from models import db


def create_app(config: Config = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    api = Api(app, doc="/swagger-ui")
    api.add_namespace(recipe_ns)
    with app.app_context():
        db.create_all()
    return app
