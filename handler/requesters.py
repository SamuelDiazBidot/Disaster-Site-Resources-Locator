from flask import jsonify
from handler.utils import CREATED, OK, registered_addresses

from dao.requesters import RequestersDAO

requester = { "username" : "username"
            , "password" : "securepassword"
            , "name" : "Maria DB"
            , "location" : registered_addresses[2]
            }

class RequesterHandler:
    def build_requester(self, row):
        result = {}
        result['email'] = row[0]
        result['first_name'] = row[1] 
        result['last_name'] = row[2]
        result['phone_number'] = row[3]
        return result

    def register(self, json):
        return jsonify(Requester = requester), CREATED

    def getAll(self):
        requesters = RequestersDAO().getAll()
        result_list = []
        for row in requesters:
            result = self.build_requester(row)
            result_list.append(result)
        return jsonify(Requesters = result_list), OK

    def getByID(self, id):
        requester = RequestersDAO().getByID(id)
        result_list = []
        for row in requester:
            result = self.build_requester(row)
            result_list.append(result)
        return jsonify(Requesters = result_list), OK