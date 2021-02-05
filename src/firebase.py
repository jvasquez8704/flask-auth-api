import firebase_admin
from firebase_admin import credentials, db, auth, firestore

import json
import requests
from config import Configuration 
from constants import Props

FIREBASE_WEB_API_KEY = Configuration.FIREBASE_WEB_API_KEY
FIREBASE_SIGNIN_URL = Configuration.KATCH_FIREBASE_SIGNIN_URL
FIREBASE_SIGNUP_URL = Configuration.KATCH_FIREBASE_SIGNUP_URL
SCHEME = Props.USER_SCHEME

#Setup
#Initialize the app with a service account, granting admin privileges
cred = credentials.Certificate(Configuration.GOOGLE_APPLICATION_CREDENTIALS)
firebase_admin.initialize_app(cred, {
    'databaseURL': Configuration.KATCH_FIREBASE_DB_URL
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

def rollback_auth_user(userID):
    return auth.delete_user(userID)

def update_user(userID, user):
    return db.reference(SCHEME).child(userID).update(user)

def get_utelly_id(firebaseRefreshToken):
    utelly_url = Configuration.KATCH_UTELLY_URL
    X_AppKey = Configuration.HEADER_X_APP_KEY

    payload = json.dumps({
        "credentials": {
            "refresh_token": firebaseRefreshToken
        },
        "link": "firebase",
        "type": "registered",
        "environment": Configuration.CURRENT_ENV
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
    
    
    
        
    
