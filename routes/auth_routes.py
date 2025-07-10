from flask import Blueprint, request, jsonify, render_template
from controllers.auth_controller import register_user 
from models.user import User
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from utils.decorators import role_required
auth_bp = Blueprint('auth', __name__)

from flask import request, jsonify, render_template

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input'}), 400
        response, status = register_user(data)
        return jsonify(response), status

    return render_template('signup.html')


@auth_bp.route("/hello", methods=['GET', 'POST'])
def hello():
    return jsonify("Hello world"), 200


@auth_bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid input: JSON data expected'}), 400

        email = data.get('email')
        password = data.get('password')
        requested_role = data.get('role')

        if not email or not password or not requested_role:
            return jsonify({'error': 'Email, password, and role are required'}), 400

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):  
            actual_role = user.group.role.name if user.group and user.group.role else None

            if actual_role is None or actual_role.lower() != requested_role.lower():
                return jsonify({'error': f'User does not have the {requested_role} role'}), 403

            login_user(user)
            return jsonify({
                'success': 'User logged in successfully',
                'role': actual_role
            }), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401

   
    return render_template('login.html')



@auth_bp.route("/logout",methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return jsonify({"success":"logout successfuly"}), 200


@auth_bp.route("/profile", methods=['GET'])
@login_required
def profile():
    username= current_user.name
    email= current_user.email
    phone_number= current_user.phone_number
    return jsonify({"user details":{
        "name":username,
        "email":email,
        "phone_number":phone_number
    }}), 200

@auth_bp.route('/admin')
@login_required
@role_required('admin')
def admin():
    return "Welcome, Admin!"

@auth_bp.route('/manager')
@login_required
@role_required('manager')
def manager():
    return "Welcome, manager!"