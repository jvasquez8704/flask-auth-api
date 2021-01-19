from flask_restful import Resource, reqparse
from firebase import sign_in_with_email_and_password, sign_up_with_email_and_password, get_utelly_id, update_user
import json
import time


class SignUp(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="email cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="password cannot be blank.")
    parser.add_argument('forename', type=str, required=True, help="forename cannot be blank.")
    parser.add_argument('surename', type=str, required=True, help="surname cannot be blank.")
    parser.add_argument('phoneNumber', type=str, required=True, help="surname cannot be blank.")
    parser.add_argument('country', type=str, required=True, help="country cannot be blank.")
    parser.add_argument('language', type=str, required=True, help="language cannot be blank.")
    parser.add_argument('age', type=int, required=True, help="age cannot be blank.")
    parser.add_argument('instagram', type=str, required=True, help="instagram cannot be blank.")
    parser.add_argument('TCVersion', type=str, required=False)
    parser.add_argument('PPVersion', type=str, required=False)

    def post(self):
        data = SignUp.parser.parse_args()
        #step1
        fb_user = json.loads(json.dumps(sign_up_with_email_and_password(data['email'], data['password'])))
        if 'error' in fb_user:
            return {'status_code': fb_user['error']['code'], 'custom_code': fb_user['error']['message'], 'message': ''}, fb_user['error']['code']

        #step2
        utelly_record = json.loads(json.dumps(get_utelly_id(fb_user['refreshToken'])))
        if 'sub_code' in utelly_record:
            #Delete userd created at the previous step
            return {'status_code': utelly_record['status_code'], 'custom_code': utelly_record['sub_code'], 'message': ''}, utelly_record['status_code']

        #step3
        firebaseUser = {
            "katchID": "",
            "utellyID": utelly_record['user']['id'],
            "UDID": "",
            "IMEI": "",
            "IDFA": "",
            "AAID": "",
            "GAID": "",
            "forename": data['forename'],
            "surename": data['surename'],
            "phoneNumber": data['phoneNumber'],
            "country": data['country'],
            "language": data['language'],
            "age": data['age'],
            "instagram": data['instagram'],
            "active": 1,
            "userCreation": int(round(time.time() * 1000)),
            "lastAction": int(round(time.time() * 1000)),
            "welcomeSeen": 0,
            "featuresSeen": 0,
            "TCVersion": data['TCVersion'],
            "PPVersion": data['PPVersion']
        }

        try:
            update_user(fb_user['localId'], firebaseUser)
        except Exception as e:
            print('Exception at update user process {0}'.format(e))
            return {'status_code': 409, "message": "User created, however, check its configuration", "user": fb_user}, 409

        user_merged = fb_user.copy()
        user_merged.update(firebaseUser)
        return {'status_code': 201, "message": "User created successfully.", "user": user_merged}, 201

        

class SignIn(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="email cannot be blank.")
    parser.add_argument('password', type=str, required=True, help="password cannot be blank.")

    def post(self):
        data = SignIn.parser.parse_args()
        fb_user = json.loads(json.dumps(sign_in_with_email_and_password(data['email'], data['password'])))
        if 'error' in fb_user:
            return {'status_code': fb_user['error']['code'], 'custom_code': fb_user['error']['message'], 'message': ''}, fb_user['error']['code']
        return {'status_code': 200, "message": "User signed successfully.", "user": fb_user}, 200


