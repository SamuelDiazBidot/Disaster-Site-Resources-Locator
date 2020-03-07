from flask import jsonify

administrator = { "username" : "admin"
                , "password" : "password"
                }

class AdministratorHandler:
    def register(self, json):
        return jsonify(Administrator = administrator), 201