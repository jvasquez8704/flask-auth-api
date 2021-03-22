import firebase_admin
from firebase_admin import credentials, db, auth, firestore

import json
import requests
import uuid
from config import Configuration 
from constants import Props

FIREBASE_WEB_API_KEY = Configuration.FIREBASE_WEB_API_KEY
FIREBASE_SIGNIN_URL = Configuration.KATCH_FIREBASE_SIGNIN_URL
FIREBASE_SIGNUP_URL = Configuration.KATCH_FIREBASE_SIGNUP_URL
SCHEME = Props.USER_SCHEME

#Setup
#Initialize the app with a service account, granting admin privileges
#cred = credentials.Certificate(Configuration.GOOGLE_APPLICATION_CREDENTIALS)
#cred = credentials.Certificate('katch-nrg-nonprod-firebase-adminsdk-tzkzy-7407e7c3e5.json')
cred = credentials.Certificate('katch-nrg-6b8c7-firebase-adminsdk-6wqgp-8e7a1e6e93.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://katch-nrg-6b8c7-default-rtdb.firebaseio.com/'#'https://katch-nrg-nonprod.firebaseio.com/'#Configuration.KATCH_FIREBASE_DB_URL
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

def create_user(id,user):
    str_uuid = str(uuid.uuid4())
    print('User id {0}'.format(id))
    users_ref = db.reference(SCHEME)
    users_ref.child(id).set(user)
    #users_ref.push(user)
    
def create_fs_user(id,user_record):
    try:
        ref = fs.collection('users').document(id)
        print('Hereee')
        ref.set(user_record)
    except Exception as e:
        print('Exception at update user process {0}'.format(e))
        return {'status_code': 409, "message": "User created, however, check its configuration", "user": user_record}, 409
    

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
    
    
    
        
    
