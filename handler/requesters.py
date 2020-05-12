from flask import jsonify
from handler.utils import to_specified_format, CREATED, OK, registered_addresses
from dao.requesters import RequestersDAO

REQUESTER_FORMAT = ['email', 'first_name', 'last_name', 'phone_number']

class RequesterHandler:
    def register(self, json):
        requester = RequestersDAO().add(json)
        requester_list = to_specified_format(requester, REQUESTER_FORMAT)
        return jsonify(Requester = requester_list), CREATED

    def getAll(self):
        requesters = RequestersDAO().getAll()
        requesters_list = to_specified_format(requesters, REQUESTER_FORMAT)
        return jsonify(Requesters = requesters_list), OK

    def getByID(self, id):
        requester = RequestersDAO().getByID(id)
        requester_list = to_specified_format(requester, REQUESTER_FORMAT)
        return jsonify(Requesters = requester_list), OK