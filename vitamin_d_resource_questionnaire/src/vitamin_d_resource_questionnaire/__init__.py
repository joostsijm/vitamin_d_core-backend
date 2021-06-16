"""Flask application"""

from os import environ, path, makedirs

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_mongoengine import MongoEngine

from vitamin_d_resource_questionnaire import application


# Find .env file
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DEBUG=environ.get('DEBUG'),
        FLASK_APP=environ.get('FLASK_APP'),
        FLASK_ENV=environ.get('FLASK_ENV'),
        SECRET_KEY=environ.get('FLASK_SECRET_KEY'),
        MONGODB_SETTINGS={
                'db': environ.get('MONGO_DB'),
                'host': environ.get('MONGO_HOST'),
            },
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    # database
    database = MongoEngine()
    database.init_app(app)

    # CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    # API
    app.register_blueprint(application.blueprint)

    return app
