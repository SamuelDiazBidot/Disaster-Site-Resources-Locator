from flask import jsonify
from handler.utils import to_specified_format, CREATED, OK, BAD_REQUEST
from dao.requesters import RequestersDAO
from dao.users import UserDAO

REQUESTER_FORMAT = ['email', 'first_name', 'last_name', 'phone_number']

class RequesterHandler:
    def register(self, json):
        if json['country'] and json['city'] and json['street'] and json['district'] and json['zipcode'] and ['longitude'] and json['latitude'] and json['user_name'] and json['email'] and json['password'] and json['first_name'] and json['last_name'] and json['dob'] and json['phone_number']:
            if not UserDAO().getByUsername(json['user_name']):
                requester = RequestersDAO().add(json)
                requester_list = to_specified_format(requester, REQUESTER_FORMAT)
                return jsonify(Requester = requester_list), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def getAll(self):
        requesters = RequestersDAO().getAll()
        requesters_list = to_specified_format(requesters, REQUESTER_FORMAT)
        return jsonify(Requesters = requesters_list), OK

    def getByID(self, id):
        requester = RequestersDAO().getByID(id)
        requester_list = to_specified_format(requester, REQUESTER_FORMAT)
        return jsonify(Requesters = requester_list), OK