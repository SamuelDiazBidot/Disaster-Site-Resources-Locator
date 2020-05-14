from flask import jsonify
from handler.utils import to_specified_format, CREATED, OK, BAD_REQUEST
from dao.users import UserDAO

USER_FORMAT = ['user_name', 'email', 'first_name', 'last_name', 'phone_number']

class UserHandler:
    def add(self, json):
        dao = UserDAO()
        if json['country'] and json['city'] and json['street'] and json['district'] and json['zipcode'] and ['longitude'] and json['latitude'] and json['user_name'] and json['email'] and json['password'] and json['first_name'] and json['last_name'] and json['dob'] and json['phone_number']:
            if not dao().getByUsername(json['user_name']):
                user = dao().add(json)
                user_list = to_specified_format(user, USER_FORMAT)
                return jsonify(User = user_list), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def getAll(self):
        users = UserDAO().getAll()
        users_list = to_specified_format(users, USER_FORMAT)
        return jsonify(Users = users_list), OK