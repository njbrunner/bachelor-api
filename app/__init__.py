"""Creates the application"""
import os
from flask import Flask
from flask_pymongo import PyMongo
from flask_mongoengine import MongoEngine
from flask_cors import CORS


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True

    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = "mongodb://localhost:27017/bachelor?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


class ProductionConfig(BaseConfig):
    # RetryableWrites are unsupported for mLab MongoDB
    MONGO_URI = os.environ.get('MONGODB_URI')
    if MONGO_URI:
        MONGO_URI = MONGO_URI + "?retryWrites=false"
    MONGODB_SETTINGS = {
        'host': MONGO_URI
    }


def create_app():

    # CREATE app
    app = Flask(__name__)

    if os.environ.get('MONGODB_URI'):
        app.config.from_object(ProductionConfig)
    else:
        app.config.from_object(DevelopmentConfig)

    initialize_extensions(app)

    register_blueprints(app)

    return app

def initialize_extensions(app):# CORS
    # Create token manager
    CORS(app)
    mongo = PyMongo(app)
    db = MongoEngine(app)

def register_blueprints(app):
    from app.routes import hello
    from app.routes import contestant_routes
    app.register_blueprint(hello.HELLO_BP)
    app.register_blueprint(contestant_routes.CONTESTANT_BP)

