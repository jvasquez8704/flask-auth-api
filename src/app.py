from flask_restful import Api
from dotenv import load_dotenv

from app_septup import Application
from user import Users, User
from auth import SignUp, SignIn, Jwt
from batch import BatchUser, Batch


load_dotenv()

app = Application.app
api = Api(app)

@app.before_first_request
def loading_config():
    print('Katch user API started!')

api.add_resource(SignUp, '/signup')
api.add_resource(SignIn, '/signin')
api.add_resource(Jwt, '/refresh')
api.add_resource(User, '/users/<string:userId>')
api.add_resource(Users, '/users')
api.add_resource(Batch, '/batch')
api.add_resource(BatchUser, '/batch-user/<string:userId>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=443, debug=True, ssl_context='adhoc')
     
