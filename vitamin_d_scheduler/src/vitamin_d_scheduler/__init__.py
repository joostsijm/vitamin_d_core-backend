"""Flask application"""

from os import environ, path, makedirs

from flask import Flask
from flask_cors import CORS


def create_app(test_config=None):
    """Create and configure the app"""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        DEBUG=environ.get('DEBUG'),
        FLASK_APP=environ.get('FLASK_APP'),
        FLASK_ENV=environ.get('FLASK_ENV'),
        SECRET_KEY=environ.get('FLASK_SECRET_KEY'),
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        makedirs(app.instance_path)
    except OSError:
        pass

    # Apscheduler
    from vitamin_d_scheduler.scheduler import scheduler, start_jobs
    scheduler.init_app(app)
    scheduler.start()
    start_jobs()

    # CORS
    CORS(app, resources={r'/*': {'origins': '*'}})

    return app
