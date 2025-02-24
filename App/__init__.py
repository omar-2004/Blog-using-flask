from flask import Flask
from .extensions import db, migrate
from .blueprints import register_blueprints  # Import the function

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register all blueprints
    register_blueprints(app)

    return app
