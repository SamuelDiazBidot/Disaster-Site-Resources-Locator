from flask import jsonify
from handler.utils import CREATED

supplier = { "username" : "SuppliesRus"
           , "password" : "plainText"
           , "name" : "johnny bravo"
           , "address" : "Caguas, Puerto Rico"
           }

class SupplierHandler:
    def register(self, json):
        return jsonify(Supplier = supplier), CREATED