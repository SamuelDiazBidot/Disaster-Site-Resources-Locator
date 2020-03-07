from flask import jsonify

supplier = { "username" : "SuppliesRus"
           , "password" : "plainText"
           , "name" : "johnny bravo"
           , "address" : "Caguas, Puerto Rico"
           }

class SupplierHandler:
    def register(self, json):
        return jsonify(Supplier = supplier), 201