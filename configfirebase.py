import firebase_admin
from firebase_admin import credentials, db, auth
from dotenv import load_dotenv
# from firebase_admin.auth import UserRecord
import os
import json
import requests

load_dotenv()

class DB:
    #Setup 
    #Initialize the app with a service account, granting admin privileges
    cred = credentials.Certificate(os.getenv('CREDENTIALS_FIREBASE_SDK_PATH'))
    firebase_admin.initialize_app(cred, {
        'databaseURL': os.getenv('KATCH_FIREBASE_DB_URL')
    })
    # FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")

    def getUser(self, userId):
        return db.reference('Users').child(userId).get()

    def getUsers(self):
        return db.reference('Users').get()
    
    def sign_in_with_email_and_password(self, email, password):
        FIREBASE_WEB_API_KEY = os.getenv('FIREBASE_WEB_API_KEY')
        firebase_url = os.getenv('KATCH_FIREBASE_SIGNIN_URL')
        payload = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": True
        })

        response = requests.post(firebase_url,
                                 params={"key": FIREBASE_WEB_API_KEY},
                                 data=payload
                                 )

        return response.json()

    def sign_up_with_email_and_password(self, email, password):
        FIREBASE_WEB_API_KEY = os.getenv('FIREBASE_WEB_API_KEY')
        firebase_url = os.getenv('KATCH_FIREBASE_SIGNUP_URL')
        payload = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": True
        })

        response = requests.post(firebase_url,
                                 params={"key": FIREBASE_WEB_API_KEY},
                                 data=payload
                                 )

        return response.json()

    def getAuthUser(self, uid):
        user = auth.get_user(uid)
        return 'Sucessfully fetched user data: {0}'.format(user.uid)
    
    def createAuthUser(self, email, password, name):
        user = auth.create_user(
            email=email,
            email_verified=False,
            password=password,
            display_name=name,
            disabled=False)
        return 'Sucessfully created new user: {0}'.format(user.uid)

    def updateUser(self, userID, user):
        db.reference('Users').child(userID).update(user)
        return 'User saved successfully {0}'.format(userID)

    def getUtellyId(self, firebaseRefreshToken):
        utelly_url = os.getenv('KATCH_UTELLY_PROXY_URL')
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
                                 #verify=False,
                                 data=payload
                                 )
        return response.json()
    
    
    
        
    
