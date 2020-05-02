from flask import jsonify

from dao.supply import SupplierDAO, SupplyDAO
from handler.utils import CREATED, OK, NOT_FOUND, to_person_format, registered_addresses, to_specified_format, SUPPLYFORMAT, SUPPLYSEARCHKEYWORDFORMAT, RESOURCEFORMAT

supplier = { "username" : "SuppliesRus"
           , "password" : "plainText"
           , "name" : "johnny bravo"
           , "address" : registered_addresses[1]
           }

class SupplierHandler:

    @staticmethod
    def register(json):
        return jsonify(Supplier = supplier), CREATED

    @staticmethod
    def getAll():        
        return jsonify(Suppliers=to_person_format(SupplierDAO.getAll())), OK

    @staticmethod
    def getSupplierById(id):
        return jsonify(Suppliers=to_person_format(SupplierDAO.getById(id))), OK
        
    
class SupplyHandler:
    
    @staticmethod
    def getAllSupply():
        return jsonify(Supplies=to_specified_format(SupplyDAO.gettAll(), RESOURCEFORMAT)), OK

    @staticmethod
    def getSupplyById(id):
        return jsonify(Supplies=to_specified_format(SupplyDAO.getById(id), RESOURCEFORMAT)), OK
         

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

        result = to_specified_format(result, RESOURCEFORMAT)

        return jsonify(Supplies=result), OK

        