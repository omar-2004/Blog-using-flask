from flask import Flask
from .user import user_bp
# from .blog import blog_bp
# from .auth import auth_bp

def register_blueprints(app: Flask):
    """Register all blueprints with the Flask application."""
    app.register_blueprint(user_bp, url_prefix='/user')
    # app.register_blueprint(blog_bp, url_prefix='/blog')
    # app.register_blueprint(auth_bp, url_prefix='/auth')
