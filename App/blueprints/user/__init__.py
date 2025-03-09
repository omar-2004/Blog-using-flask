from flask import Blueprint, render_template
from App import login_manager
user_bp = Blueprint('user', __name__)

from . import routes
@login_manager.user_loader
@user_bp.route('')
def home():
    return render_template('auth/login.html')

# @login_manager.user_loader
# @user_bp.route("/testing")
# def test():
#     return render_template('base.html')


