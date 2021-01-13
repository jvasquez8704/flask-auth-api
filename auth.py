from flask import Flask, redirect, url_for, session, request, jsonify
from authlib.integrations.flask_client import OAuth
from datetime import timedelta

#Firebase
# import firebase_admin
# from firebase_admin import credentials, db
from configfirebase import DB

# Api config
app = Flask(__name__)
oauth = OAuth(app)
# Session config
app.secret_key = 'v3ryS3cr3tK3y'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

db = DB()

# oAuth Setup
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='1096576374659-h5b1prav2k5nolkbuaj5o497md0722s2.apps.googleusercontent.com',
    client_secret='Fl6vOpWNjMZon-LOoGV0f0R4',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',  # This is only needed if using openId to fetch user info
    client_kwargs={'scope': 'openid email profile'},
)


@app.route('/')
def start():
    # email = dict(session)['profile']['email']
    email = dict(session).get('email', None)
    return 'Hola, estas logueado como ' + str(email) + ' :) '

@app.route('/login')
def login():
    google = oauth.create_client('google')  # create the google oauth client
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)


@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')  # create the google oauth client
    token = google.authorize_access_token()  # Access token from google (needed to get user info)
    resp = google.get('userinfo')  # userinfo contains stuff u specificed in the scrope
    user_info = resp.json()
    user = oauth.google.userinfo()  # uses openid endpoint to fetch user info
    # Here you use the profile/user data that you got and query your database find/register the user
    # and set ur own data in the session not the profile from google
    # print(user)
    # print(user_info)
    # print(token)
    session['email'] = user_info['email']
    session.permanent = True  # make the session permanant so it keeps existing after broweser gets closed
    return redirect('/')


@app.route('/logout')
def logout():
    for key in list(session.keys()):
        session.pop(key)
    return redirect('/')


@app.route('/signup' , methods=['POST'])
def signup():
    # return db.createUser({'email': request.json['email'], 'password': request.json['password'], 'name': request.json['name']})
    return db.createUser(request.json['email'], request.json['password'], request.json['name'])

@app.route('/users')
def getUsers():
    return db.getModel('Users')

if __name__ == '__main__':
    app.run(debug=True, port=4001)


# https://docs.authlib.org/en/latest/basic/install.html#pip-install-authlib
# https://flask.palletsprojects.com/en/1.1.x/quickstart/    
