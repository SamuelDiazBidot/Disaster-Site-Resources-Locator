from flask import jsonify

from dao.supply import SupplierDAO
from handler.utils import CREATED, OK, to_person_format, registered_addresses

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
        
    
