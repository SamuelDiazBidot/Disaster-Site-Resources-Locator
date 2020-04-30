from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list, to_specified_format ,OK, ACCEPTED, CREATED, NOT_FOUND, registered_addresses as adrs
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

class RequestHandler:
    def getAll(self):
        requests = RequestDAO().getAll()
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Requests = requests_list), OK

    def getByID(self, id):
        requests = RequestDAO().getByID(id)
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Request = requests_list), OK

    def search(self, args):
        keyword = args.get("keyword")
        resource_type = args.get("resource_type")
        dao = RequestDAO()
        if (len(args) == 2) and keyword and resource_type:
            requests = dao.getByTypeOrKeyword(resource_type, keyword)
        elif (len(args) == 1) and keyword:
            requests = dao.getByKeyword(keyword)
        elif (len(args) == 1) and resource_type:
            requests = dao.getByType(resource_type)
        else:
            return jsonify(Error = 'Malformed query string'), NOT_FOUND
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Requests = requests_list), OK

    def add(self, json):
        return jsonify(Request = resourcesRequested[0]), CREATED

    def delete(self, id):
        return jsonify(Request = resourcesRequested[0]), OK

    def update(self, id, form):
        return jsonify(Request = resourcesRequested[0]), OK
