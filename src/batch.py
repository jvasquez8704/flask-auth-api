from flask_restful import Resource, reqparse
from firebase import get_user, get_users, create_user, create_fs_user
import time
from constants import Props

class Batch(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('localId', type=str)
    parser.add_argument('utellyId', type=str)
    parser.add_argument('email', type=str)
    parser.add_argument('password', type=str)
    parser.add_argument('forename', type=str)
    parser.add_argument('surname', type=str)
    parser.add_argument('phoneNumber', type=str)
    parser.add_argument('country', type=str)
    parser.add_argument('language', type=str)
    parser.add_argument('age', type=bool)
    parser.add_argument('instagram', type=str)
    parser.add_argument('tcVersion', type=str)
    parser.add_argument('ppVersion', type=str)

    def get(self, userId):
        users = get_users()
        if users:
            return {'users': users} , 200
        return {'status_code': 404, 'custom_code': 'USER_NOT_FOUND', 'message': 'User not found'}, 404
    
    def post(self):
        data = Batch.parser.parse_args()

        for x in range(9000, 9201):
            email = 'batch-{0}@gmail.com'.format(x)
            insta = '@batch-{0}'.format(x)
            user_id = 'user-ext-nrg-' + format(x,'04')
            name = data['forename'] + format(x,'04')
            batch_user = {
                "katchID": "",
                "utellyID": "",
                "UDID": "", 
                "IMEI": "",
                "IDFA": "",
                "AAID": "",
                "GAID": "",
                "email": email,
                "forename": name,
                "surname": data['surname'],
                "phoneNumber": data['phoneNumber'],
                "country": data['country'],
                "language": data['language'],
                "age": bool(data['age']),
                "instagram": insta,
                "active": 1,
                "userCreation": int(round(time.time() * 1000)),
                "lastAction": int(round(time.time() * 1000)),
                "welcomeSeen":0,
                "featuresSeen":0,
                "role": Props.DEFAULT_USER_ROLE,
                "tcVersion":data['tcVersion'],
                "ppVersion":data['ppVersion']
            }

            fs_user = {
                    'Age': bool(data['age']),
                    'rated_count': 0,
                    'Email': email,
                    'Name': name + " " + data['surname'],
                    'lastname': data['surname'],
                    'firstname': name,
                    'uid': user_id,
                    "injected_movies": {},
                    "rated_movies": ""  # add empty rated movies
                }
            create_user(user_id,batch_user)
            create_fs_user(user_id, fs_user)
        
        return {'status_code': 200, "message": "Users created successfully.", "users length": 100}, 200


class BatchUser(Resource):
    def get(self, userId):
        print('get param {0}'.format(userId))
        if userId:
            user = get_user(userId)
            if user:
                return {"user": user}, 200
            return {'status_code': 404, 'custom_code': 'USER_NOT_FOUND', 'message': 'User not found'}, 404
        else:
            users = get_users()
            if users:
                return {'users': users} , 200
            return {'status_code': 404, 'custom_code': 'USER_NOT_FOUND', 'message': 'User not found'}, 404
    

