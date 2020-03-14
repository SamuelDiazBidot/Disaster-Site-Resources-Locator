from flask import jsonify


WATER = 'water'
MEDICATIONS = 'medications'
BABYFOOD = 'baby food'
CANNEDFOOD = 'canned food'
DRYFOOD = 'dry food'
ICE = 'ice'
FUEL = 'fuel'
MEDICALDEVICES = 'medical devices'
HEAVYEQUIPMENT = 'heavy equipment'
TOOLS = 'tools'
CLOTHING = 'clothing'
POWERGENERATOR = 'power generator'
BATTERY = 'battery'

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
    }
]

class AvailableResourceHandler:
    def getAll(self):
        return jsonify(Available = resourcesAvailable)

    def getByID(self, id):
        return jsonify(Available = resourcesAvailable[0])

    def getByKeyword(self, form):
        return jsonify(Available = resourcesAvailable[0])

    # En el futuro seria bueno añadir un metodo que busque por type y description simultaneamente
    def getByItemType(self, item_type=BABYFOOD):
        item_found = []
        for item in resourcesAvailable:
            if item['type'] == item_type:
                item_found.append(item)
        return jsonify(item_found), 201

    def add(self, json):
        return jsonify(Available = resourcesAvailable[0]), 201

    def delete(self, id):
        return jsonify(Available = resourcesAvailable[0]), 201

    def update(self, id, form):
        return jsonify(Available = resourcesAvailable[0]), 201

    def reserve(self, id):
        return jsonify(Reserved = resourcesAvailable[1]), 201