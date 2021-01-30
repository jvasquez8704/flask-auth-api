import firebase_admin
from firebase_admin import credentials, db, auth, firestore

import os
import json
import requests

FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")
FIREBASE_SIGNIN_URL = os.getenv('KATCH_FIREBASE_SIGNIN_URL')
FIREBASE_SIGNUP_URL = os.getenv('KATCH_FIREBASE_SIGNUP_URL')
SCHEME = 'Users'

#Setup
#Initialize the app with a service account, granting admin privileges
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./watchpartysite-4adf0-ce31a2eeacda.json"
cred = credentials.Certificate(os.getenv('GOOGLE_APPLICATION_CREDENTIALS'))
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv('KATCH_FIREBASE_DB_URL')
})

fs = firestore.Client()

def get_user(userId):
    return db.reference(SCHEME).child(userId).get()

def get_users():
    return db.reference(SCHEME).get()

def sign_in_with_email_and_password(email, password):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    response = requests.post(FIREBASE_SIGNIN_URL,
                             params={"key": FIREBASE_WEB_API_KEY},
                             data=payload
                             )
    return response.json()

def sign_up_with_email_and_password(email, password):
    payload = json.dumps({
        "email": email,
        "password": password,
        "returnSecureToken": True
    })

    response = requests.post(FIREBASE_SIGNUP_URL,
                             params={"key": FIREBASE_WEB_API_KEY},
                             data=payload
                             )

    return response.json()

def update_user(userID, user):
    return db.reference(SCHEME).child(userID).update(user)

def get_utelly_id(firebaseRefreshToken):
    utelly_url = os.getenv('KATCH_UTELLY_URL')
    X_AppKey = os.getenv('HEADER_X_APP_KEY')

    payload = json.dumps({
        "credentials": {
            "refresh_token": firebaseRefreshToken
        },
        "link": "firebase",
        "type": "registered",
        "environment": os.getenv('CURRENT_ENV')
    })

    response = requests.post(utelly_url,
                             headers={
                                 "X-AppKey": X_AppKey,
                                 "Content-Type": "application/json"
                             },
                             verify=False,
                             data=payload
                             )
    return response.json()
    
    
    
        
    
