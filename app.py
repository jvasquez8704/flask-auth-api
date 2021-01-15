from flask import Flask, redirect, url_for, session, request, jsonify
from datetime import timedelta
import time
import json

#Firebase
from configfirebase import DB

# Api config
app = Flask(__name__)

# Session config
app.secret_key = 'v3ryS3cr3tK3y'
app.config['SESSION_COOKIE_NAME'] = 'google-login-session'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=5)

db = DB()

@app.route('/')
def start():
  return jsonify({"message":"api running..."})

@app.route('/signup' , methods=['POST'])
def signup():
    #step1
    # userRegisted = json.loads(json.dumps(db.sign_in_with_email_and_password(request.json['email'], request.json['password'], True)))
    userRegisted = json.loads(json.dumps(db.sign_up_with_email_and_password(request.json['email'], request.json['password'])))
    print('#step1 userRegisted : {0}'.format(userRegisted))
    refreshToken = userRegisted['refreshToken']

    #step2
    utellyRecord = json.loads(json.dumps(db.getUtellyId(refreshToken)))
    print('#step2 utellyRecord : {0}'.format(utellyRecord))
    utellyId = utellyRecord['user']['id']

    #step3
    print('#step3 User : {0}'.format(utellyRecord['user']))
    print('#step3 utellyId : {0}'.format(utellyId))
    print('#step3 localId : {0}'.format(userRegisted['localId']))

    firebaseUser = {
        "katchID":"",
        "utellyID":utellyId,
        "UDID":"",
        "IMEI":"",
        "IDFA":"",
        "AAID":"",
        "GAID":"",
        "forename": request.json['forename'],
        "surename": request.json['surename'],
        "phoneNumber": request.json['phoneNumber'],
        "country": request.json['country'],
        "language": request.json['language'],
        "age": request.json['age'],
        "instagram": request.json['instagram'],
        "active":1,
        "userCreation":int(round(time.time() * 1000)),
        "lastAction":int(round(time.time() * 1000))
    }

    return db.updateUser(userRegisted['localId'], firebaseUser)

@app.route('/user/<localId>')
def get(localId):
    return db.getUser(localId)

@app.route('/users')
def getUsers():
    return db.getUsers()
    

@app.route('/user', methods=['PUT'])
def updateUser():
    firebaseUser = {
        "katchID": "",
        "utellyID": request.json['utellyId'],
        "UDID": "",
        "IMEI": "",
        "IDFA": "",
        "AAID": "",
        "GAID": "",
        "forename": request.json['forename'],
        "surename": request.json['surename'],
        "phoneNumber": request.json['phoneNumber'],
        "country": request.json['country'],
        "language": request.json['language'],
        "age": request.json['age'],
        "instagram": request.json['instagram'],
        "active": 1,
        "userCreation":int(round(time.time() * 1000)),
        "lastAction":int(round(time.time() * 1000))
        }
    return db.updateUser(request.json['localId'], firebaseUser)

if __name__ == '__main__':
    app.run(debug=True, port=4001)
     
