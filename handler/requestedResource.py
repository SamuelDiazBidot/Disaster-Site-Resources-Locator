from flask import jsonify

resourcesRequested = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "requesterName" : "Johnny Sins"
    , "location" : "NA"
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "requesterName" : "Jose Rivera"
    , "location" : "Ponce, PR"
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "requesterName" : "Miguel Navarro"
    , "location" : "San Juan, PR"
    }
]

class RequestedResourceHandler:
    def getAll(self):
        return jsonify(Requests = resourcesRequested)

    def getByID(self, id):
        return jsonify(Request = resourcesRequested[0])

    def getByKeyword(self, keywords):
        return jsonify(Request = resourcesRequested[0])

    def add(self, json):
        return jsonify(Request = resourcesRequested[0])

    def delete(self, id):
        return jsonify(Request = resourcesRequested[0]), 201
