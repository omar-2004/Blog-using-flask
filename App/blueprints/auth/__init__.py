from flask import Blueprint, render_template
from flask_login import  UserMixin
from App import login_manager

auth = Blueprint('auth', __name__)

users = {"admin": {"password": "password123"}}

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    if user_id in users:
        return User(user_id)
    return None  # If user not found

@auth.route('/Login', methods=["POST", "GET"])
def home():
    return render_template('auth/login.html')

@auth.route("/testing")
def test():
    return render_template('base.html')


