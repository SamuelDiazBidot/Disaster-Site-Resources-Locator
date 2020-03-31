from flask import jsonify
from handler.utils import CREATED

administrator = { "username" : "admin"
                , "password" : "password"
                }

class AdministratorHandler:
    def register(self, json):
        return jsonify(Administrator = administrator), CREATED