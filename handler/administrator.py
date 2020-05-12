from flask import jsonify
from handler.utils import to_specified_format ,CREATED, OK
from dao.administrators import AdministratorDAO

administrator = { "username" : "admin"
                , "password" : "password"
                }

ADMINISTARTOR_FORMAT = ['email', 'first_name', 'last_name', 'phone_number', 'permission_level']

class AdministratorHandler:
    def register(self, json):
        administrator = AdministratorDAO().add(json)
        return jsonify(Administrator = administrator), CREATED

    def getAll(self):
        administrators = AdministratorDAO().getAll()
        administrators_list = to_specified_format(administrators, ADMINISTARTOR_FORMAT)
        return jsonify(Administrators = administrators_list), OK

    def getByID(self, id):
        administrator = AdministratorDAO().getAll()
        administrator_list = to_specified_format(administrator, ADMINISTARTOR_FORMAT)
        return jsonify(Administrators = administrator_list), OK