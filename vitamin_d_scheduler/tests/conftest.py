"""Test configuration"""

import os
import tempfile

import pytest
from dotenv import load_dotenv

from vitamin_d_scheduler import create_app


load_dotenv()

@pytest.fixture()
def flask_client():
    """Initialize Flask application for testing"""
    db_fd, db_path = tempfile.mkstemp()
    app = create_app({
        'TESTING': True,
    })

    with app.test_client() as client:
        with app.app_context():
            # flask_migrate.upgrade()
            # models.db.create_all()
            yield client

    os.close(db_fd)
    os.unlink(db_path)
