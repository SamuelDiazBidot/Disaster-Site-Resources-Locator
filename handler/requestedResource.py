from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list, OK, ACCEPTED, CREATED, registered_addresses as adrs

from dao.requests import RequestDAO

# TODO Cambiar el address por uno de la clase de address y probarlo
resourcesRequested = [
    { "id" : 0
    , "type" : "water bottle"
    , "name" : "Nikini bottles"
    , "description" : "36 water bottle pack"
    , "requesterName" : "Johnny Sins"
    , "location" : adrs[0]
    },
    { "id" : 1
    , "type" : "baby food"
    , "name" : "gerber baby food"
    , "description": "bannana flavor"
    , "requesterName" : "Jose Rivera"
    , "location" : adrs[1]
    },
    { "id" : 2
    , "type" : "gasoline"
    , "name": "puma gas"
    , "description": "20 liters"
    , "requesterName" : "Miguel Navarro"
    , "location" : adrs[2]
    }
]

class RequestedResourceHandler:
    def build_request(self, row):
        result = {}
        result['id'] = row[0]
        result['type'] = row[1]
        result['name'] = row[2]
        result['description'] = row[3]
        result['quantity'] = row[4]
        result['date'] = row[5]
        result['sold'] = row[6]
        return result

    def getAll(self):
        requests = RequestDAO().getAllRequests()
        result_list = []
        for row in requests:
            result = self.build_request(row)
            result_list.append(result)
        return jsonify(Requests = result_list), OK

    def getByID(self, id):
        return jsonify(Request = resourcesRequested[0]), OK

    def getByKeyword(self, keywords):
        return jsonify(Request = resourcesRequested[0]), OK
    
    def getSortedByKeyword(self, keyword):
        return jsonify(Request = get_from_keyword_sorted_from_list(keyword, resourcesRequested, 'name')), OK

    def add(self, json):
        return jsonify(Request = resourcesRequested[0]), CREATED

    def delete(self, id):
        return jsonify(Request = resourcesRequested[0]), OK

    def update(self, id, form):
        return jsonify(Request = resourcesRequested[0]), OK
