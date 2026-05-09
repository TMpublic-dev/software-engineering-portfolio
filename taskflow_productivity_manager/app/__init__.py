"""
Application factory for TaskFlow Productivity Manager.

This file creates the Flask app, initialises the database and registers
the route blueprint. This structure is more professional than putting the
whole application into one file.
"""

from flask import Flask
from .database import init_db
from .routes import taskflow_bp


def create_app(test_config=None):
    """
    Create and configure the Flask application.

    Args:
        test_config (dict | None): Optional settings used during testing.

    Returns:
        Flask: Configured Flask application.
    """
    app = Flask(__name__)

    # Required for flash messages. In production, store this in an environment variable.
    app.config["SECRET_KEY"] = "development-secret-key"

    if test_config:
        app.config.update(test_config)

    # Automatically creates the database/table if they do not already exist.
    init_db()

    app.register_blueprint(taskflow_bp)

    return app
