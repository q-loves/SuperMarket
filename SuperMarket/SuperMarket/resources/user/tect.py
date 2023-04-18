from flask_restful import Resource
from comment.models.user import UserModel

class UserTect(Resource):

    def get(self):
        return {'hello':'tect succeed'}