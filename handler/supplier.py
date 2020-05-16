from flask import jsonify

from dao.users import UserDAO
from dao.supply import SupplierDAO, SupplyDAO
from handler.utils import CREATED, OK, NOT_FOUND, to_person_format, registered_addresses, to_specified_format, SUPPLYFORMAT, SUPPLYSEARCHKEYWORDFORMAT, RESOURCEFORMAT, make_google_map_link, append_loc_to_list, BAD_REQUEST


class SupplierHandler:

    @staticmethod
    def register(json):
        if json['country'] and json['city'] and json['street'] and json['district'] and json['zipcode'] and ['longitude'] and json['latitude'] and json['user_name'] and json['email'] and json['password'] and json['first_name'] and json['last_name'] and json['dob'] and json['phone_number']:
            if not UserDAO().getByUsername(json['user_name']):
                supplier = SupplierDAO.add(json)
                supplier_ls = to_specified_format([supplier], SUPPLYFORMAT) 
                return jsonify(Supplier=supplier_ls), CREATED
            else:
                return jsonify(Error='Username already in use'), BAD_REQUEST
        else:
            return jsonify(Error='Unexpected attributes in post request'), BAD_REQUEST

    @staticmethod
    def getAll():        
        return jsonify(Suppliers=to_person_format(SupplierDAO.getAll())), OK

    @staticmethod
    def getSupplierById(id):
        return jsonify(Suppliers=to_person_format(SupplierDAO.getById(id))), OK

    


    
class SupplyHandler:
    
    FRONTEND_FORMAT = ['id', 'type', 'name', 'description', 'quantity', 'date']
    SELECTED_SUPPLY_FORMAT = ['id', 'type', 'name', 'description', 'quantity', 'date', 'first_name', 'last_name', 'phone_number','country', 'city', 'street']

    @staticmethod
    def getAllSupply():
        return jsonify(Supplies=to_specified_format(SupplyDAO.gettAll(), SupplyHandler.FRONTEND_FORMAT)), OK

    @staticmethod
    def getSupplyById(id):                
        return jsonify(Supplies=to_specified_format(SupplyDAO.getById(id), SupplyHandler.SELECTED_SUPPLY_FORMAT)), OK
         

    @staticmethod
    def getSupplyByKeyword(keyword):
        return SupplyDAO.getByKeyword(keyword)

    
    @staticmethod
    def searchSupply(args):
        if not args:
            raise Exception
        keyword = args.get('keyword')
        res_type = args.get('resource_type')
        if keyword and res_type:
            result = SupplyDAO.getByKeywordAndType(res_type, keyword)
        elif keyword and not res_type:
            try:
                print(result)
            except:
                print('Does not exist.')
            result = SupplyDAO.getByKeyword(keyword)
        elif res_type and not keyword:
            result = SupplyDAO.getByType(res_type)
        else:
            return jsonify(Error='Malformed query string.'), NOT_FOUND

        result = to_specified_format(result, SupplyHandler.FRONTEND_FORMAT)

        return jsonify(Supplies=result), OK


    @staticmethod
    def add(json):
        if json['type'] and json['name'] and json['description'] and json['quantity'] and json['date'] and json['supplier_id']: 
            supply = SupplyDAO.add(json)
            supply_ls = to_specified_format(supply, SupplyHandler.SELECTED_SUPPLY_FORMAT)
            return jsonify(Supply = supply_ls), CREATED
        else:
            return jsonify(Error='Unexpected attributes in post request.'), BAD_REQUEST

    @staticmethod
    def delete(id):
        return jsonify(Supply='TODO'), OK

    @staticmethod
    def update(id, form):
        return jsonify(Supply='TODO'), OK
    

        