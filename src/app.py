from flask_restful import Api
from dotenv import load_dotenv

from app_septup import Application
from user import Users, User, User_Url, User_Rate
from auth import SignUp, SignIn, Jwt
from batch import BatchUser, Batch


load_dotenv()

app = Application.app
api = Api(app)

@app.before_first_request
def loading_config():
    print('NRG user API started!')

api.add_resource(User, '/user/<string:userId>', endpoint='user')
api.add_resource(User_Url, '/user/url', endpoint='user_url')
api.add_resource(User_Rate, '/user/rate', endpoint='user_rate')
api.add_resource(Users, '/users', endpoint='users')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')
     
