from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            schema = schema_name()
            data = request.get_json()
            errors = schema.validate(data)
            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)
        return wrapper
    return decorated_function


def permission_required(permission_role):
    def decorated_function(func):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            if current_user.role == permission_role:
                return func(*args, **kwargs)
            raise Forbidden("You do not have permission to access this resource")
        return wrapper
    return decorated_function
