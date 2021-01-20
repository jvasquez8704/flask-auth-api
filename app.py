from flask import Flask, redirect, url_for, session, request, jsonify
from flask_restful import Api
from flask_cors import CORS

from user import Users, User
from auth import SignUp, SignIn

from datetime import timedelta
from dotenv import load_dotenv
import time
import json
import os

load_dotenv()

# Api config
app = Flask(__name__)
CORS(app)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = os.getenv('APP_SECRET_KEY')

# Session config
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)
api = Api(app)

@app.before_first_request
def loading_config():
    print('Katch user API started!')

api.add_resource(User, '/users/<string:userId>')
api.add_resource(Users, '/users')
api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4001, debug=True)
     
