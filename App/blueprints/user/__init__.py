from flask import Blueprint, render_template
user_bp = Blueprint('user', __name__)

from . import routes

@user_bp.route('')
def home():
    return render_template('base.html')


@user_bp.route("/testing")
def test():
    return render_template('base.html')


