from models.group import Group
from models.user import User
from utils.helpers import validate_email, validate_password, validate_phone
from extensions import db
from werkzeug.security import generate_password_hash
def register_user(data):
    try:
        required_fields = ["name", "email", "password", "confirm_password", "phone_number", "group_id"]
        if not all(field in data for field in required_fields):
            return {'error': "Missing required fields"}, 400

        if not validate_email(data['email']):
            return {'error': "Invalid email format"}, 400

        if not validate_password(data['password']):
            return {'error': 'Password must be at least 8 characters long and contain at least one letter and one number'}, 400

        if not validate_phone(data["phone_number"]):
            return {'error': "Invalid phone number"}, 400

        if data['password'] != data['confirm_password']:
            return {'error': "Passwords are not equal"}, 400
        

        group = Group.query.get(data['group_id'])
        if not group:
            return {'error': 'Invalid group id'}, 400

        if User.query.filter_by(email=data['email']).first():
            return {'error': 'Email already registered'}, 400

        hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')

        new_user = User(
            name=data['name'],
            email=data['email'],
            password=hashed_password,
            phone_number=data['phone_number'],
            group_id=data['group_id']
        )

        db.session.add(new_user)
        db.session.commit()
        return {
            'message': 'User registered successfully',
            'user': {
                'user_id': new_user.user_id,
                'name': new_user.name,
                'email': new_user.email,
                'group_id': new_user.group_id
            }
        }, 201
    except Exception as e:
        db.session.rollback()
        return {'error': str(e)}, 500
