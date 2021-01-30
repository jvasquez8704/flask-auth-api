from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, create_refresh_token,
    get_jwt_identity, jwt_refresh_token_required, verify_jwt_in_request, get_jwt_claims
)
from datetime import timedelta
import os

class App:
    # Api config
    app = Flask(__name__)
    CORS(app)
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.secret_key = os.getenv('APP_SECRET_KEY')

    # Security Setup
    app.config['JWT_SECRET_KEY'] = os.getenv('APP_JWT_SECRET_SEED')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=3600)
    jwt = JWTManager(app)

    # Session config for future implementation (not work right now)
    app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)