from flask import Blueprint, render_template
auth = Blueprint('user', __name__)
# login_manager.login_view = 'login'  # Redirect to login page if not logged in

# from . import routes


@auth.route('/Login', methods=["POST", "GET"])
def home():
    return "<h1>Login</h1"

# @login_manager.user_loader
@auth.route("/testing")
def test():
    return render_template('base.html')


