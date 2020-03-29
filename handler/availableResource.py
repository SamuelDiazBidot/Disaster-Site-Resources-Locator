from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list
import re


resourcesAvailable = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "SupplierName" : "Johnny Sins"
    , "location" : "NA"
    , "price" : 0.0
    , "reserved" : False
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "SupplierName" : "Jose Rivera"
    , "location" : "Ponce, PR"
    , "price" : 0.0 
    , "reserved" : True
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    , "price" : 10.0
    , "reserved" : False
    },
    { "id" : 3
    , "type" : "gasoline"
    , "name": "Shell gas"
    , "description": "40 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    , "price" : 10.0
    , "reserved" : False
    },
    { "id" : 4
    , "type" : "watter bottle"
    , "name": "Nikini Gallons"
    , "description": "20 liters"
    , "supplierName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    , "price" : 100.0
    , "reserved" : False
    }
]

class AvailableResourceHandler:
    def getAll(self):
        return jsonify(Available = resourcesAvailable)

    def getByID(self, id):
        return jsonify(Available = resourcesAvailable[0])

    def getByKeyword(self, keyword):
        reserved = False
        return jsonify(Available = get_from_keyword_sorted_from_list(keyword, resourcesAvailable, 'name', reserved=reserved)), 201

    def add(self, json):
        return jsonify(Available = resourcesAvailable[0]), 201

    def delete(self, id):
        return jsonify(Available = resourcesAvailable[0]), 201

    def update(self, id, form):
        return jsonify(Available = resourcesAvailable[0]), 201

    def reserve(self, id):
        return jsonify(Reserved = resourcesAvailable[1]), 201