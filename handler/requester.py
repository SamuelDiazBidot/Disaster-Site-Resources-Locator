from flask import jsonify

requester = { "username" : "username"
            , "password" : "securepassword"
            , "name" : "Maria DB"
            , "location" : "Yauco, Puerto Rico"
            }

class RequesterHandler:
    def register(self, json):
        return jsonify(Requester = requester), 201