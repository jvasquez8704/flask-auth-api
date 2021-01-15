import firebase_admin
from firebase_admin import credentials, db, auth
# from firebase_admin.auth import UserRecord
import json
import requests

class DB:
    #Setup
    cred = credentials.Certificate("katchplus-firebase-adminsdk-9c7vk-e497c6bf5b.json")
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://katchplus-dev.firebaseio.com/'
    })

    # FIREBASE_WEB_API_KEY = os.environ.get("FIREBASE_WEB_API_KEY")

    def getUser(self, userId):
        return db.reference('Users').child(userId).get()

    def getUsers(self):
        return db.reference('Users').get()
    
    def sign_in_with_email_and_password(self, email, password, return_secure_token):
        # FIREBASE_WEB_API_KEY = 'AIzaSyBJM-U6ZGMF2iItNbXbDrds043_LM4htd0'
        FIREBASE_WEB_API_KEY = 'AIzaSyDwZRw0HP1zE2-QatpMIsQNhdfAAcE-d5o'
        firebase_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword'
        payload = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        })

        response = requests.post(firebase_url,
                                 params={"key": FIREBASE_WEB_API_KEY},
                                 data=payload
                                 )

        return response.json()


    def sign_up_with_email_and_password(self, email, password):
        # FIREBASE_WEB_API_KEY = 'AIzaSyBJM-U6ZGMF2iItNbXbDrds043_LM4htd0' 
        FIREBASE_WEB_API_KEY = 'AIzaSyDwZRw0HP1zE2-QatpMIsQNhdfAAcE-d5o'
        firebase_url = 'https://identitytoolkit.googleapis.com/v1/accounts:signUp'
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
        print(user)
        print('Successfully fetched user data: {0}'.format(user.uid))
        return 'Sucessfully fetched user data: {0}'.format(user.uid)
    
    def createAuthUser(self, email, password, name):
        user = auth.create_user(
            email=email,
            email_verified=False,
            password=password,
            display_name=name,
            disabled=False)
        print('Sucessfully created new user: {0}'.format(user.uid))
        return 'Sucessfully created new user: {0}'.format(user.uid)

    def updateUser(self, userID, user):
        # print('Updated entry: {0}'.format(db.reference('Users').child(userID).update({"utellyID": utellyID})))
        print('User: {0}'.format(user))
        print('Updated entry: {0}'.format(db.reference('Users').child(userID).update(user)))
        return 'Sucessfully updated new user: {0}'.format(userID)

    def getUtellyId(self, firebaseRefreshToken):
        # utelly_url = 'https://dev-api.utelly.com/phoenix/9/user'
        utelly_url = 'https://35.230.114.213:44301/user'

        payload = json.dumps({
            "credentials": {
                "refresh_token": firebaseRefreshToken
            },
            "link": "firebase",
            "type": "registered",
            "environment": "development"
        })

        response = requests.post(utelly_url,
                                 headers={
                                     "X-AppKey": "9404481bdc5f765cba251e74a71ce15b",
                                     "Content-Type": "application/json"
                                 },
                                 verify=False,
                                 data=payload
                                 )
        print('Utelly response: {0}'.format(response))
        print('Utelly response json: {0}'.format(response.json))
        return response.json()
    
    
    
        
    
