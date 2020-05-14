from flask import jsonify
from handler.utils import to_specified_format ,CREATED, OK, BAD_REQUEST
from dao.administrators import AdministratorDAO
from dao.users import UserDAO

ADMINISTARTOR_FORMAT = ['email', 'first_name', 'last_name', 'phone_number', 'permission_level']

class AdministratorHandler:
    def register(self, json):
        if json['country'] and json['city'] and json['street'] and json['district'] and json['zipcode'] and ['longitude'] and json['latitude'] and json['user_name'] and json['email'] and json['password'] and json['first_name'] and json['last_name'] and json['dob'] and json['phone_number'] and json['permission_level']:
            if not UserDAO().getByUsername(json['user_name']):
                administrator = AdministratorDAO().add(json)
                administrator_list = to_specified_format(administrator, ADMINISTARTOR_FORMAT)
                return jsonify(Administrator = administrator_list), CREATED
            else:
                return jsonify(Error = 'Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def getAll(self):
        administrators = AdministratorDAO().getAll()
        administrators_list = to_specified_format(administrators, ADMINISTARTOR_FORMAT)
        return jsonify(Administrators = administrators_list), OK

    def getByID(self, id):
        administrator = AdministratorDAO().getByID(id)
        administrator_list = to_specified_format(administrator, ADMINISTARTOR_FORMAT)
        return jsonify(Administrators = administrator_list), OK