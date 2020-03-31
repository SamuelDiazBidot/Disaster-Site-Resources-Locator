from flask import jsonify
from handler.utils import CREATED
from handler.address import registered_addresses

requester = { "username" : "username"
            , "password" : "securepassword"
            , "name" : "Maria DB"
            , "location" : registered_addresses[2]
            }

class RequesterHandler:
    def register(self, json):
        return jsonify(Requester = requester), CREATED