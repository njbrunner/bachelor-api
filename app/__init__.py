"""Creates the application"""
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()


class BaseConfig(object):
    DEBUG = False
    TESTING = False

    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    MONGO_URI = os.getenv("MONGO_URI")
    MONGODB_SETTINGS = {"host": MONGO_URI}


class ProductionConfig(BaseConfig):
    MONGO_URI = os.environ.get("MONGODB_URI")
    if MONGO_URI:
        MONGO_URI = MONGO_URI + "?retryWrites=false"
    MONGODB_SETTINGS = {"host": MONGO_URI}


def create_app():

    # CREATE app
    app = Flask(__name__)

    if os.environ.get("MONGODB_URI"):
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    initialize_extensions(app)

    register_blueprints(app)

    return app


def initialize_extensions(app):
    CORS(app)
    mongo = PyMongo(app)
    db = MongoEngine(app)
    jwt = JWTManager(app)


def register_blueprints(app):
    from app.routes import hello
    from app.routes import contestant_routes
    from app.routes import team_routes
    from app.routes import auth

    app.register_blueprint(hello.HELLO_BP)
    app.register_blueprint(contestant_routes.CONTESTANT_BP)
    app.register_blueprint(team_routes.TEAM_BP)
    app.register_blueprint(auth.AUTH_BP)
