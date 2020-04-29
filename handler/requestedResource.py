from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list, to_specified_format ,OK, ACCEPTED, CREATED, registered_addresses as adrs
from dao.requests import RequestDAO

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

REQUEST_FORMAT = ['id', 'type', 'name', 'description', 'quantity', 'date', 'sold']

class RequestedResourceHandler:
    def getAll(self):
        requests = RequestDAO().getAll()
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Requests = requests_list), OK

    def getByID(self, id):
        requests = RequestDAO().getByID(id)
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Request = requests_list), OK

    def getByKeyword(self, keyword):
        requests = RequestDAO().getByNameOrDescription(keyword)
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Request = requests_list), OK
    
    # Redundant code
    # def getSortedByKeyword(self, keyword):
        # return jsonify(Request = get_from_keyword_sorted_from_list(keyword, resourcesRequested, 'name')), OK

    def add(self, json):
        return jsonify(Request = resourcesRequested[0]), CREATED

    def delete(self, id):
        return jsonify(Request = resourcesRequested[0]), OK

    def update(self, id, form):
        return jsonify(Request = resourcesRequested[0]), OK
