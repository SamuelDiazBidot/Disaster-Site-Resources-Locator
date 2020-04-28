from flask import jsonify
from handler.utils import to_specified_format ,CREATED, OK
from dao.administrators import AdministratorDAO

administrator = { "username" : "admin"
                , "password" : "password"
                }

ADMINISTARTOR_FORMAT = ['emai', 'first_name', 'last_name', 'phone_number', 'permission_level']

class AdministratorHandler:
    # def build_administrator(self, row):
        # result = {}
        # result['email'] = row[0]
        # result['first_name'] = row[1] 
        # result['last_name'] = row[2]
        # result['phone_number'] = row[3]
        # result['permission_level'] = row[4]
        # return result

    def register(self, json):
        return jsonify(Administrator = administrator), CREATED

    def getAll(self):
        administrators = AdministratorDAO().getAll()
        # result_list = []
        # for row in administrators:
            # result = self.build_administrator(row)
            # result_list.append(result)
        administrators_list = to_specified_format(administrators, ADMINISTARTOR_FORMAT)
        return jsonify(Administrators = administrators_list), OK