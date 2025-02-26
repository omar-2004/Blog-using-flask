from flask import Flask
from .extensions import db, migrate, csrf, limiter, Talisman
from .blueprints import register_blueprints  # Import the function
from flask_debugtoolbar import DebugToolbarExtension
from dotenv import load_dotenv
from .utils import configure_logging


def create_app(config_class='config.DevelopmentConfig'):
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    csrf.init_app(app)
    limiter.init_app(app)
    Talisman(app, content_security_policy=None)  # Basic HTTP security headers
    db.init_app(app)
    migrate.init_app(app, db)
    configure_logging(app)
    # Enable the toolbar
    toolbar = DebugToolbarExtension(app)

    # Register all blueprints
    register_blueprints(app)

    return app




