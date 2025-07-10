from flask import Blueprint, render_template

from flask_login import login_required, current_user

dash_bp = Blueprint('dashboard', __name__)
@dash_bp.route("/dashboard", methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template ('dashboard.html')


@dash_bp.route("/", methods=['GET'])
def homepage():
    return render_template('index.html')