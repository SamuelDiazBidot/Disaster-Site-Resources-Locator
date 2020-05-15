from flask import jsonify
from handler.utils import get_from_keyword_sorted_from_list, to_specified_format ,OK, ACCEPTED, CREATED, NOT_FOUND, BAD_REQUEST, registered_addresses as adrs
from dao.requests import RequestDAO

REQUEST_FORMAT = ['id', 'type', 'name', 'description', 'quantity', 'date']
SELECTED_REQUEST_FORMAT = ['id', 'type', 'name', 'description', 'quantity', 'date', 'first_name', 'last_name', 'phone_number','country', 'city', 'street']

class RequestHandler:
    def getAll(self):
        requests = RequestDAO().getAll()
        requests_list = to_specified_format(requests, REQUEST_FORMAT)
        return jsonify(Requests = requests_list), OK

    def getByID(self, id):
        requests = RequestDAO().getByID(id)
        requests_list = to_specified_format(requests, SELECTED_REQUEST_FORMAT)
        return jsonify(Request = requests_list), OK

    def search(self, args):
        keyword = args.get("keyword")
        resource_type = args.get("resource_type")
        dao = RequestDAO()
        requests = []
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
        if json['type'] and json['name'] and json['description'] and json['quantity'] and json['date'] and json['requester_id']: 
            request = RequestDAO().add(json)
            request_list = to_specified_format(request, SELECTED_REQUEST_FORMAT)
            return jsonify(Request = request_list), CREATED
        else:
            return jsonify(Error = 'Unexpected attributes in post request'), BAD_REQUEST

    def delete(self, id):
        return jsonify(Request = 'TODO'), OK

    def update(self, id, form):
        return jsonify(Request = 'TODO'), OK
