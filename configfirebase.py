
import firebase_admin
from firebase_admin import credentials, db, auth

class DB:
    #Setup
    cred = credentials.Certificate("katchplus-firebase-adminsdk-9c7vk-e497c6bf5b.json")
    # Initialize the app with a service account, granting admin privileges
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://katchplus-dev.firebaseio.com/'
    })
    

    def getModel(self, model):
        return db.reference(model).get()

    def createUser(self, email, password, name):
        user = auth.create_user(
            email=email,
            email_verified=False,
            password=password,
            display_name=name,
            disabled=False)
        print('Sucessfully created new user: {0}'.format(user.uid))
        # return user
        return 'Sucessfully created new user: {0}'.format(user.uid)

    def getUser(self, uid):
        user = auth.get_user(uid)
        print('Successfully fetched user data: {0}'.format(user.uid))
        return user
    
    
    
        
    
