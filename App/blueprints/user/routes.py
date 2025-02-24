from . import user_bp
from flask import render_template

@user_bp.route('/profile')
def profile():
    return render_template('user/profile.html')
