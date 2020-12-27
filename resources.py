#: resources.py

from flask_restful import Resource, reqparse
from models import UserModel

parser = reqparse.RequestParser()

parser.add_argument(
    'username', help = 'This field cannot be blank', required = True
)

parser.add_argument(
    'password', help = 'This field cannot be blank', required = True
)

class AutoResource(Resource):
    route = ''

class UserRegistration(AutoResource):
    route = '/register'
    def post(self):
        data = parser.parse_args()
        new_user = UserModel(
            username = data['username'],
            password = data['password']
        )
        try:
            new_user.save_to_db()
            return {
                'message': 'User {} was created'.format(
                    data['username']
                )
            }
        except ValueError as e:
            return {'message': 'Something went wrong: ' + str(e)},500
        return {'message': 'User registration'}


class UserLogin(AutoResource):
    route = '/login'
    def post(self):
        return {'message': 'User login'}
      
      
class UserLogoutAccess(AutoResource):
    route = '/logout/access'
    def post(self):
        return {'message': 'User logout'}
      
      
class UserLogoutRefresh(AutoResource):
    route = '/logout/refresh'
    def post(self):
        return {'message': 'User logout'}
      
      
class TokenRefresh(AutoResource):
    route = '/token/refresh'
    def post(self):
        return {'message': 'Token refresh'}
      
      
class AllUsers(AutoResource):
    route = '/users'
    def get(self):
        return {'message': 'List of users'}

    def delete(self):
        return {'message': 'Delete all users'}
      
      
class SecretResource(AutoResource):
    route = '/secret'
    def get(self):
        return {
            'answer': 42
        }
      
