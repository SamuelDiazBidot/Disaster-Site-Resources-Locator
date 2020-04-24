from flask import jsonify
from handler.utils import CREATED, OK
from dao.administrators import AdministratorDAO

administrator = { "username" : "admin"
                , "password" : "password"
                }

class AdministratorHandler:
    def build_administrator(self, row):
        result = {}
        result['email'] = row[0]
        result['first_name'] = row[1] 
        result['last_name'] = row[2]
        result['phone_number'] = row[3]
        result['permisssion_level'] = row[4]
        return result

    def register(self, json):
        return jsonify(Administrator = administrator), CREATED

    def getAll(self):
        administrators = AdministratorDAO().getAll()
        result_list = []
        for row in administrators:
            result = self.build_administrator(row)
            result_list.append(result)
        return jsonify(Administrators = result_list), OK