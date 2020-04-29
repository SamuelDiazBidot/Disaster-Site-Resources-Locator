from flask import jsonify

from dao.supply import SupplierDAO, SupplyDAO
from handler.utils import CREATED, OK, to_person_format, registered_addresses, to_specified_format, SUPPLYFORMAT, SUPPLYSEARCHKEYWORDFORMAT

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
        return jsonify(Supply=to_specified_format(SupplyDAO.gettAll(), SUPPLYFORMAT)), OK

    @staticmethod
    def getSupplyById(id):
        return jsonify(Supply=to_specified_format(SupplyDAO.getById(id), SUPPLYFORMAT)), OK

    @staticmethod
    def getSupplyByKeyword(keyword):
        return jsonify(Supply=to_specified_format(SupplyDAO.getByKeyword(keyword), SUPPLYSEARCHKEYWORDFORMAT)), OK

        