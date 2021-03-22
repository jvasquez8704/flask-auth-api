from flask_restful import Resource, reqparse
from flask_jwt_extended import (
    jwt_required, get_jwt_identity
)
from firebase import get_user, get_users, update_user, get_utelly_id
import time
from constants import Props
from security import viewer_required

class User(Resource):
    #@jwt_required
    def get(self, userId):
        #logged_user = get_jwt_identity()
        user = get_user(userId)
        if user:
            return {"data": user, "logged_in_as": logged_user}, 200
        return {'status_code': 404, 'custom_code': 'USER_NOT_FOUND', 'message': 'User not found'}, 404


class Users(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('localId', type=str, required=True, help="localId cannot be blank.")
    parser.add_argument('utellyId', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('forename', type=str)
    parser.add_argument('surname', type=str)
    parser.add_argument('phoneNumber', type=str)
    parser.add_argument('country', type=str)
    parser.add_argument('language', type=str)
    parser.add_argument('age', type=str)
    parser.add_argument('gender', type=str)
    parser.add_argument('enthnic', type=str)
    parser.add_argument('aware', type=str)
    parser.add_argument('interest', type=str)
    parser.add_argument('fan', type=str)
    parser.add_argument('instagram', type=str)
    parser.add_argument('tcVersion', type=str)
    parser.add_argument('ppVersion', type=str)

    @jwt_required
    def get(self):
        users = get_users()
        if users:
            return {'users': users} , 200
        return {'status_code': 404, 'custom_code': 'USER_NOT_FOUND', 'message': 'User not found'}, 404
    
    @jwt_required
    def put(self):
        data = Users.parser.parse_args()
        firebase_user = {
            "katchID": "",
            "utellyID": data['utellyId'],
            "UDID": "", 
            "IMEI": "",
            "IDFA": "",
            "AAID": "",
            "GAID": "",
            "email": data['email'],
            "forename": data['forename'],
            "surname": data['surname'],
            "phoneNumber": data['phoneNumber'],
            "country": data['country'],
            "language": data['language'],
            "age": bool(data['age']),
            "instagram": data['instagram'],
            "active": 1,
            "userCreation": int(round(time.time() * 1000)),
            "lastAction": int(round(time.time() * 1000)),
            "welcomeSeen":0,
            "featuresSeen":0,
            "role": Props.DEFAULT_USER_ROLE,
            "tcVersion":data['tcVersion'],
            "ppVersion":data['ppVersion']
        }

        try:
            update_user(data['localId'], firebase_user)
        except Exception as e:
            print('Exception at update user process {0}'.format(e))
            return {'status_code': 409, "message": "User updating process failed."}, 409
        
        return {'status_code': 200, "message": "User updated successfully.", "user": firebase_user}, 200

    @viewer_required
    def post(self):
        data = Users.parser.parse_args()        
        return {'resouce': data} , 200
