from flask import Blueprint, render_template, redirect, url_for
from flask_login import  login_required

user_bp = Blueprint('user', __name__)



@user_bp.route('')
@login_required 
def home():
    return render_template('base/base.html')

@user_bp.route("/testing")
@login_required 
def test():
    return "testing"

