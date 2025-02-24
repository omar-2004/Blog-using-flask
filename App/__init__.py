from flask import Flask
from .extensions import db, migrate
# from .blueprints.user.routes import user_bp # type: ignore

def create_app(config_class='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)  # Initialize Flask-Migrate

    # Register blueprints
    # app.register_blueprint(user_bp, url_prefix='/user')

    return app
