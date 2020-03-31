from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list, registered_addresses, OK, ACCEPTED, CREATED
import re

# TODO Test methods with the new address from registeres addresses

resourcesAvailable = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "SupplierName" : "Johnny Sins"
    , "location" : registered_addresses[0]
    , "price" : 1.0
    , "reserved" : False
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "SupplierName" : "Jose Rivera"
    , "location" : registered_addresses[1]
    , "price" : 0.0 
    , "reserved" : True
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : registered_addresses[2]
    , "price" : 10.0
    , "reserved" : False
    },
    { "id" : 3
    , "type" : "gasoline"
    , "name": "Shell gas"
    , "description": "40 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : registered_addresses[3]
    , "price" : 10.0
    , "reserved" : False
    },
    { "id" : 4
    , "type" : "watter bottle"
    , "name": "Nikini Gallons"
    , "description": "20 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : registered_addresses[2]
    , "price" : 100.0
    , "reserved" : False
    }
]

class AvailableResourceHandler:
    def getAll(self):
        return jsonify(Available = resourcesAvailable), OK

    def getByID(self, id):
        return jsonify(Available = resourcesAvailable[0]), OK

    def getByKeyword(self, keyword):
        reserved = False
        return jsonify(Available = get_from_keyword_sorted_from_list(keyword, resourcesAvailable, 'name', reserved=reserved)), CREATED
    def add(self, json):
        return jsonify(Available = resourcesAvailable[0]), CREATED

    def delete(self, id):
        return jsonify(Available = resourcesAvailable[0]), CREATED

    def update(self, id, form):
        return jsonify(Available = resourcesAvailable[0]), CREATED

    def reserve(self, id):
        return jsonify(Reserved = resourcesAvailable[1]), CREATED