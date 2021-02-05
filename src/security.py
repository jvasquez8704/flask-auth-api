from functools import wraps
from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_claims
)
from firebase import get_user
from privilege import privileges
from app_septup import Application
jwt = Application.jwt

# this method verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `admin` in the access token
def viewer_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['rol'] != 'Viewer':
            return {'status_code': 403, 'custom_code': 'UNAUTHORIZED','message': 'You are not authorized to access this resource'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    # Find user rol and privileges here
    user = get_user(identity['user'])
    if identity['user'] != '':
        return {'rol': user['role']}
    else:
        return {'rol': 'none'}
