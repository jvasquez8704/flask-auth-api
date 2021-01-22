from functools import wraps
from flask_jwt_extended import (
    verify_jwt_in_request, get_jwt_claims
)

# this method verifies the JWT is present in
# the request, as well as insuring that this user has a role of
# `admin` in the access token
def admin_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claims = get_jwt_claims()
        if claims['roles'] != 'admin':
            return {'msg': 'Admins only!'}, 403
        else:
            return fn(*args, **kwargs)
    return wrapper


@jwt.user_claims_loader
def add_claims_to_access_token(identity):
    if identity == 'admin':
        return {'roles': 'admin'}
    else:
        return {'roles': 'peasant'}
