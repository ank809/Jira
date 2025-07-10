from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(*roles):
    """
    Usage: @role_required('admin', 'manager')
    Only allows users whose role matches one of the provided roles.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated:
                abort(401)  

            
            user_role = None
            if current_user.group and current_user.group.role:
                user_role = current_user.group.role.name.lower()

            
            allowed_roles = [role.lower() for role in roles]
            if user_role not in allowed_roles:
                abort(403) 

            return f(*args, **kwargs)
        return decorated_function
    return decorator
